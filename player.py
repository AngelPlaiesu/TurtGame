import turtle
class Player:

    trtl = None

    def __init__(self)-> None:
        trtl = turtle.Turtle()
        trtl.color("green")
        trtl.shape("turtle")
        trtl.penup()
        self.trtl = trtl
        self.speedMultiplier = 1


    def move_left(self)-> None:
        angle = self.trtl.heading()
        self.trtl.setheading(angle + 10)

    
    def move_right(self) -> None:
        angle = self.trtl.heading()
        self.trtl.setheading(angle - 10)

    def move_up(self)-> None:
        self.trtl.forward(10 * self.speedMultiplier)
        
    
    def move_down(self)-> None:
        self.trtl.backward(10)

    def outside_window(self) -> bool:
        left_wall = -turtle.window_width()/2
        right_wall = turtle.window_width()/2
        top_wall = turtle.window_height()/2
        bottom_wall = -turtle.window_height()/2
        (x,y) = self.trtl.pos()
        outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
        return outside
    
    def speed_up(self) -> None:
        self.speedMultiplier = self.speedMultiplier + 1