# Linux

## Wer ist Linux?

Ein Betriebssystem, mit dem du auf jeden Fall vertraut bist, ist Windows. Windows läuft aber nicht auf einem Raspberry PI, da die meisten Programmierer Linux bevorzugen. Linux ist, einfach gesagt, eine Kategorie an Betriebssystemen, die sehr ähnlich funktionieren. Damit der Raspberry PI möglichst gut funktionieren kann, nutzen wir Raspberry PI OS, ein Betriebssystem, welches Linux verwendet und für den Raspberry PI optimiert ist.  
<sub>(Außerdem ist es kostenlos)</sub>  


Auf den ersten Blick mag das Betriebssystem ähnlich aussehen &mdash; es gibt aber doch große Unterschiede.

## Das Terminal

Ein großer Unterschied zu Windows ist die Nutzung des Terminals bzw. der Befehlszeile.
Unter Windows existiert dies zwar auch, allerdings muss ein normaler Nutzer diese eigentlich nie verwenden. Bei Linux-basierten Betriebssystemen ist es normal, dass man um Programme zu installieren oder Einstellungen im System zu verändern das Terminal verwendet. Einige Nutzer bevorzugen sogar, auf eine graphische Oberfläche (bzw. den Desktop) zu verzichten, da sie die Befehlszeile als effizienter empfinden. Das machen wir in dieser Anleitung zwar nicht, aber wir werden die Befehlszeile dennoch sehr häufig verwenden. Daher eine kleine Einführung.

### Einführung

Das Terminal öffnet ihr, indem ihr in der Leiste am oberen Bildschirmrand den schwazen Kasten anklickt oder mit der Tastenkombination `Alt` + `Shift` + `T`.

So sieht das Eingabefeld dann anfangs aus:

```bash
pi@raspberry:~$ 
```

* `pi`: Der erste Teil ist der Benutzename des angemeldeten Benutzers. Ihr musstet euch wahrscheinlich nicht anmelden, aber ihr seid dennoch als `pi` angemeldet.

* `raspberry`: Der zweite Teil ist der Name des Computers. Diser ist für uns unwichtig, weil er meistens erst genutzt wird, wenn mehrere Computer miteinander kommunizieren müssen.

* `~`: Dieses Zeichen mag erst einmal unscheinbar wirken, aber es steht für den Ordner, indem du dich gerade befindest. Dabei ist `~` eine Abkürzung für `/home/pi`. Das ist dein Benutzerordner, vergleichbar mit `C:\User\Anwender` auf Windows.

