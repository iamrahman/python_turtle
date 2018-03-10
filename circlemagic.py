import turtle

def draw_square(some):
    for x in range(0, 2):
        some.forward(150)
        some.right(45)
        some.forward(100)
        some.right(135)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.speed(10)
    brad.color("yellow")
    turtle.color("yellow")
    for x in range(0, 36):
        draw_square(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(350)

draw_art()



