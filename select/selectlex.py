from ply import *

keywords = (
    'SELECT', 'FROM', 'ALL', 'DISTINCT', 'DISTINCTROW', 'WHERE'
)

tokens = keywords + (
    'COLUMN_NAME', 'TABLE_NAME', 'INT_LIT', 'DOUBLE_LIT', 'REG_CHARS', 'STRING_LIT', 'LITERALS', 'ASTERISK',
    'COMMA',
)

# Tokens
t_TABLE_NAME = r'[student|studenthistory|course|courseoffering|studcourse]'
t_COLUMN_NAME = r'[studno|studentname|birthday|degree|major|unitsearned|description|action|datefiled|dateresolved|cno|ctitle|cdesc|noofunits|haslab|semoffered|semester|acadyear|cno|section|time|maxstud]'
t_STRING_LIT = r'\'[\w*|[a-zA-Z0-9]]*\''
t_ASTERISK = r'\*'
t_COMMA = r','

def t_INT_LIT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DOUBLE_LIT(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t"
