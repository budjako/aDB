import sys
import re
import time

sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

from ply import *
import selectlex
# import selectparse
# import selectinterp




tables = {'student': ['StudNo','StudentName','Birthday','Degree','Major','UnitsEarned'],
          'studenthistory' : ['StudNo','Description','Action','DateFiled','DateResolved'],
          'course': ['CNo','CTitle','CDesc','NoOfUnits','HasLab','SemOffered'],
          'courseoffering': ['Semester','AcadYear','CNo','Section','Time','MaxStud'],
          'studcourse': ['StudNo','CNo','Semester','AcadYear']
         }
cols = ''
tabs = ''
metadata = open("metadata.txt", "r")

for line in metadata:
    nonewline = line.rstrip('\n')
    # print(nonewline);
    tokens = nonewline.split(" ")
    tokens.reverse()
    tablename = str.lower(tokens.pop())
    tokens.reverse()
    for i in range(0,len(tokens)):
        tokens[i] = str.lower(tokens[i])
    tables[tablename] = tokens

    if(tabs==''): tabs = tablename
    else: tabs = tabs + "|" + tablename
    # if(cols == None): cols = tablename
    for i in range(0, len(tokens)):
        if cols=='': cols = tokens[i]
        else: cols = cols + "|" + tokens[i]
# print(tables)

insert_keywords = ('INSERT', 'INTO', 'VALUES', 'SET')
delete_select_keywords = ('SELECT', 'DELETE')
literal_token = ('INT_LIT', 'DOUBLE_LIT', 'STRING_LIT')
arithmetic_op_token = ('ADD', 'SUBTRACT', 'DIVIDE', 'DIVIDE_INT', 'MODULO')
comparison_op_token = ('EQUAL', 'EQUAL_NULL', 'GT', 'GE', 'LT', 'LE', 'NE', 'NOT')
tokens = insert_keywords + delete_select_keywords + literal_token + arithmetic_op_token + comparison_op_token + (
    'COLUMN_NAME', 'TABLE_NAME', 'ASTERISK', # 'FILTER_ROWS',
    'COMMA', 'SEMICOLON', 'OPENPAR', 'CLOSEPAR', 'FROM', 'WHERE',
    'LIKE', 'STRCMP', 'IS', 'NULL', 'BETWEEN', 'AND'
)

t_COLUMN_NAME = r''+cols
t_TABLE_NAME = r''+tabs
# print(t_COLUMN_NAME)
# print(t_TABLE_NAME)

# Tokens
t_INSERT = r'insert'
t_SELECT = r'select'
t_DELETE = r'delete'
t_FROM = r'from'
t_WHERE = r'where'
t_INTO = r'into'
t_VALUES = r'values'
t_SET = r'set'
t_LIKE = r'like'
# t_FILTER_ROWS = r'(all|distinct|distinctrow)'
t_STRING_LIT = r'\'[^\']*\''
t_ASTERISK = r'\*'
t_COMMA = r','
t_SEMICOLON = r';'

t_ADD = r'\+'
t_SUBTRACT = r'-'
t_DIVIDE = r'/'
t_DIVIDE_INT = r'div'
t_MODULO = r'(mod | \%)'
t_EQUAL = r'='

t_NOT = r'(!|not)'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_NE = r'<>'
t_EQUAL_NULL = r'<=>'

t_STRCMP = r'strcmp'
t_IS = r'is'
t_NULL = r'null'


def t_DOUBLE_LIT(t):
    r'\-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_LIT(t):
    r'\-?\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t"

lexer = lex.lex()   # lexer
precedence = (
    ('left', 'ADD', 'SUBTRACT'),
    ('left', 'ASTERISK', 'DIVIDE', 'DIVIDE_INT')
)

operation = None
columns = []
table_selected = None
withcondition = False
value_list = None
assignment_list = None
value_list_bool = False
column_name_bool = False

condition = []  # format: lhs comparison_operator rhs

def p_statement(p):
    '''statement : insert_statement
            | select_statement
            | delete_statement'''

