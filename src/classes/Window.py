import turtle

class Window():
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Snake game by @Irchad")
        self.wn.bgcolor("grey")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)

    def launch(self):
        self.wn.mainloop()

