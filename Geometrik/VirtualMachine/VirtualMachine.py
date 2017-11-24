import ply.yacc as yacc
import sys

sys.path.append("..")

from DataStructures.FunctionsDirectory import functions_Directory
from Memory.Memory import memory_Block
from DataStructures.Stack import Stack

from turtle import *

class virtual_Machine:

    def __init__(self, quadQueue, memory, functionsDirectory):
        self.memory = memory
        self.functionsDirectory = functionsDirectory
        self.quadQueue = quadQueue
        self.pen = self.penSetup()

        print memory.memoryBlock

        quadQueue.printQueue()
        print '\n'
        # Execute quadruples operations
        self.executeQuadruples()

    # Setup turtle screen and pen
    def penSetup(self):
        pen = Pen()
        pen.up()
        screen_width = pen.screen.window_width()
        screen_height = pen.screen.window_height()
        pen.screen.setup(width=screen_width / 2 + 300, height=screen_height / 2 + 300, startx=screen_width, starty=0)

        return pen

    def isInt(self, value):
        try:
            int(value)
            return True
        except (ValueError, TypeError):
            return False

    def isFloat(self, value):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    # Execute operations from quadruples
    def executeQuadruples(self):

        instructionPointer = 0

        valuesStack = Stack()
        functionsStack = Stack()
        savedIPs = Stack()
        speed = 8

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

            if quad.operator == '+':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                 #              quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue + rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '-':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue - rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '*':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue * rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '/':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #     quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue / rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '!':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                #print ('Left Operand Value', leftOperandValue)

                result = not(leftOperandValue)
                #print ('Result Value', result, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, result)

            elif quad.operator == '=':
                # print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                #print ('Left Operand Value', leftOperandValue)

                #print ('Result Value', leftOperandValue, ' on address', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, leftOperandValue)

            elif quad.operator == '<':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue < rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '>':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue > rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '<=':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                # print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue <= rightOperandValue
                # print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '>=':
                # print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                # print ('Left Operand Value', leftOperandValue)
                # print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue >= rightOperandValue
                # print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '==':
                # print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)
                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue == rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '||':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #     quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)

                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue or rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '&&':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)

                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue and rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == '!=':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                rightOperandValue = self.memory.getValueByAddress(rightOperand)

                #print ('Left Operand Value', leftOperandValue)
                #print ('Right Operand Value', rightOperandValue)

                resultValue = leftOperandValue != rightOperandValue
                #print ('Result Value', resultValue, ' on address ', resultAddress)

                self.memory.modifyValueByAddress(resultAddress, resultValue)

            elif quad.operator == 'WRITE':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)

                #print ('Left Operand Value', leftOperandValue)

                print leftOperandValue

            elif quad.operator == 'READ':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #     quad.result)

                input = raw_input()

                if self.isInt(input):
                    if leftOperand == 'int':
                        self.memory.modifyValueByAddress(resultAddress, int(input))
                    else:
                        print('Error: Input type mismatch, expecting ' + str(leftOperand))
                        sys.exit()
                elif self.isFloat(input):
                    if leftOperand == 'float':
                        self.memory.modifyValueByAddress(resultAddress, float(input))
                    else:
                        print('Error: Input type mismatch, expecting ' + str(leftOperand))
                        sys.exit()
                elif input == 'true':
                    if leftOperand == 'bool':
                        self.memory.modifyValueByAddress(resultAddress, True)
                    else:
                        print('Error: Input type mismatch, expecting ' + str(leftOperand))
                        sys.exit()
                elif input == 'false':
                    if leftOperand == 'bool':
                        self.memory.modifyValueByAddress(resultAddress, False)
                    else:
                        print('Error: Input type mismatch, expecting ' + str(leftOperand))
                        sys.exit()
                else:
                    if leftOperand == 'string':
                        self.memory.modifyValueByAddress(resultAddress, str(input))
                    else:
                        print('Error: Input type mismatch, expecting ' + str(leftOperand))
                        sys.exit()


            elif quad.operator == 'goto':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #     quad.result)

                instructionPointer = resultAddress - 2

            elif quad.operator == 'gotof':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                if leftOperandValue == False:
                    instructionPointer = resultAddress - 2

            elif quad.operator == 'gosub':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #     quad.result)

                savedIPs.push(quad.quad_number)
                instructionPointer = resultAddress - 2

            elif quad.operator == 'RETURN':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)

                #print ('leftoperand',self.memory.getValueByAddress(resultAddress))

                self.memory.modifyValueByAddress(rightOperand, leftOperandValue)
                instructionPointer = resultAddress - 2

                #print ('resultAddress',self.memory.getValueByAddress(resultAddress))

            elif quad.operator == 'ENDPROC':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                # quad.result)

                if not functionsStack.isEmpty():
                    functionName = functionsStack.pop()
                    function = self.functionsDirectory.functions[functionName]
                    varTable = function['variables']
                    variables = varTable.variables

                    for variable in variables:
                        variableInfo = variables[variable]

                        variableVirtualAddress = variableInfo[1]
                        self.memory.modifyValueByAddress(variableVirtualAddress, valuesStack.pop())

                instructionPointer = savedIPs.pop() - 1

            elif quad.operator == 'ERA':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #quad.result)

                function = self.functionsDirectory.functions[leftOperand]
                varTable = function['variables']
                variables = varTable.variables

                for variable in variables:
                    variableInfo = variables[variable]

                    variableVirtualAddress = variableInfo[1]
                    #print('return variableVirtualAddress ', variableVirtualAddress)
                    variableValue = self.memory.getValueByAddress(variableVirtualAddress)
                    #print('return variableValue ', variableValue)
                    valuesStack.push(variableValue)
                    #print('valuesStack        ', valuesStack.items)

                functionsStack.push(leftOperand)

            elif quad.operator == 'VER':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                index = self.memory.getValueByAddress(leftOperand)

                #print ('index', index)
                #print ('inf lim', rightOperand)
                #print ('sup lim', resultAddress)

                if not (index >= rightOperand and index <= resultAddress):
                    print("ERROR: Array index is out of bounds.")
                    sys.exit()

            elif quad.operator == 'PARAM':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                #      quad.result)

                leftOperandValue = self.memory.getValueByAddress(leftOperand)
                #print ('Left Operand Value', leftOperandValue)

                self.memory.modifyValueByAddress(resultAddress, leftOperandValue)
                #self.memory.modifyValueByAddress(resultAddress, result)

            elif quad.operator == 'DRAWLINE':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                 #     quad.result)

                color = rightOperand.lower()

                self.pen.pencolor(color)
                self.pen.speed(speed)
                self.pen.up()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[0]), self.memory.getValueByAddress(leftOperand[1]))
                #self.pen.speed(1)
                self.pen.down()
                self.pen.setposition(self.memory.getValueByAddress(leftOperand[2]), self.memory.getValueByAddress(leftOperand[3]))

            elif quad.operator == 'DRAWCIRCLE':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                 #     quad.result)

                #print ('Right Operand a', rightOperand)

                color = rightOperand.lower()

                self.pen.pencolor(color)
                self.pen.speed(speed)
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
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                 #     quad.result)

                color = rightOperand.lower()
                sidelength = self.memory.getValueByAddress(leftOperand[2])

                self.pen.pencolor(color)
                self.pen.speed(speed)
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
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                 #     quad.result)

                color = rightOperand.lower()
                sidelength = self.memory.getValueByAddress(leftOperand[2])

                if self.memory.getValueByAddress(leftOperand[4]) != 1 and self.memory.getValueByAddress(leftOperand[4]) != 2:
                    print("ERROR: Parameter must be 1 or 2.")
                    sys.exit()

                self.pen.pencolor(color)
                self.pen.speed(speed)
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
                    if self.memory.getValueByAddress(leftOperand[4]) != 1:
                        self.pen.left(120)
                    if self.memory.getValueByAddress(leftOperand[4]) != 2:
                        self.pen.right(120)
                if self.memory.getValueByAddress(leftOperand[3]) == True:
                    self.pen.end_fill()

            elif quad.operator == 'DRAWPOLYGON':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                 #     quad.result)

                sides =   self.memory.getValueByAddress(leftOperand[2])

                if not (sides >= 5 and sides <= 10):
                    print("ERROR: Polygon sides must be between 5 and 10.")
                    sys.exit()
                else:
                    color = rightOperand.lower()
                    sidelength = self.memory.getValueByAddress(leftOperand[3])
                    self.pen.pencolor(color)
                    self.pen.speed(speed)
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

            elif quad.operator == 'DRAWITC':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,quad.result)

                color = rightOperand.lower()

                self.pen.pencolor(color)
                self.pen.speed(speed)
                self.pen.up()
                self.pen.setposition(-300, 100)
                #self.pen.speed(1)
                self.pen.down()
                self.pen.setposition(-100, 100)
                self.pen.up()
                self.pen.setposition(-200, 100)
                self.pen.down()
                self.pen.setposition(-200, -100)
                self.pen.up()
                self.pen.setposition(-300, -100)
                self.pen.down()
                self.pen.setposition(-100, -100)

                self.pen.up()
                self.pen.setposition(-80, 100)
                self.pen.down()
                self.pen.setposition(120, 100)
                self.pen.up()
                self.pen.setposition(20, 100)
                self.pen.down()
                self.pen.setposition(20, -100)

                self.pen.up()
                self.pen.setposition(140, 100)
                self.pen.down()
                self.pen.setposition(340, 100)
                self.pen.up()
                self.pen.setposition(140, 100)
                self.pen.down()
                self.pen.setposition(140, -100)
                self.pen.setposition(340, -100)

            elif quad.operator == 'END':
                #print("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,quad.result)
                self.pen.hideturtle()
                done()

            instructionPointer += 1
