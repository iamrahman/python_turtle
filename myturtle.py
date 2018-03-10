import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.color("yellow")
    turtle.shape("turtle")
    turtle.color("yellow")
    for x in range(0, 4):
        brad.forward(200)
        brad.right(90)
def draw_circle():
    petter = turtle.Turtle()
    petter.color("blue")
    petter.shape("arrow")
    petter.circle(100)
def draw_triangle():
    allen = turtle.Turtle()
    allen.color("red")
    for x in range(0, 3):
        allen.forward(130)
        allen.right(120)

draw_square()
draw_circle()
draw_triangle()
