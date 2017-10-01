import sys
sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

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
    # 'DATE',
    'SEMICOLON',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN = r'='
t_LTHAN = r'<'
t_GTHAN = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_NEQ = r'!='
t_SEMICOLON = r';'

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

t_INTEGER = r'[0-9]+'

def t_TEXT(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in keywords:
        t.type = t.value.upper()
    return t

# def t_DATE(t):
#     r''

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
                 | DELETE FROM TEXT SEMICOLON'''
    print(p[1] + ' ' + p[2] + ' ' + p[3] + ';')

def p_whereexp(p):
    'whereexp : WHERE wherecond'
    
    print(p[1])

def p_wherecond(p):
    '''wherecond : TEXT opexp'''
    print(p[1])

def p_opexp(p):
    '''opexp : ASSIGN INTEGER
             | ASSIGN binop
             | compop binop'''
    if p[1] == '=':
            print(p[1])

def p_opexp_compop(p):
    '''compop : LTHAN INTEGER
              | GTHAN INTEGER
              | LEQ INTEGER
              | GEQ INTEGER
              | NEQ INTEGER'''

    print(p[1] + p[2])

def p_opexp_binop(p):
    '''binop : INTEGER PLUS INTEGER
             | INTEGER MINUS INTEGER
             | INTEGER TIMES INTEGER
             | INTEGER DIVIDE INTEGER
             | INTEGER MODULO INTEGER'''
    
    print(p[1] + p[2] + p[3])

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