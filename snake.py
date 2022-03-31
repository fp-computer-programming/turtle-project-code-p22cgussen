# Author CCG 4/7/22

import turtle


# window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("grey")
wn.setup(width = 600, height = 600)
wn.tracer(0)
 
# starting snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
 

# header
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align = "center",
          font = ("system", 36, "bold"))
 
 
 
# functions for movement
def up():
    if head.direction != "down":
        head.direction = "up"
 
def down():
    if head.direction != "up":
        head.direction = "down"
 
def left():
    if head.direction != "right":
        head.direction = "left"
 
def right():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
         
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
