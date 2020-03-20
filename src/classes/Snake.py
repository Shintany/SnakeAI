import turtle

class Snake():
    def __init__(self):
        self.SetHead()

    @classmethod
    def SetHead(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0,0)
        self.head.direction = "stop"