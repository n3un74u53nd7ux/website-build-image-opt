---
author: nilo
date: 2015-01-29 17:23:43+00:00
draft: false
title: Einstellbares Stimmungslicht
type: post
url: /einstellbares-stimmungslicht/
categories:
- Fertige Projekte
tags:
- CNC
- Elektronik
- Holz
---

Für gemütliche Abende haben wir uns eine kleine Lampe gebaut, die je nach Stimmung eingestellt werden kann.Die Steuerung realisierten wir mit einem Arduino, an dem zwei Drehregler und ein Schalter, sowie ein paar WS2812 RGB LEDs angeschlossen wurden. <!-- more -->

Über die Drehregler können Parameter wie Helligkeit, Sättigung, Farbwechsel-Geschwindigkeit oder Lichtfarbe eingestellt werden. Mittels des Kippschalters kann zwischen drei verschiedenen Programmen gewechselt werden: Regenbogen-Farbwechsel, frei einstellbare Farbe und wechselnde Zufallsfarben.

Das Gehäuse entstand an der CNC-Fräse. Die Leuchtflächen wurden von innen mit LEE-Diffusionsfolie beklebt. Im Fuß der Lampe finden der Arduino sowie das Batteriefach Platz. Die Drehknöpfe für die Regler haben wir auf dem 3D-Drucker hergestellt.

Den Deckel haben wir nicht verklebt, so bleibt er abnehmbar und die Lampe zeichnet dann wunderschöne psychedelische Farbmuster an die Decke.


{{< gallery caption-effect="fade" >}}
  {{< figure link="/wp-content/uploads/2015/01/IMG_84059.jpg" >}}
{{< figure link="/wp-content/uploads/2015/01/IMG_84045.jpg" >}}
{{< figure link="/wp-content/uploads/2015/01/IMG_84054.jpg" >}}
{{< /gallery >}}

Das MDR Fernsehen hat den Bau der Lampe begleitet. [Im Archiv der Sendung "Donnerwetter" ist der Beitrag vom 29. Januar nach Ende der Sendung abrufbar.](https://www.mdr.de/donnerwetter/index.html)

Den Sourcecode für den Arduino zum Nachbauen gibt es hier: [lampe.ino.zip](/wp-content/uploads/2015/01/lampe.ino_.zip)
