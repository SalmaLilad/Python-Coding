import turtle
import math

# Create a turtle screen
myT = turtle.Turtle()
scr = myT.getscreen()
scr.setup(width=800, height=1200)

# Setup the background color of the screen and title
screen = turtle.Screen()
screen.bgcolor("beige")
screen.title("Happy Father's Day")

# Utility function to write text on the screen
def write_text(message, pos_y):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("black")  # Fixed the typo here (missing closing quote)
    pen.penup()
    pen.goto(0, pos_y)
    pen.write(message, align="center", font=("Courier", 24, "bold"))

# Function to generate a color based on angle
def get_color(angle):
    r = math.sin(math.radians(angle)) * 127 + 128  # Red component
    g = math.sin(math.radians(angle + 120)) * 127 + 128  # Green component
    b = math.sin(math.radians(angle + 240)) * 127 + 128  # Blue component
    return (r / 255, g / 255, b / 255)  # Return normalized RGB color

# Atom-like spinning paths (bigger circles)
def draw_atom():
    atom = turtle.Turtle()
    atom.speed(0)  # Fastest
    atom.pensize(2)
    atom.hideturtle()

    for angle in range(0, 360, 45):
        atom.penup()
        atom.goto(0, 0)
        atom.setheading(angle)
        atom.pendown()

        for i in range(360):
            atom.pencolor(get_color(i))  # Change color based on angle
            atom.forward(1.5)
            atom.left(1)

# Main Drawing
write_text("Happy Father's Day", 250)
write_text("Appa!", -280)
draw_atom()

# Get the canvas and save the entire screen (including text and background)
canvas = scr.getcanvas()
canvas.postscript(file="saanvi_rangarajan_card1.ps", colormode="color")

# Finish drawing
turtle.done()

