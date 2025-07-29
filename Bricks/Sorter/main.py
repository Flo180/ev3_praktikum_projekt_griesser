#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Color


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor1 = Motor(Port.A)
motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S3)



while True:
        color1 = color_sensor.color()

        if color1 == Color.GREEN:
            motor1.run(-50)
            wait(2000)
            motor1.stop()
            motor.run(50)
            wait(2500)
            motor.run(-50)
            wait(2500)
            motor.stop()
            motor1.run(50)
            wait(1900)
            motor1.stop()

        else:
            motor.stop()

        if color1 == Color.YELLOW:
            motor.run(50)
            wait(2500)
            motor.run(-50)
            wait(2500)
            motor.stop()

        else:
            motor.stop()

        if color1 == Color.BLUE:
            motor.run(50)
            wait(2500)
            motor.run(-50)
            wait(2500)
            motor.stop()

        else:
            motor.stop()

        if color1 == Color.RED:
            motor.run(50)
            wait(2500)
            motor.run(-50)
            wait(2500)
            motor.stop()

        else:
            motor.stop()
        wait(100)
