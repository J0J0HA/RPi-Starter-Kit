# Hello World

Als erstes probieren wir, ob alles funktioniert. Dazu nutzen wir ein einfaches Python-Skript, das "Hello World" ausgibt.

Alle Python-Skripts sind bereits fertig geschrieben, wenn du aber lernen willst, wie du mit Python richtig umgehst, empfehlen wir dir, die Skripts nach dem Testen zu bearbeiten und zu verändern. So lernst du am besten, wie Python funktioniert.

## Ausprobieren

Um die Beispiel-Skripte auszuführen, öffne ein Terminal und wechsle in den Ordner, in dem die Skripte liegen. Wenn du unserer Anleitung gefolgt bist, sollte das der Ordner `~/Documents/RPi-Starter-Kit/examples` sein. Je nach dem Ordner, in dem du dich gerade befindest kannst das mit den folgenden Befehlen tun:

```bash
cd Documents
cd RPi-Starter-Kit
cd examples
```

Mit `ls` kannst du jetzt alle Dateien im Ordner auflisten. Du solltest eine Datei namens `1_hello_world.py` sehen. Um das Skript auszuführen, gib den folgenden Befehl ein:

```bash
python 1_hello_world.py
```

Wenn alles funktioniert hat, solltest du die folgende Ausgabe sehen:

```text
Hello World!
```

## Erweitern

Du kannst das Skript mit dem Texteditor `nano` öffnen, um den Code anzusehen und zu bearbeiten. Gib dazu den folgenden Befehl ein:

```bash
nano 1_hello_world.py
```

Jetzt öffnet sich der Texteditor und du kannst den Code sehen. Der Code sollte so aussehen:

```python
print("Hello World!")
```

Du kannst den Text in den Anführungszeichen ändern, um eine andere Nachricht auszugeben. Zum Beispiel:

```python
print("Hallo Welt!")
```

Wenn du fertig bist, drücke `Ctrl` + `X`, um den Editor zu verlassen. Du wirst gefragt, ob du die Änderungen speichern möchtest. Drücke `Y` für Ja und dann Enter, um die Datei zu speichern.

Jetzt kannst du das Skript erneut ausführen, um die neue Nachricht zu sehen:

```bash
python 1_hello_world.py
```

Wenn du alles richtig gemacht hast, solltest du jetzt die neue Nachricht sehen:

```text
Hallo Welt!
```

Das ist es! Du hast dein erstes Python-Skript auf dem Raspberry Pi ausgeführt und bearbeitet. Jetzt kannst du mit den anderen Beispielen weitermachen und mehr über Python und den Raspberry PI lernen.
