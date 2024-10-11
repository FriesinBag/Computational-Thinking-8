import turtle, random, math 

t = turtle.Turtle()

# Intro
t.goto(-170,90)
colors = ["cyan", "white"]
turtle. bgcolor("black")

# circle 1
colors = ["Red"]
for i in range(75):
    t.color(random.choice(colors))
    t.forward(150)
    t.left(120+1)
    t.left(45)
    t.speed(70)
# circle 2
t.penup()
t.goto(175,-50)
t.pendown()
colors = ["white"]
for i in range(75):
    t.color(random.choice(colors))
    t.forward(150)
    t.left(120+1)
    t.left(45)
    t.speed(70)
# circle 3
t.penup()
t.goto(90,26)
t.pendown()
colors = ["blue"]
for i in range(75):
    t.color(random.choice(colors))
    t.forward(150)
    t.left(120+1)
    t.left(45)
    t.speed(70)
# circle 4
t.penup()
t.goto(-100,-23)
t.pendown()
colors = ["red", "blue"]
for i in range(75):
    t.color(random.choice(colors))
    t.forward(150)
    t.left(120+1)
    t.left(45)
    t.speed(70)


turtle.exitonclick()