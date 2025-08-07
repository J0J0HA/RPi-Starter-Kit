# Secret of the Treasure Chest

Hier nutzen wir einen Hall-Sensor. Ein Hall-Sensor ist ein Sensor, der mithilfe des (wer hätte es gedacht) Hall-Effekts Magnetfelder erkennen kann. Es gibt aber eines zu beachten &mdash; der Sensor erkennt die Abwesenheit eines magnetischen Südpols. Das bedeutet, anders als beim Taster steht `False` für "Hier ist ein Magnet" und `True` für "Hier ist kein Magnet".

Die Idee hinter diesem Beispiel ist das Glitzern von Gold in einer Schatztruhe. Die rote und gründe LED blinken, um das glitzernde Gold zu simulieren, sobald die Schatztruhe geöffnet ist. Das erkennen wir mithilfe eines Magneten im Deckel der Schatzkiste und dem Hallsensor in der unteren Hälfte.

## Einrichten

| Port | Bauteil |
| ---- | ------- |
| D4 | Hall-Sensor |
| D5 | Rote LED |
| D6 | Grüne LED |

Wie vorher ist es egal, welche PINs du im D-Bereich wählst, solage du auch die Nummern im Code anpasst.

## Ausprobieren

Starte das Skript und schaue, was passiert:

```bash
python 5_trasure_chest.py
```

Wenn du mit deinem Finger in die Nähe des Touch-Sensors kommst, summt der Summer für drei Sekunden.

## Verstehen

Du kannst den Code mit `nano 5_trasure_chest.py` öffnen und bearbeiten.

Dieser Code arbeitet auch nach dem selben Prinzip, wie die vorherigen Beispiele.

```python
import time
import RPi.GPIO as GPIO
from keyboard import is_pressed

hall_pin = 4
green_pin = 5
red_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(hall_pin, GPIO.IN)

while not is_pressed("enter"):
    if not GPIO.input(hall_pin):
        GPIO.output(green_pin, GPIO.HIGH)
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.LOW)
        time.sleep(0.5)
    else:
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.LOW)

GPIO.cleanup()

```

## Erweitern

Wenn du willst, kannst du die Zeit anpassen, für die der Summer summt, oder eine LED hinzufügen, die leuchtet (oder sogar blinkt) während der Summer summt. Probiere einfach etwas herum und verzweifle nicht, wenn etwas mal nicht klappt.
