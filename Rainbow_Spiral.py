import turtle as t
import time
colors = ["lavender", "pink", "light blue"]
t.shape("turtle")
t.speed(25)



for x in range(360):
    t.pencolor(colors[x % 3])
    t.forward(x)
    t.left(59)
 
        
t.setpos(-364.8986688927097, -10.42586197167094)

#t.pencolor("black")
#t. write("Thanks for Watching.\n\nWish the turtle your best regards, it's pretty dizzy.", font=("Arial", 20, 'italic'))


