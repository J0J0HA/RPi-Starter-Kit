# Blinking LED

Was ist das einfachste, was wir mit dem Raspberry PI Starter Kit machen können? Richtig, eine LED zum Blinken bringen! In diesem Beispiel zeigen wir dir, wie du eine LED mit dem Raspberry PI steuern kannst.

## Einrichten

In dem roten Verbindungsboard musst du LED an den Stecker D5 anschließen. Wo dieser liegt, kannst du &lt;TODO&gt;.
Die Kabel sind etwas schwergängig, daher solltest du sicherstellen, dass sie komplett eingesteckt sind.

## Ausprobieren

Um die LED zum Blinken zu bringen, musst du das Skript `2_blinking_led.py` ausführen. Das kannst du mit dem folgenden Befehl:

```bash
python 2_blinking_led.py
```

Du solltest jetzt sehen, dass die LED angeht und nach einer halben Sekunde wieder ausgeht.

> [!NOTE]
> Beim Einstecken der LED ist es meistens so, dass die LED direkt leuchtet, auch wenn sie nicht extra eingeschaltet wurde. In diesem Fall siehst du nur, dass die LED ausgeht. Starte das Skript einfach nochmal, dann sollte sich die LED normal verhalten.

## Verstehen

Du kannst den Code mit `nano 2_blinking_led.py` öffnen und bearbeiten. Wir haben ihr allerdings auch hier nocheinmal mit Kommentaren versehen, damit du verstehst, was passiert. Hier ist der Code:

```python
# Wir importieren die benötigten Bibliotheken (kannst du erstmal ignorieren)
import time
import RPi.GPIO as GPIO

# Wir setzen die Pin-Nummer, an die die LED angeschlossen ist.
# Wenn du deine LED ausversehen woanders angeschlossen hast, kannst du auch einfach diese Zahl anpassen, anstatt die LED umzustecken.
led_pin = 5

GPIO.setmode(GPIO.BCM)
# Hier legen wir fest, dass wir den Pin als Ausgang verwenden wollen. Die LED ist ja schließlich kein Sensor :)
GPIO.setup(led_pin, GPIO.OUT)

# Hier passiert das eigentliche Blinken.
# Wir schalten die LED auf "HIGH" (also an), warten eine halbe Sekunde und schalten sie dann wieder auf "LOW" (also aus).
GPIO.output(led_pin, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(led_pin, GPIO.LOW)

# Damit wir unsere Einstellungen zurücksetzen, sodass wir den Pin später wieder verwenden können, rufen wir GPIO.cleanup() auf.
GPIO.cleanup()
```

## Erweitern

Wenn du willst, kannst du auch hier versuchen, das Skript anzupassen. Zum Beispiel könntest du die Wartezeit ändern oder die LED mehrmals blinken lassen. In den nächsten Kapiteln wird es aber noch spannender, also halte dich nicht zu lange mit diesem Beispiel auf.
