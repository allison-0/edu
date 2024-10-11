import turtle

def draw_circle(t, x, y, color):
    t.penup() # Lift pen to move without drawing anything
    t.setpos(x, y - 45) # Move to the bottom of the circle
    t.pendown() # Start drawing
    t.color(color) # Make color generic for flexibility
    t.circle(45) # Draw circle with a radius of 45

def main():
    # Set up screen for the program
    screen = turtle.Screen()
    screen.setup(400, 300)
    screen.title("Olympic Rings")

    t = turtle.Turtle() # Create turtle
    t.width(5) # Set line width
    t.speed(6) # Make the animation a bit faster
    t.hideturtle() # Hide turtle cursor

    # Draw the Olympic rings
    draw_circle(t, -110, 0, "blue")
    draw_circle(t, 0, 0, "black")
    draw_circle(t, 110, 0, "red")
    draw_circle(t, -55, -50, "yellow")
    draw_circle(t, 55, -50, "green")

    screen.exitonclick() # Be able to exit the program quickly

if __name__ == "__main__":
    main()