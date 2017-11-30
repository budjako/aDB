from BTrees.OOBTree import OOBTree

tablename = "student"
primarykey = []
cols = []
datatypes = []
btree = OOBTree()

tabledata = open(tablename+".dat", "r")
counter = 0
# Read data on <tablename>.dat

for line in tabledata:
    if(counter == 0):       # column names
        nonewline = line.rstrip('\n')
        column_names = nonewline.split(";")
        # print(column_names)
        for i in range(0,len(column_names)):
            if(column_names[i] != ""):
                column = column_names[i].split(",")
                # print(column)
                for i in range(0,len(column)):
                    name = column[i].split(" ")
                    # print(name)
                    # print(name[0])
                    cols.append(name[0])
                    datatypes.append(name[1])
        counter = counter + 1
    elif(counter == 1):     # primary key/s
        print("Primary Key: ", line)

        nonewline = line.rstrip('\n')
        keys = nonewline.split(";")
        # print(column_names)
        for i in range(0,len(keys)):
            if(keys[i] != ""):
                primarykey.append(keys[i])
        counter = counter + 1
    else:
        nonewline = line.rstrip('\n')
        # print(nonewline);
        rows = nonewline.split(";")
        # print(len(rows))
        for i in range(0,len(rows)):
            # print(rows[i])
            if(rows[i] != ""):
                data = rows[i].split(",")
                for i in range(0, len(data)):
                    data[i] = data[i].rstrip('\'')
                    data[i] = data[i].lstrip('\'')

                btree.update({data[0]: {cols[1]: data[1], cols[2]: data[2], cols[3]: data[3], cols[4]: data[4], cols[5]: data[5]}})
        # print(list(btree))
tabledata.close()


# print(btree["2011-29712"])

# Update data here

btree['2011-29712']['major'] = "Security"
# print(btree["2011-29712"])
# print(cols)
# print(datatypes)
# print(primarykey)

# From BTree to .dat file
tabledata = open(tablename+".dat", "w")
column_name_row = primarykey[0]+" "+datatypes[0]
print(cols)
print(datatypes)

for i in range(1, len(data)):
    column_name_row = column_name_row+","+cols[i]+" "+datatypes[i]
# print(column_name_row)
# print(primarykey[0])

tabledata.write(column_name_row)
tabledata.write("\n")
tabledata.write(primarykey[0])
tabledata.write("\n")

for i in btree.keys():
    # print(i)
    # create string for the whole row
    if(datatypes[0] == 'varchar'): row = "\'"+i+"\'"
    else: row = i

    for j in range(1,len(cols)):
        if(datatypes[j] == 'varchar'): row = row+",\'"+btree[i][cols[j]]+"\'"
        else: row = row+","+btree[i][cols[j]]
    row = row+";"
    # print(row)
    tabledata.write(row)
    tabledata.write("\n")


operation = "insert"
table_selected = "student"
#table_selected = "studenthistory"
#table_selected = "course"
#table_selected = "courseoffering" #1. Acad Year as b-tree key 2. list of primary key as b-tree key
#table_selected = "studcourse" #1. Auto-increment primary key

value_list = "'2011-12314','Gerald Emalada','1995-06-10','BSCS','null','18'"
#value_list = "'2011-12314','abcdesc','complete','string1','string2'"
#value_list = "'CMSC 123','Data Structures','Data Structures desc','3','1','2nd'"
#value_list = "'2nd','2017-2018','CMSC 123','AB','1-2','120'"

val_ins = '';
col_name = ' studno , studentname , birthday , degree , major , unitsearned ';
#col_name = ' studno , desription , action , datefiled , dateresolved '
#col_name = ' cno , ctitle , cdesc , noofunits , haslab , semoffered '
#col_name = ' semester , acadyear , cno , section , time , maxstud '

value_list_bool = True;
column_name_bool = False;

