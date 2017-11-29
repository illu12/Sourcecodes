from turtle import *
s=Screen()
t=Turtle()
def up():
    y=ycor()
    x=xcor()
    goto(x,y+100)

def down():
    y=ycor()
    x=xcor()
    goto(x,y-100)

def left():
    y=ycor()
    x=xcor()
    goto(x-100,y)

def right():
    y=ycor()
    x=xcor()
    goto(x+100,y)

s.onkey(up, 'w')
s.onkey(down, 's')
s.onkey(left, 'a')
s.onkey(right, 'd')
s.listen()

