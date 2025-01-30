import turtle
import time
import datetime
import random

# set up the screen
window=turtle.Screen()
# title
window.title("Snake Game")
# colour of background
window.bgcolor("black")
# size of window
window.setup(width=1000,height=700)
# window.tracer(n): The argument n specifies the number of turtle actions between updates. If n=0, updates are disabled until window.update() is called manually.
# window.tracer(0) turns off automatic screen updates. After calling this, the screen won’t update until you explicitly call window.update(), making complex drawings much faster.
window.tracer(0)

# snake head
head=turtle.Turtle()
# set the animation speed
head.speed(0) # 0 is the fastest speed without animation
head.shape("circle")
head.color("white")
head.penup() # no tracing of the path
# set the starting location of snake
head.goto(0,0)
head.direction="stop" # initially the snake is stopped

# snake food
food=turtle.Turtle()
food.shape("square")
food.color("red")
food.shapesize(0.5)
food.penup()
food.goto(100,100)

# special food
sp=turtle.Turtle()
sp.shape("square")
sp.color("orange")
sp.penup()
sp.goto(1000,1200)
        

# display of score
ps=turtle.Turtle()
ps.speed(0)
ps.shape("square")
ps.color("green")
ps.penup()
ps.hideturtle() # hide the turtle
ps.goto(0,300)
ps.write("Score : 0                        High Score : 0", align="center",font=("arial",28,"normal"))

# score
score=0
highscore=0

#body of the snake
body=[]
 
# directions giving functions
def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"

# main functions
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    elif head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    elif head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    elif head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

# set delay
delay=0.3 

check=True
tt=time.time()
check1=True
ss=0

# keyboard inputs
window.listen()
window.onkeypress(moveup,"Up")
window.onkeypress(movedown,"Down")
window.onkeypress(moveleft,"Left")
window.onkeypress(moveright,"Right")

# variable for setting snake speed 
speed=0

# main game loop
while True:
    window.update()
    
    # head touches the borders
    if head.xcor()>490:
        x=(-1)*head.xcor()
        y=head.ycor()
        head.goto(x,y)
    elif head.xcor()<-490:
        x=(-1)*head.xcor()
        y=head.ycor()
        head.goto(x,y)
    elif head.ycor()>340:
        y=(-1)*head.ycor()
        x=head.xcor()
        head.goto(x,y)
    elif head.ycor()<-340:
        y=(-1)*head.ycor()
        x=head.xcor()
        head.goto(x,y)
    
    # snake eats the food
    if head.distance(food)<20:
        y=random.randint(-340,295)
        x=random.randint(-490,490)
        food.goto(x,y)
        
        #increasing the length of the body
        bodypart=turtle.Turtle()
        bodypart.speed(0)
        bodypart.color("yellow")
        bodypart.shape("square")
        bodypart.penup()
        body.append(bodypart)
        
        # increase the score
        score += 5
        highscore=max(score,highscore)
        ps.clear()
        ps.write("Score : {}                        High Score : {}".format(score,highscore), align="center",font=("arial",28,"normal"))
    
    # for special food
    if head.distance(sp)<20:
        sp.goto(1000,1000)
        score += 10
        highscore=max(score,highscore)
        ps.clear()
        ps.write("Score : {}                        High Score : {}".format(score,highscore), align="center",font=("arial",28,"normal"))
        check=True
        check1=True
        # increase the length of body
        bodypart=turtle.Turtle()
        bodypart.speed(0)
        bodypart.color("yellow")
        bodypart.shape("square")
        bodypart.penup()
        body.append(bodypart)
    
    # move the body parts
    for index in range(len(body)-1,0,-1):
        x=body[index-1].xcor()
        y=body[index-1].ycor()
        body[index].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()

    
    # head meets the body
    for bp in body:
        if bp.distance(head)<20:
            time.sleep(0.5)
            head.goto(0,0)
            food.goto(100,100)
            sp.goto(1000,1000)
            head.direction="stop"
            for bparts in body:
                bparts.goto(2000,2000)
            body.clear()
            score=0
            ps.clear()
            ps.write("Score : {}                        High Score : {}".format(score,highscore), align="center",font=("arial",28,"normal"))
            delay=0.3
    
    if score>30 and score<50:
        delay=0.3*0.75
    
    if score >50 and score<80:
        delay=0.225*0.75 
    
    if score >80 and score<100:
        delay=0.16*0.75 
    
    if score >100 and score<150:
        delay=0.12*0.75     
    
    if score >150 and score<200:
        delay=0.094*0.75 
    
    if score >200 and score<300:
        delay=0.07*0.75 
        
    if score >300:
        delay=0.05*0.75 
    
    if score>ss and ss%30==0:
        check1=True  
    
    if score%30==0 and score!=0:
        t=time.time()
        if check1==True:    
            if check==True:
                y=random.randint(-340,295)
                x=random.randint(-490,490)
                sp.goto(x,y)
                check=False
                tt=t
                ss=score
    if score!=0 and time.time()-tt>=10:
            sp.goto(1000,1000)
            check=True
            check1=False    
    time.sleep(delay) #delay in the movement of snake


window.mainloop()