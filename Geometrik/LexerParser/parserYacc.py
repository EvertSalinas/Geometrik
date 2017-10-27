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
quadCont = 1
tempCont = 0

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
    program : PROGRAM ID add_global_func SEMICOLON programvars programfunction main
    '''

    print("Correct Sintax.")

def p_add_global_func(p):
    '''add_global_func : '''

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

def p_PROGRAMVARS(p):
    '''
    programvars : vars programvars
                | empty
    '''

def p_PROGRAMFUNCTION(p):
    '''
    programfunction : function programfunction
                    | empty
    '''

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
    condition : IF LPAREN conditionprima RPAREN block
    '''

def p_CONDITIONPRIMA(p):
    '''
    conditionprima : condprimaaux
                   | NOT condprimaaux
    '''

def p_CONDPRIMAAUX(p):
    '''
    condprimaaux : functioncall
                 | singularexp2
    '''

def p_VARS(p):
    '''
    vars : VAR type ID array store_variable SEMICOLON
    '''

def p_ARRAY(p):
    '''
    array : LBRACKET singularexp2 RBRACKET
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

    print("store_variable",currentScope, functionsDirectory.getFunctionVariable(currentScope, varName))

def p_TYPE(p):
    '''
    type : INTTYPE
         | FLOATTYPE
         | STRINGTYPE
         | BOOLEANTYPE
    '''
    p[0] = p[1]


def p_ASSIGNMENT(p):
    '''
    assignment : ID push_id_operand ASSIGN push_operator singularexp2 SEMICOLON
    '''
    print("assignment:")
    createQuad(p)

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
            print('Error: variable ' + str(varId) + ' not declared in line ' + str(p.lexer.lineno))
            sys.exit()
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
                    | LBRACKET singularexp2 RBRACKET
    '''

def p_ASSIGNMENT_PRIMA(p):
    '''
    assignmentprima : functioncall
                    | singularexp2
    '''

def p_S_EXPRESSION2(p):
    '''
    singularexp2 : singularexp
                 | NOT singularexp

    '''

def p_S_EXPRESSION(p):
    '''
    singularexp : singularexp AND expression
                | singularexp OR expression
                | expression
    '''

def p_EXPRESSION(p):
    '''
    expression : expression LESSER exp
               | expression GREATER exp
               | expression EQUAL exp
               | expression NOTEQUAL exp
               | expression LESSEROREQUAL exp
               | expression GREATEROREQUAL exp
               | exp
    '''

def p_EXP(p):
    '''
    exp : exp PLUS term
        | exp MINUS term
        | term
    '''

def p_TERM(p):
    '''
    term : term TIMES factor
         | term DEVIDE factor
         | factor
    '''

def p_FACTOR(p):
    '''
    factor : LPAREN singularexp2 RPAREN
           | PLUS constant
           | MINUS constant
           | constant
    '''

def p_CONSTANT(p):
    '''
    constant : ID push_id_operand constantprima
             | FLOAT push_float_operand
             | INT push_int_operand
             | boolean push_boolean_operand
             | STRING push_string_operand
    '''

def p_BOOLEAN(p):
    '''
    boolean : TRUE
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

def p_push_boolean_operand(p):
    '''
    push_boolean_operand :
    '''

    booleanType = p[-1]

    global operandsStack
    global operatorsStack

    operandsStack.push(booleanType)
    typesStack.push('boolean')

    print("push_boolean_operand", operandsStack.top(), typesStack.top())

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

def p_CONSTANTPRIMA(p):
    '''
    constantprima : empty
                  | LBRACKET singularexp2 RBRACKET
    '''

def p_FUNCTIONCALL(p):
    '''
    functioncall : ID LPAREN funcparam RPAREN SEMICOLON
    '''


def p_FUNCPARAM(p):
    '''
    funcparam : empty
              | singularexp2
              | singularexp COMMA funcparam
    '''

def p_FUNCTION(p):
    '''
    function : FUNCTION VOID ID LPAREN parameter RPAREN block
             | FUNCTION type ID LPAREN parameter RPAREN block
    '''

def p_RETURN(p):
    '''
    return : RETURN singularexp2 SEMICOLON
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
    write : PRINT LPAREN singularexp2 RPAREN SEMICOLON
    '''
    global quadCont

    operand = operandsStack.pop()
    type = typesStack.pop()

    print("...operand", operand)

    quad = Quadruple(quadCont, 'print', operand, None, None)
    quadQueue.enqueue(quad)
    quadCont += 1

    print("write", "Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand, quad.result)

def p_READ(p):
    '''
    read : ID push_id_operand ASSIGN push_operator INPUT SEMICOLON
    '''

    global tempCont
    global quadCont

    rightOperand = operandsStack.pop()
    rightType = typesStack.pop()
    operator = operatorsStack.pop()

    # CHECK READ INPUT STRUCTURE....................................................................................................................
    quad = Quadruple(quadCont,'input', 'input', None, rightOperand)
    print("read", "Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand, quad.result)

def p_CYCLE(p):
    '''
    cycle : WHILE LPAREN singularexp2 RPAREN block
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
    drawline : DRAWLINE LPAREN singularexp2  COMMA singularexp2  COMMA singularexp2  COMMA singularexp2  COMMA color RPAREN SEMICOLON
    '''

def p_DRAWSQUARE(p):
    '''
    drawsquare : DRAWSQUARE LPAREN singularexp2  COMMA singularexp2 COMMA color RPAREN SEMICOLON
    '''

def p_DRAWTRIANGLE(p):
    '''
    drawtriangle : DRAWTRIANGLE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON
    '''

def p_DRAWCIRCLE(p):
    '''
    drawcircle : DRAWCIRCLE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON
    '''

def p_DRAWCURVE(p):
    '''
    drawcurve : DRAWCURVE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON
    '''

def p_DRAWPOLYGON(p):
    '''
    drawpolygon : DRAWPOLYGON LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON
    '''

def p_error(p):
    print("Syntax error!")

def p_EMPTY(p):
    '''
    empty :
    '''
    pass

# NoYacc FUNCTIONS..................

def createQuad(p):
    rightOperand = operandsStack.pop()
    rightType = typesStack.pop()
    leftOperand = operandsStack.pop()
    leftType = typesStack.pop()
    operator = operatorsStack.pop()

    global semanticCube
    global tempCont
    global quadCont

    result = semanticCube.getType(leftType, rightType, operator)
    print("result", result)

    if result != 'Error':
        # Assignment quadruple
        quad = Quadruple(quadCont, operator, rightOperand, None, leftOperand)
        quadQueue.enqueue(quad)
        quadCont += 1
        print("createQuad", "Quad " + str(quad.quad_number), quad.operator, quad.left_operand, quad.right_operand, quad.result)
    else:
        print('Type Missmatch')

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
