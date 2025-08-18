
import turtle
num_petals = int(input("Enter the number of petals for the flower: "))
radius = 100
angle = 60
screen = turtle.Screen()
t = turtle.Turtle()
for _ in range(num_petals):
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
    
    t.left(360 / num_petals)
t.hideturtle()
screen.mainloop()