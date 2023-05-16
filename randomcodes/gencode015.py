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

    # Calculate angle for shading
    angle = (numerator / denominator) * 360

    # Draw the shaded fraction
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor('gray')
    pen.left(90)
    pen.forward(200)
    pen.right(90)
    pen.circle(200, angle)
    pen.right(90)
    pen.forward(200)
    pen.left(90)
    pen.end_fill()

    # Hide the turtle
    pen.hideturtle()

    # Exit on click
    turtle.done()

# Example usage
draw_fraction_circle(1, 2)  # Draws a circle with one side shaded to represent 1/2
