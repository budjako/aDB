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
        print(list(btree))
tabledata.close()


# print(btree["2011-29712"])

# Update data here

btree['2011-29712']['major'] = "Security"
print(btree["2011-29712"])
# print(cols)
# print(datatypes)
# print(primarykey)

# From BTree to .dat file
tabledata = open(tablename+".dat", "w")
column_name_row = primarykey[0]+" "+datatypes[0]

for i in range(1, len(data)):
    column_name_row = column_name_row+","+cols[i]+" "+datatypes[i]
print(column_name_row)
print(primarykey[0])

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
    print(row)
    tabledata.write(row)
    tabledata.write("\n")


operation = "insert"
#operation = "select"



table_selected = "student"
#table_selected = "studenthistory"
#table_selected = "course"
#table_selected = "courseoffering" #1. Four btrees
#table_selected = "studcourse" #1. Auto-increment primary key

value_list = "'2011-12314','Gerald Emalada','1995-06-10','BSCS','NULL','18'"
#value_list = "'2011-12314','abcdesc','complete','string1','string2'"
#value_list = "'CMSC 123','Data Structures','Data Structures desc','3','1','2nd'"
#value_list = "'2nd','2017-2018','CMSC 123','AB','1-2','120'"
#value_list = "'2011-12314','CMSC 123','2nd','2017-2018'"

val_ins = '';
col_name = ' studno , studentname , birthday , degree , major , unitsearned ';
#col_name = ' studno , desription , action , datefiled , dateresolved '
#col_name = ' cno , ctitle , cdesc , noofunits , haslab , semoffered '
#col_name = ' semester , acadyear , cno , section , time , maxstud '
#col_name = ' studno , cno , semester , acadyear '

value_list_bool = True;
column_name_bool = False;

assignment_list = " 'studno' = '2011-12314' , 'studentname' = 'Gerald Emalada' , 'birthday' = '1995-06-10' , 'degree' = 'bscs' , 'major' = 'null' , 'unitsearned' = '18' ";
#assignment_list = " 'studno' = '2011-12314' , 'description' = 'desc1' , 'action' = 'completed' , 'datefiled' = 'filed1' , 'dateresolved' = 'resolved1' "
#assignment_list = " 'cno' = 'CMSC 123' , 'ctitle' = 'Data Structures' , 'cdesc' = 'Data Structures desc' , 'noofunits' = '3' , 'haslab' = '1' , 'semoffered' = '2nd' "
#assignment_list = " 'semester' = '2nd' , 'acadyear' = '2017-2018' , 'cno' = 'CMSC 123' , 'section' = 'AB' , 'time' = '1-2' , 'maxstud' = '120' "
#assignment_list = " 'studno' = '2011-12314' , 'cno' = 'CMSC 123' , 'semester' = '2nd' , 'acadyear' = '2nd' "

student_primary_key = "studno"
studenthistory_primary_key = 'studno'
course_primary_key = 'cno'
courseoffering_primary_key = ['semester','acadyear','cno','section']


