---
author: Anna.Fuchs
date: 2017-02-03 18:21:23+00:00
draft: false
title: Ich bau mir einen Infinity-table
type: post
url: /ich-bau-mir-einen-infinty-table/
categories:
- Fertige Projekte
tags:
- Elektronik
- Glas
- Holz
- LED
---

Wenn ihr wissen möchtet, wie das funktioniert findet ihr nachfolgend eine Schritt für Schritt Anleitung.

[![](/wp-content/uploads/2017/01/Bearbeitung1-1024x618.png)
](/ich-bau-mir-einen-infinty-table/bearbeitung1/)

<!-- more -->

Da ich beim Surfen im Netz auf die Idee gekommen war, hatte ich dort zunächst nach Anleitungen gesucht und eine Vielzahl gefunden.

Dann habe ich mir einen groben Plan erstellt, welche Teile ich brauche.
- einen Tisch mit Glasplatte (gebraucht, über Kleinanzeige im Netz, 25 €)
- einen Spiegel 120x80 cm (=Maß der Glasplatte, gebraucht, über Kleinanzeige im Netz, 10 €)
- Spiegelfolie 2x1 m (Internet, ca. 10  €)
- Holzleisten für den Rahmen (Baumarkt, ca. 5 €)
- MDF Platte, damit der Spiegel nicht so durchhängt (Baumarkt, ca 10 €)
- Sprühlack für die Holzleisten (Baumarkt, ca. 9 €)
- LED Streifen 4 m WS2812B (Internet, ca 90 €)
(den kriegt man auch billiger, aber ich wollte es unbedingt gleich da haben)
- Netzteil (ca. 35 €)
- Arduiono Nano (war im EBK auf Lager, ca. 4 €)


###### Vorbereitung


Welche Folie soll ich nehmen?
Ich hatte im Netz verschiedene Varianten gesehen, mit schwarzer Tönungsfolie und mit Spiegelfolie. Da mir die Lösung mit der schwarzen Folie besser gefiel, ich aber unsicher war, ob das was wird, bestellte ich einfach beide.

**Folie aufziehen**
Fazit: Nichts für Perfektionisten.
Trotzdem ich es in der Küche gemacht habe, vorher gesaugt und gewischt und einige Stunden den Raum nicht betreten hatte; man hat trotzdem immer Staubkrümel mit drin. Wenn das passiert, lebt am besten damit. Denn wenn man die Folie wieder abzieht und versucht es wegzuwischen, wird alles nur noch viel schlimmer.
Mit der schwarzen Folie funktionierte es, wie befürchtet, dann doch nicht so gut. Der Effekt war da, aber leider nur schwach ausgeprägt. Die Reflexion ergab nur ca. 4-5 Reihen, was ca. 10-15 cm entspricht.
Mit etwas mehr Erfahrung habe ich dann doch die Spiegelfolie aufgezogen und der erste Effekttest war vielversprechend.
Nach dem dann alles ca. 1 Monat fröhlich meine Küche blockierte, entschied ich mich dann doch mal los zu legen.


###### Habe ich von diesem "Elektronikkram" alles was ich brauche und wird das auch funktionieren?


[![](/wp-content/uploads/2017/01/DSC_0113-1024x576.jpg)
](/ich-bau-mir-einen-infinty-table/dsc_0113/)

Mit freundlicher Unterstützung von Menschen aus dem Eigenbaukombinat, die mehr von Elektronik verstehen als ich, machten wir also gemeinsam erst mal einen Testaufbau.
Der Arduino Microcontroller steuert den LED Streifen und braucht 5V Strom via Micro-USB, da passt also das Handyladekabel. Der Microcontroller wird zur Datenübermittlung mit dem LED Streifen an den entsprechenden Pins verbunden. Der LED Streifen braucht auch noch Strom und den bekommt er vom Netzteil. Dann hat alles wie erwartet bunt geblinkt.


