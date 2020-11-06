import os
from image_mapping import mapping
from html.parser import HTMLParser

fname = []
for root,d_names,f_names in os.walk('./content'):
    for f in f_names:
        fname.append(os.path.join(root, f))


class GalleryParser(HTMLParser):

    image_ids = []

    def __init__(self, gallerytxt):
        super().__init__()
        gallerytxt = gallerytxt.replace('[', '<').replace(']', '>')
        self.feed(gallerytxt)

    def handle_starttag(self, tag, attrs):
        self.image_ids = dict(attrs)['ids'].split(',')


GALLERY_OUTER = '''
{{< gallery caption-effect="fade" >}}
  %s
{{< /gallery >}}
'''

IMG = '{{< figure link="/wp-content/uploads/%s" >}}'



for mdfile_name in fname:
    changed = False
    with open(mdfile_name, 'r') as mdfile:
        content = mdfile.readlines()
        changed_file = []
        for line in content:
            if '[gallery' in line:
                print('----')
                changed = True
                line = line.strip()
                print(line)
                gal = GalleryParser(line)
                imgs = []
                for img_id in gal.image_ids:
                    if img_id.strip() not in mapping.keys():
                        print(f"ERROR: {mdfile_name}, {img_id}")
                    imgs.append(IMG % mapping[img_id.strip()])
                line = GALLERY_OUTER % '\n'.join(imgs)
                print(line)
            changed_file.append(line)
    if changed:
        with open(mdfile_name, 'w') as mdfile:
            mdfile.writelines(changed_file)
