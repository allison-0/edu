import turtle

def draw_circle(t, x, y, color):
    t.penup() # Lift pen to move without drawing anything
    t.setpos(x, y - 45) # Move to the bottom of the circle
    t.pendown() # Start drawing
    t.color(color) # Make color generic for flexibility
    t.circle(45) # Draw circle with a radius of 45

def main():
    t = turtle.Turtle() # Create turtle
    t.width(10) # Set line width
    t.speed(6) # Make the animation a bit faster
    t.hideturtle() # Hide turtle cursor

    # Draw the Olympic rings
    draw_circle(t, -110, 0, "#0079d1") # Blue
    draw_circle(t, 0, 0, "#000000") # Black
    draw_circle(t, 110, 0, "#f02329")  # Red
    draw_circle(t, -55, -50, "#FFB20C") # Yellow/orange
    draw_circle(t, 55, -50, "#00a750") # Green

if __name__ == "__main__":
    main()