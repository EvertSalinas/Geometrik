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

functionsDirectory = functions_Directory();
semanticCube = semantic_Cube();

currentScope = ""
globalScope = ""
quadCont = 1
tempCont = 0

operatorsStack = Stack()
operandsStack = Stack()
typesStack = Stack()
quadCont = []
jumpsStack = Stack()


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
    program : PROGRAM ID SEMICOLON programvars programfunction main
    | assignment
    | read
    '''

    print("Correct Sintax.")

def p_MAIN(p):
    '''
    main : INTTYPE MAIN LPAREN RPAREN block
    '''

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
    vars : VAR type varsprima SEMICOLON
    '''

def p_VARSPRIMA(p):
    '''
    varsprima : ID
              | ID COMMA varsprima
              | empty
    '''

def p_TYPE(p):
    '''
    type : INTTYPE
         | FLOATTYPE
         | STRINGTYPE
         | BOOLEANTYPE
         | array
    '''

def p_ARRAY(p):
    '''
    array : INTTYPE arrayprima
          | FLOATTYPE arrayprima
          | STRINGTYPE arrayprima
    '''

def p_ARRAYPRIMA(p):
    '''
    arrayprima : LBRACKET INT RBRACKET
    '''


def p_ASSIGNMENT(p):
    '''
    assignment : ID push_id_operand ASSIGN push_operator singularexp2 SEMICOLON
    '''

def p_push_id_operand(p):
    '''
    push_id_operand :
    '''
    print(p[-1])

    '''
    global currentScope
    
    variable = functionsDirectory.getVariable(currentScope, p[-1])

    if variable is None:
        variable = functionsDirectory.getVariable(globalScope, p[-1])

        if variable is None:
            print('Error: variable {0} not declared in line {1}'.format(p[-1], p.lexer.lineno))
            sys.exit('variable_not_declared')
        else:
            variableInfo = variable[1]

            operandsStack.push(variableInfo[1])
            typesStack.push(variableInfo[0])
    else:
        variableInfo = variable[1]

        operandsStack.push(variableInfo[1])
        typesStack.push(variableInfo[0])

    print(operandsStack.push())
    '''

def p_push_operator(p):
    '''
    push_operator :
    '''

    operatorsStack.push(p[-1])
    print(operatorsStack.top())


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
    constant : ID constantprima
             | FLOAT
             | INT
    '''

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

def p_READ(p):
    '''
    read : ID push_id_operand ASSIGN push_operator INPUT SEMICOLON
    '''

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
