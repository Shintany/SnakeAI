from classes.Window import Window
from classes.Snake import Snake

# Set up the screen
if __name__ == "__main__":
    window = Window()
    print("Window initialization\t\t:\tSUCCESS")

    snake = Snake()
    print("Snake initialization\t\t:\tSUCCESS")

    window.launch()