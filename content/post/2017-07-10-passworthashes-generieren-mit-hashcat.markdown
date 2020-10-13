---
author: Christian
date: 2017-07-10 14:55:07+00:00
draft: false
title: Passworthashes generieren mit Hashcat
type: post
url: /passworthashes-generieren-mit-hashcat/
categories:
- Fertige Projekte
- Wissen
---

Vorgeschichte:
Anfang des Jahres haben wir im Rahmen unserer [Techniknotaufnahme](/technik-notaufnahme/) ein altes, teildefektes, Notebook eingemottet und durch ein gebrauchtes Businessgerät ersetzt.<!-- more -->
In dem Zuge wurde ein Ubuntu samt Verschlüsselung des Benutzerverzeichnisses, via ecryptfs, installiert.
Natürlich gab es auch gleich einen Crashkurs in der richtigen Wahl eines sicheren und leicht merkbaren Passwortes ([xkcd password strength](/xkcd.com/936/) ).
Soweit alles wie immer.

In der nachfolgenden Zeit wurde das Notebook jedoch, aufgrund eines längeren Auslandaufenthaltes, etwa drei Monate nicht benutzt.
Und es kam wie es kommen musste: das Loginpasswort, und damit auch das Passwort zum Entschlüsseln der Daten, wurde vergessen.

Da es von dem Passwort kein Backup gibt und die Wiederherstellungspassphrase der Verschlüsselung auch nicht aufzutreiben war, blieb nur eine sinnvolle Lösung:
Ein vermeintlicher Rumpf des Passwortes war in der Erinnerung noch vorhanden, was ein errechnen des Passwortes unter Umständen einfacher macht.

Das Tool der Wahl war [hashcat](/hashcat.net/) .

Also los:

Loginpasswörter werden unter Linux nicht im Klartext abgespeichert.
Stattdessen wird ein Hash des Passwortes in der Datei _/etc/shadow_ abgelegt:

`hashtest:$6$AR/Jnfuiquw1FLYP$FWSpoRcReZYfLX3EGdJOCYAaR9eZhMJe3JtYrTs/GvgsqSSJ.XY1VHO8AwXfVXVk/hJTwoHrqCJ4Xn02O//5F.:17344:0:99999:7:::`

Die auf den ersten Blick chaotisch aussehende Zeichenkette setzt sich aus mehreren Teilen zusammen, die durch _$_ und _:_ Zeichen begrenzt werden.
Für uns relevant ist der Teil zwischen dem ersten und dem zweiten Doppelpunkt. Dieser setzt sich wie folgt zusammen:

`$6$AR/Jnfuiquw1FLYP$FWSpoRcReZYfLX3EGdJOCYAaR9eZhMJe3JtYrTs/GvgsqSSJ.XY1VHO8AwXfVXVk/hJTwoHrqCJ4Xn02O//5F.`

$Hashverfahren$Salt$Hash

Das Hashverfahren 6 steht für das Linuxanmeldesystemen mit dem Hashverfahren SHA512.
Der Salt ist eine Zeichenkette, um die das Passwort vor dem Erzeugen des Hashes ergänzt wird. Der daraus entstandene Hash kann dadurch nicht in einer Rainbowtable gefunden und das Passwort somit viel leichter geknackt werden.
Für weitere Informationen zu dem Thema möchte ich auf Wikipedia und einschlägige Literatur verwiesen.

Vorbereitend werden noch zwei Textdateien angelegt, _hash.lst_ für den/die Hash/es (siehe oben relevanter Teil) und _cracked.txt_ für die errechneten Ergebnisse.

Um ein sinnvolles Muster für das Zielpasswort festzulegen stehen in hashcat sogenannte Masken zur Verfügung. Die erlauben es bestimmte Muster für ein Passwort festzulegen und nur innerhalb dieses Musters die Variationen auszurechnen.
Das ist wichtig und sinnvoll um die Berechnungen in machbaren Grenzen zu halten - ich spare mir an der Stelle die Hochrechnung der möglichen Variationen.

Zur Verfügung stehen:
`
?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
?a = ?l?u?d?s
?b = 0x00 - 0xff`

Außerdem können bis zu 4 verschiedene eigene Zeichenkombinationen festgelegt werden, mehr dazu unter [/hashcat.net/](/hashcat.net/wiki/doku.php?id=mask_attack) .

Man gibt nun für jedes Zeichen die entsprechende Abkürzung an und bildet so das vermutete Passwort ab.

Hier ein Beispiel:

Für das Passwort _pass123_ steht die Maske _?l?l?l?l?d?d?d_.

Wichtig: Kennt man die Anzahl der Zeichen des Zielpasswortes nicht müssen alle Varianten separat durchgerechnet werden.

