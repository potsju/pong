import turtle

wn = turtle.Screen()
wn.title("Pong by potsju")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#paddlea
paddlea = turtle.Turtle()
paddlea.speed(0) 
paddlea.shape("square")
paddlea.color("white")
paddlea.shapesize(stretch_wid = 5, stretch_len = 1 )
paddlea.penup()
paddlea.goto(-350, 0)

#paddleb
paddleb = turtle.Turtle()
paddleb.speed(0) 
paddleb.shape("square")
paddleb.color("white")
paddleb.shapesize(stretch_wid = 5, stretch_len = 1 )
paddleb.penup()
paddleb.goto(350, 0)

#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#Function
def paddle_a_up():
    y = paddlea.ycor()
    y += 20
    paddlea.sety(y)
def paddle_a_down():
    y = paddlea.ycor()
    y -= 20 
    paddlea.sety(y)  
def paddle_b_up():
    y = paddleb.ycor()
    y += 20
    paddleb.sety(y)
def paddle_b_down():
    y = paddleb.ycor()
    y -= 20 
    paddleb.sety(y)  


    

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#maingameloop
while True:
    wn.update()
    #move theball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 
    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.ycor() < paddlea.ycor() + 50 and ball.ycor() > paddlea.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
