import turtle
win = turtle.Screen() 
shape = turtle.Turtle()


for sqaure in range(4):
    shape.forward(50)
    shape.right(90)


for triangle in range(3):
    shape.forward(50)
    shape.left(120)
    
win.mainloop()
