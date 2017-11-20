import ply.yacc as yacc
import sys

sys.path.append("..")

from DataStructures.FunctionsDirectory import functions_Directory
from Memory.Memory import memory_Block
from DataStructures.Stack import Stack

from turtle import *

class virtual_Machine:

    def __init__(self, quadQueue, memory, functionsDirectory, programid):
        self.memory = memory
        self.functionsDirectory = functionsDirectory
        self.quadQueue = quadQueue
        self.programID = programid
        self.pen = self.penSetup()
        self.windowHeight = 500
        self.windowWidth = 500

        print memory.memoryBlock
        quadQueue.printQueue()
        print '\n'
        self.executeOperations()
        print memory.memoryBlock

    def penSetup(self):
        pen = Pen()
        pen.up()
        screen_width = pen.screen.window_width()
        screen_height = pen.screen.window_height()
        pen.screen.setup(width=screen_width / 2 + 150, height=screen_height / 2 + 150, startx=screen_width, starty=0)

        return pen

    def executeOperations(self):

        instructionPointer = 0
        saveIP = 0

        while instructionPointer < self.quadQueue.size():

            quadLocation = self.quadQueue.size() - instructionPointer - 1
            quad = self.quadQueue.get(quadLocation)

            leftOperand = quad.left_operand
            rightOperand = quad.right_operand
            resultAddress = quad.result

            if isinstance(quad.left_operand, list):
                if len(quad.left_operand) == 1:
                    leftOperand = self.memory.getValueByAddress(quad.left_operand[0])
            if isinstance(quad.right_operand, list):
                if len(quad.right_operand) == 1:
                    rightOperand = self.memory.getValueByAddress(quad.right_operand[0])
            if isinstance(quad.result, list):
                if len(quad.result) == 1:
                    resultAddress = self.memory.getValueByAddress(quad.result[0])

            # Addition operations
            if quad.operator == '+':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                               quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue + rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '-':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue - rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '*':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue * rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '/':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue / rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '!':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                print ('Left Operand Value', leftOperandValue)

                result = not(leftOperandValue)
                print ('Result Value', result, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, result)

            elif quad.operator == '=':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                print ('Left Operand Value', leftOperandValue)

                print ('Result Value', leftOperandValue, ' on address', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, leftOperandValue)

            elif quad.operator == '<':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue < rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '>':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue > rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '<=':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue <= rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '>=':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue >= rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '==':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue == rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '||':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)

                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue or rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '&&':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)

                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue and rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '!=':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)

                print ('Left Operand Value', leftOperandValue)
                print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue != rightOperandValue
                print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == 'WRITE':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)

                print ('Left Operand Value', leftOperandValue)

                print leftOperandValue

            elif quad.operator == 'READ':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                value = raw_input()

                self.memory.modifyValueByAddress(resultAddress, value)

            elif quad.operator == 'goto':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                instructionPointer = resultAddress - 2

            elif quad.operator == 'gotof':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)
                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                if leftOperandValue == False:
                    instructionPointer = resultAddress - 2

            elif quad.operator == 'gosub':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                saveIP = quad.quad_number
                instructionPointer = resultAddress - 2
                #funcsStack.push(instructionPointer)

            elif quad.operator == 'RETURN':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)

                functionVariable = self.functionsDirectory.getFunctionVariable(self.programID, quad.result)

                funcVirtualAddress = functionVariable[1][1]

                self.memory.modifyValueByAddress(funcVirtualAddress, leftOperandValue)

            elif quad.operator == 'ENDPROC':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                instructionPointer = saveIP - 1

            elif quad.operator == 'VER':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                index = self.memory.getValueByAddress(leftOperand)

                print ('index', index)
                print ('inf lim', rightOperand)
                print ('sup lim', resultAddress)

                if not (index >= rightOperand and index <= resultAddress):
                    print("ERROR: Array index is out of bounds.")
                    sys.exit()
                else:
                    print('in Bounds')

            elif quad.operator == 'PARAM':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                print ('Left Operand Value', leftOperandValue)

                self.memory.modifyValueByAddress(resultAddress, leftOperandValue)
                #self.memory.modifyValueByAddress(resultAddress, result)

            elif quad.operator == 'DRAWLINE':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                print ('Right Operand a', rightOperand)

                color = rightOperand.lower()

                self.pen.pencolor(color)
                self.pen.speed(8)
                self.pen.up()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[0]), self.memory.getValueByAddress(leftOperand[1]))
                #self.pen.speed(1)
                self.pen.down()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[2]), self.memory.getValueByAddress(leftOperand[3]))

            elif quad.operator == 'DRAWCIRCLE':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                print ('Right Operand a', rightOperand)

                color = rightOperand.lower()

                self.pen.pencolor(color)
                self.pen.speed(8)
                self.pen.up()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[0]), self.memory.getValueByAddress(leftOperand[1]))
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.color(color)
                    self.pen.begin_fill()
                #self.pen.speed(1)
                self.pen.down()
                self.pen.circle(self.memory.getValueByAddress(leftOperand[2]))
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.end_fill()

            elif quad.operator == 'DRAWSQUARE':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                print ('Left Operand 0', self.memory.getValueByAddress(leftOperand[0]))
                print ('Left Operand 1', self.memory.getValueByAddress(leftOperand[1]))
                print ('Left Operand 2', self.memory.getValueByAddress(leftOperand[2]))

                print ('Right Operand a', rightOperand)

                color = rightOperand.lower()
                sidelength = self.memory.getValueByAddress(leftOperand[2])

                self.pen.pencolor(color)
                self.pen.speed(8)
                self.pen.up()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[0]), self.memory.getValueByAddress(leftOperand[1]))
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.color(color)
                    self.pen.begin_fill()
                #self.pen.speed(1)
                self.pen.down()
                for i in range(0, 4):
                    self.pen.forward(sidelength)
                    self.pen.left(90)
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.end_fill()

            elif quad.operator == 'DRAWTRIANGLE':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                print ('Left Operand 0', self.memory.getValueByAddress(leftOperand[0]))
                print ('Left Operand 1', self.memory.getValueByAddress(leftOperand[1]))
                print ('Left Operand 2', self.memory.getValueByAddress(leftOperand[2]))

                print ('Right Operand a', rightOperand)

                color = rightOperand.lower()
                sidelength = self.memory.getValueByAddress(leftOperand[2])

                self.pen.pencolor(color)
                self.pen.speed(8)
                self.pen.up()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[0]),
                                     self.memory.getValueByAddress(leftOperand[1]))
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.color(color)
                    self.pen.begin_fill()
                #self.pen.speed(1)
                self.pen.down()
                for i in range(0, 3):
                    self.pen.forward(sidelength)
                    self.pen.left(120)
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.end_fill()

            elif quad.operator == 'DRAWPOLYGON':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                print ('Left Operand 0', self.memory.getValueByAddress(leftOperand[0]))
                print ('Left Operand 1', self.memory.getValueByAddress(leftOperand[1]))
                print ('Left Operand 2', self.memory.getValueByAddress(leftOperand[2]))
                print ('Left Operand 3', self.memory.getValueByAddress(leftOperand[3]))
                print ('Left Operand 3', self.memory.getValueByAddress(leftOperand[4]))

                sides =   self.memory.getValueByAddress(leftOperand[2])

                if not (sides >= 5 and sides <= 10):
                    print("ERROR: Polygon sides must be between 5 and 10.")
                    sys.exit()
                else:
                    color = rightOperand.lower()
                    sidelength = self.memory.getValueByAddress(leftOperand[3])
                    self.pen.pencolor(color)
                    self.pen.speed(8)
                    self.pen.up()
                    self.pen.setposition(self.memory.getValueByAddress(leftOperand[0]),
                                         self.memory.getValueByAddress(leftOperand[1]))
                    #self.pen.speed(1)
                    self.pen.down()

                    if self.memory.getValueByAddress(leftOperand[4]) == True:
                        self.pen.color(color)
                        self.pen.begin_fill()

                    if sides == 5:
                        for i in range(0, 5):
                            self.pen.forward(sidelength)
                            self.pen.left(72)
                    elif sides == 6:
                        for i in range(0, 6):
                            self.pen.forward(sidelength)
                            self.pen.left(60)
                    elif sides == 7:
                        for i in range(0, 7):
                            self.pen.forward(sidelength)
                            self.pen.left(51.43)
                    elif sides == 8:
                        for i in range(0, 8):
                            self.pen.forward(sidelength)
                            self.pen.left(45)
                    elif sides == 9:
                        for i in range(0, 9):
                            self.pen.forward(sidelength)
                            self.pen.left(40)
                    elif sides == 10:
                        for i in range(0, 10):
                            self.pen.forward(sidelength)
                            self.pen.left(36)

                    if self.memory.getValueByAddress(leftOperand[4]) == True:
                        self.pen.end_fill()

            elif quad.operator == 'END':
                print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                      quad.result)

                done()

            instructionPointer += 1