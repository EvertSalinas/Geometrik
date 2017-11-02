import ply.yacc as yacc
import sys

sys.path.append("..")

from scannerLex import tokens
from DataStructures.FunctionsDirectory import functions_Directory
from DataStructures.Stack import Stack
from DataStructures.VariablesTable import vars_Table
from DataStructures.Quadruple import Quadruple
from DataStructures.Queue import Queue
from SemanticCube.SemanticCube import semantic_Cube

#-----------------------------------------------------------------

# Directories
functionsDirectory = functions_Directory();
semanticCube = semantic_Cube();

# Scope management variables
currentScope = ""
globalScope = ""

# Counter variables
quadCounter = 1
tempCounter = 1

# Stacks
operatorsStack = Stack()
operandsStack = Stack()
typesStack = Stack()
jumpsStack = Stack()

# Queues
quadQueue = Queue()

# Dimension management variables
dimension = {}
dimensionVar = ""

# Precedence rules
precedence = (
    ('left', 'EQUAL', 'NOTEQUAL'),
    ('left', 'LESSER', 'GREATER', 'LESSEROREQUAL','GREATEROREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DEVIDE'),
    ('nonassoc', 'LPAREN', 'RPAREN')
)

# Grammar rules
def p_PROGRAM(p):
    '''
    program : PROGRAM ID add_global_function SEMICOLON vars function main
            | sexpression
    '''

    print("Correct Sintax.")

def p_add_global_function(p):
    '''add_global_function : '''

    global currentScope
    global globalScope

    # Save the current function name
    globalScope = p[-1]
    currentScope = p[-1]

    # Create function directory variable
    functionsDirectory.insert(currentScope, 'void')
    print("add_global_func", currentScope, functionsDirectory.getFunctionType(currentScope))

    # a = functionsDirectory.getFunctionType(currentScope)
    # print(a)

def p_MAIN(p):
    '''
    main : INTTYPE MAIN LPAREN RPAREN switch_to_global_scope block
    '''

def p_switch_to_global_scope(p):
    '''
    switch_to_global_scope :
    '''

    global currentScope
    global globalScope

    # Switch to global scope
    currentScope = globalScope

    #functionsDirectory.addStartingQuad(globalScope, quadCont)
    #print("switch_to_global_scope", functionsDirectory.getStartingQuad(currentScope))

def p_BLOCK(p):
    '''
    block : LBRACE blockprima RBRACE
    '''

def p_BLOCKPRIMA(p):
    '''
    blockprima : statute blockprima
               | empty
    '''

def p_STATUTE(p):
    '''
    statute : assignment
            | condition
            | write
            | read
            | cycle
            | functioncall
            | predefined
            | return
    '''

def p_CONDITION(p):
    '''
    condition : IF LPAREN sexpression RPAREN do_condition_operation block
    '''

def p_do_condition_operation(p):
    'do_condition_operation : '
    doConditionOperation(p)

def p_CONDITIONPRIMA(p):
    '''
    conditionprima : condprimaaux
                   | NOT condprimaaux
    '''

def p_CONDPRIMAAUX(p):
    '''
    condprimaaux : functioncall
                 | sexpression
    '''

def p_VARS(p):
    '''
    vars : VAR type ID array store_variable SEMICOLON vars
         | empty
    '''

def p_store_variable(p):
    '''
    store_variable :
    '''

    global currentScope

    # Get varable name and type
    varName = p[-2]
    varType = p[-3]

    # varName needs to be change to virtual address
    if not functionsDirectory.addFunctionVariable(currentScope, varName, varType, varName):
        print('Error, variable already declared')

    print("store_variable", currentScope, functionsDirectory.getFunctionVariable(currentScope, varName),
          "line: " + str(p.lexer.lineno))

def p_ARRAY(p):
    '''
    array : LBRACKET sexpression RBRACKET
          | empty
    '''

def p_TYPE(p):
    '''
    type : INTTYPE
         | FLOATTYPE
         | STRINGTYPE
         | BOOLTYPE
    '''
    p[0] = p[1]


def p_ASSIGNMENT(p):
    '''
    assignment : ID push_id_operand ASSIGN push_operator sexpression SEMICOLON
    '''
    doAssignOperation(p)

