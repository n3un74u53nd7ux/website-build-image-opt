---
author: Roberto
date: 2019-10-21 10:53:00+00:00
draft: false
title: Ringmanufaktur
type: post
url: /ringmanufaktur/
categories:
- 3D-Druck
- Fertige Projekte
- Wissen
---




Da Ringe aus dem 3D-Drucker sich großer Beliebtheit erfreuen, möchte ich anstatt nur nachzudrucken gern selber welche gestalten. Daher habe ich mit OpenSCAD einen parametrisierten, d.h. einstellbaren Ringgenerator, gebaut, den ich hier kurz vorstellen möchte.





<!-- more -->



{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/image-3.png" >}}
{{< /gallery >}}





Durch die Parameter am Anfang der Datei kann einfach der gewünschte Ring eingestellt werden. Z.B. kann der Ringinnendurchmesser definiert werden (Einstellung hier: 18mm) und auch alle anderen Parameter, wie zum Beispiel:





  * Innendurchmesser des Ringes (16-25mm sinnvoll) 
  * Anzahl der Facetten-Reihen (1 bis 5 sinnvoll)  * Höhe einer einzelnen Reihe ( 1-5mm sinnvoll)  
  * Anzahl der Facetten pro Reihe (6-24 sinnvoll)  
  * Höhe des Steges in der mittleren Reihe (0.01mm für nicht-vorhanden bis 0.6 x Höhe einer einzelnen Reihe sinnvoll)  
  * Zusatzradius: bei vielen Facetten ist die Plastizität relativ gering, daher kann hier für den mittleren Teil einer Reihe ein Zusatz gewählt werden (0.1mm bis 0.25mm 





## Beispiele





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/image-2.png" >}}
{{< /gallery >}}
18mm Innenradius, 1 Reihe, 2mm hoch, 11 Facetten, ohne mittleren Steg.



{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/image-1.png" >}}
{{< /gallery >}}
18mm Innenradius, 2 Reihen, jeweils 5mm hoch, 12 Facetten ringsum, mittleren Steg mit einer Höhe von 30% von 5mm, und ohne Zusatzradius.



{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/image.png" >}}
{{< /gallery >}}
3 Reihen mit Facetten, jede Reihe 3mm hoch (also insgesamt 9mm), 40 Facetten ringsum mit einem Extraradius von 0.15mm für mehr Plastizität.





Die OpenSCAD-Datei findet ihr [hier im GitHub-Repository ringmanufaktur](https://github.com/Eigenbaukombinat/ringmanufaktur). Viel Spaß damit! :)



