# Control LED

Es wäre schon praktisch, wenn wir die LED nicht nur blinken lassen könnten, sondern sie auch an- und ausschalten könnten. In diesem Kapitel zeigen wir dir, wie du die LED mit einem Knopf steuern kannst.

## Einrichten

Schließe einen Taster an den Stecker D6 an. Die LED bleibt an D5 angeschlossen.

## Ausprobieren

Du kannst das Programm mit diesem Befehl starten:

```bash
python 3_control_led.py
```

Wenn du jetzt den Knopf drückst, sollte die LED angehen. Wenn du den Knopf loslässt, sollte die LED wieder ausgehen.

## Verstehen

Du kannst den Code mit `nano 3_control_led.py` öffnen und bearbeiten. Hier ist der Code mit Kommentaren, die erklären, was passiert:

```python
# Importieren von Bibliotheken
import RPi.GPIO as GPIO
from keyboard import is_pressed

# Setzen der Pin-Nummern
led_pin = 5
button_pin = 6

# Einrichten der GPIO-Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

# Diese Schleife läuft, bis die Enter-Taste gedrückt wird
# - "while not" = solage nicht = bis
# - Die Funktion "is_pressed" haben wir von der Bibliothek "keyboard" importiert. Sie gibt uns "True" (= wahr) zurück, wenn die Taste gedrückt wird und "False" (= falsch), wenn sie nicht gedrückt wird.
while not is_pressed("enter"):
    # Wir lesen hier den Status des Knopfes aus.
    # Auch diese Funktion gibt uns entweder "True" oder "False" zurück, je nachdem, ob der Knopf gedrückt ist oder nicht.
    if GPIO.input(button_pin):
        # Wenn der Knopf gedrückt ist, schalten wir die LED ein.
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        # Wenn der Knopf nicht gedrückt ist, schalten wir die LED aus.
        GPIO.output(led_pin, GPIO.LOW)

# Freigeben der GPIO-Pins
GPIO.cleanup()
```

Wichtig ist hier zu verstehen, dass die Schleife sich wiederholt, und zwar so schnell, wie es die CPU des Raspberry Pi zulässt. Das bedeutet, dass die LED sofort reagiert, wenn du den Knopf drückst oder loslässt.

## Erweitern

