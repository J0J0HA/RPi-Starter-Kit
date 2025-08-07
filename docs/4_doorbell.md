# Doorbell

Das Setup ist prinzipiell gleich wie bei ***Control LED***, allerdings verwenden wir hier einen Touch-Sensor und einen Summer anstelle eines Tasters und einer LED.

Der Touch-Sensor hat den Vorteil, dass er den Finger anhand von änderungen im Spannungsfeld bei einer Distanz von bis zu 3mm erkennt. Man könnte ihn also hinter einer nichtmetallischen Schutzschicht verbauen, entweder um ihn vor Wasser zu schützen oder um ihn zu verstecken.

## Einrichten

| Port | Bauteil |
| ---- | ------- |
| D5 | Summer |
| D6 | Touch-Sensor |

Wenn du Probleme damit hast, die Kabel rauszuziehen, kannst du die Bauteile auch einfach an andere D-Ports anschließen. Du musst dann im Skript nur entsprechend die Pin-Nummern ändern.

## Ausprobieren

Starte das Skript und schaue, was passiert:

```bash
python 4_doorbell.py
```

Wenn du mit deinem Finger in die Nähe des Touch-Sensors kommst, summt der Summer für drei Sekunden.

## Verstehen

Du kannst den Code mit `nano 4_doorbell.py` öffnen und bearbeiten.

Wenn du verstanden hast, wie die letzten Skripts funktioniert haben, solltest du verstehen, wie dieser Code funktioniert.

```python
import time
import RPi.GPIO as GPIO
from keyboard import is_pressed

touch_pin = 5
buzzer_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)

while not is_pressed("enter"):
    if GPIO.input(touch_pin):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()
```

## Erweitern

Wenn du willst, kannst du die Zeit anpassen, für die der Summer summt, oder eine LED hinzufügen, die leuchtet (oder sogar blinkt) während der Summer summt. Probiere einfach etwas herum und verzweifle nicht, wenn etwas mal nicht klappt.
