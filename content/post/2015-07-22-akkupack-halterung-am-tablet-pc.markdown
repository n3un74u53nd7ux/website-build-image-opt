---
author: gj
date: 2015-07-22 10:27:51+00:00
draft: false
title: Akkupack-Halterung am Tablet-PC
type: post
url: /akkupack-halterung-am-tablet-pc/
categories:
- Fertige Projekte
tags:
- 3D-Drucker
---

Für die Datenerfassung in der Natur, Orientierung im Gelände mit GPS und Dokumentationsfotos nutze ich einen 8"-Tablet-PC. Gerade bei angeschaltetem GPS-Empfänger reicht die Laufzeit des internen Akkus für einen Arbeitstag nicht aus. Da dieser auch nicht auswechselbar ist, musste ein Akkupack her. <!-- more -->

Nur gibt es kein Zeitfenster zum Laden des Tablets zwischendurch. Also musste das Akkupack irgendwie am Tablet befestigt werden. Die einfachste Möglichkeit: An beide Geräte Klettband kleben, schied wegen des Risikos, dass die Garantie erlischt, aus. Außerdem war der Bastler-Ergeiz geweckt.

Mit [FreeCAD](https://www.freecadweb.org/) - das Programm ist gewöhnungsbedürftig, aber nach kurzer Einführung gut nutzbar - konstruierte ich eine Umhüllung für das Akkupack in zwei Teilen:

  * Boden mit Seitenwänden
  * Deckel

[caption id="attachment_9858" align="aligncenter" width="300"][![Akkupack_Konstruktion_Boden_und_Wände](/wp-content/uploads/2015/07/Akkupack_Konstruktion_Boden_und_Wände-300x167.jpg)
](/wp-content/uploads/2015/07/Akkupack_Konstruktion_Boden_und_Wände.jpg) Konstruktionsskizze des Bodens mit Seitenwänden[/caption]



[caption id="attachment_9859" align="aligncenter" width="300"][![Deckel gerendert](/wp-content/uploads/2015/07/Akkupack_Konstruktion_Deckel-300x199.jpg)
](/wp-content/uploads/2015/07/Akkupack_Konstruktion_Deckel.jpg) Deckel gerendert[/caption]

Beide Teile wurden zur Materialersparnis, zur Reduzierung der Druckzeit und zur Belüftung/Kühlung des Akkupacks großzügig mit Leerräumen versehen. Die Wandstärke ist 2mm. In beide Teile wurden Nuten bzw. Federn in 1mm Stärke zur Fixierung beim Kleben eingebaut.

Für die USB-Anschlüsse, die zum Laden von Geräten dienen, wurden ebenfalls passende Öffnungen eingebaut.

[caption id="attachment_9855" align="aligncenter" width="225"][![fertige Rohlinge](/wp-content/uploads/2015/07/Akkupack_3D_Druck_Fertig-225x300.jpg)
](/wp-content/uploads/2015/07/Akkupack_3D_Druck_Fertig.jpg) fertige Rohlinge[/caption]

Der Druck erbrachte beim ersten Versuch ein gut nutzbares Ergebnis und die Konstruktion passte in der Größe perfekt. Die Halterung wurde in Breite und Höhe 0,5 mm größer geplant als das Akkupack.



[caption id="attachment_9854" align="aligncenter" width="300"][![Problemstellen: Zu dünn geplant.](/wp-content/uploads/2015/07/Akkupack_3D_Druck_Fehler-300x198.jpg)
](/wp-content/uploads/2015/07/Akkupack_3D_Druck_Fehler.jpg) Problemstellen: Zu dünn geplant.[/caption]

Kleine Schwachstellen zeigten sich auch sofort. So waren die Nuten und Federn zu klein geplant und wurden nur rudimentär gedruckt. Deswegen habe ich die Federreste vor dem Verkleben der Teile glatt abgeschliffen. Trotzdem funktionierte das Kleben mit Sekundenkleber problemlos.

[caption id="attachment_9857" align="aligncenter" width="300"][![Das Akkupack wird mit einfachen Gummis fixiert](/wp-content/uploads/2015/07/Akkupack_fertig-300x225.jpg)
](/wp-content/uploads/2015/07/Akkupack_fertig.jpg) Das Akkupack wird mit einfachen Gummis fixiert[/caption]

Über die Fixierung des Akkupacks in der Halterung habe ich lange nachgedacht, bin aber zu keiner guten 3D-druckbaren Konstruktion gekommen. Also habe ich einfach Befestigungsmöglichkeiten für normale Küchengummis konstruiert. In der Praxis funktioniert das prima und ist einfach.

Am Boden habe ich eine durchgängige Fläche zur Befestigung des Klettbandes (4 x 8cm) konstruiert. Diese so entstandene Klettfläche hält das Akkupack (im aktuell neuen Zustand des Klettbandes) fast schon zu fest.

[caption id="attachment_9856" align="aligncenter" width="300"][![In Verbindung mit dem Tablet](/wp-content/uploads/2015/07/Akkupack_am_Tablet-300x225.jpg)
](/wp-content/uploads/2015/07/Akkupack_am_Tablet.jpg) In Verbindung mit dem Tablet[/caption]

Beim Tablet gibt es keine aufwändige Konstruktion. Hier habe ich das Klettband einfach an die Schutzhülle des Tablets geklebt. Ein USB-Kabel mit winkligen Anschlüssen gekauft und fertig ist das Ganze.

Nach mehreren Tagen in Nutzung hat sich die Konstruktion bewährt.

Zur Verbesserung gibt es schon einige Ideen, die aber aus Gründen der Ressourcenschonung in Warteschleife liegen, da nicht zwingend nötig:
  * etwas dickere Wände, um Nuten und Federn druckbar zu machen oder eine andere Konstruktion zur seitlichen Fixierung beim Kleben
  * 2 bis 3 mm kürzer, damit der Akkupack durch den Gummi stabiler gehalten wird; momentan ist etwas Spiel
  * Öffnungen für Ladebuchse des Akkupacks und der eingebauten LED-Taschenlampe frei lassen (wurde aus Unsicherheit mit Blick auf die Stabilität in der vorliegenden Version vermieden)
  * Bessere Verteilung der Öffnungen im Deckel, damit der Druckschalter zur Ladeanzeige besser zugänglich wird und evtl. auch freilassen der länglichen LED zur Ladestandsanzeige
  * seitliche Öffnungen eher als Ellipsen formen und mit weniger Material bei den Stegen; das müßte zur Stabilität auch ausreichen, sieht gefälliger aus und reduziert das Material
  * seitlich kleine Klips als Halterungen für das Ladekabel und ein USB-Adapterkabel, welche immer mit dabei sein sollen

