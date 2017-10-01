import sys
sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

keywords = ( 
    'INSERT', 'INTO', 'VALUES', 'SET',
)

tokens = keywords + (
    'COLUMN_NAME', 'TABLE_NAME', 'LPAREN', 'RPAREN', 'EQUALS', 'STRING_LIT', 'INT_LIT', 'DOUBLE_LIT', 'DATE_LIT', 'COMMA', #'VALUE_LIST', 'ASSIGNMENT_LIST', 'COLUMN', 'VALUE_LIST',
    #'VALUE', 'ASSIGNMENT', 
)

tables = ('student')

t_COLUMN_NAME = r'(studno|studentname|birthday|degree|major|unitsearned|description|action|datefiled|dateresolved|cno|ctitle|cdesc|noofunits|haslab|semoffered|semester|acadyear|cno|section|time|maxstud)'
t_TABLE_NAME = r'(student|studenthistory|course|courseoffering|studcourse)'
t_STRING_LIT = r'\'.*\'|\".*\"'


t_INSERT = r'insert'
t_INTO = r'into'
t_VALUES = r'values'
t_SET = r'set'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_COMMA = r','

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_DATE_LIT(t):
    r'\d{4}\-(0?\d|10|11|12)\-(3[01]|(0|1|2)?\d)' # Year-Month-Day
    t.value = t.value
    return t 
    # t_value = date(2017, 10, 1)

def t_DOUBLE_LIT(t):
    r'\-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_LIT(t):
    r'\-?\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

names = {}

def p_statement_query(p):
    '''statement : INSERT INTO TABLE_NAME VALUES LPAREN valuelist RPAREN
            | INSERT INTO TABLE_NAME SET assignmentlist'''

def p_value_list(p):
    '''valuelist : expr
            | expr COMMA valuelist'''

def p_assignment_list(p):
    '''assignmentlist : assignment
            | assignment COMMA assignment'''

def p_assignment(p):
    '''assignment : COLUMN_NAME EQUALS expr'''

def p_expr(p):
    '''expr : STRING_LIT
            | INT_LIT
            | DOUBLE_LIT
            | DATE_LIT'''

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
        s = s.lower()
        lex.input(s)
        for tok in iter(lex.token, None):
            print(tok)
            print(repr(tok.type), repr(tok.value))
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)