> [!NOTE]
> Anders als Windows haben Linux-basierte Betriebssysteme keine sog. Drive-Letters. Der oberste Ordner ist `/`, vergleichbar mit `C:\`. Wenn du weitere Speichermedien anschließt, findest du sie unter `/media/<NAME>`, anders als unter `D:\`, `E:\`, usw. bei Windows.

So. Jetzt wissen wir, was das bedeutet. Aber &mdash;

### Was kann man jetzt damit machen?

Ja... alles. Also alles, was man mit einem Computer so machen kann.

Fangen wir mit etwas Einfachem an und ändern, in welchem Ordner wir uns befinden.

Gib mal `ls` in deinem Terminal ein und drücke Enter.

```bash
pi@raspberry:~$ ls
Bookshelf  Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
pi@raspberry:~$
```

`ls` ist ein Befehl, der alle Dateien und Ordner in dem Ordner auflistet, in dem du dich gerade befindest. In diesem Fall also in deinem Benutzerordner.

Jetzt wollen wir in den Ordner `Documents` wechseln. Das geht mit dem Befehl `cd` (change directory, also "Ordner wechseln"). Gib also `cd Documents` ein und drücke Enter.

```bash
pi@raspberry:~$ cd Documents
pi@raspberry:~/Documents$ 
```

Jetzt siehst du, dass sich der Ordner geändert hat. Das `~` wurde durch `~/Documents` ersetzt. Das bedeutet, dass du jetzt im Ordner `Documents` bist. Wenn du jetzt wieder `ls` eingibst, siehst du die Dateien und Ordner auf deinem Documents.

```bash
pi@raspberry:~/Documents$ ls
pi@raspberry:~/Documents$ 
```

Hmm, ziemlich leer. Lass uns eine Datei erstellen. Das geht mit dem Befehl `touch`. Gib also `touch test.txt` ein und drücke Enter. Mit `ls` kannst du jetzt sehen, dass die Datei `test.txt` erstellt wurde.

```bash
pi@raspberry:~/Documents$ touch test.txt
pi@raspberry:~/Documents$ ls
test.txt
pi@raspberry:~/Documents$ 
```

Jetzt wollen wir die Datei mal öffnen. Das geht mit dem Befehl `nano`. Gib also `nano test.txt` ein und drücke Enter.

```bash
pi@raspberry:~/Documents$ nano test.txt
```

Jetzt öffnet sich ein Texteditor, in dem du die Datei bearbeiten kannst. Du kannst jetzt etwas Text eingeben. Wenn du fertig bist, drücke `Ctrl` + `X`, um den Editor zu verlassen. Du wirst gefragt, ob du die Änderungen speichern möchtest. Drücke `Y` für Ja und dann Enter, um die Datei zu speichern.

Mit `ls` kannst du jetzt sehen, dass die Datei `test.txt` immer noch existiert. Wenn du sie jetzt mit `nano test.txt` öffnest, siehst du den Text, den du eingegeben hast.

Diesen Editor werden wir später verwenden, um Python-Skripte zu schreiben und zu bearbeiten.

Jetzt wollen wir die Datei wieder löschen. Das geht mit dem Befehl `rm`. Gib also `rm test.txt` ein und drücke Enter.

```bash
pi@raspberry:~/Documents$ rm test.txt
pi@raspberry:~/Documents$ ls
pi@raspberry:~/Documents$ 
```

Du siehst, dass die Datei `test.txt` gelöscht wurde.

Diese Befehle sollten ausreichen, um dich im Terminal zurechtzufinden.

### Weitere Befehle

Hier sind ein paar weitere nützliche Befehle, die dir helfen können:

* `mkdir <Ordnername>`: Erstellt einen neuen Ordner mit dem angegebenen Namen.
* `rmdir <Ordnername>`: Löscht den angegebenen Ordner. Der Ordner muss leer sein, damit er gelöscht werden kann.
* `rmdir -r <Ordnername>`: Löscht den angegebenen Ordner und alle darin enthaltenen Dateien und Unterordner. Sei vorsichtig, dieser Befehl löscht alles ohne Rückfrage!
* `cp <Quelldatei> <Zieldatei>`: Kopiert die angegebene Datei.
* `mv <Quelldatei> <Zieldatei>`: Verschiebt die angegebene Datei oder benennt sie um.
* `clear`: Löscht den Inhalt des Terminals, sodass du eine leere Eingabezeile hast.
* `sudo <Befehl>`: Führt den angegebenen Befehl mit Administratorrechten aus. Das ist notwendig, um bestimmte Systemänderungen vorzunehmen. Du wirst nach deinem Passwort gefragt, wenn du diesen Befehl verwendest.
* `apt install <Paketname>`: Installiert das angegebene Paket. Das ist der Befehl, den wir verwenden werden, um Programme und Bibliotheken zu installieren.
* `man <Befehl>`: Zeigt die Handbuchseite für den angegebenen Befehl an. Das ist eine gute Möglichkeit, um mehr über einen Befehl zu erfahren und
seine Optionen zu sehen. Zum Beispiel `man ls` zeigt dir die Handbuchseite für den Befehl `ls`.

### Zusammenfassung

Okay, das war ganz schön viel. Aber keine Sorge, du musst dir das nicht alles merken. Wir zeigen dir immer, welche Befehle du verwenden musst. Und du wirst die Befehle mit der Zeit immer besser kennenlernen.

## Weitere Informationen

Wenn du mehr über Linux und das Terminal lernen möchtest, gibt es viele Ressourcen im Internet. Hier sind ein paar Links, die dir helfen können:

* [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) (Englisch)
* [Linux Command Line Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/linux-command-line/) (Englisch)