def p_insert_statement(p):
    '''insert_statement : INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON
            | INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON
            | INSERT into_kw TABLE_NAME SET assignment_list SEMICOLON'''
    # print("Insert statement")

    p[0] = ""
    for i in p:
        if(i is not None):
            p[0] = p[0] + " " + i

    global operation
    global table_selected
    global value_list
    global assignment_list
    global value_list_bool
    global column_name_bool
    
    operation = p[1]

    table_selected = p[3]


    if value_list_bool:
        if column_name_bool:
            value_list = p[9]
        else:
            value_list = p[6]
        #print("Value list: " + value_list)
    else:
        assignment_list = p[5]
        #print("Assignment list: " + assignment_list)


def p_select_statement(p):
    '''select_statement : SELECT columns FROM TABLE_NAME SEMICOLON
            | SELECT columns FROM TABLE_NAME WHERE condition SEMICOLON'''
            # SELECT filter_rows_op columns FROM TABLE_NAME SEMICOLON
            #         | SELECT filter_rows_op columns FROM TABLE_NAME WHERE condition SEMICOLON'''
    # print("Select statement")

    global operation
    global columns
    global table_selected
    global withcondition
    global condition

    p[0] = ""
    for i in p:
        # print (i)
        if(i is not None):
            p[0] = p[0] + " " + i

    operation = p[1]
    columns = p[2].split(',')

    table_selected = p[4]
    if table_selected in tables.keys():
        print("Valid table name")
    else:
        print("Invalid table name")

    for x1 in columns:
        if x1 in tables[table_selected]:
            print("Column " + x1 + " is in " + table_selected)
        else:
            print("Column " + x1 + " is not in " + table_selected)

    if(len(p) == 6):
        withcondition = False
        condition = []

    elif(len(p) == 8):
        withcondition = True
        condition = p[6]

def p_delete_statement(p):
    '''delete_statement : DELETE FROM TABLE_NAME SEMICOLON
            | DELETE FROM TABLE_NAME WHERE condition SEMICOLON'''
    # print("Delete statement")

    global operation
    global columns
    global table_selected
    global withcondition
    global condition

    p[0] = ""
    for i in p:
        if(i is not None):
            p[0] = p[0] + " " + i

    operation = p[1]
    table_selected = p[3]

    if table_selected in tables.keys():
        print("Valid table name")
    else:
        print("Invalid table name")

    if(len(p) == 5):
        withcondition = False
        condition = []

    elif(len(p) == 7):
        withcondition = True
        condition = p[5]

def p_into_kw(p):
    '''into_kw : INTO
            | empty'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = ""

# def p_filter_rows_op(p):
#     '''filter_rows_op : FILTER_ROWS
#             | empty'''
#     if(len(p) == 2):
#         p[0] = p[1]
#     else:
#         p[0] = ""

def p_columns(p):
    '''columns : ASTERISK
            | column_name'''
    p[0] = p[1]

def p_column_name(p):
    '''column_name : COLUMN_NAME
            | column_name COMMA COLUMN_NAME'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[1] + " " + p[2] + " " + p[3]
    global column_name_bool
    column_name_bool = True

def p_assignment_list(p):
    '''assignment_list : COLUMN_NAME EQUAL literals
            | assignment_list COMMA COLUMN_NAME EQUAL literals'''

    p[0] = ""
    for i in p:
        if(i is not None):
            p[0] = p[0] + " " + i
    global value_list_bool
    value_list_bool = False

def p_value_list(p):
    '''value_list : literals
            | value_list COMMA literals'''

    p[0] = ""
    for i in p:
        if(i is not None):
            p[0] = p[0] + " " + i
    global value_list_bool
    value_list_bool = True

def p_literals(p):
    '''literals : STRING_LIT
            | INT_LIT
            | DOUBLE_LIT'''
    p[0] = p[1]

def p_condition(p):
    '''condition : string_cond
            | num_cond
            | NOT OPENPAR string_cond CLOSEPAR
            | NOT OPENPAR num_cond CLOSEPAR'''

    p[0] = ""
    for i in p:
        if(i is not None):
            p[0] = p[0] + " " + i

def p_string_cond(p):
    '''string_cond : string_exp LIKE string_exp
            | string_exp NOT LIKE string_exp
            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR'''

    p[0] = ""
    for i in p:
        if(i is not None):
            p[0] = p[0] + " " + i

def p_string_exp(p):
    'string_exp : STRING_LIT'
            # | COLUMN_NAME''' # string literals include regexpressions
    # print(p)
    p[0] = p[1]

