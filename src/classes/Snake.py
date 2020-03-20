import turtle

class Snake():
    # Class attributes
    head = turtle.Turtle()
    body = []

    def __init__(self):
        self.SetHeadProperties()

    def SetHeadProperties(self):
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0,0)
        self.head.direction = "stop"
        # print("Snake initialization\t\t:\tSUCCESS")

    def Grow(self):
        new_block = turtle.Turtle()
        new_block.speed(0)
        new_block.shape("square")
        new_block.color("black")
        new_block.penup()
        self.body.append(new_block)

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

    def Reset(self):
        self.head.direction = "stop"
        for body_part in self.body:
            # Hide body parts
            body_part.hideturtle()
        self.body.clear()
        self.head.goto(0, 0)

    def SetDirectionUp(self):
        if len(self.body) == 0:
            self.head.direction = "up"
        else:
            if self.head.direction != "down":
                self.head.direction = "up"
            
    def SetDirectionDown(self):
        if len(self.body) == 0:
            self.head.direction = "down"
        else:
            if self.head.direction != "up":
                self.head.direction = "down"
    
    def SetDirectionLeft(self):
        if len(self.body) == 0:
            self.head.direction = "left"
        else:
            if self.head.direction != "right":
                self.head.direction = "left"
    
    def SetDirectionRight(self):
        if len(self.body) == 0:
            self.head.direction = "right"
        else:
            if self.head.direction != "left":
                self.head.direction = "right"
    
    def PrintSnakePos(self):
        print("X : ", self.head.xcor(), "\tY : ", self.head.ycor())