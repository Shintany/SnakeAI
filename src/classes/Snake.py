import turtle

class Snake():
    # Class attributes
    head = turtle.Turtle()

    def __init__(self):
        self.SetHead()

    def SetHead(self):
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0,0)
        self.head.direction = "stop"
        print("Snake initialization\t\t:\tSUCCESS")

    def Move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def SetDirectionUp(self):
        self.head.direction = "up"
    
    def SetDirectionDown(self):
        self.head.direction = "down"

    def SetDirectionLeft(self):
        self.head.direction = "left"

    def SetDirectionRight(self):
        self.head.direction = "right"