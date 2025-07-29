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
Code: /Bricks/Sorter/main.py
