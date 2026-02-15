from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt') as data:
            h_score = data.read()
            self.high_score = int(h_score)  if h_score else 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} high score: {self.high_score}', align='center', font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align='center', font=("Arial", 24, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
