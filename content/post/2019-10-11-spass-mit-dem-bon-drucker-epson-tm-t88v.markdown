---
author: Roberto
date: 2019-10-11 20:50:04+00:00
draft: false
title: Spaß mit dem Bon-Drucker Epson TM-T88V
type: post
url: /spass-mit-dem-bon-drucker-epson-tm-t88v/
categories:
- Fertige Projekte
---




Wir haben als neues Spielzeug einen Bon-Drucker Epson TM-T88V bekommen, wie er auch an normalen Registrierkassen zu finden ist. Er druckt auf 80mm breites Thermopapier in schwarz-weiß und wir können allerhand Blödsinn damit anstellen. Wir werden sehen, wo er landen wird. ;)





<!-- more -->





Als erstes geht es mal an die Anbindung: zum Glück hat er neben einer üblichen seriellen Schnittstelle auch noch einen USB-Anschluss. Damit er auch als normaler Drucker unter Ubuntu funktioniert gibt es Treiber für fast alle Systeme [auf der Epson-Seite.](https://download.epson-biz.com/modules/pos/index.php?page=prod&pcat=3&pid=36)







## Einfach: Drucken per Druckertreiber







Einfach das beiliegende Script ausführen damit der Treiber im passenden Cups-Verzeichnis landet, und dann normal über "Add Printer" z.B. unter Ubuntu den Drucker via USB auswählen und manuell den Treiber über "Epson" und "TM Printer" auswählen.







Als wichtige Optionen sollte noch die Bandbreite (hier 80mm) und die DPI-Zahl im Drucker passend eingestellt werden. Dieser Drucker kann nur 180dpi, auch wenn der Druckertreiber 204dpi als Option zulässt, was aber zu Fehldrucken führt.







{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/printer-config.png" >}}
{{< /gallery >}}







Hier ist auch eingestellt, dass nach Druckende das Band geschnitten wird (paper source: document [feed, cut]), und dass weißes Papier am Ende des Druckes nicht mit "ausgedruckt" wird (paper reduction).







Alternativ kann auch A4 als Papiergröße mit einer 38% Skalierung benutzt werden. Dann "sieht" die benutzte Anwendung A4-Papier und der Druckertreiber skaliert dann passend herunter. Dabei gehen natürlich ein paar Details verloren, aber die "Printer Test Page" lässt sich noch gut erkennen.







Das Handbuch zum Drucker [findet ihr hier.](https://files.support.epson.com/pdf/pos/bulk/tm-t88v_hwum_en_02.pdf) Das hilft bei den vielen DIP-Switches, die unter eine Wartungsklappe verborgen sind. Neben der Konfiguration der seriellen Schnittstelle kann dort z.B. die Druckgeschwindigkeit und die Intensität eingestellt werden.







In das interne Konfigurationsmenü des Druckers gelangst Du, wenn Du beim Einschalten die FEED-Taste gedrückt hälst. Als erstes gibt es einen schönen Printout der eingestellten Optionen sowie die Wahlmöglichkeit weitere Menüpunkte abzurufen. Die Kommunikation erfolgt über den Bon-Ausdruck und durch das x-malige Drücken bzw. längere Gedrückthalten der FEED-Taste.







Wenn alles passend eingestellt ist kann es endlich ans Drucken gehen! Mit der Standard-80mm-Rolle können bis 72mm breite Vorlagen bzw. 512 Pixel pro Zeile 1:1 drucken. Also vorhandene Vorlagen bitte gleich passend erstellen oder entsprechend skalieren. In LibreOffice Writer am besten direkt eine Seite mit Breite 72mm erstellen:







{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/libreoffice.png" >}}
{{< /gallery >}}







Und hier das Ergebnis direkt aus Writer:





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5172b.jpeg" >}}
{{< /gallery >}}





## Schön: Drucken per serieller Schnittstelle







Wer gern Spaß mit der seriellen Schnittstelle hat, hat es etwas einfacher. Der Drucker kann direkt, oder z.B. via seriell-USB-Adapter, angeschlossen werden. Ab da kannst Du einfach per echo auf /dev/ttyUSB0 die gewünschten Zeichen auf's Thermopapier schreiben. Es passen in der Standardeinstellung 42 Zeichen in eine Zeile, im schmalen Font sogar 56 Zeichen. Dem Ausdruck von ASCII-Art jeglicher Art steht also nichts mehr im Wege! :)







Es gibt im Drucker zwei voreingestellte Schriftarten: 12x24 Pixel, und 9x17 Pixel für kleine Schrift. Jede dieser beiden gibt es auch noch in doppelt-hoch/doppelt-breit und doppelt hoch und breit. Bei zu breiter Schrift oder zuviel Text gibt es einen Umbruch und nichts mehr zu erkennen:





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5176b.jpg" >}}
{{< /gallery >}}






Direkt per USB angeschlossen findet sich der Drucker bei mir (Ubuntu 16.04 LTS) unter /dev/usb/lp0, direktes Schreiben per Kommandozeile geht aber  nicht. Daher bleiben wir dafür beim Seriell-auf-USB-Adapter. Ich habe hier einen mit Prolific-Chipsatz benutzt. Für Neugierige hier die Ausgabe von lsusb:






    
    <code>Bus 001 Device 064: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port</code>







Eine Tabelle der üblichen Steuercodes namens ESC/POS gibt es übrigens [hier als PDF zum Herunterladen.](https://content.epson.de/fileadmin/content/files/RSD/downloads/escpos.pdf) Eine ausführlichere Version inklusive Hinweisen für Graphikerstellung gibt es [hier](https://203.72.2.173/nhu/upload/171106230059.pdf). Wenn die Datei nicht mehr verfügbar sein sollte, einfach nach "ESC POS Quick Reference" googlen.







Über die Kommandozeile kann ich also z.B. über den Befehl echo mit Parametern "e" und "n" direkt die ausgewählten Hexadezimal-Codes ausgeben und den zugehörigen Text.






    
    <code>echo -en '\x1B\x21\x01 HalloWelt!\n\n\n\n\n' > /dev/ttyUSB0</code>







Diese Befehlt schreibt ESC+"!"+den Bit-Code für FontB (sonst bleibt alles normal) an den Drucker. Mittels \x39 statt \x01 schalte ich den Drucker auf doppelt breit, doppelt hoch, fett + FontB um. Binär also statt 00000001 die 00111001.





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5174b.jpeg" >}}
{{< /gallery >}}






Jetzt können wir noch eine Geldschublade anschließen. Der Drucker hat einen DK-Connector (normaler RJ-Anschluss) für eine Geldschublade. DK steht hier für "drawer kickout". Dh. wenn ich im Druckertreiber einstelle, dass nach dem Druck die Schublade aufgeht, oder per serieller Schnittstelle den Befehl






    
    echo -en '\x1B\x70\x30\x0A\x0A' > /dev/ttyUSB0







übermittle, kommt die Schublade herausgefahren (ESC + p + 30h + 10*2ms Impuls an + 10*2ms Impuls aus). :)







Manuelles Schneiden des Papieres löse ich aus mittels:






    
    echo -en '\x1D\x56\x30' > /dev/ttyUSB0







Auch noch sehr lustig: Die Erzeugung von 1D-Barcodes, z.B. nach EAN13-System. Der zugehörige Code sieht so aus:






    
    <code> echo -en '\x1D\x6B\x43\x0D1234567890123' > /dev/ttyUSB0</code>







Bedeutung: ESC + k + Nummer des Barcodes (hier für EAN13 67dec = 43h) + 13 Ziffern des Barcodes. Wer nachgerechnet hat: Ja, die letzte Ziffer, die Prüfziffer, stimmt hier nicht, es müsste natürlich eine 8 statt einer 3 sein. ;)





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5175b.jpg" >}}
{{< /gallery >}}





## Drucken: ASCII art







Natürlich können auch direkt Ascii-Dateien per cat auf den Drucker gegeben werden. Dazu sollten wir eine passende Schriftart einstellen. Ein kleiner Test mit der Ziffernfolge 123456789 und einem Leerzeichen als Zehnertrenner ergibt sich folgendes Bild für FontB (oben) und FontA(unten):





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5178b.jpg" >}}
{{< /gallery >}}






Font A erreicht, wie oben bereits angemerkt, 42 Zeichen pro Zeile.  
Font B erreicht 56 Zeichen in einer Zeile bevor der Umbruch einsetzt.  
Ob die Schriftart fett eingestellt ist oder nicht ist dabei egal. Daher können wir für mehr Schwarz auf dem Papier idealerweise die Hervorhebung auch noch anschalten (FontB = +1, Hervorhebung = +8 == 9).






    
    <code>echo -en '\x1B\x21\x09' > /dev/ttyUSB0</code>







Damit die Grafiken möglichst gut aussehen reduzieren wir den Zeilenabstand noch auf das mögliche Minimum (ESC + '3' + 0 Abstand). Leider bleiben trotzdem noch ein paar leere Pixelreihen dazwischen.






    
    <code>echo -en '\x1B30' > /dev/ttyUSB0</code>







Zum Drucken kann jetzt beispielsweise einfach ein Logo als PNG oder JPG genommen, und durch einen Konverter wie [den ASCII Art Generator](https://www.ascii-art-generator.org/) umgewandelt werden. Das kann dann zum Beispiel so aussehen:






    
    <code>MMMMMMMMMMMMMMMMMMWKOxllcloxk0NMMMMMMMMMMMMMMMMMMMMMMMMM
    WXXXXXXNMMMMMMMNOdc;'.......',:okXMMMMMMMNK00000000000XW
    0:,,,,,dNMMMMXx:'................;oKWMMMM0:.'.'...'.'.cK
    0,.....lXMMWk;.....................,oKWMMXc...........:K
    K;.....cXMNd'........................;kNMXc...........cX
    Xc.....,OWx'..........................'dNK:...........oN
    Wx......oO;.....,coxkx:.....':dO000kl,.'xx,..........,OM
    M0;.....,:'..:x0XWMMMM0;.''lOXMMMMMMWO;.,,...........lXM
    MWx'.....''.'kMMMMMMMMXl,lcdNWMMMMMMMWo''...........:0MM
    MMXl.....,:''kMMMMMMMM0lcxdcd0MMMMMMW0c:,..........,kWMM
    MMM0:....'c;.:x0XWMMMMkoOKO;.lNMMN0xl,':,.........'xNMMM
    MMMM0;...'c;...',:ok0kcdWMX:..cdl;'....;;........,xNMMMM
    MMMMW0c..'c;...........xWMXc...........;;.......;kWMMMMM
    MMMMMMXd,.:c...........cXNk,..........':,.....'c0WMMMMMM
    MMMMMMMW0l,,'..........'cl,...........,,.....;xXMMMMMMMM
    MMMMMMMMMW0l,..............................;dKWMMMMMMMMM
    MMMMMWNXKNWWKd:;l:;l:,okclOo;;cc,:c,....,cxKWMMNOddxONMM
    MMMWOl;,,;oKMM0x0ddNkoXNdkMKxoO0lkKc':okKWMMMWO:.....:OW
    MMWx'......lXMWKkoodlloo:cdl::ll:llckNNNNNNNN0:.......cX
    MMWx'......':lllcccxXOc,,,,lkd;',;;oXWOc::::;,........lX
    MMM0:.............l0O;....c0WNd'....c0Nx,............'xW
    MMKc............'o0k,...'lKMMMNx,....;dOk:............;O
    MMO,......,looool:;'....,kWMMMMKc......'cxxddo;.......,k
    MMNd'.....:KMMMK:........lNMMMMO,........cKMMWO:....';xN
    MMMW0o;,,l0WMMMNd,.'cc;;o0WMMMMNkc;;cc,.'lXMMMMNOxxkOXWM
    MMMMMWX00NMMMMMMNOdkXNKXWMMMMMMMMNKKNNOdxXWMMMMMMMMMMMMM</code>







Und ausgedruckt dann so:





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5182b.jpg" >}}
{{< /gallery >}}





Es gibt natürlich viele verschiedene Tools um Logos und ASCII aus Schriftarten zu erstellen, z.B. bei [pastojk.com](https://patorjk.com/software/taag/#p=display&f=Bloody&t=EIGENBAU%0A%20KOMBINAT). Dabei kommt dann zum Beispiel so etwas heraus.





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/Screenshot-from-2019-10-11-22-45-45.png" >}}
{{< /gallery >}}






Leider sind die höheren ASCII-Zeichen offenbar nicht im Standard-Zeichensatz des Druckers enthalten, auch die Auswahl einer anderen Codepage brachte keine Besserung außer deftigen Zeichensalat. Einfachere Logos sind aber problemlos möglich:





{{< gallery caption-effect="fade" >}}
{{< figure link="/wp-content/uploads/2019/10/IMG_5179b.jpg" >}}
{{< /gallery >}}






## Resümee







Ein toller Spaß, dieser kleiner Bondrucker. Offen sind noch folgende Fragen, die auf engagierte Tüftler warten:





  * Wie können wir Grafiken über die Kommandozeile definieren und ausgeben (Befehle "FS q" und "FS p")  * Herausfinden, wie die leeren Pixelreihen zwischen den Zeilen komplett verhindert werden können  * Umschalten des Zeichensatzes, oder definieren eines eigenen, damit auch die high-ASCII Zeichen gedruckt werden können.





Jetzt gucken wir mal, ob der Drucker in der Öffnungsanzeige, oder in der Holzwerkstatt beim Materialabrechnen, oder womöglich beim Mate-Trinken einen künftigen Einsatzzweck findet. Wer auch mal damit spielen möchte kann gern innerhalb der nächsten Wochen einfach zu einem der Hackerspace-Treffen vorbeikommen.







Viel Spaß beim Spielen! :-)



