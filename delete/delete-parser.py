import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

keywords = ( 
	'DELETE', 'FROM',
)

tokens = keywords + (
	'SPACE', 'COLNAME', #'VALUE_LIST', 'ASSIGNMENT_LIST', 'COLUMN', 'VALUE_LIST',
	#'VALUE', 'ASSIGNMENT', 
)

t_SPACE = r'[ ]+'

def t_COLNAME(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t

t_DELETE = r'[Dd][Ee][Ll][Ee][Tt][Ee]'

t_FROM = r'[Ff][Rr][Oo][Mm]'


# t_TBLNAME = r'[A-Z]+'#r'[a-zA-Z_][a-zA-Z0-9_]*'

# t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

names = {}

tables = {'students'}

def p_statement_query(p):
    "statement : DELETE SPACE FROM SPACE COLNAME"
    print(p[1]+' '+p[3]+' '+p[5])

def p_statement_delete(p):
    "statement : DELETE"
    print(p[1])

def p_statement_from(p):
    'statement : INTO'
    print(p[1])

# def p_statement_tblname(p):


# def p_statement_tblname(p):
#     'statement : TBLNAME'
#     print(p[1])

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