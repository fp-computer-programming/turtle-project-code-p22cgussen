# Author CCG 4/7/22

import turtle
import random
import time


#creating turtle screen
screen = turtle.Screen()
screen.title('Snake')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('purple')



##creating a border for our game

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('white')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('white')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(100,0)

body = []

#scoring
score = 0
delay = 0.1
scoring = turtle.Turtle()
scoring.hideturtle()



#######define how to move
def up():
    if snake.direction != "down":
        snake.direction = "up"

def down():
    if snake.direction != "up":
        snake.direction = "down"

def left():
    if snake.direction != "right":
        snake.direction = "left"

def right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

#main loop

while True:
        screen.update()
            #snake and fruit coliisions
        if snake.distance(fruit)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                fruit.goto(x,y)
                scoring.clear()
                score+=1
                
                ## creating new_ball
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('square')
                new_fruit.color('red')
                new_fruit.penup()
                body.append(new_fruit)
                

        #adding ball to snake
        
        for index in range(len(body)-1,0,-1):
                a = body[index-1].xcor()
                b = body[index-1].ycor()

                body[index].goto(a,b)
                                     
        if len(body)>0:
                a= snake.xcor()
                b = snake.ycor()
                body[0].goto(a,b)
        move()

        ##snake and border collision    
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('grey')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Arial",40,"bold"))


        ## snake collision
        for food in body:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('grey')
                        scoring.goto(0,0)
                        scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Arial",40,"bold"))


                
        time.sleep(delay)

turtle.Terminator()