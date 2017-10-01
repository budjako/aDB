import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

keywords = ( 
	'DELETE', 
    'FROM', 
    'WHERE', 
)

tokens = keywords + (
	'SPACE', 
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
    'SEMICOLON',
)

t_SPACE = r'[ ]+'
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

t_DELETE = r'DELETE'

t_FROM = r'FROM'

t_WHERE = r'WHERE'

t_INTEGER = r'[0-9]+'

t_ignore = " \t"

def t_TEXT(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in keywords:
        t.type = t.value.upper()
    return t

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
    'whereexp : WHERE SPACE wherecond'

def p_wherecond(p):
    '''wherecond : TEXT SPACE opexp
                 | TEXT opexp'''
    print('WHERE ' + p[1])

def p_opexp(p):
    '''opexp : ASSIGN SPACE INTEGER
             | ASSIGN INTEGER
             | compop SPACE binop
             | compop binop'''
    if p[1] == '=':
        if p[2] == ' ':
            print(p[1] + p[3])
        else:
            print(p[1] + p[2])

            # | ASSIGN SPACE binop
            #  | ASSIGN binop

def p_opexp_compop(p):
    '''compop : LTHAN INTEGER
              | GTHAN INTEGER
              | LEQ INTEGER
              | GEQ INTEGER
              | NEQ INTEGER
              | LTHAN SPACE INTEGER
              | GTHAN SPACE INTEGER
              | LEQ SPACE INTEGER
              | GEQ SPACE INTEGER
              | NEQ SPACE INTEGER'''
    if p[2] == ' ':
        print(p[1] + p[2] + p[3])
    else:
        print(p[1] + p[2])

def p_opexp_binop(p):
    '''binop : INTEGER PLUS INTEGER
             | INTEGER MINUS INTEGER
             | INTEGER TIMES INTEGER
             | INTEGER DIVIDE INTEGER
             | INTEGER MODULO INTEGER
             | INTEGER SPACE PLUS SPACE INTEGER
             | INTEGER SPACE MINUS SPACE INTEGER
             | INTEGER SPACE TIMES SPACE INTEGER
             | INTEGER SPACE DIVIDE SPACE INTEGER
             | INTEGER SPACE MODULO SPACE INTEGER'''

    if p[2] == ' ':
        print(p[1] + p[3] + p[5])
    else:
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