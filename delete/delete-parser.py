# library
import sys
sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

# initialization
keywords = ( 
	'DELETE', 
    'FROM', 
    'WHERE', 
)

tokens = keywords + (
    # 'NAME',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'ASSIGN',
    'LTHAN',
    'GTHAN',
    'LEQ',
    'GEQ',
    'NEQ',
    'INTEGER',
    'TEXT',
    'DATE',
    'DOUBLE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
)

# keywords
def t_DELETE(t):
    r'[Dd][Ee][Ll][Ee][Tt][Ee]'
    if t.value in keywords:
        t.type = t.value.upper()
    return t

def t_FROM(t):
    r'[Ff][Rr][Oo][Mm]'
    if t.value in keywords:
        t.type = t.value.upper()
    return t

def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'
    if t.value in keywords:
        t.type = t.value.upper()
    return t

# binary operations
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'

# comparison operations
t_ASSIGN = r'='
t_LTHAN = r'<'
t_GTHAN = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_NEQ = r'!='

# data types
t_INTEGER = r'[0-9]+'

def t_TEXT(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in keywords:
        t.type = t.value.upper()
    return t

def t_DATE(t):
    r'\d{4}\-(0?[1-9]|10|11|12)\-(30|31|((0|1|2)?[0-9]))' # Year-Month-Day
    t.value = t.value
    return t

def t_DOUBLE(t):
    r'\-?\d+\.\d+'
    t.value = float(t.value)
    return t

# 
t_LPAREN = r'('
t_RPAREN = r')'
t_SEMICOLON = r';'

t_ignore = " \t"

# def t_NAME(t):
#     r'[A-Za-z][A-Za-z0-9_]*'
#     if t.value.upper() in keywords:
#         t.type = t.value.upper()
#     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_statement_query(p):
    '''statement : DELETE FROM TEXT whereexp SEMICOLON
                 | DELETE FROM TEXT SEMICOLON
                 | DOUBLE'''
    # print(p[1] + ' ' + p[2] + ' ' + p[3] + ';')

    print(p[1])

def p_whereexp(p):
    'whereexp : WHERE wherecond'
    
    print(p[1])

def p_wherecond(p):
    '''wherecond : TEXT opexp'''
    print(p[1])

def p_opexp(p):
    '''opexp : ASSIGN datatype
             | ASSIGN binop
             | compop binop'''
    if p[1] == '=':
            print(p[1])

def p_opexp_compop(p):
    '''compop : LTHAN leftparen numtype rightparen
              | GTHAN numtype
              | LEQ numtype
              | GEQ numtype
              | NEQ numtype'''

    print(p[1])

def p_opexp_binop(p):
    '''binop : numtype PLUS numtype
             | numtype MINUS numtype
             | numtype TIMES numtype
             | numtype DIVIDE numtype
             | numtype MODULO numtype'''
    
    print(p[1] + p[2] + p[3])

def p_data_type(p):
    '''datatype : TEXT
                | DATE
                | numtype'''

    print(p[1])

def p_number_type(p):
    '''numtype : INTEGER
               | DOUBLE'''

    print(p[1])

def p_left_paren(p):
    '''leftparen : LPAREN
                 |'''

def p_right_paren(p):
    '''rightparen : LPAREN
                 |'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('sql > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)