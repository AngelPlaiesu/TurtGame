import turtle
import random

class Poo:

    def __init__(self) -> None:
        trtl = turtle.Turtle()
        leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
        turtle.register_shape('leaf',leaf_shape)
        trtl.shape('leaf')
        trtl.color('brown')
        trtl.penup()
        trtl.hideturtle()
        trtl.speed()
        self.trtl = trtl
    
    def spawn(self) -> None:
        self.trtl.hideturtle()
        self.trtl.setx(random.randint(-200,200))
        self.trtl.sety(random.randint(-200,200))
        self.trtl.showturtle()
        