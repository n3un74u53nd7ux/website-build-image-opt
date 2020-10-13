---
author: Roberto
date: 2019-10-08 22:06:59+00:00
draft: false
title: Temperaturmessung mit Arduino
type: post
url: /temperaturmessung-mit-arduino/
categories:
- Fertige Projekte
tags:
- Arduino
---




Während des Brennens von Keramik möchten wir gern einen Überblick über die Temperatur im Raum über die Zeit haben. Daher habe ich zusammen mit Cornelius kurzerhand einen Arduino dafür genutzt.





<!-- more -->





Folgende Teile werden für den Spaß benötigt:





  * Arduino Uno (ein Nano würde wohl auch gehen)  
  * einen AM2302 Temperatursensor auf Platine mit 3-Pin-Anschluss  
  * ZS-042 Echtzeituhr mit CR2032 Pufferbatterie  
  * MicroSD-Board  
  * ein 4-Ziffer-LED Display TM1637 für die Anzeige vor Ort

Prinzipiell misst auch die Echtzeituhr die Temperatur, um eine genaue Zeiterfassung zu ermöglichen, ich wollte aber auch die Luftfeuchte mit erfassen.

Angeschlossen wird wie folgt:


AM2302 hat 3 Pins: +, OUT, -






    
    <code>  + == PIN2 (per Software auf 5V)
    OUT == PIN3
      - == PIN4 (per Software auf GND)</code>







LED-Display TM1637 hat 4 Pins: CLK, DIO, GND, 5V






    
    <code>CLK == PIN5
    DIO == PIN6
    GND == GND auf der Powerseite
    5V  == 5V auf der Powerseite</code>







Realtime Clock (RTC DS3231 Modul ZS-042): SCL, SDA, VCC, GND (+ weitere, die wir nicht benutzen)






    
    <code>SCL  == PIN SCL
    SDA  == PIN SDA
    3.3V == 3.3V auf der Powerseite vom UNO
    GND  == GND auf der Powerseite vom UNO</code>







MicroSD-Kartenleser: CS, DI, DO, CLK, GND, 5V (+ weitere, die wir nicht benutzen)






    
    <code>CS  == PIN10
    DI  == MOSI == PIN11
    DO  == MISO == PIN12
    CLK == PIN13
    GND == GND neben PIN13
    5V  == 5V auf Powerseite</code>





  {{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5164_b.jpeg" >}}

{{< figure link="/wp-content/uploads/2019/10/IMG_5163_b.jpeg" >}}

{{< figure link="/wp-content/uploads/2019/10/IMG_5161_b.jpeg" >}}

{{< figure link="/wp-content/uploads/2019/10/IMG_5160_b.jpeg" >}}

{{< figure link="/wp-content/uploads/2019/10/IMG_5158_b.jpeg" >}}

{{< figure link="/wp-content/uploads/2019/10/Screenshot-from-2019-10-05-01-12-07.png" >}}
{{< /gallery >}}





Den Quellcode dazu findet ihr in unserem Github im [github-Projekt temperature_logger](https://github.com/Eigenbaukombinat/temperature_logger).







Vielleicht möchte ja jemand das Projekt auf einem ESP8266 fortsetzen, damit die Daten direkt im lokalen WLAN sichtbar werden.







## Update 1







Nach einem Einsatz über 4 Tage gibt es einen Haufen an Messwerten, die wir mit LibreOffice Calc einfach auswerten können. Dazu müssen wir die Punkte in der TXT-Datei nach dem Import noch durch Kommata ersetzen. Dann ergeben sich folgende Diagramme mit Temperatur (blau) und Luftfeuchte (orange). Die Peaks bei beiden Messungen liegen an interessierten Nutzern, die kurz ihre Hände um den Temperatur- und Feuchtigkeitssensor gelegt haben.





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/Screenshot-from-2019-10-09-04-03-26.png" >}}
{{< /gallery >}}






Den Quellcode habe ich im Repository angepasst, dass jetzt nur noch jede Minute ein Messwert protokolliert wird. Die Anzeige wird trotzdem regelmäßig aktualisiert.



