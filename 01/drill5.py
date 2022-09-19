import turtle

def turtle_move_top():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)    

def turtle_move_bottom():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def turtle_move_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
    
def turtle_move_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_move_top,'w')
turtle.onkey(turtle_move_bottom,'s')
turtle.onkey(turtle_move_left,'a')
turtle.onkey(turtle_move_right,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
