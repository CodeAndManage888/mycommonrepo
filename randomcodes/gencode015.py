import turtle

def draw_fraction_circle(numerator, denominator):
    # Set up the turtle
    screen = turtle.Screen()
    screen.setup(500, 500)
    pen = turtle.Turtle()
    pen.speed(0)

    # Draw the circle
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.circle(200)

    # Shade the other half of the circle
    pen.penup()
    pen.goto(0, -200)  # Move to the bottom of the circle
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("gray")
    pen.circle(200, -180)  # Draw a semicircle
    pen.end_fill()

    # Hide the turtle
    pen.hideturtle()

    # Keep the turtle window open
    turtle.done()

# Example usage
draw_fraction_circle(1, 2)
