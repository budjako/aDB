from ply import *

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
    datatype = {}
    for i in range(0,len(tokens),2):
        tokens[i] = str.lower(tokens[i])
        datatype[tokens[i]] = tokens[i+1]

    tables[tablename] = datatype

    if(tabs==''): tabs = tablename
    else: tabs = tabs + "|" + tablename
    # if(cols == None): cols = tablename
    for i in range(0, len(tokens),2):
        if cols=='': cols = tokens[i]
        else: cols = cols + "|" + tokens[i]


print("tables")
print(tables)

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

lexer = lex.lex(debug=0)   # lexer
