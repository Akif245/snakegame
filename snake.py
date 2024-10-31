from turtle import Turtle


POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self. box=[]
        self.create_snake()
        self.head=  self.box[0]

    def create_snake(self):
        for pos in POSITIONS:
            tim=Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(pos)
            self.box.append(tim)
    
    def move(self):
        for seg_num in range(len(self.box)-1,0,-1):
            new_x=self.box[seg_num-1 ].xcor()
            new_y=self.box[seg_num-1 ].ycor()
            self.box[seg_num].goto(new_x,new_y)
        self.box[0].forward(MOVE)
    
    def up(self):
        self.head.setheading(UP)
    
    def down(self):
        self.head.setheading(DOWN)
    
    def right(self):
        self.head.setheading(RIGHT)
    
    def left(self):
        self.head.setheading(LEFT)

