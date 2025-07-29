# ev3_praktikum_projekt_griesser

## Projektbeschreibung

Im Ramen meines Praktikums am Lehrstuhl für Cyber-Physical-Systems habe ich eine auf LEGO EV3 basierende automatisierte Produktionsstätte mit Sortiersystem gebaut.
Der Code ist unter dem Ordner "Bricks" (Projektname) aufzufinden.

### Umsetzung

- Bau einer Sortiermaschiene, die grüne Teile aussortiert und Programmierung dieser
- Erweiterung des Förderbands mit einer Maschiene die die blauen Teile aussortiert
- Programierung von Lift, Sortiermaschiene, Greifarm und Laufbändern (in Python3)
- Recherche zum gleichzeitigem ansteuern aller EV3 Bricks 

### Herausforderung 

Gleichzeitiges Ansteuern aller EV3 Bricks

### Fazit

Ich konnte meine Kenntnisse in Robotik, Automatisierung und Programmierung anwenden und erweitern.

## Projektumsetzung

### Aufbauen von physischen Lego Komponenten

Verwendete Teile:
  1) Lift
  2) Förderband mit Sortiermaschine
  3) Rutsche
  4) Kleines Förderband
  5) Greifarm
  6) Sortiermaschine
  7) USB Hub mit Stromversorgung
  8) 4x EV3
Verbaute Komponenten: 8x Motoren, 4x Farbsensoren mit Infrarot

![side_view](https://github.com/user-attachments/assets/43bedd7e-1f8f-4f06-b61c-9742230ca800)
Seitenansicht des Setups

![top_view](https://github.com/user-attachments/assets/508d663d-48f5-48f3-a702-9b5bec7882bd)
Ansicht des Setups von oben

### Aufsetzen der Entwicklungsumgebung

Alle Programme und Skripte wurden in Visual Studio Code geschrieben.
Download von Extensions:
  1) LEGO® MINDSTORMS® EV3 MicroPython (Version: 2.0.0)
  2) Remote - SSH (Version 0.120.0)
  3) ev3dev-browser (Version: 1.2.1, Testzwecke)

### Erstellen des Codes
#### 1) Sortiermaschine
[Code zur Sortiermaschine](Bricks/Sorter/main.py)

##### Funktionsweise des Codes
Sortiert grüne von restlichen Farben in eine Box aus, die nicht betroffenen Farben werden weiterbefördert.

"motor1 = Motor(Port.A)" -> Reserviert für Grüne um den Apparat zur Seite zu drehen
"motor = Motor(Port.B)" -> Für alle Farben zum Auswerfen der Blöcke auf das Förderband

"if color1 == Color.GREEN:" ist die erste Condition in der While(1) Schleife die den Motor1 betätigt (GREEN stammt aus der Colour Library)

##### Limitationen / Komplikationen
1) Befüllen muss manuell ablaufen
2) Sortiert im momentanen Zustand nur eine Farbe aus (bei Abänderung etwas anderes als Grün)
3) Blöcke könnten vom Förderband bei Ablage rutschen
4) Bei Verlagerung der Box zum Aussortieren landet der Block im Nichts
5) Bei Veränderung der Startpositionen der Motoren könnten Probleme auftreten

#### 2) Laufband (Groß)
[Code zum großen Laufband](/Bricks/Laufband/main.py)

##### Funktionsweise des Codes
Aktiviert das Laufband auf eine fixe Geschwindigkeit.
Es wurden 2 Motoren verwendet um die Leistung zu erhöhen.

##### Limitationen / Komplikationen
1) Startet, aber stoppt das Laufband nicht mehr
2) Muss mit Befehl von einem Endgerät angesteuert werden zum Start, nicht über gespeichertem Programm auf dem Brick alleine möglich.

#### 3) Lift / Sorter / Laufband (Klein)
[Code zur Kombinierung dieser Komponenten](Bricks/Lift_Sorter_Laufband/main.py)

##### Funktionsweise des Codes
[Sorter:](/Gifs_demo/sorter_blau.gif) Sortiert nur die blauen in die daneben liegende Box (4x Blöcke Limit) aus.

[Lift:](/Gifs_demo/lift.gif) Fängt einen Block auf und transportiert ihn rauf und rüber zur Rutsche

[Sensor / Rutsche:](/Gifs_demo/foerderband_sensor.gif) Erkennt Block und fangt ihn ab bevor er zum Greifarm vorgelassen wird.
 
##### Limitationen / Komplikationen
1) Falls der Lift noch aktiv läuft, kann der Sensor am Laufband vorne nichts erkennen oder reagieren
2) Der Sensor erkennt die Farbe Gelb sehr schwer
3) Platzierung des Blockes ist für den Greifarm wichtig bzw. kann nicht gedreht werden
4) In den Lift passt nur ein Block und das Laufband stoppt nicht während der Lift aktiv ist
