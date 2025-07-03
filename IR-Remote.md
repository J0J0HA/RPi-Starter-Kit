# IR Remote

## Setup

1. Füge `ir-keytable -p all` ans Ende der Datei `/etc/rc.local` an.
2. Füge `dtoverlay=gpio-ir,gpio_pin=12` ans Ende der Datei `/boot/firmware/config.txt`
3. Führe `sh install-ir.sh` aus



## IR Codes

| Button | Code |
| ------ | ---- |
| EQ     | 9    |
| Vol-   | 7    |
| Vol+   | 21   |
| FOL-   | 25   |
| FOL+   | 13   |
| Next   | 64   |
| Play / Pause | 67   |
| Prev   | 68   |
| CH-    | 69   |
| CH     | 70   |
| CH+    | 71   |
| 0      | 22   |
| 1      | 12   |
| 2      | 24   |
| 3      | 94   |
| 4      | 8    |
| 5      | 28   |
| 6      | 90   |
| 7      | 66   |
| 8      | 82   |
| 9      | 74   |

[Quelle](https://ignorantofthings.com/receiving-infrared-on-the-raspberry-pi-with-python/)
