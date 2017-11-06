import sys
import re
import time

sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

import mysqllex
import mysqlparse

while 1:
    try:
        s = raw_input('mysql > ')
        s = s.lower()
    except EOFError:
        raise SystemExit
    if not s:
        continue
    prog = mysqlparse.parse(s)
    if not prog:
        continue

    print(prog)
        # for tok in iter(lex.token, None):
            # print(to)
            # print(repr(tok.type), repr(tok.value))
    # except EOFError:
    #     break
    # if not s:
    #     continue


    # print("Operation: ", operation)
    # if operation == 'select':
    #     print("Columns: ")
    #     for i in columns:
    #         if(i is not None):
    #             print(i)
    #     print("table_selected: ", table_selected)
    #     print("withcondition: ", withcondition)
    #     print("condition: ", condition)
    # elif operation == 'insert':
    #     print("table_selected:", table_selected)
    #     if value_list_bool:
    #         print("Value list: " + value_list)
    #     else:
    #         print("Assignment list: " + assignment_list)
    # elif operation == 'delete':
    #     print("table_selected:", table_selected)
    #     if withcondition:
    #         print("Condition: ", condition)
    #     else:
    #         print("Condition: No Condition")
    #
    #
    # operation = ''
    # columns = ''
    # table_selected = '';
    # withcondition = '';
    # condition = '';
    # value_list = '';
    # assignment_list = '';