###### Oh, ich muss in den Spiegel bohren...


Beim Plan die Kabel zu verlegen, fiel auf dass, wenn es hübsch sein soll, ich durch den Spiegel durch muss. Zum Glück gab es zuvor einen Flaschenscheidenworkshop im EBK und ich wusste wie man Glas mit einem Dremel (handlichen Rotationswerkzeug) mit speziellen Diamandaufsätzen bearbeiten kann. Da ich aber trotzdem den Spiegel nicht kaputt machen wollte, habe ich zuvor an einer Glasflasche getestet.


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2017/01/DSC_0114-e1486211981341.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0115-e1486211999959.jpg" >}}
{{< /gallery >}}

Die Leisten habe ich weil es schnell gehen musste und die Dübelfräsen für die kleinen Leisten zu groß waren, einfach zusammen getackert. Das ist nicht schön aber erfüllt seinen Zweck.
[![](/wp-content/uploads/2017/01/DSC_0124-300x169.jpg)
](/ich-bau-mir-einen-infinty-table/dsc_0124/)


###### Die Schichten


Für das weitere Vorgehen mussten jetzt erst Mal die ersten Schichten übereinander gelegt werden.
Tisch                           Holzplatte                Spiegel                     Leisten


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2017/01/DSC_0125-e1486212022918.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0126-e1486212031773.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0127-e1486212039361.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0128-e1486212049356.jpg" >}}
{{< /gallery >}}

Dann konnten wir das Kabel durch den Spiegel ziehen.

[![](/wp-content/uploads/2017/01/DSC_0129-1024x576.jpg)
](/ich-bau-mir-einen-infinty-table/dsc_0129/)

Anschließend mussten die Kabel vom Netzteil und vom Microcontroller an den LED Streifen gelötet werden.


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2017/01/DSC_0134-e1486212073268.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0135-e1486212082924.jpg" >}}
{{< /gallery >}}

Als nächstes konnte ich den LED Streifen einkleben.


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2017/01/DSC_0136-e1486212092197.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0137-e1486212103371.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0138-e1486212112612.jpg" >}}
{{< /gallery >}}

Damit die Glasplatte nicht auf den Holzleisten rutscht, habe ich Klebepunkte dazwischen platziert.

[![](/wp-content/uploads/2017/01/DSC_0139-300x169.jpg)
](/ich-bau-mir-einen-infinty-table/dsc_0139/)

Die Kabel wurden alle zusammen in einer Plastikbox verstaut, damit sie nicht so lose runter hängen.

[![](/wp-content/uploads/2017/01/DSC_0140-300x169.jpg)
](/ich-bau-mir-einen-infinty-table/dsc_0140/)

Letzter Test vorm finalen Zusammensetzen.


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2017/01/DSC_0141-e1486212157198.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0142-e1486212168923.jpg" >}}
{{< /gallery >}}

Und fertig...


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2017/01/DSC_0151-e1486212179842.jpg" >}}
{{< figure link="/wp-content/uploads/2017/01/DSC_0153-e1486212383219.jpg" >}}
{{< /gallery >}}


###### Was noch besser werden kann


Ziel ist es den Prototypen weiter zu entwickeln.
Von der Seite betrachtet sieht man die einzelnen Schichten deutlich und es entweicht ein wenig Licht zur Seite. Zur Lösung soll es einen neuen Holzrahmen geben. Bei diesem werden die Leisten dann gefräst und die Glasplatte wird eingelegt. Weiterhin hat sich gezeigt, dass das Licht des Tisches beim Fernseh gucken zu hell ist, hierfür soll noch ein Dimmer angebaut werden. Noch liegt die Elektronik unter dem Tisch. Die Plastikbox soll unten an der Tischplatte befestigt werden und es soll noch eine Steckerleiste angefügt werden, damit man den Strom dann direkt vom Couchtisch beziehen kann.
