#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()
motor = Motor(Port.A)
motor1 = Motor(Port.B)
motor2 = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)


while True:
    color1 = color_sensor.color()

    if color1 == Color.BLUE:
        motor1.run(-80)
        wait(3000)
        motor1.run(-20)
        motor2.run(120)
        wait(3000)
        motor1.stop()
        motor2.run(1)
        motor1.run(25)        
        motor.run(-30)
        wait(3700)
        motor.stop()
        motor1.stop()
        wait(2000)
        motor.run(60)
        wait(3500)
        motor1.run(-80)
        wait(2000)
        motor2.run(-180)
        wait(4300)
        motor2.run(1)
        motor1.stop()
        wait(750)
        motor1.run(-3)
        wait(2000)
        motor.run(-40)
        wait(2000)
        motor.stop()
        motor1.run(-100)
        wait(2000)
        motor2.run(200)
        wait(1900)
        motor2.stop()
        motor1.stop()
        motor.run(30)
        wait(3000)
        motor.stop()
        
    else:
        motor.stop()