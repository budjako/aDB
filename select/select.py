import sys
import re
sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

from datetime import date
from ply import *
import selectlex
# import selectparse
# import selectinterp


tables = {}
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
literal_token = ('INT_LIT', 'DOUBLE_LIT', 'STRING_LIT', 'DATE_LIT')
arithmetic_op_token = ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'DIVIDE_INT', 'MODULO')
comparison_op_token = ('EQUAL', 'EQUAL_NULL', 'GT', 'GE', 'LT', 'LE', 'NE', 'NOT')
date_keywords = (
    'ADDDATE', 'CURDATE', 'CURRENT_DATE', 'DATEDIFF', 'DAY', 'DAYNAME', 'DAYOFMONTH', 'DAYOFWEEK', 'DAYOFYEAR', 'LAST_DAY',
    'MAKEDATE', 'MONTH', 'MONTHNAME', 'SUBDATE', 'INTERVAL', 'YEAR'
)
tokens = insert_keywords + delete_select_keywords + literal_token + arithmetic_op_token + comparison_op_token + date_keywords + (
    'COLUMN_NAME', 'TABLE_NAME', 'FILTER_ROWS', 'ASTERISK', 'DATE_UNIT',
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
t_FILTER_ROWS = r'(all|distinct|distinctrow)'
t_STRING_LIT = r'\'[^\']*\''
t_ASTERISK = r'\*'
t_COMMA = r','
t_SEMICOLON = r';'

t_ADD = r'\+'
t_SUBTRACT = r'-'
t_MULTIPLY = r'\*'
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

t_BETWEEN = r'between'
t_AND = r'and'
t_ADDDATE = r'adddate'
t_CURDATE = r'curdate'
t_CURRENT_DATE = r'current_date'
t_DATEDIFF = r'datediff'
t_DAY = r'day'
t_DAYNAME = r'dayname'
t_DAYOFMONTH = r'dayofmonth'
t_DAYOFWEEK = r'dayofweek'
t_DAYOFYEAR = r'dayofyear'
t_LAST_DAY = r'last_day'
t_MAKEDATE = r'makedate'
t_MONTH = r'month'
t_MONTHNAME = r'monthname'
t_SUBDATE = r'subdate'
t_INTERVAL = r'interval'
t_YEAR = r'year'


def t_DATE_LIT(t):
    r'\'\d{4}\-(0?[1-9]|10|11|12)\-(30|31|((0|1|2)?[0-9]))\'' # Year-Month-Day
    date_tokens = t.value.split("-")
    print(date_tokens)
    t.value = date(int(date_tokens[0]), int(date_tokens[1]), int(date_tokens[2]))
    return t

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

def t_DATE_UNIT(t):
    r'(second|minute|day|week|month|quarter|year)'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t"

lexer = lex.lex()   # lexer
precedence = (
    ('left', 'ADD', 'SUBTRACT'),
    ('left', 'MULTIPLY', 'DIVIDE', 'DIVIDE_INT')
)
command = {}

def p_statement(p):
    '''statement : insert_statement
            | select_statement
            | delete_statement'''

def p_insert_statement(p):
    '''insert_statement : INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON
            | INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON
            | INSERT into_kw TABLE_NAME SET assignment_list SEMICOLON'''
    print("Insert statement")
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i
    print(p[0])
    # p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7] + " "

def p_select_statement(p):
    '''select_statement : SELECT filter_rows_op columns FROM TABLE_NAME SEMICOLON
            | SELECT filter_rows_op columns FROM TABLE_NAME WHERE condition SEMICOLON'''
    print("Select statement")
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i
    print(p[0])


def p_delete_statement(p):
    '''delete_statement : DELETE FROM TABLE_NAME SEMICOLON
            | DELETE FROM TABLE_NAME WHERE condition SEMICOLON'''
    print("Delete statement")
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i
    print(p[0])

def p_into_kw(p):
    '''into_kw : INTO
            | empty'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None

def p_filter_rows_op(p):
    '''filter_rows_op : FILTER_ROWS
            | empty'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None

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

def p_assignment_list(p):
    '''assignment_list : COLUMN_NAME EQUAL literals
            | assignment_list COMMA COLUMN_NAME EQUAL literals'''
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i

def p_value_list(p):
    '''value_list : literals
            | value_list COMMA literals'''
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i

def p_literals(p):
    '''literals : STRING_LIT
            | INT_LIT
            | DOUBLE_LIT
            | DATE_LIT'''
    p[0] = p[1]

def p_condition(p):
    '''condition : string_cond
            | num_cond
            | date_cond
            | NOT OPENPAR string_cond CLOSEPAR
            | NOT OPENPAR num_cond CLOSEPAR
            | NOT OPENPAR date_cond CLOSEPAR'''
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i

def p_string_cond(p):
    '''string_cond : string_exp LIKE string_exp
            | string_exp NOT LIKE string_exp
            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR'''
    p[0] = None
    for i in p:
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
    p[0] = None
    for i in p:
        p[0] = p[0] + " " + i

def p_num_exp(p):
    '''num_exp : num_exp ADD num_factor
            | num_exp SUBTRACT num_factor
            | num_factor'''
    if p[2] == '+':
      p[0] = p[1] + p[3]
    elif p[2] == '-':
      p[0] = p[1] - p[3]
    else:
      p[0] = p[1]

def p_num_factor(p):
    '''num_factor : num_factor MULTIPLY num_term
            | num_factor DIVIDE num_term
            | num_factor DIVIDE_INT num_term
            | num_factor MODULO num_term
            | num_term'''
    if p[2] == '*':
      p[0] = p[1] * p[3]
    elif p[2] == '/':
      p[0] = p[1] / p[3]
    elif p[2] == 'div':
      p[0] = p[1] // p[3]
    elif p[2] == '%':
      p[0] = p[1] % p[3]
    else:
      p[0] = p[1]

def p_num_term(p):
    '''num_term : OPENPAR num_val CLOSEPAR
            | num_val'''
    p[0] = p[2]

def p_num_val(p):
    '''num_val : INT_LIT
            | DOUBLE_LIT
            | COLUMN_NAME'''    #also accepts column compared to column
    p[0] = p[1]

def p_date_cond(p):
    '''date_cond : date_exp comparison_op date_exp
            | date_exp'''
    if(len(p) == 2):
    p[0] = p[1]

def p_date_exp(p):
    '''date_exp : date_function
            | DATE_LIT'''
    p[0] = p[1]

def p_date_function(p):
    '''date_function : ADDDATE OPENPAR date_exp COMMA date_exp CLOSEPAR
             | CURDATE OPENPAR CLOSEPAR
             | CURRENT_DATE OPENPAR CLOSEPAR
             | CURRENT_DATE
             | DATEDIFF OPENPAR date_exp COMMA date_exp CLOSEPAR
             | DAY OPENPAR date_exp CLOSEPAR
             | DAYNAME OPENPAR date_exp CLOSEPAR
             | DAYOFMONTH OPENPAR date_exp CLOSEPAR
             | DAYOFWEEK OPENPAR date_exp CLOSEPAR
             | DAYOFYEAR OPENPAR date_exp CLOSEPAR
             | LAST_DAY OPENPAR date_exp CLOSEPAR
             | MAKEDATE OPENPAR num_exp COMMA num_exp CLOSEPAR
             | MONTH OPENPAR date_exp CLOSEPAR
             | MONTHNAME OPENPAR date_exp CLOSEPAR
             | SUBDATE OPENPAR date_exp COMMA INTERVAL num_exp DATE_UNIT CLOSEPAR
             | YEAR OPENPAR date_exp CLOSEPAR'''

def p_comparison_op(p):
    '''comparison_op : GE
            | GT
            | LE
            | LT
            | NE
            | EQUAL
            | EQUAL_NULL'''
    p[0] = p[1]

# def p_arithmetic_op(p):
#     '''arithmetic_op : ADD
#             | SUBTRACT
#             | MULTIPLY
#             | DIVIDE
#             | DIVIDE_INT
#             | MODULO'''

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
        for tok in iter(lex.token, None):
            print(tok)
            print(repr(tok.type), repr(tok.value))
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
