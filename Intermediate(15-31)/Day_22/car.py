from turtle import Turtle
import random as rn


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.speed("fastest")
        self.goto(400, 0)
        self.setheading(180)
        self.shapesize(1, 2)