Man könnte natürlich auch sämtliche Zeichen an jeder Stelle berechnen, aber das erhöht die Anzahl der Möglichkeiten, und damit die Zeit um diese zu berechnen, erheblich.

Mit diesen Informationen kann nun der Bruteforceangriff in Form der "mask attack" mit hashcat durchgeführt werden:

`hashcat -m 1800 -a 3 -o crackecd.txt --remove hash.lst ?l?l?l?l?d?d?d`

Die Option -m 1800 steht für das oben genannte Linuxanmeldeverfahren mit SHA512, -a 3 definiert Bruteforce als Angriffsmodus, -o und --remove verweisen auf die beiden Textdateien, zum Schluss folgt die Maske für das Zielpasswort.

Da meine Grafikkarte, eine AMD R9 280X, nur ca _45000 Hashes pro Sekunde_ berechnen kann habe ich die Maske für das Beispielpasswort angepasst und das erste Zeichen als _p_ definiert:

`p?l?l?l?d?d?d`

Die Berechnung hätte sonst mehrere Stunden gedauert.

Die Berechnung via CPU kann man getrost ignorieren, ein AMD Ryzen R6 1600X (6Kerne, 12Threads) schafft nicht einmal 1000 Hashes pro Sekunde zu berechnen.

`F:\progs\hashcat-3.5.0>hashcat64.exe -m 1800 -a 3 -o crackecd.txt --remove hash.lst p?l?l?l?d?d?d
hashcat (v3.5.0) starting...
OpenCL Platform #1: Advanced Micro Devices, Inc.
===========================================p=====
* Device #1: Tahiti, 2816/3072 MB allocatable, 32MCU
* Device #2: AMD Ryzen 5 1600X Six-Core Processor , skipped.
  
Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
  
Applicable optimizers:
* Zero-Byte
* Single-Hash
* Single-Salt
* Brute-Force
* Uses-64-Bit
  
Watchdog: Temperature abort trigger set to 90c
Watchdog: Temperature retain trigger set to 75c
  
[s]tatus [p]ause [r]esume [b]ypass [c]heckpoint [q]uit =>
  
Session..........: hashcat
Status...........: Running
Hash.Type........: sha512crypt $6$, SHA512 (Unix)https://www.debian.org/distrib/packages
Hash.Target......: $6$AR/Jnfuiquw1FLYP$FWSpoRcReZYfLX3EGdJOCYAaR9eZhMJ...O//5F.
Time.Started.....: Tue Jun 27 11:43:02 2017 (2 secs)
Time.Estimated...: Tue Jun 27 11:49:42 2017 (6 mins, 38 secs)
Guess.Mask.......: p?l?l?l?d?d?d [7]
Guess.Queue......: 1/1 (100.00%)
Speed.Dev.#1.....: 44120 H/s (7.90ms)
Recovered........: 0/1 (0.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 0/17576000 (0.00%)
Rejected.........: 0/0 (0.00%)
Restore.Point....: 0/17576000 (0.00%)
Candidates.#1....: pari198 -> przl667
HWMon.Dev.#1.....: Temp: 55c Fan: 33% Util: 64% Core:1100MHz Mem:1500MHz Bus:16
  
Cracking performance lower than expected? Append -w 3 to the commandline.
  
Session..........: hashcat
Status...........: Cracked
Hash.Type........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$AR/Jnfuiquw1FLYP$FWSpoRcReZYfLX3EGdJOCYAaR9eZhMJ...O//5F.
Time.Started.....: Tue Jun 27 11:43:02 2017 (41 secs)
Time.Estimated...: Tue Jun 27 11:43:43 2017 (0 secs)
Guess.Mask.......: p?l?l?l?d?d?d [7]
Guess.Queue......: 1/1 (100.00%)
Speed.Dev.#1.....: 47952 H/s (7.88ms)
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 1966080/17576000 (11.19%)
Rejected.........: 0/1966080 (0.00%)
Restore.Point....: 1835008/17576000 (10.44%)
Candidates.#1....: phtm456 -> ptmw123
HWMon.Dev.#1.....: Temp: 65c Fan: 33% Util: 97% Core:1100MHz Mem:1500MHz Bus:16
  
Started: Tue Jun 27 11:43:01 2017
Stopped: Tue Jun 27 11:43:45 2017`

Der Hash des Passwortes wurde erfolgreich in 44 Sekunden berechnet, prognostiziert waren 6-7 Minuten.

Man findet jetzt in der Textdatei cracked.txt folgendes Ergebnis:

`$6$AR/Jnfuiquw1FLYP$FWSpoRcReZYfLX3EGdJOCYAaR9eZhMJe3JtYrTs/GvgsqSSJ.XY1VHO8AwXfVXVk/hJTwoHrqCJ4Xn02O//5F.:pass123`

Der Hash aus der Textdatei hash.lst wurde automatisch gelöscht.
