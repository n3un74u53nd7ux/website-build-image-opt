---
author: Roberto
date: 2013-06-07 21:26:14+00:00
draft: false
title: 'CNC-Fräse: BZT PF-1410P'
type: page
url: /cnc-frase-bzt-pf-1410p/
categories:
- Maschinen
---

**HARDWARE**



	  * Fräsmotor Kress FME-1050
	  * Spannzangen für 1/8" (3.175mm), 6mm, 1/4"(6.35mm), 8mm Fräser
	  * Standard-Fräser in 1.2mm, 2mm, 3mm lang (15mm), 6mm
	  * Steuerung BZT ST 63.1, 3 Achsen, 6 Ampere, 1/8 Microschritt
	  * Fräse BZT PF-1410P mit Kugelumlaufspindeln
	  * Rechner Intel Atom D510 Dualcore mit [LinuxCNC 2.5 Distribution](http://linuxcnc.org)
	  * Monitor 19" TFT Eizo S1920

**SOFTWARE**



	  * **[QCad](http://qcad.org)** Seit Version 3.1 wieder OpenSource!! ([Download hier](http://qcad.org/de/qcad-downloads-trial))
	  * **Cut2D** Tutorials zu Cut2D: [VIDEO Teil 1](http:/https:/https://www.youtube.com/watch?v=WmbxOpfgGFI), [VIDEO Teil 2](http:/https:/https://www.youtube.com/watch?v=r7Y7ViTkUXA)
	  * **[LinuxCNC](http://linuxcnc.org/)**

**LINKS**



	  * [ein anderer Nutzer mit Aufbau unter LinuxCNC](http://builditbrakeitfixit.wordpress.com/bzt-cnc-router-with-linux-cnc-emc/)
	  * [Infos über Chinaspindeln bei Estlcam.de](http:/https://www.estlcam.de/chinaspindel.php)
	  * [Legierungsübersicht Fräsbarkeit ALUMINIUM](http:/https://www.alu-verkauf.de/Werkstoffe)
	  * [GARANT Zerspanungshandbuch (PDF)](http:/https://www.karstenschneider.de/download-ebook-garant-zerspanungshandbuch.html), Formelsammlung und Praxistabellen

**NACHRÜSTEN EINEN LÄNGEN-SENSORS**

Erstellen von folgenden G-Codes in ~/linuxcnc/nc_files/touch-probe.ngc :

    
    O sub
    G49                                 ( delete previous tool length correction )
    G30                                 ( go to home position )
    
    #<_offset_to_top> = 8.1             ( set touch probe offset relative to table )
    
    G91                                 ( relative movement )
    G38.2 Z-90 F600                     ( touch off fast, max 90mm down )
    (debug, position fast: #5063)       ( output measured offset )
    G0 Z2                               ( back off two millimeters )
    G38.2 Z-10 F30                      ( touch off slowly, max 10mm down)
    (debug, position slow: #5063)       ( output measured offset )
    G90                                 ( absolute movement )
    G30                                 ( return to safe Z )
    G43.1 Z[#5063 - #<_offset_to_top>]  ( set new Z touchoff position )
    
    O endsub
    


Verbinden des PyVCP-Buttons per Befehl in der ~/linuxcnc/configs/bztpf1410p/custom_postgui.hal

    
    # Include your customized HAL commands here
    # The commands in this file are run after the AXIS GUI (including PyVCP panel) starts
    net remote-touch-probe halui.mdi-command-00 <= pyvcp.touch-probe
    
    


Definieren eines Buttons im Frontend in ~/linuxcnc/configs/bztpf1410p/panel.xml

    
    <pyvcp>
      <button>
        <halpin>"touch-probe"</halpin>
        <text>"Länge ermitteln"</text> 
        <pady>20</pady>
        <font>('Fixed',12)</font>
      </button>    
    </pyvcp>
    


In ~/linuxcnc/configs/bztpf1410p/bztp1410p.hal hinzufügen um den Hardware-Pin auf das interne Netz zu legen:

    
    net probe parport.0.pin-12-in => motion.probe-input
    


In ~/linuxcnc/configs/bztpf1410p/bztp1410p.ini anpassen:

    
    [HAL]
    HALFILE = bztpf1410p.hal
    HALFILE = custom.hal
    HALUI=halui
    POSTGUI_HALFILE = custom_postgui.hal
    
    [HALUI]
    MDI_COMMAND = O<touch-probe> CALL
    



FERTIG!

[![touch probe](/wp-content/uploads/2013/06/touch-probe-300x212.png)
](/wp-content/uploads/2013/06/touch-probe.png)