def p_num_cond(p):
    '''num_cond : num_exp comparison_op num_exp
            | num_exp BETWEEN num_exp AND num_exp
            | num_exp NOT NULL
            | num_exp IS NULL'''

    p[0] = ""
    #print(p[2] + 'dapatgt')
    if(p[2] == '<=>'):
        if((p[1] == 'null' and p[3] != 'null') or (p[1] != 'null' and p[3] == 'null')):
            print('<=> no entry')
            p[0] = 'False'
        elif(p[1] == 'null' and p[3] == 'null'):
            p[0] = 'True'
        elif((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            if(p[1] == p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
        else:
            print('<=> no entry')
            p[0] = p[1];
    elif((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float) ):
        if(p[2] == '>'):
            if(p[1] > p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
        elif(p[2] == '>='):
            if(p[1] >= p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
        elif(p[2] == '<'):
            if(p[1] < p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
        elif(p[2] == '<='):
            if(p[1] <= p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
        elif(p[2] == '='):
            if(p[1] == p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
        elif(p[2] == '<>'):
            if(p[1] != p[3]):
                p[0] = 'True'
            else:
                p[0] = 'False'
    else:
        for i in p:
            if(i is not None):
                p[0] = p[0] + " " + str(i)

def p_num_exp(p):
    '''num_exp : num_exp ADD num_factor
            |  num_factor SUBTRACT num_exp
            | num_factor'''
    if(len(p) > 2):
        if((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float) ):
            if p[2] == '+':
              p[0] = p[1] + p[3]
            elif p[2] == '-':
              p[0] = p[1] - p[3]
        else:
            p[0] = str(p[1]) + " " + p[2] + " " + str(p[3])
    else:
      p[0] = p[1]
    print("p0",p[0])

def p_num_factor(p):
    '''num_factor : num_factor ASTERISK num_term
            | num_factor DIVIDE num_term
            | num_factor DIVIDE_INT num_term
            | num_factor MODULO num_term
            | num_term'''
    if(len(p) > 2):
        if((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float) ):
            if p[2] == '*':
                p[0] = p[1] * p[3]
            elif p[2] == '/':
              p[0] = p[1] / p[3]
            elif p[2] == 'div':
              p[0] = p[1] // p[3]
            elif p[2] == '%':
              p[0] = p[1] % p[3]
        else:
            p[0] = str(p[1]) + " " + p[2] + " " + str(p[3])
    else:
      p[0] = p[1]

def p_num_term(p):
    '''num_term : OPENPAR num_exp CLOSEPAR
            | num_val'''
    if(len(p) == 4):
        if(type(p[2]) == int or type(p[2]) == float):
            p[0] = p[2]
        else:
            p[0] = p[1]+p[2]+p[3]
    else:
        p[0] = p[1]

def p_num_val(p):
    '''num_val : INT_LIT
            | DOUBLE_LIT
            | COLUMN_NAME'''    #also accepts column compared to column
    if(p[1] == "INT_LIT"):
        p[0] = int(p[1])
    elif(p[1] == "DOUBLE_LIT"):
        p[0] = float(p[1])
    else:
        p[0] = p[1]

def p_comparison_op(p):
    '''comparison_op : GE
            | GT
            | LE
            | LT
            | NE
            | EQUAL
            | EQUAL_NULL'''
    p[0] = p[1]


def p_empty(p):
    'empty : '
    pass

def p_error(p):
    # vars(p)
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc() # parser

while 1:
    try:
        s = raw_input('mysql > ')
        s = s.lower()
        lex.input(s)
        # for tok in iter(lex.token, None):
            # print(to)
            # print(repr(tok.type), repr(tok.value))
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)


    print("Operation: ", operation)
    if operation == 'select':
        print("Columns: ")
        for i in columns:
            if(i is not None):
                print(i)
        print("table_selected: ", table_selected)
        print("withcondition: ", withcondition)
        print("condition: ", condition)
    elif operation == 'insert':
        print("table_selected:", table_selected)
        if value_list_bool:
            print("Value list: " + value_list)
        else:
            print("Assignment list: " + assignment_list)
    elif operation == 'delete':
        print("table_selected:", table_selected)
        if withcondition:
            print("Condition: ", condition)
        else:
            print("Condition: No Condition")


    operation = ''
    columns = ''
    table_selected = '';
    withcondition = '';
    condition = '';
    value_list = '';
    assignment_list = '';
