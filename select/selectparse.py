from ply import *
import selectlex

tokens = selectlex.tokens

def p_select_statement(p):
    '''statement : SELECT COLUMN_NAME FROM TABLE_NAME'''
    p[0] = 'Select Statement';

def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

selectparser = yacc.yacc()

def parse(data, debug=0):
    selectparser.error = 0
    p = selectparser.parse(data, debug=debug)
    if selectparser.error:
        return None
    return p
