import turtle as t

turtle = t.Turtle()
turtle.shape(name="turtle")
turtle.color("#FFCC00")
turtle.width(8)
turtle.speed(200)
# TODO
distance = 30
angle = 20
ang = 3
ang1 = -3
turtle.up()
turtle.setpos(-12,-85)
turtle.down()
for i in range(18):
    turtle.forward(distance)
    turtle.left(angle)

turtle.up()
turtle.setpos(0,38)
turtle.down()
turtle.left(15)
turtle.forward(70)
turtle.left(75)
for i in range(12):
    turtle.forward(20.6)
    turtle.left(ang)

turtle.up()
turtle.setpos(0,38)
turtle.down()
turtle.right(135)
turtle.back(70)
turtle.right(80)
for i in range(12):
    turtle.back(20.6)
    turtle.right(ang)

turtle.up()
turtle.setpos(0,-38)
turtle.down()
turtle.left(-40)
turtle.forward(70)
turtle.left(75)
for i in range(12):
    turtle.forward(20.6)
    turtle.left(ang)

turtle.up()
turtle.setpos(0,-38)
turtle.down()
turtle.right(140)
turtle.back(70)
turtle.right(75)
for i in range(12):
    turtle.back(20.6)
    turtle.right(ang)

turtle.up()
turtle.setpos(38,0)
turtle.down()
turtle.right(155)
turtle.back(70)
turtle.right(75)
for i in range(12):
    turtle.back(20.6)
    turtle.right(ang)

turtle.up()
turtle.setpos(38,0)
turtle.down()
turtle.left(140)
turtle.forward(70)
turtle.left(75)
for i in range(12):
    turtle.forward(20.6)
    turtle.left(ang)

turtle.up()
turtle.setpos(-38,0)
turtle.down()
turtle.right(-35)
turtle.back(70)
turtle.right(75)
for i in range(12):
    turtle.back(20.6)
    turtle.right(ang)

turtle.up()
turtle.setpos(-38,0)
turtle.down()
turtle.left(140)
turtle.forward(70)
turtle.left(75)
for i in range(12):
    turtle.forward(20.6)
    turtle.left(ang)

turtle.up()
turtle.setpos(0,0)
turtle.down()
screen = t.Screen()
screen.bgcolor("#360500")
screen.mainloop();