assignment_list = " 'studno' = '2011-12314' , 'studentname' = 'Gerald Emalada' , 'birthday' = '1995-06-10' , 'degree' = 'bscs' , 'major' = 'null' , 'unitsearned' = '18' ";
#assignment_list = " 'studno' = '2011-12314' , 'description' = 'desc1' , 'action' = 'completed' , 'datefiled' = 'filed1' , 'dateresolved' = 'resolved1' "
#assignment_list = " 'cno' = 'CMSC 123' , 'ctitle' = 'Data Structures' , 'cdesc' = 'Data Structures desc' , 'noofunits' = '3' , 'haslab' = '1' , 'semoffered' = '2nd' "
#assignment_list = " 'semester' = '2nd' , 'acadyear' = '2017-2018' , 'cno' = 'CMSC 123' , 'section' = 'AB' , 'time' = '1-2' , 'maxstud' = '120' "

student_primary_key = "studno"
studenthistory_primary_key = 'studno'
course_primary_key = 'cno'
courseoffering_primary_key = ['semester','acadyear','cno','section']
curr_table_primary = ''

# print(cols)
#cols = ['studno','description','action','datefiled','dateresolved'] #for studenthistory testing
#cols = ['cno', 'ctitle', 'cdesc', 'noofunits', 'haslab', 'secmoffered'] #for course testing
#cols = ['semester', 'acadyear', 'cno', 'section', 'time', 'maxstud'] #for courseoffering testing
# print(cols)
if operation == 'insert':
    if table_selected == 'student':     #For primary key of table
        curr_table_primary = student_primary_key
    elif table_selected == 'studenthistory':
        curr_table_primary = studenthistory_primary_key
    elif table_selected == 'course':
        curr_table_primary = course_primary_key


    if table_selected == 'student':
        if value_list_bool and not column_name_bool: #first case input
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            if value_list[0] not in btree:
                if len(value_list) == 6:
                    # print("value list length is 6")
                    btree.update({value_list[0]: {cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3], cols[4]: value_list[4], cols[5]: value_list[5]}})
                    # print(value_list)
                else:
                    print("Column values are lacking")
            else:
                print("Already in BTree")

        elif value_list_bool and column_name_bool: #second case input
            col_name = col_name.replace(" ", "")
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            col_name = col_name.split(',')
            if "studno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("studno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

        elif not value_list_bool and not column_name_bool: #third case input
            assignment_list = assignment_list.split(',')
            insert_list = []
            col_name = []
            value_list = []

            for i in range(0,len(assignment_list)):
                split_list = assignment_list[i].split("=")
                col_ext = split_list[0][2:-2]
                val_ext = split_list[1][2:-2]
                col_name.append(col_ext)
                value_list.append(val_ext)

            if "studno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("studno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

    elif table_selected == 'studenthistory':
        if value_list_bool and not column_name_bool: #first case input
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            if value_list[0] not in btree:
                if len(value_list) == 5:
                    print("value list length is 5")
                    btree.update({value_list[0]: {cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3], cols[4]: value_list[4]}})
                else:
                    print("Column values are lacking")
            else:
                print("Already in BTree")

        elif value_list_bool and column_name_bool: #second case input
            col_name = col_name.replace(" ", "")
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            col_name = col_name.split(',')
            if "studno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("studno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

        elif not value_list_bool and not column_name_bool: #third case input
            assignment_list = assignment_list.split(',')
            insert_list = []
            col_name = []
            value_list = []

            for i in range(0,len(assignment_list)):
                split_list = assignment_list[i].split("=")
                col_ext = split_list[0][2:-2]
                val_ext = split_list[1][2:-2]
                col_name.append(col_ext)
                value_list.append(val_ext)

            if "studno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("studno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

    elif table_selected == 'course':
        if value_list_bool and not column_name_bool: #first case input
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            if value_list[0] not in btree:
                if len(value_list) == 6:
                    print("value list length is 6")
                    btree.update({value_list[0]: {cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3], cols[4]: value_list[4], cols[5]: value_list[5]}})
                else:
                    print("Column values are lacking")
            else:
                print("Already in BTree")

        elif value_list_bool and column_name_bool: #second case input
            col_name = col_name.replace(" ", "")
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            col_name = col_name.split(',')
            if "cno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("cno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

        elif not value_list_bool and not column_name_bool: #third case input
            assignment_list = assignment_list.split(',')
            insert_list = []
            col_name = []
            value_list = []

            for i in range(0,len(assignment_list)):
                split_list = assignment_list[i].split("=")
                col_ext = split_list[0][2:-2]
                val_ext = split_list[1][2:-2]
                col_name.append(col_ext)
                value_list.append(val_ext)

            if "cno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("cno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

    elif table_selected == 'courseoffering':
        if value_list_bool and not column_name_bool: #first case input
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            if value_list[0] not in btree:
                if len(value_list) == 6:
                    print("value list length is 6")
                    btree.update({value_list[0]: {cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3], cols[4]: value_list[4], cols[5]: value_list[5]}})
                else:
                    print("Column values are lacking")
            else:
                print("Already in BTree")

        elif value_list_bool and column_name_bool: #second case input
            col_name = col_name.replace(" ", "")
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            col_name = col_name.split(',')
            if "cno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("cno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")

        elif not value_list_bool and not column_name_bool: #third case input
            assignment_list = assignment_list.split(',')
            insert_list = []
            col_name = []
            value_list = []

            for i in range(0,len(assignment_list)):
                split_list = assignment_list[i].split("=")
                col_ext = split_list[0][2:-2]
                val_ext = split_list[1][2:-2]
                col_name.append(col_ext)
                value_list.append(val_ext)

            if "cno" not in col_name:
                print("No primary key")
            else:
                key_index = col_name.index("cno")
                key_col_name = col_name.pop(key_index)
                key_value_list = value_list.pop(key_index)
                dict_cols_vals = dict(zip(col_name,value_list))

                if key_value_list not in btree:
                    btree.update({key_value_list: dict_cols_vals})
                else:
                    print("Already in BTree")


