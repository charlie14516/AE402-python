import turtle
t=turtle.Turtle()
t.shape('turtle')
t.penup()
for i in range(0,100,3):
    t.forward(30+i)
    t.left(30)
    t.stamp()