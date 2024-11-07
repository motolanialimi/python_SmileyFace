import turtle

# Create turtle screen and setup
screen = turtle.Screen()
screen.title("Interactive Smile Face Emoji")
screen.bgcolor("lightblue")

# Initialize turtle for drawing
pen = turtle.Turtle()
pen.speed(3)

# Function to draw circle with color and radius
def draw_circle(pen, color, radius, x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.up()

# Function to draw eyes
def draw_eyes():
    # Left eye
    draw_circle(pen, 'white', 15, -40, 120)
    draw_circle(pen, 'black', 5, -37, 125)
    # Right eye
    draw_circle(pen, 'white', 15, 40, 120)
    draw_circle(pen, 'black', 5, 40, 125)

# Function to draw mouth and tongue
def draw_mouth():
    pen.goto(-40, 85)
    pen.down()
    pen.setheading(-60)  # Start drawing mouth downwards
    pen.circle(40, 120)  # Smile arc
    pen.up()
    # Tongue
    draw_circle(pen, 'red', 10, -10, 45)

# Main function to draw smiley face
def draw_smiley(face_color="yellow"):
    # Draw face
    draw_circle(pen, face_color, 100, 0, 0)
    # Draw eyes
    draw_eyes()
    # Draw nose
    draw_circle(pen, 'black', 8, 0, 75)
    # Draw mouth
    draw_mouth()
    pen.hideturtle()

# Prompt user for face color
face_color = screen.textinput("Choose Face Color", "Enter color for the smiley face:")
if not face_color:
    face_color = "yellow"  # Default color

# Draw the smiley face
draw_smiley(face_color)

# Keep the window open until closed by the user
screen.mainloop()