# print(list(btree))
#print(btree["2012-29339"])

select = 'studentname,birthday,studno'

# for j, k in zip(btree.keys(), btree.values()):
#     if select == '*':
#         print(j + " ", end="")
#         print(k['studentname'] + " ", end="")
#         print(k['birthday'] + " ", end="")
#         print(k['degree'] + " ", end="")
#         print(k['major'] + " ", end="")
#         print(k['unitsearned'] + " ", end="")
#         print("")
#     else:
#         if select == 'studno':
#             print(j)
#         else:
#             select_query = select.split(',')
#             for item in select_query:
#                 if item == 'studno':
#                     print(j + " ", end="")
#                 else:
#                     print(k[item] + " ", end="")
#             print("")
'''
#for studenthistory
for j, k in zip(btree.keys(), btree.values()):
    if select == '*':
        print(j + " ", end="")
        print(k['description'] + " ", end="")
        print(k['action'] + " ", end="")
        print(k['datefiled'] + " ", end="")
        print(k['dateresolved'] + " ", end="")
        print("")
    else:
        if select == 'studno':
            print(j)
        else:
            select_query = select.split(',')
            for item in select_query:
                if item == 'studno':
                    print(j + " ", end="")
                else:
                    print(k[item] + " ", end="")
            print("")

#for course
for j, k in zip(btree.keys(), btree.values()):
    if select == '*':
        print(j + " ", end="")
        print(k['ctitle'] + " ", end="")
        print(k['cdesc'] + " ", end="")
        print(k['noofunits'] + " ", end="")
        print(k['haslab'] + " ", end="")
        print(k['semoffered'] + " ", end="")
        print("")
    else:
        if select == 'cno':
            print(j)
        else:
            select_query = select.split(',')
            for item in select_query:
                if item == 'cno':
                    print(j + " ", end="")
                else:
                    print(k[item] + " ", end="")
            print("")
'''