def p_push_id_operand(p):
    '''
    push_id_operand :
    '''

    varId = p[-1]

    global currentScope

    funcVar = functionsDirectory.getFunctionVariable(currentScope, varId)

    if funcVar is None:
        funcVar = functionsDirectory.getFunctionVariable(globalScope, varId)
        print("funcVar", funcVar)
        if funcVar is None:
            errorVariableNotDeclared(p, varId)
        else:
            funcVarInfo = funcVar[1]

            funcVarType = funcVarInfo[0]
            funcVarOperand = funcVarInfo[1]

            operandsStack.push(funcVarOperand)
            typesStack.push(funcVarType)
    else:
        funcVarInfo = funcVar[1]

        funcVarType = funcVarInfo[0]
        funcVarOperand = funcVarInfo[1]

        operandsStack.push(funcVarOperand)
        typesStack.push(funcVarType)

    print("push_id_operand", operandsStack.top(), typesStack.top())

def p_push_operator(p):
    '''
    push_operator :
    '''

    operator = p[-1]

    operatorsStack.push(operator)
    print('push_operator', operatorsStack.top())


def p_ASSIGNMENT_ARRAY(p):
    '''
    assignmentarray : empty
                    | LBRACKET sexpression RBRACKET
    '''

def p_ASSIGNMENT_PRIMA(p):
    '''
    assignmentprima : functioncall
                    | sexpression
    '''

def p_SEXPRESSION(p):
    '''
    sexpression : negation expression do_not_operation
    '''

def p_EXPRESSION_NEGATION(p):
    '''
    negation : NOT push_operator
             | empty
    '''

def p_do_not_operation(p):
    '''
    do_not_operation :
    '''

    global semanticCube
    global tempCounter
    global quadCounter

    if operatorsStack.size() > 0:
        if operatorsStack.top() == '!':
            # Retrieve operands with their types, and the operator of the expression from the stacks
            operand = operandsStack.pop()
            type = typesStack.pop()
            operator = operatorsStack.pop()

            if type == 'bool':
                resultType = 'bool'
            else:
                resultType = 'Error'

            if resultType == 'bool':
                tempOperand = "Temp"+str(tempCounter)
                quad = Quadruple(quadCounter, operator, operand, None,
                                 tempOperand)  # Last parameter should be the VirtualAddress
                quadQueue.enqueue(quad)
                operandsStack.push(tempOperand)
                typesStack.push(resultType)

                quadCounter += 1
                tempCounter += 1

                print("doNotOperation",("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
                quad.result), str(p.lexer.lineno))
            else:
                errorTypeMismatch(p)

def p_EXPRESSION(p):
    '''
    expression : expression relationaloperators push_operator exp do_relational_operation
               | exp
    '''

def p_RELATIONAL_OPERATORS(p):
    '''
    relationaloperators : LESSER
                        | GREATER
                        | EQUAL
                        | NOTEQUAL
                        | LESSEROREQUAL
                        | GREATEROREQUAL
                        | AND
                        | OR
    '''
    p[0] = p[1]

def p_do_relational_operation(p):
    '''
    do_relational_operation :
    '''
    operator = operatorsStack.top();
    if operator == '<' or operator == '>' or operator == '==' or operator == '!=' or operator == '<=' or \
                    operator == '>=' or operator == '||' or operator == '&&':
        doOperations(p)

def p_EXP(p):
    '''
    exp : exp mathoperators1 push_operator term do_math_operation1
        | term
    '''

def p_MATH_OPERATORS1(p):
    '''
    mathoperators1 : PLUS
                   | MINUS
    '''
    p[0] = p[1]

def p_do_math_operation1(p):
    '''
    do_math_operation1 :
    '''
    operator = operatorsStack.top()
    if operator == '+' or operator == '-':
        doOperations(p)

def p_TERM(p):
    '''
    term : term mathoperators2 push_operator factor do_math_operation2
         | factor
    '''

def p_MATH_OPERATORS2(p):
    '''
    mathoperators2 : TIMES
                   | DEVIDE
    '''
    p[0] = p[1]

def p_do_math_operation2(p):
    '''
    do_math_operation2 :
    '''
    operator = operatorsStack.top()
    if operator == '*' or operator == '/':
        doOperations(p)

