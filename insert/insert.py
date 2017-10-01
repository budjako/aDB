import sys
sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

keywords = ( 
    'INSERT', 'INTO', 'VALUES',
)

tokens = keywords + (
    'COLUMN_NAME', 'TABLE_NAME', 'LPAREN', 'RPAREN', 'NAME', 'EQUALS' #'VALUE_LIST', 'ASSIGNMENT_LIST', 'COLUMN', 'VALUE_LIST',
    #'VALUE', 'ASSIGNMENT', 
)

tables = ('student')

t_COLUMN_NAME = r'(studno|studentname|birthday|degree|major|unitsearned|description|action|datefiled|dateresolved|cno|ctitle|cdesc|noofunits|haslab|semoffered|semester|acadyear|cno|section|time|maxstud)'
t_TABLE_NAME = r'(student|studenthistory|course|courseoffering|studcourse)'

t_INSERT = r'INSERT'

t_INTO = r'INTO'

t_VALUES = r'VALUES'

t_LPAREN = r'\('

t_RPAREN = r'\)'

t_EQUALS = r'='

# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    # print(keywords)
    # print("value: " + t.value.upper())
    # print("type: " + t.type)
    if t.value.upper() in keywords:
        t.type = t.value.upper()
        # print("pumasok " + t.value)
        # print("newtype "+ t.type)
    return t

# t_TBLNAME = r'[A-Z]+'#r'[a-zA-Z_][a-zA-Z0-9_]*'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

names = {}

# tables = {
#           'student' : {'StudNo', 'StudentName', 'Birthday', 'Degree', 'Major', 'UnitsEarned'}, 
#           'studenthistory' : {'StudNo', 'Description', 'Action', 'DataFiled', 'DateResolved'}, 
#           'course' : {'CNo', 'CTitle', 'CDesc', 'NoOfUnits', 'HasLab', 'SemOffered'}, 
#           'courseoffering' : {'Semester', 'AcadYear', 'CNo', 'Section', 'Time', 'MaxStud'}, 
#           'studcourse' : {'StudNo', 'CNo', 'Semester', 'AcadYear' } 
#           }

# columns = {'name'}

# def p_statement_insert(p):
#     "statement : INSERT"
#     print(p[1])

# def p_statement_into(p):
#     'statement : INTO'
#     print(p[1])
def p_statement_query(p):
    'statement : INSERT INTO TABLE_NAME'

def p_insert_option(p):
    """
    insertoption : valuelist
                |   assignmentlist
    """

def p_value_list(p):
    'valuelist : VALUES LPAREN NAME RPAREN'

def p_assignment_list(p):
    'assignmentlist : NAME'


# def p_statement_tblname(p):

# def p_expression_column(p):
#         'column : NAME'
#         if p[1] in columns:
#             print(p[1])

# def p_expression_tblname(p):
#         'tblname : NAME'
#         if p[1] in tables:
#             print(p[1])
#         else:
#             print("Undefined table '%s'" % p[1])
        # try:
        #     p[0] = tables[p[1]]
        # except LookupError:
        #     print("Undefined table '%s'" % p[1])
        #     p[0] = 0

# def p_statement_tblname(p):
#     'statement : NAME'
#     print("high" + p[1])

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