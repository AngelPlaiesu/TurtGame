import turtle
import random

class Wall:
    def __init__(self):
        self.trtl = turtle.Turtle()
        self.trtl.color("red")
        self.trtl.shape("triangle")
        self.trtl.penup()
        self.originalSize = self.trtl.turtlesize()  

    def spawn(self) -> None:
        self.trtl.hideturtle()
        self.trtl.goto(random.randint(-200,200),random.randint(-200,200))
        self.trtl.setheading(random.randint(0,360))
        self.trtl.showturtle()
    
    def increaseSize(self) -> None:
        if random.randint(0,1) == 0:
            self.trtl.turtlesize(*self.originalSize)
        
        size = self.trtl.turtlesize()
        increase = tuple([random.uniform(0.5, 5.5) * num for num in size])
        self.trtl.turtlesize(*increase) 
