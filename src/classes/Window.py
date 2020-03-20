import turtle
import time
from .Snake import Snake
from .Food import Food

class Window():
    # Class attributes
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    delay = 0.1
    snake = Snake()
    food = Food(WINDOW_WIDTH, WINDOW_HEIGHT)

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Snake game by @Irchad")
        self.wn.bgcolor("grey")
        self.wn.setup(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
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

            # Check whether the snake eats the food or not
            self.CheckSnakeFoodDistance()

            # Move snake whole body in reverse order
            for idx in range(len(self.snake.body)-1, 0, -1):
                x = self.snake.body[idx-1].xcor()
                y = self.snake.body[idx-1].ycor()
                self.snake.body[idx].goto(x, y)

            # Move segment 0 to where the head is
            if len(self.snake.body) > 0:
                x = self.snake.head.xcor()
                y = self.snake.head.ycor()
                self.snake.body[0].goto(x,y)

            self.snake.Move()

            time.sleep(self.delay)

        self.wn.mainloop()


    def CheckSnakeFoodDistance(self):
        if self.snake.head.distance(self.food.food) < 20:
            self.food.SetRandomPosition()
            self.snake.Grow()
