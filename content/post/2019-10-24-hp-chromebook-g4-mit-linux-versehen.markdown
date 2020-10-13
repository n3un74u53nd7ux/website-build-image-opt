---
author: Roberto
date: 2019-10-24 16:08:19+00:00
draft: false
title: HP ChromeBook G4 mit Linux versehen
type: post
url: /hp-chromebook-g4-mit-linux-versehen/
categories:
- Fertige Projekte
- Wissen
---




Obwohl die ChromeBooks technisch und optisch schön sind, stört sich mancher am Google-Betriebssystem. Glücklicherweise gibt es [GalliumOS](https://www.galliumos.org), eine speziell angepasste Ubuntu-Version, die auf den Intel-basierten ChromeBooks läuft. 





<!-- more -->





Im Unterschied zu einem normalen Ubuntu 16.04 oder 18.04 sind hier die speziellen Treiber schon mit drin, damit WLAN, Webcam und vor allem Videobeschleunigung ruckelfrei funktionieren. So lässt es sich dann angenehm arbeiten, inklusiver sehr langer Akkulaufzeit!







Der Umbau auf Linux ist etwas anstrengend, aber [in diesem Video hier](https://www.youtube.com/watch?v=T6-5y24-95w) sehr ausführlich und verständlich beschrieben. Es sind inklusive Installation etwa 2-3 Stunden einzuplanen. Der Ablauf gliedert sich dabei grob in folgende Schritte:





  * Wechsel des ChromeBooks in den sogenannten Developermodus  
  * Booten und Ausführen eines speziellen Scriptes, das Teile der Firmware/des Bootloaders mit Custom-Code überschreibt, damit wir  von einem USB-Stick booten können  
  * Reboot und Aktivieren des Bootens vom USB-Stick  
  * Erneuter Reboot und booten von GalliumOS vom USB-Stick, hier für die Intel BayTrail-Plattform   
  * Installation des Betriebssystems. Dabei können wir alles überschreiben, was auf der 32GB mmc-Karte vorhanden ist. ACHTUNG: Bei mir lief die Installation nur erfolgreich durch, wenn ich "Updates bei der Installation installieren" und "Drittanbieter-Software" deaktiviert hatte.  
  * Fertig! 





Zwar beschwert sich das ChromeBook beim Booten jedesmal, dass das ChromeOS kaputt ist. Aber durch Drücken von STRG-L bootet dann trotzdem das GalliumOS.







Ich hab hier die Version 2.1 von GalliumOS installiert, die auf Ubuntu 16.04 LTS basiert. Mittlerweile ist auch die Version 3.0 (basierend auf Ubuntu 18.04 LTS) herausgekommen, zu der ich aber noch keine Erfahrungen habe.





  {{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5548.jpeg" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5562.jpeg" >}}
{{< /gallery >}}





Wenn Euch das Drücken von STRG-L bei jedem Anschalten nervt (zumal mit einer falschen Taste ChromeOS die Wiederherstellung versucht und dabei das Linux zerschießt), gibt es auch die Möglichkeit den originalen Bootloader komplett zu überschreiben.







Dazu ist es erforderlich auf dem Mainboard eine sogenannte "Schreibschutz-Schraube", zumindest vorübergehend, zu entfernen. Dafür müssen alle Schrauben auf der Unterseite des Gehäuses entfernt werden (auch diejenigen unter den hinteren Gummipuffern bzw. Standfüßen!). Dann kann die silberne Tastatur vorsichtig mit einer Kreditkarte herausgehebelt werden.







Dann offenbar sich folgendes Bild:





  {{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5626.jpeg" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5628.jpeg" >}}
{{< /gallery >}}





Die Schraube ist diejenige mit dem geviertelten Lötpad. Nach dem Entfernen der Schraube (siehe Bild rechts) kann, auch ohne Schließen des Gehäuses, dann mit dem Flash-Tool aus obigem Video der Bootloader überschrieben werden. Danach habe ich die Schraube einfach wieder reingedreht und das Gehäuse verschlossen. 







Jetzt bootet Linux jedesmal direkt und ohne Nachfrage. :)



