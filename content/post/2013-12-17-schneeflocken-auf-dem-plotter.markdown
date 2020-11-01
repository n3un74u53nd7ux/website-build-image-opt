---
author: Roberto
date: 2013-12-17 14:15:24+00:00
draft: false
title: Schneeflocken auf dem Plotter
type: post
url: /schneeflocken-auf-dem-plotter/
categories:
- Fertige Projekte
tags:
- Plotter
---

Bewaffnet mit dem [Schneeflockengenerator ](https://www.evilmadscientist.com/2008/vector-snowflake-application/)aus dem letzten [Blick über den Tellerrand](/blick-ueber-den-tellerrand-40/) habe ich mich direkt ans Plotten gewagt. Eine einfache Flocke ist schnell erzeugt und lässt sich problemlos in [Inkscape](https://inkscape.org) öffnen.<!-- more -->

Damit wir auch ohne proprietäre Software plotten können, benutze ich [die aktuelle Entwicklerversion r12832 von Inkscape für Windows](https://www.oss-marketplace.com/index.php/downloads-mainmenu-63/func-startdown/101/), in der bereits eine Erweiterung zur Plotteransteuerung via HPGL und DMPL integriert ist.

Unser HELO Plotter bereitet uns noch ein paar Bauchschmerzen mit komplexeren Plots, einfache Formen und Schriftzüge funktionieren aber problemlos. Hier kurz im Überblick die Einstellungen für unseren Plotter. Im Wesentlichen habe ich alles erstmal auf den Standardeinstellungen belassen, einzig die Ausrichtung wird noch um 90° gedreht. Dann entspricht der am Plotter gesetzte Nullpunkt dem rechten unteren Ende der Graphik. Weitere Optimierungen von overcut etc. werden aber sicher noch folgen.

[![snowflake plotter](/wp-content/uploads/2013/12/snowflake-plotter-1024x632.png)
](/wp-content/uploads/2013/12/snowflake-plotter.png)WICHTIG: In Inkscape unbedingt als Standardeinheit im Dokument "px" (also Pixel) eingestellt lassen. Sonst funktioniert die Umrechnung durch das Plotterplugin aktuell nicht korrekt und die Grafik wird viel zu groß oder zu klein geplottet. Die Skalierung auf das gewünschte Finalmaß könnt ihr natürlich wie gewohnt in mm oder cm vornehmen.

Und nach langer Rede endlich ein paar Ergebnisse. Obige Schneeflocke, und auch ein Namensschriftzug mit einer Scriptschriftart namens Pacifico.

[![plotter_snowflake](/wp-content/uploads/2013/12/plotter_snowflake-1024x682.jpg)
](/wp-content/uploads/2013/12/plotter_snowflake.jpg)

[![plotter_juliane](/wp-content/uploads/2013/12/plotter_juliane-1024x682.jpg)
](/wp-content/uploads/2013/12/plotter_juliane.jpg)

[![plotter_juliane_snowflake](/wp-content/uploads/2013/12/plotter_juliane_snowflake-1024x682.jpg)
](/wp-content/uploads/2013/12/plotter_juliane_snowflake.jpg)
