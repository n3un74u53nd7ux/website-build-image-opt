---
author: floink
date: 2013-02-10 14:08:30+00:00
draft: false
title: 'Pennypusher /Münzschieber - Teil 1: Idee und Prototyp'
type: post
url: /pennypusher-munzschieber-teil-1-idee-und-prototyp/
categories:
- Laufende Projekte
tags:
- Elektronik
- Holz
---

Ziel des Projektes ist es einen Pennypusher (auch bekannt als Coin Pusher oder Münzschieber) zu bauen. Die Dokumentation wird sich über mehrere Beiträge aufteilen. In diesem soll das Projekt erläutert werden.

Für die, die sich unter einem Pennypusher nichts vorstellen können, hier ein kleiner link: [https://vimeo.com/29833767](https://vimeo.com/29833767)

Das Projekt teilt sich in drei Teile:

<!-- more -->

**1. Die Holzarbeiten**

Das Gehäuse und auch die beweglichen Teile sollen aus Multiplex und MDF Holz gefertigt werden. Dies soll weitestgehend Modular geschehen, damit einzelne Teile später leicht ersetzt werden können.

**2. Die Mechanik**

Die Vor- und Zurückbewegung wird über einen Getriebemotor realisiert. Dessen Achse ist mit einer Exzenterscheibe verbunden, welche wiederum den Schlitten antreibt. Ziel ist es, die Exzenterscheibe sowie die Aufnahmen der Kugellager mit dem 3D Drucker (/node/87) zu fertigen.

**3. Die Elektronik**
Folgende Funktionen sollen realisiert werden:



	  * LED Rückwand mit ca 60 LEDs in der rückwärtigen Wand. Die Gehäuse der LEDs sollen gleichzeitig die Münze während dem Fall ablenken. Ziel ist es, die LEDs einzeln anzusteuern und somit auch komplexere Lichtspiele zu realisieren.


	  * Lautsprecher zur Melodiewiedergabe. Dieser hat zwei Aufgaben: Eine Melodie wird ausgelöst, wenn eine Münze in den Auffang fällt, der Spieler also gewinnt. Hierfür muss im Münzauffang ein Bewegungsmelder verbaut werden. Desweiteren soll ein Alarmton wird ausgegeben werden, wenn am Münzschieber gewackelt wird (tilt)


	  * Über einen Tiltsensor wird die Bewegung des Gerätes überwacht, bei zu starkem Wackeln hält das Gerät an, die LEDs Blinken und ein Alarmton wird ausgegeben


	  * Ein PWM-gesteuerte Motor kommt für die Bewegung des Schlittens zum Einsatz. Dieser soll regelbar sein um den Automaten in verschiedenen Schwierigkeitsgraden zu betreiben


	  * LED Beleuchtung des Münzauffangs

Gesteuert werden soll die gesamte Elektonik über einen Arduino Mikrocontroller (https://de.wikipedia.org/wiki/Arduino-Plattform)




## **Der Prototyp**


Angefangen haben wir mit einem Pappmodell um die Dimensionen und die Aufbaureihenfolge abschätzen zu können:

[caption id="attachment_1056" align="alignnone" width="231"][![Pennypusher - Modell](/wp-content/uploads/2013/02/Pennydoku-1-231x300.jpg)
](/wp-content/uploads/2013/02/Pennydoku-1.jpg) Pennypusher - Modell[/caption]

In den nächsten Wochen folgen weitere Beiträge die den weiteren Aufbau dokumentieren.
