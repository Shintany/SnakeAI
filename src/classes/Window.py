import turtle
import time
from .Snake import Snake

class Window():
    # Class attributes
    delay = 0.1
    snake = Snake()

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Snake game by @Irchad")
        self.wn.bgcolor("grey")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0) #Turns off screen update

        # Listen to keyboard input
        self.ListenKeyboard()

        print("Window initialization\t\t:\tSUCCESS")


    def ListenKeyboard(self):
        self.wn.listen()
        self.wn.onkeypress(self.snake.SetDirectionUp, "w")
        self.wn.onkeypress(self.snake.SetDirectionDown, "s")
        self.wn.onkeypress(self.snake.SetDirectionLeft, "a")
        self.wn.onkeypress(self.snake.SetDirectionRight, "d")

    def Launch(self):
        while True:
            self.wn.update()
            self.snake.Move()
            time.sleep(self.delay)

        self.wn.mainloop()
