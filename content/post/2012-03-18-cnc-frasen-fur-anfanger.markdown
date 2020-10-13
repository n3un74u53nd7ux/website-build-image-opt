---
author: marian
date: 2012-03-18 15:32:07+00:00
draft: false
title: CNC-Fräsen für Anfänger
type: post
url: /cnc-frasen-fur-anfanger/
categories:
- Maschinen
---

In diesem Artikel möchten wir eine kleine Einführung in die Kunst des CNC-Fräsens geben. Unser Beispielprojekt ist ein kleiner Schrank für ein Puppenhaus (Maßstab 1:24), der aus 4 mm dickem Birke MPX gefräst werden soll.

Am Anfang steht die Zeichnung, die in einem CAD-Programm erstellt wird. Wie man sieht, besteht der Schrank aus mehreren Teilen: den Seitenteilen (in der Zeichnung weiß), Vorder- und Rückseite (grün) und Zwischenböden (rot). Damit die Teile zusammenhalten, haben wir Nasen und Vertiefungen in den Teilen vorgesehen - anhand der Zeichnung kann man schon erkennen, wo die Teile stecken sollen.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese1alt.png" >}}
{{< /gallery >}}

Allerdings ist in dieser Zeichnung noch keine Information darüber enthalten, wie sie interpretiert werden soll. Wir müssen also festlegen, welche Vektoren durchgefräst werden sollen (wie etwa die Außenkonturen der Teile), welche nur als Nuten eingefräst werden sollen (die Dekorationen am Unterteil des Schranks) und wo die gesamte Fläche geräumt werden soll (die Vertiefungen). Dazu brauchen wir ein weiteres Programm.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese2.png" >}}
{{< /gallery >}}

Eine Kleinigkeit müssen wir noch beachten: Würden wir die einzelnen Teile vollständig ausfräsen, würden sie sich selbstständig machen, wenn sie keine Verbindung zum umgebenden Holz mehr haben. Dem kann man entweder mit einem Vakuumtisch (den wir nicht haben) begegnen oder damit, dass man Tabs setzt, also kleine Verbindungsstücke, die erhalten bleiben sollen. Nachdem wir unsere Pfade fertig berechnet haben, können wir uns eine Vorschau anzeigen lassen.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese3.png" >}}
{{< /gallery >}}

Wir erhalten nun eine fertige Datei, die G-Code-Befehle enthält - also genau festlegt, was die Maschine machen soll. In der Zwischenzeit haben wir schon das Holzstück auf dem Frästisch aufgespannt.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese4.jpg" >}}
{{< /gallery >}}

Jetzt ist Millimeterarbeit gefragt. Die Fräse weiß nämlich nicht, wie hoch das Werkstück im Vergleich zum Nullpunkt ist. Wir könnten natürlich einfach den Startpunkt unter Zuhilfename der Dicke des Holzes berechnen, haben aber die Erfahrung gemacht, dass als "4 mm dick" verkauftes Holz gerne auch einmal 3,8 oder 4,2 mm dick sein kann, und gehen daher auf Nummer sicher. Die Fräse lässt sich in Zweihundertstelmillimeterschritten bewegen - das ist genauer als jeder Messschieber.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese5.jpg" >}}
{{< /gallery >}}

Los geht's!

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese6.jpg" >}}
{{< /gallery >}}


Der fertig gefräste Bogen, gut sichtbar die Tabs. Nicht im Bild: etwa hundert Gramm Holzstaub.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese7.jpg" >}}
{{< /gallery >}}

Zunächst muss das Holz noch glattgeschliffen werden...

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese8.jpg" >}}
{{< /gallery >}}

...damit wir, auf viel weniger brachiale Weise als es dieses Bild suggerieren mag, die einzelnen Teile entnehmen können.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese9.jpg" >}}
{{< /gallery >}}


Nach dem erfolgreichen Brechen der Tabs müssen wir noch die letzten Reste wegschleifen.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese10.jpg" >}}
{{< /gallery >}}

Zum Schluss kommt noch der Zusammenbau. Im Bild ist der Schrank nur zusammengesteckt; sinnvollerweise verleimt man die einzelnen Teile, um den Schrank stabiler zu machen.

{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2013/02/fraese11.jpg" >}}
{{< /gallery >}}