def p_FACTOR(p):
    '''
    factor : LPAREN sexpression RPAREN
           | varConst
    '''

def p_CONSTANT(p):
    '''
    varConst : ID push_id_operand
             | FLOAT push_float_operand
             | INT push_int_operand
             | bool push_bool_operand
             | STRING push_string_operand
    '''

def p_CONSTANTPRIMA(p):
    '''
    constantprima : empty
                  | LBRACKET sexpression RBRACKET
    '''


def p_bool(p):
    '''
    bool : TRUE
         | FALSE
    '''
    p[0] = p[1]

def p_push_float_operand(p):
    '''
    push_float_operand :
    '''

    floatType = p[-1]

    global operandsStack
    global operatorsStack

    operandsStack.push(floatType)
    typesStack.push('float')

    print("push_float_operand", operandsStack.top(), typesStack.top())

def p_push_int_operand(p):
    '''
    push_int_operand :
    '''

    intType = p[-1]

    global operandsStack
    global operatorsStack

    operandsStack.push(intType)
    typesStack.push('int')

    print("push_int_operand", operandsStack.top(), typesStack.top())

def p_push_bool_operand(p):
    '''
    push_bool_operand :
    '''

    boolType = p[-1]

    global operandsStack
    global operatorsStack

    operandsStack.push(boolType)
    typesStack.push('bool')

    print("push_bool_operand", operandsStack.top(), typesStack.top())

def p_push_string_operand(p):
    '''
    push_string_operand :
    '''

    stringType = p[-1]

    global operandsStack
    global operatorsStack

    operandsStack.push(stringType)
    typesStack.push('string')

    print("push_string_operand", operandsStack.top(), typesStack.top())


def p_FUNCTIONCALL(p):
    '''
    functioncall : ID LPAREN funcparam RPAREN SEMICOLON
    '''


def p_FUNCPARAM(p):
    '''
    funcparam : empty
              | sexpression
              | sexpression COMMA funcparam
    '''

def p_FUNCTION(p):
    '''
    function : FUNCTION functiontype ID LPAREN parameter RPAREN block function
             | empty
    '''

def p_FUNCTION_TYPE(p):
    '''
    functiontype : VOID
                 | type
    '''
    p[0] = p[1]

def p_RETURN(p):
    '''
    return : RETURN sexpression SEMICOLON
    '''

def p_PARAMETER(p):
    '''
    parameter : empty
              | parameterprima
    '''

def p_PARAMETERPRIMA(p):
    '''
    parameterprima : type ID
                   | type ID COMMA parameterprima
    '''

