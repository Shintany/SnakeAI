from classes.Window import Window

# AMOUNT OF ITERATIONS
ITERATIONS = 5

# Set up the screen
if __name__ == "__main__":

    for iteration in range(0, ITERATIONS):
        print("ITERATION : ", iteration)
        window = Window()
        window.Launch()
        print("Game ended with score : ", window.score)