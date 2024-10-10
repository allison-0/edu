import turtle

def draw_circle(t, x, y, color):
    t.penup() # Lift pen to move without drawing anything
    t.setpos(x, y - 45) # Move to the bottom of the circle
    t.pendown() # Start drawing
    t.color(color) # Make color generic for flexibility
    t.circle(45) # Draw circle with a radius of 45


def main():

if __name__ == "__main__":
    main()