import turtle
from player import Player
from score import Score
from poo import Poo
from wall import Wall

class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.scoreC = Score()
        self.poo = Poo()
        self.wall = Wall()  
        self.gameRunning = False

    def startScreen(self)  -> None:
        turtle.penup()
        turtle.hideturtle()
        turtle.write('Press SPACE to start',align='center' , font=('Aerial',16,'normal'))

    def game_over(self)  -> None:
        turtle.penup()
        turtle.hideturtle()
        turtle.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

    def gameRules (self) -> None:
        if self.player.trtl.distance(self.poo.trtl) < 20:
            self.poo.spawn()
            self.scoreC.game_score = self.scoreC.game_score + 10
            self.scoreC.show()
            self.player.speed_up()
            self.wall.spawn()
            self.wall.increaseSize()

            if self.wall.trtl.distance(self.poo.trtl) < 25:
                self.wall.spawn()

            if self.wall.trtl.distance(self.player.trtl) < 25:
                self.wall.spawn()

        if self.player.outside_window() or self.player.trtl.distance(self.wall.trtl) < 20:
            self.game_over()
            self.gameRunning = False
            self.player.trtl.hideturtle()
            return
        
        turtle.ontimer(self.gameRules, 1)

    def startGame(self)  -> None:
        if self.gameRunning:
            return
        turtle.clear()
        self.gameRunning = True
        self.player.trtl.showturtle()
        self.player.trtl.goto(0,0)
        self.scoreC.game_score = 0
        self.poo.spawn()
        self.wall.spawn()
        self.gameRules() 

    def run(self)  -> None:
        self.startScreen()
        self.scoreC.show()
        turtle.onkey(self.player.move_up,'Up')
        turtle.onkey(self.player.move_right,'Right')
        turtle.onkey(self.player.move_down,'Down')
        turtle.onkey(self.player.move_left,'Left')
        turtle.onkey(self.startGame, 'space')
        turtle.listen()
        turtle.mainloop()
