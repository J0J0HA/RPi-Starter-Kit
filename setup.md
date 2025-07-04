# Setup

## Einrichten

1. Gehe mit dem Befehl `cd` in einen Ordner deiner Wahl (Bspw. `Desktop`).
1. Führe  
  `git clone https://github.com/GollumBree/RPi-Starter-Kit/`  
  aus.
1. Gehe mit `cd RPi-Starter-Kit` in den neuen Unterordner
1. Führe `install-packages.sh` aus, wenn alle Bibliotheken automatisch installiert werden sollen. Alternativ stehen in den Dokumentation der jeweiligen Scripts die nötigen Bibliotheken.

## Ausführen der Beispiele

## IR Remote

1. Füge `ir-keytable -p all` ans Ende der Datei `/etc/rc.local` an.
2. Füge `dtoverlay=gpio-ir,gpio_pin=12` ans Ende der Datei `/boot/firmware/config.txt`
3. Führe `sh install-ir.sh` aus

[Quelle](https://ignorantofthings.com/receiving-infrared-on-the-raspberry-pi-with-python/)
