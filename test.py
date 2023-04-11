from turtle import *
from time import sleep 

my_window = Screen()
my_window.bgcolor("red")

pensize(5)
# house 
forward (100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

# door 
left(90)
forward(40)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)

# top
left(90)
forward(40)
left(90)
forward(100)
left(45)
forward(70)
left(90)
forward(70)
left(45)

#sun
penup()
setposition(200,200)
pendown()
circle(40, 360)

#floor 
penup()
setposition(-100,0)
pendown()
left(90)
forward(350)

#child
setposition(150,0)
left(75)
forward(30)
right(150)
forward(30)
backward(30)
left(165)
forward(20)
penup()
setposition(165,60)
pendown()
circle(10, 360)



#child 2
penup()
setposition(200,0)
pendown()
right(50)
forward(30)
right(100)
forward(30)
#backward(30)
#left(165)
#forward(20)
#penup()
#setposition(165,60)
#pendown()
#circle(10, 360)





	


sleep (8)