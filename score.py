import turtle


class Score:

    def __init__(self) -> None:
        trtl = turtle.Turtle()
        trtl.hideturtle()
        trtl.speed()
        self.trtl = trtl
        self.game_score = 0
    
    def show(self) -> None:
        x = (turtle.window_width() / 2)-50
        y = (turtle.window_height() / 2)-50
        score_turtle = self.trtl
        score_turtle.clear()
        score_turtle.penup()
        score_turtle.setpos(x,y)
        score_turtle.write(str(self.game_score) , align = 'right',font=('Arial',40,'bold'))
        

