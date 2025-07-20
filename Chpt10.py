#####################################
## Alice Hsu
## Chapter 6: Programming Exercise
## HW Pg 407: #4, 6, 9, Pg150: #15 p 262 #15  p 34 #22
#####################################


## Item Counter
file=open("names.txt","r")
lines=file.readlines()
file.close()

count=0
for line in names:
    name=line.strip()
    if name and name[0].isupper():
        count+=1

print("Number of names in the file:",count)


## Average Number
with open("numbers.txt","r") as file:
    total=0
    count=0
    for line in file:
        number=int(line.strip())
        total+=number
        count+=1
    if count>0:
        average=total/count
        print("Average:",average)
    else:
        print("The file is empty.")


## Exception Handling
file=open("numbers.txt","r")
total=0
count=0
lines=file.readlines()
file.close()

for line in lines:
    clean_line=line.strip()
    if clean_line.isdigit():
        number=int(clean_line)
        total+=number
        count+=1
    else:
        print("Skipping invalid value:",clean_line)

if count>0:
    average=total/count
    print("Average:",average)
else:
    zprint("No valid numbers to average.")


## Draw Pattern
rows=6
for row in range(rows):
    for col in range(row+1):
        if col==0 or col==row:
            print("#",end="")
        else:
            print(" ",end="")
    print()
    

## Turtle Graphics Drawings
#1
import turtle
turtle.pensize(2)

def diamond(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.setheading(45)
    turtle.begin_fill()
    for length in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

diamond(-80,0)
diamond(60,0)

turtle.hideturtle()
turtle.done()

#2
import turtle
turtle.pensize(2)
turtle.color("black")

def large_triangle():
    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()
    turtle.goto(100,0)
    turtle.goto(0,200)
    turtle.goto(-100,0)

def small_triangle():
    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.goto(100,0)
    turtle.goto(0,100)
    turtle.goto(-100,0)
    turtle.end_fill()

large_triangle()
small_triangle()

turtle.hideturtle()
turtle.done()

#3
import turtle
turtle.pensize(2)

front_bl=(-50,-50)
front_br=(50,-50)
front_tr=(50,50)
front_tl=(-50,50)
back_bl=(front_bl[0]+100,front_bl[1]+-100)
back_br=(front_br[0]+100,front_br[1]+-100)
back_tr=(front_tr[0]+100,front_tr[1]+-100)
back_tl=(front_tl[0]+100,front_tl[1]+-100)

turtle.penup()
turtle.goto(front_bl)
turtle.pendown()

turtle.goto(front_br)
turtle.goto(front_tr)
turtle.goto(front_tl)
turtle.goto(front_bl)
turtle.goto(back_bl)
turtle.goto(back_br)
turtle.goto(back_tr)
turtle.goto(back_tl)
turtle.goto(back_bl)
turtle.goto(front_bl)
turtle.goto(back_bl)
turtle.goto(back_br)
turtle.goto(front_br)
turtle.goto(front_tr)
turtle.goto(back_tr)
turtle.goto(back_tl)
turtle.goto(front_tl)

turtle.hideturtle()
turtle.done()

#4
import turtle
turtle.pensize(2)

def circle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.circle(40)

circle(-100,0)
circle(0,0)
circle(100,0)
circle(-60,-50)
circle(60,-50)

turtle.hideturtle()
turtle.done()

#5
import turtle
turtle.pensize(2)

turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
turtle.circle(20)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.goto(0,100)
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.goto(100,0)

turtle.penup()
turtle.goto(0,110)
turtle.write("North",align="center",font=("Arial",12,"normal"))
turtle.goto(140,-10)
turtle.write("East",align="center",font=("Arial",12,"normal"))
turtle.goto(0,-120)
turtle.write("South",align="center",font=("Arial",12,"normal"))
turtle.goto(-140,-10)
turtle.write("West",align="center",font=("Arial",12,"normal"))

turtle.hideturtle()
turtle.done()

#6
import turtle
turtle.pensize(2)

points=[(-100,100),(100,100),(100,-100),(-100,-100)]
center=(0,0)

def dot(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(10,"black")

def dash_line(start,end,dash=20):
    turtle.penup()
    turtle.goto(start)
    turtle.setheading(turtle.towards(end))
    dist=turtle.distance(end)
    steps=int(dist/dash/2)
    for length in range(steps):
        turtle.pendown()
        turtle.forward(dash)
        turtle.penup()
        turtle.forward(dash)

dash_line(points[0],points[1])
turtle.penup()
turtle.goto(points[1])
turtle.pendown()
turtle.goto(points[2])
dash_line(points[2],points[3])
turtle.penup()
turtle.goto(points[3])
turtle.pendown()
turtle.goto(points[0])

for p in points:
    dot(p[0],p[1])
dot(center[0],center[1])

for p in points:
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.goto(p)

turtle.hideturtle()
turtle.done()
