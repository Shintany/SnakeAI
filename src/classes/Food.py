import turtle
import random

class Food():
    # Class attributes
    food = turtle.Turtle()

    def __init__(self, win_width, win_height):
        self.x_lb = (int)(win_width * -1 / 2) + 20
        self.x_hb = (int)(win_width / 2) - 20
        self.y_lb = (int)(win_height * -1 / 2) + 20
        self.y_hb = (int)(win_height / 2) - 20
        self.x_range, self.y_range = self.SetFoodPosArray() 

        self.SetFoodProperties()

    def SetFoodProperties(self):
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.SetRandomPosition()
        # print("Food initialization\t\t:\tSUCCESS")

    def SetFoodPosArray(self):
        x_range = range(self.x_lb, self.x_hb)
        y_range = range(self.y_lb, self.y_hb)
        return x_range, y_range

    def SetRandomPosition(self):
        self.food.goto(random.choice(self.x_range),random.choice(self.y_range))
