import turtle
t=turtle.Turtle()
n=int(input('請問要畫幾邊形'))
for i in range(n):
    t.forward(10)
    t.left(360/n)