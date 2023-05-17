import turtle

def animate_shading():
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

    # Animate the shading
    pen.penup()
    pen.goto(0, -200)  # Move to the bottom of the circle
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("gray")

    angle = 0
    while angle <= 180:
        pen.circle(200, 5)  # Draw a small section of the semicircle
        angle += 5  # Increase the angle

        # Update the screen to show the animation
        turtle.update()

    pen.end_fill()

    # Hide the turtle
    pen.hideturtle()

    # Keep the turtle window open
    turtle.done()

# Example usage
animate_shading()
