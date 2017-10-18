import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ['ID', 'FUNCTIONID', 'PARAMID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DEVIDE', #Operators
          'ASSIGN', 'EQUAL', 'NOTEQUAL', 'GREATER', 'LESSER', # Operators
          'GREATEROREQUAL', 'LESSEROREQUAL', 'AND', 'OR', 'NOT', # Operators
          'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', # Delimiters
          'PERIOD', 'COMMA', 'COLON', 'SEMICOLON', # Delimiters
          'INT', 'STRING', 'FLOAT',
]


reserved = {
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'print': 'PRINT',
    'function': 'FUNCTION',
    'return' : 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'program': 'PROGRAM',
    'break': 'BREAK',
    'DrawCircle': 'DRAWCIRCLE',
    'DrawLine': 'DRAWLINE',
    'DrawTriangle': 'DRAWTRIANGLE',
    'DrawSquare': 'DRAWSQUARE',
    'DrawPolygon': 'DRAWPOLYGON',
    'DrawCurve': 'DRAWCURVE',
    'Red': 'RED',
    'Green': 'GREEN',
    'Blue': 'BLUE',
    'Yellow': 'YELLOW',
    'Brown': 'BROWN',
    'Black': 'BLACK',
    'int': 'INTTYPE',
    'boolean': 'BOOLEANTYPE',
    'float': 'FLOATTYPE',
    'string': 'STRINGTYPE',
    'void': 'VOID',
    'input': 'INPUT',
    'var': 'VAR'
}

tokens = tokens+list(reserved.values())

t_ignore = ' '

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DEVIDE = r'/'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATER = r'>'
t_LESSER = r'<'
t_GREATEROREQUAL = r'>='
t_LESSEROREQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PERIOD = r'\.'
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_ASSIGNID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_PARAMID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_FUNCTIONID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# String literal
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
int a = 1;
'''

# Give the lexer some input
lexer.input(data)
'''
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
'''
##################################################################################
