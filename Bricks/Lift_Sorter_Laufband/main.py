#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor1 = Motor(Port.A)
color_sensor = ColorSensor(Port.S3)

motor = Motor(Port.B)
color_sensor1 = ColorSensor(Port.S2)

motor2 = Motor(Port.D)
color_sensor2 = ColorSensor(Port.S4)
# Write your program here.

while True:
    color1 = color_sensor1.color()
    color2 = color_sensor.color()
    color3 = color_sensor2.color()
    
    if color3 == Color.YELLOW:
        motor2.run(-200)
        wait(2600)
        motor2.stop()
    else:
        motor2.stop()

    if color3 == Color.RED:
        motor2.run(-200)
        wait(2600)
        motor2.stop()
    else:
        motor2.stop()
    
    if color1 == Color.BLUE:
        motor.run(-80)
        wait(990)
        motor.stop()
        wait(500)
        motor.run(80)
        wait(990)
        motor.stop()
    else:
        motor.stop()
   
    if color2 == Color.YELLOW:
        wait(2000)
        motor1.run(200)
        wait(5900)
        motor1.run(-200)
        wait(6070)
        motor1.stop()
    else:
        motor1.stop()
    
    if color2 == Color.RED:
        wait(2000)
        motor1.run(200)
        wait(5900)
        motor1.run(-200)
        wait(6070)
        motor1.stop()
    else:
        motor1.stop()
    wait(100)


