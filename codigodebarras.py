#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
md = Motor(Port.C)
mi = Motor(Port.B)
robot = DriveBase(mi,md,55.5,104)

color_sensor = ColorSensor(Port.S4)
c1 = 0
c2 = 0
color_detectado = color_sensor.color()

while color_detectado == Color.WHITE:
    color_detectado = color_sensor.color()
    robot.straight(1)

while color_detectado != Color.WHITE:
    color_detectado = color_sensor.color()
    robot.straight(1)
    c1 = c1 + 1
print(c1)

while color_detectado == Color.WHITE:
    color_detectado = color_sensor.color()
    robot.straight(1)

while color_detectado != Color.WHITE:
    color_detectado = color_sensor.color()
    robot.straight(1)
    c2 = c2 + 1
print(c2)

while True:
    c3 = 0
    color_detectado = color_sensor.color()
    robot.straight(1)
    while color_detectado != Color.WHITE:
        color_detectado = color_sensor.color()
        robot.straight(1)
        c3 = c3 + 1
    if c3 >= c2 - 2 and c3 <= c2 + 2:
        print("1")
    elif c3 >= c1 - 2 and c3 <= c1 + 2:
        print("0")