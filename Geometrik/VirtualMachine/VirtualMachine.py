import ply.yacc as yacc
import sys

sys.path.append("..")

from DataStructures.FunctionsDirectory import functions_Directory
from Memory.Memory import memory_Block

from Tkinter import *
from turtle import *

class virtual_Machine:

    def __init__(self, quadQueue, memory, functionsDirectory, programid):
        self.memory = memory_Block()
        self.functionsDirectory = functions_Directory()
        self.instructionPointer = 0
        self.rootWindow = Tk()
        self.windowHeight = 500
        self.windowWidth = 500
        print memory.memoryBlock

    def printMemory(self):
        print self.memory.memoryBlock


'''
pen = Pen()
pen.pencolor("red")
pen.forward(100)
pen.left(45)
pen.forward(100)
done()
'''