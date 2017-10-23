from Directories.VariablesTable import VarsTable

# Create functions directory with capacity for 1000 records
#FunctionsDirectory = funcDirectory()

# Create variables table with capacity for 1000 records
globalVariables = VarsTable()

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

globalVariables.insert("nombre", "int", "2000")

print(globalVariables.get('nombre'))
print(globalVariables.getVarsTotals())

