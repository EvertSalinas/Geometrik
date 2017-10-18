import ply.lex as lex
import ply.yacc as yacc
from scannerCompis import tokens

precedence = (
    ('left', 'EQUAL', 'NOTEQUAL'),
    ('left', 'LESSER', 'GREATER', 'LESSEROREQUAL','GREATEROREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DEVIDE'),
    ('nonassoc', 'LPAREN', 'RPAREN')
)

def p_PROGRAM(p):
    '''
    program : PROGRAM ID SEMICOLON programvars programfunction block

    '''
    print(p[1],p[2],p[4],p[5],p[6])

def p_PROGRAMVARS(p):
    '''
    programvars : vars
                | empty
    '''
    p[0] = p[1]

def p_PROGRAMFUNCTION(p):
    '''
    programfunction : function programfunction
                    | empty
    '''
    if (len(p) == 3):
        p[0] = (p[1],p[2])
    if (len(p) == 1):
        p[0] = (p[1])

def p_BLOCK(p):
    '''
    block : LBRACE blockprima RBRACE
    '''
    p[0] = (p[2])

def p_BLOCKPRIMA(p):
    '''
    blockprima : statute blockprima
               | empty
    '''
    if (len(p) == 3):
        p[0] = (p[1],p[2])

def p_STATUTE(p):
    '''
    statute : assignment
            | condition
            | write
            | read
            | cycle
            | functioncall
            | predefined
    '''
    p[0] = p[1]
    
def p_CONDITION(p):
    '''
    condition : IF LPAREN singularexp2 RPAREN block
              | IF LPAREN functioncall RPAREN block
              | IF LPAREN singularexp2 RPAREN block ELSE block
              | IF LPAREN functioncall RPAREN block ELSE block
              | IF LPAREN NOT singularexp2 RPAREN block
              | IF LPAREN NOT functioncall RPAREN block
              | IF LPAREN NOT singularexp2 RPAREN block ELSE block
              | IF LPAREN NOT functioncall RPAREN block ELSE block
    '''
    if (len(p) == 6):
        p[0] = (p[1],p[3],p[5])
    if (len(p) == 8):
        p[0] = (p[1],p[3],p[5],p[7])
    if (len(p) == 7):
        p[0] = (p[1],p[3],p[4],p[6])
    if (len(p) == 9):
        p[0] = (p[1],p[3],p[4],p[6],p[8])

def p_VARS(p):
    '''
    vars : VAR ID varsprima COLON type SEMICOLON
    '''
    p[0] = (p[1],p[2],p[3])

def p_VARSPRIMA(p):
    '''
    varsprima : COMMA ID varsprima
              | empty
    '''
    if (len(p) == 4):
        p[0] = (p[2], p[3])
    elif (len(p) == 2):
        p[0] = 'empty'

def p_TYPE(p):
    '''
    type : INTTYPE
         | FLOATTYPE
         | STRINGTYPE
         | BOOLEANTYPE
         | array
    '''
    p[0] = p[1]

def p_ARRAY(p):
    '''
    array : INTTYPE LBRACKET ID RBRACKET
          | INTTYPE LBRACKET NUMBER RBRACKET
          | FLOATTYPE LBRACKET NUMBER RBRACKET
          | FLOATTYPE LBRACKET ID RBRACKET
          | STRING LBRACKET ID RBRACKET
          | STRING LBRACKET NUMBER RBRACKET
    '''
    p[0] = ('ARRAY',p[1], p[3])

def p_ASSIGNMENT(p):
    '''
    assignment : ID ASSIGN singularexp2 SEMICOLON
               | ID ASSIGN functioncall 
    '''
    if (len(p) == 5):
        p[0] = (p[2], p[1],p[3])
    elif (len(p) == 4):
        p[0] = (p[2],p[1],p[3])


def p_SS_EXPRESSION(p):
    '''
    singularexp2 : singularexp
    			 | NOT singularexp
                
    '''
    if (len(p) == 3):
        p[0] = (p[1], p[2])
    elif (len(p) == 2):
        p[0] = p[1]

