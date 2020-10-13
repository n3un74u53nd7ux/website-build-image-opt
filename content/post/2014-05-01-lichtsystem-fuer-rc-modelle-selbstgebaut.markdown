---
author: nilo
date: 2014-05-01 10:03:48+00:00
draft: false
title: Lichtsystem für RC-Modelle selbstgebaut
type: post
url: /lichtsystem-fuer-rc-modelle-selbstgebaut/
categories:
- Fertige Projekte
tags:
- Elektronik
- RC-Modellbau
---

Für meinen neuen Drifter wollte ich, wie sich das gehört, eine Beleuchtung einbauen. Da die am Markt erhältlichen Lösungen erstens zu unflexibel und zweitens viel zu teuer sind, habe ich aus vorhandenem Material an einem Abend selbst eine Arduino-basierte Beleuchtung gebaut.<!-- more -->


## Hardware


Als Basis nehme ich einen "Arduino Pro Mini" (oder kompatibel, z.B. [Wattuino Pro Mini](https://www.watterott.com/de/Wattuino-pro-mini-5V-16MHz) für 10€). Wichtig ist hierbei, dass es sich um die 5V-Variante handelt. Allerdings wird für den Pro Mini noch ein USB-Programmieradapter benötigt, der nochmal ca. 5€ kostet (jedoch im EBK selbstverständlich vorhanden ist).


[![Arduino Pro Mini](/wp-content/uploads/2014/05/IMG_70382.jpg)
](/wp-content/uploads/2014/05/IMG_70382.jpg)


Alternativ kann auch ein "Arduino Nano" (oder kompatibel) genommen werden. Diese Variante hat den Vorteil, einen USB-Anschluss zu besitzen, so dass kein Programmieradapter benötigt wird.

Die LEDs werden aus einem flexiblen LED-Streifen mit "WS2812" RGB-Leds herausgeschnitten. Es handelt sich hier um LEDs in SMD-Gehäusen mit integriertem Controller-Chip. Dies hat den Vorteil, dass man beliebig viele dieser LEDs einfach hintereinander schalten kann, und jeweils nur 3 Leitungen braucht (Masse, Stromversorgung und Daten).


[![LED Streifen](/wp-content/uploads/2014/05/IMG_70391.jpg)
](/wp-content/uploads/2014/05/IMG_70391.jpg)


Ein Stück LED-Streifen mit 20 LEDs kostet bei ebay ca. 10€.

Für die Auswahl der Beleuchtungsprogramme benutze ich den 3. Kanal meiner Spektrum DX3C. Hier kann ich konfigurieren, dass ich mittels "Schalter A" 3 Zustände einstellen kann.


[![Einstellung Spektrum DX3C](/wp-content/uploads/2014/05/IMG_70393.jpg)
](/wp-content/uploads/2014/05/IMG_70393.jpg)


Für die Stromversorgung von Arduino und LEDs wird ebenfalls der 3. Kanal des Empfängers benutzt. Eine LED verbraucht maximal 20mA, der Arduino liegt bei maximal 150mA. Ich komme also mit 10 verbauten LEDs auf maximal 350mA.

Soweit die Theorie, jetzt wird der Lötkolben geschwungen! Ich habe mich dazu entschlossen, alle Kabel anzulöten, damit der gesamte Controller nachher schön flach wird.

Von einem kaputten Servo habe ich mir ein Kabel abgeschnitten, welches ich an den Arduino löte:
Das Kabel mit dem Signal kommt an den Pin 2, hier wird später im Programm der Wert eingelesen, den der Empfänger liefert. Die Masseleitung wird mit der Masse des Arduino verbunden, und die 5V-Leitung mit dem Stromeingang des Arduino (VCC).

Ein weiteres abgeschnittenes Servokabel wird als Anschluss für die LEDs vorgesehen, auch hier wird wieder an Masse und VCC angelötet. Die Leitung für die LED-Daten löte ich an Pin 6. Um Beschädigungen durch Verpolung zu vermeiden, lege ich die Masse auf den mittleren Pin. Somit kann maximal Daten und Stromversorgung vertauscht werden, und das ist ungefährlich.


[![Verkabelter Arduino](/wp-content/uploads/2014/05/IMG_70396.jpg)
](/wp-content/uploads/2014/05/IMG_70396.jpg)


Um den Arduino programmieren zu können, muss noch eine 5-polige Stiftleiste an die vorgesehene Stelle gelötet werden. Dies entfällt natürlich bei der Variante mit integriertem USB-Port.

Nachdem sichergestellt wurde, dass alles funktioniert, wird das Ganze noch in ein Stück breiten Schrumpfschlauch eingepackt, damit es keine Kurzschlüsse geben kann.


[![](/wp-content/uploads/2014/05/IMG_70413.jpg)
](/wp-content/uploads/2014/05/IMG_70413.jpg)


Nun müssen natürlich noch die LEDs verdrahtet und in der Karosserie eingeklebt werden. Es empfiehlt sich hier, vor dem Einkleben zu löten, speziell wenn mit Heißkleber gearbeitet werden soll. Ich habe dafür neues Flachbandkabel von der Rolle verwendet, man kann aber auch alte Kabel recyclen. Vermutlich eigenen sich alte IDE-Festplattenkabel ganz gut.


[![Karosserie innen mit verkabelten Lichtern](/wp-content/uploads/2014/05/IMG_70399.jpg)
](/wp-content/uploads/2014/05/IMG_70399.jpg)


WICHTIG: Die LEDs haben einen Ein- und einen Ausgang, meistens durch einen Pfeil gekennzeichnet. Dies muss beachtet werden, sonst funktioniert nachher gar nichts.

Während man die LEDs verkabelt und einklebt empfiehlt es sich eine Skizze zu erstellen, und die LEDs durchzunummerieren. Praktischerweise fängt man dabei bei 0 an, das entspricht dann der Nummerierung, die man später beim Programmieren verwendet.

An den Anfang des LED-Strangs löte ich aus einem 3er-Stück 2,54mm Pfostenleiste einen kleinen Stecker und isoliere diesen mit einem Stück Schrumpfschlauch.


[![Anschluss](/wp-content/uploads/2014/05/IMG_70402.jpg)
](/wp-content/uploads/2014/05/IMG_70402.jpg)





## Software


Hier sind der Kreativität natürlich keine Grenzen gesetzt. Ich habe zunächst nur ein einfaches Programm geschrieben, welches 3 verschiedene Beleuchtungsmuster auswählbar macht.

Das Programm besteht aus 2 Teilen: Einlesen der Werte vom Empfänger und Ansteuern der LEDs.

Für das Einlesen des Signals vom Empfänger wird die Funktion pulseIn verwendet. Das Resultat wird dann verglichen, und je nach Wert die Funktion zum "Abspielen" des jeweiligen Beleuchtungsprogramms aufgerufen.

    
    void loop() {
        ch1 = pulseIn(2, HIGH, 25000); 
        if (ch1 < 1200) {
          normal();
        } else if (ch1 < 1600) {
          strobo();
        } else {
          police();
        }
    }


Das Ansteuern der LEDs ist dank der Adafruit_NeoPixel-Library sehr einfach. Zuerst wird der LED-Streifen mit Angabe der LED-Anzahl (10) und dem Pin an dem die LEDs angeschlossen sind (6) initialisiert:

    
    Adafruit_NeoPixel strip = Adafruit_NeoPixel(10, 6, NEO_GRB + NEO_KHZ800);


Dann kann mittels der setPixel-Funktion die Farbe für eine einzelne LED gesetzt werden. Im folgenden Beispiel wird die Farbe für die erste LED in der Reihe auf blau gesetzt.

    
    strip.setPixelColor(0, strip.Color(0,0,255));


Sobald alle Farben für einen Schritt gesetzt sind können die LEDs aktualisiert werden.

    
    strip.show()


Pausen können mit der delay-Funktion eingefügt werden. Als Argument werden Millisekunden angegeben.

    
    delay(500)


Den vollständigen Code gibt es bei [github](https://github.com/Eigenbaukombinat/rclight).


## Weiterentwicklung


Mit 2 weiteren Kabeln kann man mit dem Arduino noch das Lenk- und das Gas-Signal abgreifen und abhängig davon weitere Beleuchtungsfunktionen einbauen (Aufblenden bei Vollgas, Blinken bei Lenkeinschlag, Bremslicht, ...).

Das Non-Plus-Ultra wäre natürlich die Integration eines SD-Karten-Lesers, damit man die Lichtprogramme auf dem PC bearbeiten oder "an der Strecke" austauschen kann, ohne den Arduino neu programmieren zu müssen.


## Materialliste





	  * Arduino Nano oder Pro Mini (ab 3€ aus China, ansonsten ca. 10€)
	  * LEDs (20 Stück für 10€ oder 10 Stück für 7€)
	  * Kabel und Stecker (Recycling)

Gesamtkosten: zwischen 10€ und 20€.

<iframe src="https://player.vimeo.com/video/93433151" allowfullscreen="" width="500" frameborder="0" height="282"></iframe>

[RC LIGHT in Action](https://vimeo.com/93433151) from [Eigenbaukombinat](https://vimeo.com/eigenbaukombinat) on [Vimeo](https://vimeo.com).