print(cols)
#cols = ['studno','description','action','datefiled','dateresolved'] #for studenthistory testing
#cols = ['cno', 'ctitle', 'cdesc', 'noofunits', 'haslab', 'secmoffered'] #for course testing
#cols = ['semester', 'acadyear', 'cno', 'section', 'time', 'maxstud'] #for courseoffering testing
#cols = ['studno' , 'cno', 'semester', 'acadyear']
print(cols)
if operation == 'insert':
    if table_selected == 'student':
        if value_list_bool and not column_name_bool: #first case input
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            if value_list[0] not in btree:
                if len(value_list) == 6:
                    print("value list length is 6")
                    btree.update({value_list[0]: {cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3], cols[4]: value_list[4], cols[5]: value_list[5]}})
                    print(btree[value_list[0]])
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

                if 'studentname' not in dict_cols_vals:
                    dict_cols_vals['studentname'] = None;
                if 'birthday' not in dict_cols_vals:
                    dict_cols_vals['birthday'] = None;
                if 'degree' not in dict_cols_vals:
                    dict_cols_vals['degree'] = None;
                if 'major' not in dict_cols_vals:
                    dict_cols_vals['major'] = None;
                if 'unitsearned' not in dict_cols_vals:
                    dict_cols_vals['unitsearned'] = None;

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

                if 'studentname' not in dict_cols_vals:
                    dict_cols_vals['studentname'] = None;
                if 'birthday' not in dict_cols_vals:
                    dict_cols_vals['birthday'] = None;
                if 'degree' not in dict_cols_vals:
                    dict_cols_vals['degree'] = None;
                if 'major' not in dict_cols_vals:
                    dict_cols_vals['major'] = None;
                if 'unitsearned' not in dict_cols_vals:
                    dict_cols_vals['unitsearned'] = None;


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

                if 'description' not in dict_cols_vals:
                    dict_cols_vals['description'] = None;
                if 'action' not in dict_cols_vals:
                    dict_cols_vals['action'] = None;
                if 'datefiled' not in dict_cols_vals:
                    dict_cols_vals['datefiled'] = None;
                if 'dateresolved' not in dict_cols_vals:
                    dict_cols_vals['dateresolved'] = None;

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

                if 'description' not in dict_cols_vals:
                    dict_cols_vals['description'] = None;
                if 'action' not in dict_cols_vals:
                    dict_cols_vals['action'] = None;
                if 'datefiled' not in dict_cols_vals:
                    dict_cols_vals['datefiled'] = None;
                if 'dateresolved' not in dict_cols_vals:
                    dict_cols_vals['dateresolved'] = None;

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

                if 'ctitle' not in dict_cols_vals:
                    dict_cols_vals['ctitle'] = None;
                if 'cdesc' not in dict_cols_vals:
                    dict_cols_vals['cdesc'] = None;
                if 'noofunits' not in dict_cols_vals:
                    dict_cols_vals['noofunits'] = None;
                if 'haslab' not in dict_cols_vals:
                    dict_cols_vals['haslab'] = None;
                if 'semoffered' not in dict_cols_vals:
                    dict_cols_vals['semoffered'] = None;

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

                if 'ctitle' not in dict_cols_vals:
                    dict_cols_vals['ctitle'] = None;
                if 'cdesc' not in dict_cols_vals:
                    dict_cols_vals['cdesc'] = None;
                if 'noofunits' not in dict_cols_vals:
                    dict_cols_vals['noofunits'] = None;
                if 'haslab' not in dict_cols_vals:
                    dict_cols_vals['haslab'] = None;
                if 'semoffered' not in dict_cols_vals:
                    dict_cols_vals['semoffered'] = None;

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
            print(value_list[0:4])
            if (value_list[0:4]) not in btree.keys():
                if len(value_list) == 6:
                    print("value list length is 6")
                    str123 = ",".join(value_list[0:4])
                    btree.update({",".join(value_list[0:4]): {cols[0]: value_list[0], cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3], cols[4]: value_list[4], cols[5]: value_list[5]}})
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

            if ("semester" not in col_name) or ("acadyear" not in col_name) or ("cno" not in col_name) or ("section" not in col_name):
                print("No primary key/s")
            else:
                key_index = ['','','','']
                key_col_name = ['','','','']
                key_value_list = ['','','','']

                key_index[0] = col_name.index("semester")
                key_col_name[0] = col_name.pop(key_index[0])
                key_value_list[0] = value_list.pop(key_index[0])

                key_index[1] = col_name.index("acadyear")
                key_col_name[1] = col_name.pop(key_index[1])
                key_value_list[1] = value_list.pop(key_index[1])

                key_index[2] = col_name.index("cno")
                key_col_name[2] = col_name.pop(key_index[2])
                key_value_list[2] = value_list.pop(key_index[2])

                key_index[3] = col_name.index("section")
                key_col_name[3] = col_name.pop(key_index[3])
                key_value_list[3] = value_list.pop(key_index[3])

                dict_cols_vals = dict(zip(col_name,value_list))

                if 'time' not in dict_cols_vals:
                    dict_cols_vals['time'] = None;
                if 'maxstud' not in dict_cols_vals:
                    dict_cols_vals['maxstud'] = None;

                primary_key_string = key_value_list[0] + "," + key_value_list[1] + "," + key_value_list[2] + "," + key_value_list[3]
                if primary_key_string not in btree:
                    new_dict_container = {key_col_name[0]: key_value_list[0], key_col_name[1]: key_value_list[1], key_col_name[2]: key_value_list[2], key_col_name[3]: key_value_list[3]}
                    new_dict_container.update(dict_cols_vals)
                    btree.update({primary_key_string: new_dict_container})
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

            if ("semester" not in col_name) or ("acadyear" not in col_name) or ("cno" not in col_name) or ("section" not in col_name):
                print("No primary key")
            else:
                key_index = ['','','','']
                key_col_name = ['','','','']
                key_value_list = ['','','','']

                key_index[0] = col_name.index("semester")
                key_col_name[0] = col_name.pop(key_index[0])
                key_value_list[0] = value_list.pop(key_index[0])

                key_index[1] = col_name.index("acadyear")
                key_col_name[1] = col_name.pop(key_index[1])
                key_value_list[1] = value_list.pop(key_index[1])

                key_index[2] = col_name.index("cno")
                key_col_name[2] = col_name.pop(key_index[2])
                key_value_list[2] = value_list.pop(key_index[2])

                key_index[3] = col_name.index("section")
                key_col_name[3] = col_name.pop(key_index[3])
                key_value_list[3] = value_list.pop(key_index[3])

                dict_cols_vals = dict(zip(col_name,value_list))

                if 'time' not in dict_cols_vals:
                    dict_cols_vals['time'] = None;
                if 'maxstud' not in dict_cols_vals:
                    dict_cols_vals['maxstud'] = None;

                primary_key_string = key_value_list[0] + "," + key_value_list[1] + "," + key_value_list[2] + "," + key_value_list[3]

                if primary_key_string not in btree:
                    new_dict_container = {key_col_name[0]: key_value_list[0], key_col_name[1]: key_value_list[1], key_col_name[2]: key_value_list[2], key_col_name[3]: key_value_list[3]}
                    new_dict_container.update(dict_cols_vals)
                    btree.update({primary_key_string: new_dict_container})
                else:
                    print("Already in BTree")

    elif table_selected == 'studcourse':
        if value_list_bool and not column_name_bool: #first case input
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
                if len(value_list) == 4:
                    print("value list length is 4")
                    btreelen = str(len(btree) + 1)
                    btree.update({btreelen + "": {cols[0]: value_list[0], cols[1]: value_list[1], cols[2]: value_list[2], cols[3]: value_list[3]}})
                else:
                    print("Column values are lacking")

        elif value_list_bool and column_name_bool: #second case input
            col_name = col_name.replace(" ", "")
            value_list = value_list.split(',')
            for i in range(0, len(value_list)):
                value_list[i] = value_list[i].rstrip('\'')
                value_list[i] = value_list[i].lstrip('\'')
            col_name = col_name.split(',')
            dict_cols_vals = dict(zip(col_name,value_list))

            if 'studno' not in dict_cols_vals:
                    dict_cols_vals['studno'] = None;
            if 'cno' not in dict_cols_vals:
                    dict_cols_vals['cno'] = None;
            if 'semester' not in dict_cols_vals:
                    dict_cols_vals['semester'] = None;
            if 'acadyear' not in dict_cols_vals:
                    dict_cols_vals['acadyear'] = None;


            btree.update({str(len(btree) + 1): dict_cols_vals})

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

            dict_cols_vals = dict(zip(col_name,value_list))

            if 'studno' not in dict_cols_vals:
                    dict_cols_vals['studno'] = None;
            if 'cno' not in dict_cols_vals:
                    dict_cols_vals['cno'] = None;
            if 'semester' not in dict_cols_vals:
                    dict_cols_vals['semester'] = None;
            if 'acadyear' not in dict_cols_vals:
                    dict_cols_vals['acadyear'] = None;


            btree.update({str(len(btree) + 1): dict_cols_vals})


