from DataStructures.VariablesTable import VarsTable
from DataStructures.FunctionsDirectory import FunctionsDirectory

funcDirectory = FunctionsDirectory()
globalVariables = VarsTable()

funcDirectory.insert('func1', 'void')
funcDirectory.addParameterTypes('func1', ['int', 'float', 'string'])

funcDirectory.insert('func2', 'int')
funcDirectory.addParameterTypes('func2', ['int', 'boolean'])

parameters = funcDirectory.functions['func1']
parameters2 = funcDirectory.functions['func2']

funcDirectory.addFunctionVariable('func1','y','float','2000')

variable = funcDirectory.getVariable('func1', 'y')

print(variable)

# Insert reserved words to prevent them being used as identifiers
'''
globalVariables.insert("if", "if", "if")
globalVariables.insert("else", "else", "else")
globalVariables.insert("while", "while", "while")
globalVariables.insert("print", "print", "print")
globalVariables.insert("function", "function", "function")
globalVariables.insert("return", "return", "return")
globalVariables.insert("true", "true", "true")
globalVariables.insert("false", "false", "false")
globalVariables.insert("program", "program", "program")
globalVariables.insert("break", "break", "break")
globalVariables.insert("DrawCircle", "DrawCircle", "DrawCircle")
globalVariables.insert("DrawLine", "DrawLine", "DrawLine")
globalVariables.insert("DrawTriangle", "DrawTriangle", "DrawTriangle")
globalVariables.insert("DrawSquare", "DrawSquare", "DrawSquare")
globalVariables.insert("DrawPolygon", "DrawPolygon", "DrawPolygon")
globalVariables.insert("DrawCurve", "DrawCurve", "DrawCurve")
globalVariables.insert("Red", "Red", "Red")
globalVariables.insert("Green", "Green", "Green")
globalVariables.insert("Blue", "Blue", "Blue")
globalVariables.insert("Yellow", "Yellow", "Yellow")
globalVariables.insert("Brown", "Brown", "Brown")
globalVariables.insert("Black", "Black", "Black")
globalVariables.insert("int", "int", "int")
globalVariables.insert("boolean", "boolean", "boolean")
globalVariables.insert("float", "float", "float")
globalVariables.insert("string", "string", "string")
globalVariables.insert("void", "void", "void")
globalVariables.insert("input", "input", "input")
globalVariables.insert("var", "var", "var")
'''
