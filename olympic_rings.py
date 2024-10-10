import turtle

def draw_circle(t, x, y, color):
    t.penup() # Lift pen to move without drawing anything
    t.setpos(x, y - 45) # Move to the bottom of the circle
    t.pendown() # Start drawing
    t.color(color) # Make color generic for flexibility
    t.circle(45) # Draw circle with a radius of 45

def main():
    t = turtle.Turtle() # Create turtle
    t.width(5) # Set line width
    t.speed(6) # Make the animation a bit faster
    t.hideturtle() # Hide turtle cursor

if __name__ == "__main__":
    main()