import sys
sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

from datetime import date
from ply import *
import selectlex
# import selectparse
# import selectinterp


tables = {}

def readMetadata():
    metadata = open("metadata.txt", "r")

    for line in metadata:
        nonewline = line.rstrip('\n')
        print(nonewline);
        tokens = nonewline.split(" ")
        tokens.reverse()
        tablename = tokens.pop()
        tokens.reverse()
        for i in range(0,len(tokens)):
            tokens[i] = str.lower(tokens[i])
        tables[str.lower(tablename)] = tokens
    print(tables)
#     updateColumnNames()
#     updateTableNames()
#
# def updateColumnNames():
#
#
# def updateTableNames():


keywords = (
    'FROM', 'WHERE', 'SELECT', 'LIKE', 'STRCMP', 'IS', 'NULL', 'BETWEEN', 'AND'
)

date_keywords = (
    'ADDDATE', 'CURDATE', 'CURRENT_DATE', 'DATEDIFF', 'DAY', 'DAYNAME', 'DAYOFMONTH', 'DAYOFWEEK', 'DAYOFYEAR', 'LAST_DAY',
    'MAKEDATE', 'MONTH', 'MONTHNAME', 'SUBDATE', 'INTERVAL', 'YEAR'
)

tokens = keywords + date_keywords + (
    'COLUMN_NAME', 'TABLE_NAME', 'FILTER_ROWS', 'INT_LIT', 'DOUBLE_LIT', 'STRING_LIT', 'DATE_LIT', 'ASTERISK', 'DATE_UNIT',
    'COMMA', 'SEMICOLON', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'DIVIDE_INT', 'MODULO', 'EQUAL', 'EQUAL_NULL',
    'GT', 'GE', 'LT', 'LE', 'NE', 'NOT', 'OPENPAR', 'CLOSEPAR'
)

# Tokens
t_FROM = r'from'
t_WHERE = r'where'
t_SELECT = r'select'
t_LIKE = r'like'
t_COLUMN_NAME = r'(studno|studentname|birthday|degree|major|unitsearned|description|action|datefiled|dateresolved|cno|ctitle|cdesc|noofunits|haslab|semoffered|semester|acadyear|cno|section|time|maxstud)'
t_TABLE_NAME = r'(student|studenthistory|course|courseoffering|studcourse)'
t_FILTER_ROWS = r'(all|distinct|distinctrow)'
t_STRING_LIT = r'\'.*\''
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

def t_INT_LIT(t):
    r'\-?\d+'
    t.value = int(t.value)
    return t

def t_DOUBLE_LIT(t):
    r'\-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_DATE_LIT(t):
    r'\d{4}\-(0?[1-9]|10|11|12)\-(0?[1-9]|1[0-9]|2[0-9]|30|31)' # Year-Month-Day
    t_value = date(2017, 10, 1)

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

def p_select_statement(p):
    '''statement : SELECT filter_rows_op columns FROM TABLE_NAME SEMICOLON
            | SELECT filter_rows_op columns FROM TABLE_NAME WHERE condition SEMICOLON'''
    # '''statement : SELECT columns FROM TABLE_NAME SEMICOLON
    #         | SELECT columns FROM TABLE_NAME WHERE condition SEMICOLON'''
    # print(p);

def p_filter_rows_op(p):
    '''filter_rows_op : FILTER_ROWS
            | empty'''

def p_columns(p):
    '''columns : ASTERISK
            | column_name'''
    # print(p)

def p_column_name(p):
    '''column_name : COLUMN_NAME
            | column_name COMMA COLUMN_NAME'''

def p_condition(p):
    '''condition : string_cond
            | num_cond
            | date_cond
            | NOT OPENPAR string_cond CLOSEPAR
            | NOT OPENPAR num_cond CLOSEPAR
            | NOT OPENPAR date_cond CLOSEPAR'''
    # print(p)

def p_string_cond(p):
    '''string_cond : string_exp LIKE string_exp
            | string_exp NOT LIKE string_exp
            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR'''
            # | string_exp EQUAL string_exp
    # print(p)

def p_string_exp(p):
    '''string_exp : STRING_LIT
            | COLUMN_NAME''' # string literals include regexpressions
    # print(p)

def p_num_cond(p):
    '''num_cond : num_exp comparison_op num_exp
            | num_exp BETWEEN num_exp AND num_exp
            | num_exp NOT NULL
            | num_exp IS NULL'''

def p_num_exp(p):
    '''num_exp : num_exp ADD num_factor
            | num_exp SUBTRACT num_factor
            | num_factor'''

def p_num_factor(p):
    '''num_factor : num_factor MULTIPLY num_term
            | num_factor DIVIDE num_term
            | num_factor DIVIDE_INT num_term
            | num_factor MODULO num_term
            | num_term'''

def p_num_term(p):
    '''num_term : OPENPAR num_val CLOSEPAR
            | num_val'''

def p_num_val(p):
    '''num_val : INT_LIT
            | DOUBLE_LIT
            | COLUMN_NAME'''    #also accepts column compared to column

def p_date_cond(p):
    '''date_cond : date_exp comparison_op date_exp
            | date_exp'''

def p_date_exp(p):
    '''date_exp : date_function
            | DATE_LIT'''

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
