from BTrees.OOBTree import OOBTree
import re

class TableBTree:

    def __init__(self, tablename, tablespecs):
        self.tablename = tablename
        self.primarykey = []
        self.columns = []
        self.tablespecs = tablespecs
        self.data = OOBTree()
        self.counter = 0

        # print("Initialize "+tablename)
        self.loadData()
        # print("tablespecs")
        # print(tablespecs)
        # self.printData()

    def loadData(self):
        # print("Loading data of "+self.tablename+" table.")
        tabledata = open("data/"+self.tablename+".dat", "r")
        counter = 0
        cols = []
        datatypes = []
        # Read data on <tablename>.dat

        for line in tabledata:
            if(counter == 0):       # column names
                nonewline = line.rstrip('\n')
                column = nonewline.split(",")
                for i in range(0,len(column)):
                    name = column[i].split(" ")
                    cols.append(name[0])
                    self.columns.append(name[0])
                    datatypes.append(name[1])
                counter = counter + 1

            elif(counter == 1):     # primary key/s
                nonewline = line.rstrip('\n')
                if(nonewline == ""):    # table has no primary key
                    self.counter = 0
                else:                   # table has one or more primary keys
                    keyset = nonewline.split(",")
                    for i in range(0,len(keyset)):
                        if i != '':
                            self.primarykey.append(keyset[i])

                    # print(keyset)
                counter = counter + 1
            else:
                nonewline = line.rstrip('\n')
                data = nonewline.split("^")
                value = {}
                for i in range(0, len(data)):
                    # print("data: "+data[i])
                    # data[i] = data[i].rstrip('\'')
                    # data[i] = data[i].lstrip('\'')
                    value[cols[i]] = data[i]
                if(len(self.primarykey) == 0):
                    self.data.update({self.counter: value})
                    self.counter = self.counter + 1
                else:
                    # create a list out of the primary keys then use as key
                    key = ""
                    for i in range(0, len(self.primarykey)):
                        if(i>0): key = key+","+str(value[self.primarykey[i]])
                        else: key = str(value[self.primarykey[i]])
                    self.data.update({key: value})
                    # print(key)
                    # print(value)
        tabledata.close()

    def printData(self):
        for i in self.data.keys():
            # print(str(i))
            # print(self.data[i])
            return

    def insert(self, value_list_bool, column_name_bool, value_list, col_name, assignment_list):


        error1 = None
        birthday_pattern = re.compile("^'\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])'$")
        studno_pattern = re.compile("^'\d{4}-\d{5}'$")
        time_pattern = re.compile("^'([0-1]?[0-9]|2[0-3]):[0-5][0-9]-([0-1]?[0-9]|2[0-3]):[0-5][0-9]'$")
        sem_pattern = re.compile("'((1st)|(2nd)|(Sum))'")

        if self.tablename == 'student':
            if value_list_bool and not column_name_bool: #first case input
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][12:]
                    print("-"+value_list[i]+"-")
                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if not birthday_pattern.match(value_list[2]):
                    print("Birthday format isn't correct")
                    error1 = "Birthday format isn't correct"
                if not studno_pattern.match(value_list[0]):
                    print("Student number format isn't correct")
                    error1 = "Student number format isn't correct"
                if not value_list[5].isdigit():
                    print("Units earned format isn't correct")
                    error1 = "Units earned format isn't correct"

                if value_list[0] not in self.data and not error1:
                    if len(value_list) == 6:
                        self.data.update({value_list[0]: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4], self.columns[5]: value_list[5]}})
                    else:
                        print("Column values are lacking")
                        error1 = "Column values are lacking"
                elif error1:
                    print("Input is wrong")
                else:
                    print("Already in BTree")
                    error1 = "Already in BTree"

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.lower().replace(" ", "")
                #value_list = value_list.split(' , ')
                #value_list = re.split(" , ",value_list)
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][12:]
                    print(value_list[i])

                key_index = col_name.index("studno")
                #value_list[key_index] = "'" + value_list[key_index].split("'")[1] + "'"

                if not studno_pattern.match(value_list[key_index]):
                    print("Student number format isn't correct")
                    error1 = "Student number format isn't correct"

                col_name = col_name.split(',')
                if "studno" not in col_name:
                    print("No primary key")
                    error1 = "No primary key"
                else:
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'studentname' not in dict_cols_vals:
                        dict_cols_vals['studentname'] = "NULL";
                    if 'birthday' not in dict_cols_vals:
                        dict_cols_vals['birthday'] = "NULL";
                    else:
                        if not birthday_pattern.match(value_list[col_name.index("birthday")]):
                            print("Birthday format isn't correct")
                            error1 = "Birthday format isn't correct"
                    if 'degree' not in dict_cols_vals:
                        dict_cols_vals['degree'] = "NULL";
                    if 'major' not in dict_cols_vals:
                        dict_cols_vals['major'] = "NULL";
                    if 'unitsearned' not in dict_cols_vals:
                        dict_cols_vals['unitsearned'] = "NULL";
                    else:
                        if not value_list[col_name.index("unitsearned")].isdigit():
                            print("Units earned format isn't correct")
                            error1 = "Units earned format isn't correct"

                    if key_value_list not in self.data and not error1:
                        self.data.update({key_value_list: dict_cols_vals})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(' , ')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    if i == 0:
                        split_list[0] = split_list[0][12:]

                    col_ext = split_list[0].lower().replace(" ","")
                    val_ext = split_list[1][1:]
                    if i == len(assignment_list) - 1:
                        val_ext = val_ext[:-1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    print(col_ext + "-" + val_ext + "-")
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if "studno" not in col_name:
                    print("No primary key")
                    error1 = "No primary key"
                else:
                    key_index = col_name.index("studno")
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if not studno_pattern.match(dict_cols_vals['studno']):
                        print("Student number format isn't correct")
                        error1 = "Student number format isn't correct"


                    if 'studentname' not in dict_cols_vals:
                        dict_cols_vals['studentname'] = "NULL";
                    if 'birthday' not in dict_cols_vals:
                        dict_cols_vals['birthday'] = "NULL";
                    else:
                        if not birthday_pattern.match(dict_cols_vals['birthday']):
                            print("Birthday format isn't correct")
                            error1 = True
                    if 'degree' not in dict_cols_vals:
                        dict_cols_vals['degree'] = "NULL";
                    if 'major' not in dict_cols_vals:
                        dict_cols_vals['major'] = "NULL";
                    if 'unitsearned' not in dict_cols_vals:
                        dict_cols_vals['unitsearned'] = "NULL";
                    else:
                        if not dict_cols_vals['unitsearned'].isdigit():
                            print("Units earned format isn't correct")
                            error1 = "Units earned format isn't correct"


                    if key_value_list not in self.data and not error1:
                        self.data.update({key_value_list: dict_cols_vals})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

        elif self.tablename == 'studenthistory':
            if value_list_bool and not column_name_bool: #first case input
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][10:]
                    print("-"+value_list[i]+"-")
                #key_index = col_name.index("studno")
                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if not studno_pattern.match(value_list[0]):
                    print("Student number format isn't correct")
                    error1 = "Student number format isn't correct"

                if value_list[0] not in self.data and not error1:
                    if len(value_list) == 5:
                        self.data.update({value_list[0]: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4]}})
                    else:
                        print("Column values are lacking")
                        error1 = "Column values are lacking"
                elif error1:
                    print("Input is wrong")
                else:
                    print("Already in BTree")
                    error1 = "Already in BTree"

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.lower().replace(" ", "")
                #value_list = (value_list + " ").split(',')
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][10:]
                    print(value_list[i])

                key_index = col_name.index("studno")
                #value_list[key_index] = "'" + value_list[key_index].split("'")[1] + "'"
                col_name = col_name.split(',')

                if not studno_pattern.match(value_list[key_index]):
                    print("Student number format isn't correct")
                    error1 = "Student number format isn't correct"

                if "studno" not in col_name:
                    print("No primary key")
                    error1 = "No primary key"
                else:
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'description' not in dict_cols_vals:
                        dict_cols_vals['description'] = "NULL";
                    if 'action' not in dict_cols_vals:
                        dict_cols_vals['action'] = "NULL";
                    if 'datefiled' not in dict_cols_vals:
                        dict_cols_vals['datefiled'] = "NULL";
                    if 'dateresolved' not in dict_cols_vals:
                        dict_cols_vals['dateresolved'] = "NULL";

                    if key_value_list not in self.data and not error1:
                        self.data.update({key_value_list: dict_cols_vals})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(' , ')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    if i == 0:
                        split_list[0] = split_list[0][10:]

                    col_ext = split_list[0].lower().replace(" ","")
                    val_ext = split_list[1][1:]
                    if i == len(assignment_list) - 1:
                        val_ext = val_ext[:-1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    print(col_ext + "-" + val_ext + "-")
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if "studno" not in col_name:
                    print("No primary key")
                    error1 = "No primary key"
                else:
                    key_index = col_name.index("studno")
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if not studno_pattern.match(dict_cols_vals['studno']):
                        print("Student number format isn't correct")
                        error1 = "Student number format isn't correct"

                    if 'description' not in dict_cols_vals:
                        dict_cols_vals['description'] = "NULL";
                    if 'action' not in dict_cols_vals:
                        dict_cols_vals['action'] = "NULL";
                    if 'datefiled' not in dict_cols_vals:
                        dict_cols_vals['datefiled'] = "NULL";
                    if 'dateresolved' not in dict_cols_vals:
                        dict_cols_vals['dateresolved'] = "NULL";

                    if key_value_list not in self.data and not error1:
                        self.data.update({key_value_list: dict_cols_vals})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

        elif self.tablename == 'course':
            if value_list_bool and not column_name_bool: #first case input
                #value_list = (value_list + " ").split(' , ')
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][12:]
                    print("-"+value_list[i]+"-")
                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"

                if not value_list[3].isdigit():
                    print("NoOfUnits format isn't correct")
                    error1 = "NoOfUnits format isn't correct"
                if not value_list[4].isdigit():
                    print("HasLab format isn't correct")
                    error1 = "HasLab format isn't correct"
                if not sem_pattern.match(value_list[5]):
                    print("SemOffered format isn't correct")
                    error1 = "SemOffered format isn't correct"

                if value_list[0] not in self.data and not error1:
                    if len(value_list) == 6:
                        self.data.update({value_list[0]: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4], self.columns[5]: value_list[5]}})
                    else:
                        print("Column values are lacking")
                        error1 = "Column values are lacking"
                elif error1:
                    print("Input is wrong")
                else:
                    print("Already in BTree")
                    error1 = "Already in BTree"

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.lower().replace(" ", "")
                #value_list = (value_list + "  ").split(',')
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][12:]

                key_index = col_name.index("cno")
                #value_list[key_index] = "'" + value_list[key_index].split("'")[1] + "'"
                col_name = col_name.split(',')
                if "cno" not in col_name:
                    print("No primary key")
                    error1 = "No primary key"
                else:
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'ctitle' not in dict_cols_vals:
                        dict_cols_vals['ctitle'] = "NULL";
                    if 'cdesc' not in dict_cols_vals:
                        dict_cols_vals['cdesc'] = "NULL";
                    if 'noofunits' not in dict_cols_vals:
                        dict_cols_vals['noofunits'] = "NULL";
                    else:
                        if not value_list[col_name.index("noofunits")].isdigit():
                            print("NoOfUnits format isn't correct")
                            error1 = "NoOfUnits format isn't correct"
                    if 'haslab' not in dict_cols_vals:
                        dict_cols_vals['haslab'] = "NULL";
                    else:
                        if not value_list[col_name.index("haslab")].isdigit():
                            print("HasLab format isn't correct")
                            error1 = "HasLab format isn't correct"
                    if 'semoffered' not in dict_cols_vals:
                        dict_cols_vals['semoffered'] = "NULL";
                    else:
                        if not sem_pattern.match(dict_cols_vals['semoffered']):
                            print("SemOffered format isn't correct")
                            error1 = "SemOffered format isn't correct"

                    if key_value_list not in self.data and not error1:
                        self.data.update({key_value_list: dict_cols_vals})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(' , ')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    if i == 0:
                        split_list[0] = split_list[0][12:]

                    col_ext = split_list[0].lower().replace(" ","")
                    val_ext = split_list[1][1:]
                    if i == len(assignment_list) - 1:
                        val_ext = val_ext[:-1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    print(col_ext + "-" + val_ext + "-")
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if "cno" not in col_name:
                    print("No primary key")
                    error1 = "No primary key"
                else:
                    key_index = col_name.index("cno")
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'ctitle' not in dict_cols_vals:
                        dict_cols_vals['ctitle'] = "NULL";
                    if 'cdesc' not in dict_cols_vals:
                        dict_cols_vals['cdesc'] = "NULL";
                    if 'noofunits' not in dict_cols_vals:
                        dict_cols_vals['noofunits'] = "NULL";
                    else:
                        if not dict_cols_vals['noofunits'].isdigit():
                            print(dict_cols_vals['noofunits'])
                            print("NoOfUnits format isn't correct")
                            error1 = "NoOfUnits format isn't correct"
                    if 'haslab' not in dict_cols_vals:
                        dict_cols_vals['haslab'] = "NULL";
                    else:
                        if not dict_cols_vals['haslab'].isdigit():
                            print(dict_cols_vals['haslab'])
                            print("HasLab format isn't correct")
                            error1 = "HasLab format isn't correct"
                    if 'semoffered' not in dict_cols_vals:
                        dict_cols_vals['semoffered'] = "NULL";
                    else:
                        if not sem_pattern.match(dict_cols_vals['semoffered']):
                            print("SemOffered format isn't correct")
                            error1 = "SemOffered format isn't correct"

                    if key_value_list not in self.data and not error1:
                        self.data.update({key_value_list: dict_cols_vals})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

        elif self.tablename == 'courseoffering':
            if value_list_bool and not column_name_bool: #first case input
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][12:]
                    print("-"+value_list[i]+"-")
                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"


                if not sem_pattern.match(value_list[0]):
                    print("Semester format isn't correct")
                    error1 = "Semester format isn't correct"
                if not time_pattern.match(value_list[4]):
                    print("Time format isn't correct")
                    error1 = "Time format isn't correct"
                if not value_list[5].isdigit():
                    print("MaxStud format isn't correct")
                    error1 = "MaxStud format isn't correct"

                print(value_list[0:4])
                if (value_list[0:4]) not in self.data.keys() and not error1:
                    if len(value_list) == 6:
                        str123 = ",".join(value_list[0:4])
                        self.data.update({",".join(value_list[0:4]): {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4], self.columns[5]: value_list[5]}})
                    else:
                        print("Column values are lacking")
                        error1 = "Column values are lacking"
                elif error1:
                    print("Input is wrong")
                else:
                    print("Already in BTree")
                    error1 = "Already in BTree"

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.lower().replace(" ", "")
                #value_list = value_list.split(',')

                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][12:]
                    print(value_list[i])
                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                col_name = col_name.split(',')

                if ("semester" not in col_name) or ("acadyear" not in col_name) or ("cno" not in col_name) or ("section" not in col_name):
                    print("No primary key/s")
                    error1 = "No primary key/s"
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

                    if not sem_pattern.match(key_value_list[0]):
                        print("Semester format isn't correct")
                        error1 = "Semester format isn't correct"

                    if 'time' not in dict_cols_vals:
                        dict_cols_vals['time'] = "NULL";
                    else:
                        if not time_pattern.match(dict_cols_vals['time']):
                            print("Time format isn't correct")
                            error1 = "Time format isn't correct"
                    if 'maxstud' not in dict_cols_vals:
                        dict_cols_vals['maxstud'] = "NULL";
                    else:
                        if not dict_cols_vals['maxstud'].isdigit():
                            print("MaxStud format isn't correct")
                            error1 = "MaxStud format isn't correct"

                    primary_key_string = key_value_list[0] + "," + key_value_list[1] + "," + key_value_list[2] + "," + key_value_list[3]
                    if primary_key_string not in self.data and not error1:
                        new_dict_container = {key_col_name[0]: key_value_list[0], key_col_name[1]: key_value_list[1], key_col_name[2]: key_value_list[2], key_col_name[3]: key_value_list[3]}
                        new_dict_container.update(dict_cols_vals)
                        self.data.update({primary_key_string: new_dict_container})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(',')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    col_ext = split_list[0].lower().replace(" ","")
                    val_ext = split_list[1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    else:
                        val_ext = split_list[1][1:-1]
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if ("semester" not in col_name) or ("acadyear" not in col_name) or ("cno" not in col_name) or ("section" not in col_name):
                    print("No primary key")
                    error1 = "No primary key"
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

                    if not sem_pattern.match(key_value_list[0]):
                        print("Semester format isn't correct")
                        error1 = "Semester format isn't correct"

                    if 'time' not in dict_cols_vals:
                        dict_cols_vals['time'] = "NULL";
                    else:
                        if not time_pattern.match(dict_cols_vals['time']):
                            print("Time format isn't correct")
                            error1 = "Time format isn't correct"
                    if 'maxstud' not in dict_cols_vals:
                        dict_cols_vals['maxstud'] = "NULL";
                    else:
                        if not dict_cols_vals['maxstud'].isdigit():
                            print("MaxStud format isn't correct")
                            error1 = "MaxStud format isn't correct"

                    primary_key_string = key_value_list[0] + "," + key_value_list[1] + "," + key_value_list[2] + "," + key_value_list[3]

                    if primary_key_string not in self.data and not error1:
                        new_dict_container = {key_col_name[0]: key_value_list[0], key_col_name[1]: key_value_list[1], key_col_name[2]: key_value_list[2], key_col_name[3]: key_value_list[3]}
                        new_dict_container.update(dict_cols_vals)
                        self.data.update({primary_key_string: new_dict_container})
                    elif error1:
                        print("Input is wrong")
                    else:
                        print("Already in BTree")
                        error1 = "Already in BTree"

        elif self.tablename == 'studcourse':
            if value_list_bool and not column_name_bool: #first case input
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][8:]
                    print("-"+value_list[i]+"-")

                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if not studno_pattern.match(value_list[0]):
                    print("Student number format isn't correct")
                    error1 = "Student number format isn't correct"
                if not sem_pattern.match(value_list[2]):
                    print("Semester format isn't correct")
                    error1 = "Semester format isn't correct"

                if len(value_list) == 4 and not error1:
                    #btreelen = self.counter + 1
                    #print(btreelen + "-btreelen")
                    #for k in self.data.keys():
                    #print(k + "-dsa")
                    self.data.update({self.counter: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3]}})
                    self.counter = self.counter + 1
                elif error1:
                    print("Input is wrong")
                else:
                    print("Column values are lacking")
                    error1 = "Column values are lacking"



            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.lower().replace(" ", "")
                value_list = re.split(" , ",value_list)
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    elif i == 0:
                        value_list[i] = value_list[i][8:]
                    print(value_list[i])
                col_name = col_name.split(',')
                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                dict_cols_vals = dict(zip(col_name,value_list))


                if 'studno' not in dict_cols_vals:
                        dict_cols_vals['studno'] = "NULL";
                else:
                    if not studno_pattern.match(dict_cols_vals['studno']):
                        print("Student number format isn't correct")
                        error1 = "Student number format isn't correct"
                if 'cno' not in dict_cols_vals:
                        dict_cols_vals['cno'] = "NULL";
                if 'semester' not in dict_cols_vals:
                        dict_cols_vals['semester'] = "NULL";
                else:
                    if not sem_pattern.match(dict_cols_vals['semester']):
                        print("Semester format isn't correct")
                        error1 = "Semester format isn't correct"
                if 'acadyear' not in dict_cols_vals:
                        dict_cols_vals['acadyear'] = "NULL";

                if not error1:
                    self.data.update({self.counter: dict_cols_vals})
                    self.counter = self.counter + 1
                else:
                    print("Input is wrong")

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(' , ')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    if i == 0:
                        split_list[0] = split_list[0][8:]

                    col_ext = split_list[0].lower().replace(" ","")
                    val_ext = split_list[1][1:]
                    if i == len(assignment_list) - 1:
                        val_ext = val_ext[:-1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    print(col_ext + "-" + val_ext + "-")
                    col_name.append(col_ext)
                    value_list.append(val_ext)


                #value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                dict_cols_vals = dict(zip(col_name,value_list))

                if 'studno' not in dict_cols_vals:
                        dict_cols_vals['studno'] = "NULL";
                else:
                    if not studno_pattern.match(dict_cols_vals['studno']):
                        print("Student number format isn't correct")
                        error1 = "Student number format isn't correct"
                if 'cno' not in dict_cols_vals:
                        dict_cols_vals['cno'] = "NULL";
                if 'semester' not in dict_cols_vals:
                        dict_cols_vals['semester'] = "NULL";
                else:
                    if not sem_pattern.match(dict_cols_vals['semester']):
                        print("Semester format isn't correct")
                        error1 = "Semester format isn't correct"
                if 'acadyear' not in dict_cols_vals:
                        dict_cols_vals['acadyear'] = "NULL";

                if not error1:
                    self.data.update({self.counter + 1: dict_cols_vals})
                    self.counter = self.counter + 1
                else:
                    print("Input is wrong")
        if error1 is None:
            self.saveToFile()
        return error1

    def select(self, columns, withcondition, condition, col_name, comp_operator, cond_exp):
        retdata = []
        cols = []
        row = []
        where_column = False

        print("SELECT OPERATION ON "+self.tablename)
        print("Condition:  ", condition)

        if col_name is not None:
            where_column = True

        if condition and where_column:
            print("colname:'"+col_name+"'")
            print("comp_operator:'"+comp_operator+"'")
            print("cond_exp:'"+str(cond_exp)+"'")
        if columns[0] == "*":
            for i in self.columns:
                cols.append(i)
            retdata.append(cols)

            for j in self.data:
                row = []
                if withcondition and where_column:#If True lang, print all pa din
                    if isinstance(cond_exp,str):
                        print(self.data[j][col_name] + " = " + cond_exp)
                        if(self.data[j][col_name] == cond_exp):  #just to lowercase until input is normalized
                        # if(str.lower(self.data[j][col_name]) == cond_exp):  #just to lowercase until input is normalized
                            for i in self.columns:
                                print(self.data[j][i])
                                row.append(self.data[j][i])
                            retdata.append(row)
                    else:
                        if comp_operator == '=':
                            if float(self.data[j][col_name]) == float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '>=':
                            if float(self.data[j][col_name]) >= float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '>':
                            if float(self.data[j][col_name]) > float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '<':
                            if float(self.data[j][col_name]) < float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '<=':
                            if float(self.data[j][col_name]) <= float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '!=':
                            if float(self.data[j][col_name]) != float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '<>':
                            if float(self.data[j][col_name]) != float(cond_exp):
                                for i in self.columns:
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                else:
                    for i in self.columns:
                        print(self.data[j][i])
                        row.append(self.data[j][i])
                    retdata.append(row)

        else:
            #print(columns)

            for i in columns:
                cols.append(i)
                # print(i)
            retdata.append(cols)

            for j in self.data:
                row = []
                if withcondition and where_column:
                    if isinstance(cond_exp,str):
                            print(self.data[j][col_name] + " = " + cond_exp)
                            if(self.data[j][col_name] == cond_exp):  #just to lowercase until input is normalized
                            # if(str.lower(self.data[j][col_name]) == cond_exp):  #just to lowercase until input is normalized
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                    else:
                        if comp_operator == '=':
                            if float(self.data[j][col_name]) == float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '>=':
                            if float(self.data[j][col_name]) >= float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '>':
                            if float(self.data[j][col_name]) > float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '<':
                            if float(self.data[j][col_name]) < float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '<=':
                            if float(self.data[j][col_name]) <= float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '!=':
                            if float(self.data[j][col_name]) != float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                        elif comp_operator == '<>':
                            if float(self.data[j][col_name]) != float(cond_exp):
                                for i in columns:
                                    i = i.strip(" ")
                                    print(self.data[j][i])
                                    row.append(self.data[j][i])
                                retdata.append(row)
                else:
                    for i in columns:
                        i = i.strip(" ")
                        print(self.data[j][i])
                        row.append(self.data[j][i])
                    retdata.append(row)
        return retdata

    def delete(self, columns, withCond, selCol, compOp, condExp):
        retdata = []
        colNames = []
        row = []

        # append column names
        for col in self.columns:
            colNames.append(col)
        retdata.append(colNames)

        # delete with condition
        if withCond:
            for key in list(self.data.keys()):                                          # search value in btrees
                dataValue = self.data[key][selCol]
                if isinstance(condExp, str):                                            # if value is a string
                    dataValue = str(dataValue).lower()
                    condExp = condExp.lower()
                    if (compOp == 'like' and dataValue == condExp):                     # delete like
                        self.data.pop(key)
                    elif (compOp == 'not like' and dataValue != condExp):
                        self.data.pop(key)
                else: 
                    dataValue = float(dataValue)                                        # if value is an integer 
                    condExp = float(condExp)
                    if (compOp == '<' and dataValue < condExp):                         # delete less than
                        self.data.pop(key)
                    elif (compOp == '>' and dataValue > condExp):                       # delete greater than
                        self.data.pop(key)
                    elif (compOp == '<=' and dataValue <= condExp):                     # delete less than or equal
                        self.data.pop(key)
                    elif (compOp == '>=' and dataValue >= condExp):                     # delete greather than or equal
                        self.data.pop(key)
                if (compOp == '=' and dataValue == condExp):                            # delete equal
                    self.data.pop(key)
                if ((compOp == '!=' or compOp == '<>') and dataValue != condExp):       # delete not equal
                    self.data.pop(key)
                if (compOp == 'is null' and dataValue == 'null'):                       # delete equal null
                    self.data.pop(key)                                                  
                if (compOp == 'not null' and dataValue != 'null'):                      # delete not equal null
                    self.data.pop(key)                    
                    

        # delete all
        else:
            self.data.clear()

        # append row values
        for key in self.data:
            for col in columns:
                col = col.strip(" ")
                row.append(self.data.values(key)[key][col])
            retdata.append(row)

        self.saveToFile()
        return retdata

    # def insertData(self):

    # this function overwrites the contents of the destination file
    def saveToFile(self):
        print("Writing data of "+self.tablename+" table.")
        tabledata = open("data/"+self.tablename+".dat", "w")
        # print("Writing data of "+self.tablename+" table.")
        # tabledata = open("data/"+self.tablename+"save.dat", "w")

        out = ""
        for i in range(0, len(self.columns)):
            if(i == 0): out = self.columns[i] + " " + self.tablespecs[self.columns[i]]
            else: out = out + "," + self.columns[i] + " " + self.tablespecs[self.columns[i]]
        tabledata.write(out)
        tabledata.write("\n")

        out = ""
        for i in range(0, len(self.primarykey)):
            if(i == 0): out = self.primarykey[i]
            else: out = out + "," + self.primarykey[i]
        tabledata.write(out)
        tabledata.write("\n")

        keys = self.data.keys()
        for i in range(0, len(keys)):               # keys - primary keys of the data
            out = ""                                # for each row in the table
            for j in range(0, len(self.columns)):   # self.columns is an array
                if(j == 0): out = str(self.data[keys[i]][self.columns[j]])
                else: out = out + "^" + str(self.data[keys[i]][self.columns[j]])
            tabledata.write(out)
            tabledata.write("\n")

        tabledata.close()
