import turtle
turtle.bgcolor("white")
def draw_polygon(side_length, sides):
    angle = 360 / sides
    for _ in range(sides):
        p.forward(side_length)
        p.left(angle)
        p.width(2)


screen = turtle.Screen()
p=turtle.Pen()

#p = turtle.Turtle()

draw_polygon(80, 3)

# square
draw_polygon(80, 4)


draw_polygon(80, 5)

draw_polygon(80, 6)

draw_polygon(80, 7)

draw_polygon(80, 8)

draw_polygon(80, 9)

draw_polygon(80, 10)

draw_polygon(80, 11)


draw_polygon(80, 12)

screen.mainloop()