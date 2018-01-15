# Turtle
# 24 October 2015

from turtle import *

colors = {0 : "blue", 1 : "green", 2 : "orange", 3 : "red", 4 : "purple"}


def koch_curve(size, level):
    speed(0)
    if (level == 0):
        forward(size)
    else:
        kochCurve(size/3, level-1)
        left(60)
        kochCurve(size/3, level-1)
        right(120)
        kochCurve(size/3, level-1)
        left(60)
        kochCurve(size/3, level-1)

def spiral_pentagon():
    for x in range(500):
        speed(0)
        color(colors[x%5])
        forward(x)
        right(70)

def draw_polygon(s, n):   
    angle = 180*(n-2)/n # interior angle
    for i in range(n):
        forward(s)
        right(180-angle)
