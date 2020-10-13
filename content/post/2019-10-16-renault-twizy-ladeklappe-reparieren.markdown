---
author: Johann
date: 2019-10-16 10:00:23+00:00
draft: false
title: 'Renault Twizy: Ladeklappe reparieren'
type: post
url: /renault-twizy-ladeklappe-reparieren/
categories:
- 3D-Druck
- Fertige Projekte
- Reparatur
---




Beim Renault Twizy meiner Eltern, der ein super Stadtflitzer mit Elektroantrieb ist, gehen leider bei der Ladeklappe oft die Kunststoffscharniere kaputt. Als Ersatzteil müsste eine komplett neue Klappe eingebaut werden, die über 40 EUR kostet und extra aus Frankreich angeliefert werden muss. Da ich gerne mit FreeCAD konstruiere, und wir ja 3D-Drucker im Eigenbaukombinat haben, war die Lösung naheliegend!





<!-- more -->



  {{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_20191015_132643.jpg" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_20191015_132703-1.jpg" >}}
{{< /gallery >}}






Die Konstruktion in FreeCAD habe ich nach den abgebrochenen Scharnieren dimensioniert.





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/freecad.png" >}}
{{< /gallery >}}






In FreeCAD hab ich dann eine Zeichnung erstellt und eine STL-Datei zum Drucken exportiert. Die Datei wurde in Cura gesliced und so für den Drucker vorbereitet.





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5474.jpg" >}}
{{< /gallery >}}





Auf zum 3D-Drucker! Wir haben ein PET-G-Filament, das wir bei 240°C drucken. Insgesamt werden zwei Teile benötigt.





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5477.jpg" >}}
{{< /gallery >}}





Etwas Nacharbeit mit einer kleinen Feile oder nachbohren und die Löcher passen perfekt und die Muttern können mit etwas Kraft reingedrückt werden. 





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5480.jpg" >}}
{{< /gallery >}}






Nach der Montage sieht es so aus:





  {{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/twizzy-ladeklappeoffen.jpg" >}}
{{< figure link="/wp-content/uploads/2019/10/twizzy-scharnieremontiert.jpg" >}}
{{< figure link="/wp-content/uploads/2019/10/twizzy-klappezu.jpg" >}}
{{< /gallery >}}





Ich habe noch zwei Durchgangslöcher in die Klappe gebohrt um die Scharniere daran festzuschrauben. Durch die Bruchstellen der alten Scharniere erkennt man sehr gut, wo die neuen hingehören. Zur Befestigung werden pro Scharnier eine M4-Schraube aus Edelstahl in 20 mm Länge mit passender Unterlegscheibe, sowie die Mutter, die vorher in das Scharnier gepresst wurde, benötigt.







Die Gesamtkosten für die Reparatur belaufen sich somit auf 2€ für die 3D-gedruckten Teile (10g pro Stück) und etwas weniger als 1 EUR für die Schrauben mit Scheiben.







Hier noch die Datei zum Bearbeiten [als FreeCAD-Datei](/wp-content/uploads/2019/10/Scharnier_Twizy.FCStd) oder direkt zum Nachdrucken [als STL-Datei](/wp-content/uploads/2019/10/Scharnier_Twizy.stl). Ansonsten findet ihr die [aktuellste Version im GitHub-Repository](https://github.com/Eigenbaukombinat/renault_twizy_hinge).



