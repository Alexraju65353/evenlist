import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("My Turtle Square") 
my_turtle = turtle.Turtle()
my_turtle.pencolor("white")
my_turtle.pensize(8)
for _ in range(3):
    my_turtle.forward(100) 
    my_turtle.right(120) 
turtle.done()