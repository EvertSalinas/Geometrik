from Tkinter import *
from turtle import *
from VirtualMachine.VirtualMachine import virtual_Machine

pen = Pen()
screen_width = pen.screen.window_width()
screen_height = pen.screen.window_height()
pen.screen.setup(width=screen_width / 2 + 150, height=screen_height / 2 + 150, startx=screen_width, starty=0)
pen.pencolor("red")
pen.down()
pen.speed(1)
pen.setposition(100, 0)
pen.speed(6)
pen.left(90)
pen.speed(1)
pen.setposition(100, 100)

'''
pen = Pen()
pen.pencolor("red")
pen.up()
pen.setposition(1, 1)
pen.down()
'''
'''
pen.forward(100)
pen.left(45)
pen.forward(100)
'''

done()


