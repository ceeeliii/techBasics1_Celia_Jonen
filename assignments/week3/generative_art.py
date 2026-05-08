from turtle import *

# setup
setup(600, 600)
bgcolor("skyblue")
tracer(0, 0)

# draw pot
penup()
goto(-35, -220)
pendown()
color("saddlebrown")
begin_fill()
for i in range(2):
    forward(120)
    left(90)
    forward(80)
    left(90)
end_fill()

# draw flower stem
penup()
goto(25, -140)
pendown()
color("green")
pensize(12)
setheading(90)
forward(180)

# left leaf
penup()
goto(20, -40)
pendown()
setheading(140)
color("darkgreen")
begin_fill()
circle(60, 70)
left(110)
circle(60, 70)
end_fill()

# right leaf
penup()
goto(40, -70)
pendown()
setheading(40)
begin_fill()
circle(50, 70)
left(100)
circle(60, 70)
end_fill()

# flower center
penup()
goto(0, 60)
pendown()
pensize(1)
color("orange")
begin_fill()
circle(30)
end_fill()

# petals
for angle in range(0, 360, 45):
    penup()
    goto(30, 65)
    setheading(angle)
    forward(50)
    pendown()
    color("pink")
    begin_fill()
    circle(25)
    end_fill()

# little details in the center
penup()
goto(25, 60)
pendown()
color("yellow")
begin_fill()
circle(8)
end_fill()

# finish
update()
exitonclick()