print(list(btree))
#print(btree["2012-29339"])
'''
elif operation == 'select':
    select = 'studentname,birthday,studno'
    
    for j, k in zip(btree.keys(), btree.values()):
        if select == '*':
            print(j + " ", end="")
            print(k['studentname'] + " ", end="")
            print(k['birthday'] + " ", end="")
            print(k['degree'] + " ", end="")
            print(k['major'] + " ", end="")
            print(k['unitsearned'] + " ", end="")
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
    '''
    
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
'''
#for courseoffering
        select = "*"
        for j, k in zip(btree.keys().split(','), btree.values()):
            if select == '*':
                print(j[0] + " ", end="")
                print(j[1] + " ", end="")
                print(j[2] + " ", end="")
                print(j[3] + " ", end="")
                #print(k['semester'] + " ", end="")
                #print(k['acadyear'] + " ", end="")
                #print(k['cno'] + " ", end="")
                #print(k['section'] + " ", end="")
                print(k['time'] + " ", end="")
                print(k['maxstud'] + " ", end="")
                print("")
            else:
                select_query = select.split(',')
                for item in select_query:
                    print(k[item] + " ", end="")
                print("")
'''
'''
#for studcourse
    for j, k in zip(btree.keys(), btree.values()):
        if select == '*':
            print(k['studno'] + " ", end="")
            print(k['cno'] + " ", end="")
            print(k['semester'] + " ", end="")
            print(k['acadyear'] + " ", end="")
            print("")
        else:
            select_query = select.split(',')
            for item in select_query:
                print(k[item] + " ", end="")
            print("")
'''