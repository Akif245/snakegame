from snake import Snake 
from turtle import Turtle,Screen
from food import food
import time
snake=Snake()
fd =food()
t=Turtle(shape="square")
t1=Turtle(shape="square")
t2=Turtle(shape="square")
screen=Screen() 
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Akif's Turtle Game\n")

t1.penup()
t2.penup()
screen.tracer(0)

                    
                                       #OTHER METHOD

#box=[]#segment
#positions=[(0,0),(-20,0),(-40,0)]

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(fd) < 15:
        print("pom pom pom")
   
 














screen.exitonclick()