# Einrichten des Raspberry PIs

Bevor du mit loslegen kannst, musst du ein paar Sachen einstellen, damit alles funktioniert.

## Update & Upgrade

Zuerst solltest du sicherstellen, dass dein Raspberry PI auf dem neuesten Stand ist. Das geht mit den folgenden Befehlen:

```bash
sudo apt update
sudo apt upgrade
```

Das erste Kommando aktualisiert die Paketliste, das zweite installiert die neuesten Versionen der Pakete.  
Das kann eine Weile dauern, je nachdem, wie viele Pakete aktualisiert werden müssen.

## SPI und I2C

Einige der Beispiele benutzen SPI und I2C. Das sind Schnitstellen, über die der Raspberry PI mit bestimmten Bausteilen kommuniziert. Diese Schnittstellen sind standartmäßig deaktiviert, sodass wir diese manuell einschalten müssen.

1. Entweder: Wähle die Himbeere &gt; Preferences &gt; Raspberry Pi Configuration
   Oder: Führe `raspi-config` im Terminal aus.
2. Aktiviere unter dem Tab "Interfaces" SPI und I2C
3. Drücke auf "OK".
4. Entweder: Wähle die Himbeere &gt; Shutdown &gt; Reboot
   Oder: Führe `reboot` im Terminal aus.

## Herunterladen der Beispiele

Als nächstes Laden wir die Beispieldateien herunter. Dazu nutzen wir `git`. Diesen Befehl kennst du noch nicht, aber du wirst ihn später auch nicht mehr brauchen. Gehe einfach in deinen Dokumente-Ordner und führe den untenstehenden Befehl aus. Er lädt die Dateien von GitHub herunter, einer Plattform, auf der viele Open-Source-Projekte gehostet werden.

```bash
cd Documents
git clone https://github.com/GollumBree/RPi-Starter-Kit/
```

Das lädt die Dateien in einen neuen Ordner namens `RPi-Starter-Kit` herunter. Du kannst den Ordner mit dem Befehl `ls` auflisten, um zu sehen, dass er erstellt wurde. Wechsle mit `cd RPi-Starter-Kit` in den neuen Ordner.

## Installieren der benötigten Bibliotheken

Wir benutzen einige Python-Bibliotheken, die Standartmäßig nicht auf dem Raspberry PI installiert sind. Um diese Bibliotheken zu installieren, können wir den Befehl `pip` benutzen. `pip` ist ein Paketmanager für Python, der es dir ermöglicht, Bibliotheken zu installieren und zu verwalten.

Du kannst die benötigten Bibliotheken mit dem folgenden Befehl installieren:

```bash
pip install -r requirements.txt --break-system-packages
```

Dieser Befehl installiert alle Bibliotheken, die in der Datei `requirements.txt` aufgelistet sind. Diese Datei befindet sich im Ordner `RPi-Starter-Kit`. Wenn du die Bibliotheken manuell installieren möchtest, kannst du die Namen der Bibliotheken aus der Datei `requirements.txt` kopieren und sie einzeln mit `pip install <Bibliotheksname>` installieren.

## Los gehts

Du bist jetzt startklar. Bei manchen Beispielen benötigst du weitere Schritte, um sie auszuführen. Diese Schritte sind in den jeweiligen Beispielen beschrieben.