def p_WRITE(p):
    '''
    write : PRINT LPAREN sexpression RPAREN SEMICOLON
    '''
    global quadCounter

    operand = operandsStack.pop()
    popType = typesStack.pop()

    quad = Quadruple(quadCounter, 'print', operand, None, None)
    quadQueue.enqueue(quad)
    quadCounter += 1

    print("write",( "Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand, quad.result),
          "line: " + str(p.lexer.lineno))

def p_READ(p):
    '''
    read : ID push_id_operand ASSIGN push_operator INPUT SEMICOLON
    '''

    global quadCounter

    operand = operandsStack.pop()
    type = typesStack.pop()
    operator = operatorsStack.pop()

    # CHECK READ INPUT STRUCTURE....................................................................................................................
    quad = Quadruple(quadCounter,'input', type, None, operand)
    quadCounter += 1
    print("read", ("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand, quad.result),
          "line: " + str(p.lexer.lineno))

def p_CYCLE(p):
    '''
    cycle : WHILE LPAREN sexpression RPAREN block
    '''

def p_COLOR(p):
    '''
    color : BLUE
          | GREEN
          | RED
          | YELLOW
          | BROWN
          | BLACK
    '''
    p[0] = p[1]

def p_PREDEFINED(p):
    '''
    predefined : drawline
               | drawsquare
               | drawtriangle
               | drawcircle
               | drawcurve
               | drawpolygon
    '''

def p_DRAWLINE(p):
    '''
    drawline : DRAWLINE LPAREN sexpression  COMMA sexpression  COMMA sexpression  COMMA sexpression  COMMA color RPAREN SEMICOLON
    '''

def p_DRAWSQUARE(p):
    '''
    drawsquare : DRAWSQUARE LPAREN sexpression  COMMA sexpression COMMA color RPAREN SEMICOLON
    '''

def p_DRAWTRIANGLE(p):
    '''
    drawtriangle : DRAWTRIANGLE LPAREN sexpression COMMA sexpression COMMA color RPAREN SEMICOLON
    '''

def p_DRAWCIRCLE(p):
    '''
    drawcircle : DRAWCIRCLE LPAREN sexpression COMMA sexpression COMMA color RPAREN SEMICOLON
    '''

def p_DRAWCURVE(p):
    '''
    drawcurve : DRAWCURVE LPAREN sexpression COMMA sexpression COMMA color RPAREN SEMICOLON
    '''

def p_DRAWPOLYGON(p):
    '''
    drawpolygon : DRAWPOLYGON LPAREN sexpression COMMA sexpression COMMA color RPAREN SEMICOLON
    '''

def p_error(p):
    print('ERROR: Syntax Error in line: ' + str(p.lexer.lineno))
    sys.exit()

def p_EMPTY(p):
    '''
    empty :
    '''
    pass

# NoYacc FUNCTIONS..................
def doConditionOperation(p):
    global quadCounter

    expressionType = typesStack.pop()

    if expressionType != 'bool':
        errorTypeMismatch(p)
    else:
        expressionResult = operandsStack.pop()
        quad = Quadruple(quadCounter, 'gotof', expressionResult, None, None)
        quadQueue.enqueue(quad)

        #JumpStack.append(quadCont - 1)
        quadCounter += 1
        print("doConditionOperation", ("Quad " + str(quad.quad_number), quad.operator, quad.left_operand,
                                    quad.right_operand, quad.result), "line: " +str(p.lexer.lineno))

def doAssignOperation(p):
    # Global variables to use
    global semanticCube
    global quadCounter

    # Retrieve operands with their types, and the operator of the expression from the stacks
    rightOperand = operandsStack.pop()
    rightType = typesStack.pop()
    leftOperand = operandsStack.pop()
    leftType = typesStack.pop()
    operator = operatorsStack.pop()
    resultType = semanticCube.getType(leftType, rightType, operator)

    if resultType != 'Error':
        # Assignment quadruple
        quad = Quadruple(quadCounter, operator, rightOperand, None, leftOperand) # Last parameter should be the VirtualAddress
        quadQueue.enqueue(quad)
        quadCounter += 1
        print("doAssignOperation", ("Quad " + str(quad.quad_number), quad.operator, quad.left_operand,
              quad.right_operand, quad.result), "line: " +str(p.lexer.lineno))
    else:
        errorTypeMismatch(p)

def doOperations(p):
    # Global variables to use
    global semanticCube
    global tempCounter
    global quadCounter

    # Retrieve operands with their types, and the operator of the expression from the stacks
    rightOperand = operandsStack.pop()
    rightType = typesStack.pop()
    leftOperand = operandsStack.pop()
    leftType = typesStack.pop()
    operator = operatorsStack.pop()

    resultType = semanticCube.getType(leftType, rightType, operator)

    if resultType != 'Error':
        tempOperand = "Temp" + str(tempCounter)
        quad = Quadruple(quadCounter, operator, leftOperand, rightOperand, tempOperand) # Last parameter should be the VirtualAddress
        quadQueue.enqueue(quad)
        operandsStack.push(tempOperand)
        typesStack.push(resultType)
        tempCounter += 1
        quadCounter += 1

        print("doOperation", ("Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand,
              quad.result), "line: " +str(p.lexer.lineno))
    else:
        errorTypeMismatch(p)

# Error functions
def errorTypeMismatch(p):
    print('ERROR: Type mismatch in line ' + str(p.lexer.lineno))
    sys.exit()

def errorVariableNotDeclared(p, varId):
    print('Error: variable ' + str(varId) + ' not declared in line ' + str(p.lexer.lineno))
    sys.exit()

# Build parser
parser = yacc.yacc()

#print("Filename or path: ")
#filename = raw_input()

file = open("../Tests/TestCode", 'r')

parser.parse(file.read())

'''
while True:
    try:
       s = raw_input('calc> ')
    except EOFError:
        break
    parser.parse(s)
'''