def p_S_EXPRESSION(p):
    '''
    singularexp : singularexp AND expression
                | singularexp OR expression
                | expression
    '''
    if (len(p) == 4):
        p[0] = (p[2], p[1], p[3])
    elif (len(p) == 2):
        p[0] = p[1]

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
    if (len(p) == 4):
        p[0] = (p[2], p[1], p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_EXP(p):
    '''
    exp : exp PLUS term
        | exp MINUS term
        | term
    '''
    if (len(p) == 4):
        p[0] = (p[2], p[1], p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_TERM(p):
    '''
    term : term TIMES factor
         | term DEVIDE factor
         | factor
    '''
    if (len(p) == 4):
        p[0] = (p[2], p[1], p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_FACTOR(p):
    '''
    factor : LPAREN singularexp2 RPAREN
           | PLUS varcte
           | MINUS varcte
           | varcte
    '''
    if (len(p) == 4):
        p[0] = (p[2])
    elif (len(p) == 3):
        p[0] = (p[1],p[2])
    elif (len(p) == 2):
        p[0] = p[1]

def p_VARCTE(p):
    '''
    varcte : INT
           | FLOAT
           | STRING
           | ID
           | bool
    '''
    p[0] = p[1]

def p_BOOLEAN(p):
    '''
    bool : TRUE
         | FALSE
    '''
    p[0] = p[1]


def p_FUNCTIONCALL(p):
    '''
    functioncall : FUNCTIONID LPAREN RPAREN SEMICOLON
                 | FUNCTIONID LPAREN funcparam RPAREN SEMICOLON
    '''
    if (len(p) == 5):
        p[0] = (p[1])
    elif (len(p) == 6):
        p[0] = (p[1],p[3])

def p_FUNCPARAM(p):
    '''
    funcparam : singularexp2 funcparamprima
              | ID funcparamprima
    '''
    p[0] = (p[1],p[2])

def p_FUNCPARAMPRIMA(p):
    '''
    funcparamprima : COMMA funcparam
                   | empty
    '''
    if (len(p) == 3):
        p[0] = (p[2])
    elif (len(p) == 1):
        p[0] = (p[1])


def p_FUNCTION(p):
    '''
    function : FUNCTION VOID FUNCTIONID LPAREN parameter RPAREN block
             | FUNCTION type FUNCTIONID LPAREN parameter RPAREN block
             | FUNCTION VOID FUNCTIONID LPAREN RPAREN block
             | FUNCTION type FUNCTIONID LPAREN RPAREN block
    '''
    p[0] = (p[1],p[2],p[3],p[5],p[7])

def p_PARAMETER(p):
    '''
    parameter : type ID parameterprima
    '''
    if (len(p) == 4):
        p[0] = (p[1],p[2],p[3])

def p_PARAMETERPRIMA(p):
    '''
    parameterprima : COMMA type ID parameterprima
                   | empty
    '''
    if (len(p) == 4):
        p[0] = (p[2],p[3],p[4])

def p_WRITE(p):
    '''
    write : PRINT LPAREN singularexp2 RPAREN SEMICOLON
          | PRINT LPAREN ID RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5])

def p_READ(p):
    '''
    read : ID ASSIGN INPUT SEMICOLON
    '''
    p[0] = (p[2], p[1], p[3])

def p_CYCLE(p):
    '''
    cycle : WHILE LPAREN singularexp2 RPAREN block
    '''
    p[0] = (p[1],p[3],p[5])

def p_COLOR(p):
    '''
    color : BLUE
          | GREEN
          | RED
          | YELLOW
          | BROWN
          | BLACK
    '''
    p[0] = p[1],'color'

def p_PREDEFINED(p):
    '''
    predefined : drawline
               | drawsquare
               | drawtriangle
               | drawcircle
               | drawcurve
               | drawpolygon
    '''
    p[0] = p[1]

def p_DRAWLINE(p):
    '''
    drawline : DRAWLINE LPAREN idssexp COMMA idssexp COMMA idssexp COMMA idssexp COMMA color RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5],p[7],p[9],p[11])

def p_DRAWSQUARE(p):
    '''
    drawsquare : DRAWSQUARE LPAREN idssexp COMMA idssexp COMMA color RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5],p[7])

def p_DRAWTRIANGLE(p):
    '''
    drawtriangle : DRAWTRIANGLE LPAREN idssexp COMMA idssexp COMMA color RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5],p[7])

def p_DRAWCIRCLE(p):
    '''
    drawcircle : DRAWCIRCLE LPAREN idssexp COMMA idssexp COMMA color RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5],p[7])

def p_DRAWCURVE(p):
    '''
    drawcurve : DRAWCURVE LPAREN idssexp COMMA idssexp COMMA color RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5],p[7])

def p_DRAWPOLYGON(p):
    '''
    drawpolygon : DRAWPOLYGON LPAREN idssexp COMMA idssexp COMMA color RPAREN SEMICOLON
    '''
    p[0] = (p[1],p[3],p[5],p[7])


def p_IDSSEXP(p):
    '''
    idssexp : PARAMID
            | singularexp2
    '''
    p[0]= p[1]


def p_error(p):
    print("Syntax error!")

def p_EMPTY(p):
    '''
    empty :
    '''

parser = yacc.yacc()


while True:
    try:
       s = raw_input('calc> ')
    except EOFError:
        break
    parser.parse(s)
    