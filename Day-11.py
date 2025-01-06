#ARROW REPRESENTATION USING TURTLE
import turtle
t= turtle.Turtle()
turtle.mainloop()

#SHAPE USING TURTLE
t.shape("arrow")    
help(turtle)
help(turtle.shape)

#COLOR AND SHAPE USING TURTLE
import turtle
t= turtle.Turtle()
t.shape("arrow")
t.color()
t.forward(100)
t.color("blue")
t.forward(100)
t.color("green","red")
turtle.color_mode(225)
t.color(10,20,30)
t.home()
turtle.done()

#BACKGROUND COLOR USING TURTLE
import turtle
wn=turtle.Screen()
wn.bgcolor("blue")
turtle.colormode(255)
turtle.done()

#BACKGROUND COLOR USING TURTLE
import turtle
t=turtle.Turtle()
turtle.bgcolor("red")
turtle.mainloop()

#TITLE USING TURTLE
import turtle
wn=turtle.Screen()
wn.title("PYTHON PROGRAMMING USING TURTLE")
turtle.done()

#BACKGROUND IMAGE USING TURTLE
import turtle
wn = turtle.Screen()
wn.bgpic("")  
turtle.done()

#TURTLE DIRECTIONS - FORWARD, BACKWARD, LEFT, RIGHT
#MOVING FORWARD USING TURTLE 
import turtle
t=turtle.Turtle()
t.forward(100)
turtle.mainloop()

#MOVING BACKWARD USING TURTLE 
import turtle
t=turtle.Turtle()
t.backward(100)
t.hideturtle()
turtle.mainloop()

#MOVING RIGHT USING TURTLE 
import turtle
t=turtle.Turtle()
t.heading()
t.right(25)
t.heading()
turtle.mainloop()

#MOVING LEFT USING TURTLE 
import turtle
t=turtle.Turtle()
t.heading()
t.left(100)
t.heading()
turtle.mainloop()

#MOVING TO ANY POSITION USING TURTLE 
import turtle
t=turtle.Turtle()
t.heading()
t.setpos(100, 80)
turtle.mainloop()

#RECTANGLE USING TURTLE
import turtle
t=turtle.Turtle()
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

#CIRCLE USING TURTLE
import turtle
t=turtle.Turtle()
t.circle(50)
turtle.mainloop()

#CHANGING PENSIZE USING TURTLE
import turtle
t=turtle.Turtle()
t.pensize(3)
t.forward(200)
turtle.mainloop()

#PEN COLOR USING TURTLE
import turtle
t=turtle.Turtle()
t.shapesize(3,3,3)
t.fillcolor("blue")
t.pencolor("yellow")
turtle.mainloop()

#ROUND USING TURTLE
import turtle
t=turtle.Turtle()
t.speed(0)
for x in range(1,50):
    t.forward(2*x)
    t.left(91)
turtle.mainloop()

#ROUND COLOR USING TURTLE
import turtle
t=turtle.Turtle()
t.speed(0)
for x in range(1,50):
    if x%4==0:
        t.pencolor("red")
    elif x%4==2:
        t.pencolor("blue")
    else:
        t.pencolor("yellow")
    t.forward(3*x)
    t.left(91)
turtle.mainloop()

#FILLUP COLORS
import turtle
t= turtle.Turtle()
t.pencolor("red")
t.fillcolor("orange")
t.pensize(10)
t.speed(7)
t.begin_fill()
t.circle(75)
turtle.bgcolor("blue")
t.end_fill()
turtle.mainloop()

#SPIRO
import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
while(True):
    for i in range(6):
        for colors in ["red","blue","magenta","green","yellow","white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)
        
#STAR USING TURTLE
import turtle
my_pen=turtle.Turtle()
for i in range(50):
    my_pen.forward(50)
    my_pen.right(144)
turtle.done()

#TIC-TAC-TOE USING TURTLE
import turtle
window = turtle.Screen()
window.title("Tic-Tac-Toe Game")
window.bgcolor("white")
t = turtle.Turtle()
t.pensize(5)
t.pencolor("dark red")
t.penup()
t.goto(-50, 100)
t.pendown()
t.setheading(270)
t.forward(200)
t.penup()
t.goto(50, 100)
t.pendown()
t.forward(200)
t.penup()
t.goto(-100, 50)
t.pendown()
t.setheading(0)
t.forward(200)
t.penup()
t.goto(-100, -50)
t.pendown()
t.forward(200)
t.hideturtle()
turtle.done()

#VIRUS
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
    t.hideturtle()
turtle.done() 

#HEART
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
turtle.pensize(2)
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
t.speed(5)
t.color("red","pink")
t.begin_fill()
t.left(140)
t.forward(111.65)
curve()
t.left(120)
curve()
t.forward(111.65)
t.end_fill()
t.hideturtle()
turtle.mainloop()

#CHESS BOARD
import turtle
scr = turtle.Screen()
ttl = turtle.Turtle()
def draw():
    for i in range(4):
        ttl.forward(35)
        ttl.left(90)
    ttl.forward(35)
if __name__ == "__main__":
    scr.setup(500, 700)
    ttl.speed(90)
    for j in range(8):
        ttl.up()
        ttl.setpos(-110, 35 * j)
        ttl.down()
        for k in range(8):
            if (j + k) % 2 == 0:
                clr = 'black'
            else:
                clr = 'white'
            ttl.fillcolor(clr)
            ttl.begin_fill()
            draw()
            ttl.end_fill()
ttl.hideturtle()
turtle.done()

#INDIAN FLAG
import turtle
from turtle import *
scr = turtle.Screen()
ttl = turtle.Turtle()
ttl.hideturtle()
speed(20)
ttl.penup()
ttl.goto(-150, 125)
ttl.pendown()
ttl.color("orange")
ttl.begin_fill()
for _ in range(2):
    ttl.forward(400)
    ttl.right(90)
    ttl.forward(133)
    ttl.right(90)
ttl.end_fill()
ttl.penup()
ttl.goto(-150, -8)
ttl.pendown()
ttl.color("white")
ttl.begin_fill()
for _ in range(2):
    ttl.forward(400)
    ttl.right(90)
    ttl.forward(133)
    ttl.right(90)
ttl.end_fill()
ttl.penup()
ttl.goto(-150, -125)
ttl.pendown()
ttl.color("green")
ttl.begin_fill()
for _ in range(2):
    ttl.forward(400)
    ttl.right(90)
    ttl.forward(133)
    ttl.right(90)
ttl.end_fill()
ttl.penup()
ttl.goto(60, -80)
ttl.pendown()
ttl.color("navy")
ttl.begin_fill()
ttl.circle(30)
ttl.end_fill()
ttl.penup()
ttl.goto(60, -50)
ttl.pendown()
ttl.color("white")
ttl.begin_fill()
ttl.circle(1)
ttl.end_fill()
ttl.color("navy")
ttl.penup()
ttl.goto(60, -50)
ttl.pendown()
ttl.begin_fill()
ttl.circle(10)
ttl.end_fill()
ttl.color("white")
ttl.penup()
ttl.goto(60, -50)
ttl.pendown()
ttl.pensize(1)
for j in range(24):
    ttl.forward(30)
    ttl.backward(30)
    ttl.left(15)
ttl.hideturtle()
turtle.done()

#ON-CLICK
import turtle
def fxn(x,y):
    turtle.right(90)
    turtle.forward(100)
turtle.speed(1)
turtle.fd(100)
turtle.onclick(fxn)
turtle.done()

#DRAG THE CURSOR
import turtle
def fxn(x, y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(fxn)
turtle.speed(1)
turtle.ondrag(fxn)
turtle.done()
