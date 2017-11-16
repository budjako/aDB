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
        error1 = False
        

        if self.tablename == 'student':
            if value_list_bool and not column_name_bool: #first case input
                value_list = value_list.split(',')
                for i in range(0, len(value_list)):
                    value_list[i] = value_list[i].rstrip('\'')
                    value_list[i] = value_list[i].lstrip('\'')
                    value_list[i] = value_list[i][1:]
                    if re.search("'null'",value_list[i]):
                        value_list[i] = "NULL"
                    if not value_list[i].isdigit() and not value_list[i] == "NULL":
                        value_list[i] = value_list[i][:-1]
                #key_index = col_name.index("studno")
                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if value_list[0] not in self.data:
                    if len(value_list) == 6:
                        self.data.update({value_list[0]: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4], self.columns[5]: value_list[5]}})
                    else:
                        print("Column values are lacking")
                        error1 = True
                else:
                    print("Already in BTree")
                    error1 = True

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.replace(" ", "")
                value_list = value_list.split(',')
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    else:
                        value_list[i] = value_list[i].rstrip('\'')
                        value_list[i] = value_list[i].lstrip('\'')
            
                        value_list[i] = value_list[i][1:]

                    if not value_list[i].isdigit() and value_list[i] != "NULL":
                        value_list[i] = value_list[i][:-1]
                    print(value_list[i])
                    
                key_index = col_name.index("studno")
                value_list[key_index] = "'" + value_list[key_index].split("'")[1] + "'"
                col_name = col_name.split(',')
                if "studno" not in col_name:
                    print("No primary key")
                    error1 = True
                else:
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'studentname' not in dict_cols_vals:
                        dict_cols_vals['studentname'] = "NULL";
                    if 'birthday' not in dict_cols_vals:
                        dict_cols_vals['birthday'] = "NULL";
                    if 'degree' not in dict_cols_vals:
                        dict_cols_vals['degree'] = "NULL";
                    if 'major' not in dict_cols_vals:
                        dict_cols_vals['major'] = "NULL";
                    if 'unitsearned' not in dict_cols_vals:
                        dict_cols_vals['unitsearned'] = "NULL";

                    if key_value_list not in self.data:
                        self.data.update({key_value_list: dict_cols_vals})
                    else:
                        print("Already in BTree")
                        error1 = True

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(',')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    col_ext = split_list[0].replace(" ","")
                    val_ext = split_list[1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    else:
                        val_ext = split_list[1][1:-1]
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if "studno" not in col_name:
                    print("No primary key")
                    error1 = True
                else:
                    key_index = col_name.index("studno")
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'studentname' not in dict_cols_vals:
                        dict_cols_vals['studentname'] = "NULL";
                    if 'birthday' not in dict_cols_vals:
                        dict_cols_vals['birthday'] = "NULL";
                    if 'degree' not in dict_cols_vals:
                        dict_cols_vals['degree'] = "NULL";
                    if 'major' not in dict_cols_vals:
                        dict_cols_vals['major'] = "NULL";
                    if 'unitsearned' not in dict_cols_vals:
                        dict_cols_vals['unitsearned'] = "NULL";


                    if key_value_list not in self.data:
                        self.data.update({key_value_list: dict_cols_vals})
                    else:
                        print("Already in BTree")
                        error1 = True

        elif self.tablename == 'studenthistory':
            if value_list_bool and not column_name_bool: #first case input
                value_list = (value_list + " ").split(',')
                for i in range(0, len(value_list)):
                    value_list[i] = value_list[i].rstrip('\'')
                    value_list[i] = value_list[i].lstrip('\'')
                    value_list[i] = value_list[i][1:]
                    if re.search("'null'",value_list[i]):
                        value_list[i] = "NULL"
                    if not value_list[i].isdigit() and value_list[i] == "NULL":
                        value_list[i] = value_list[i][:-1]
                #key_index = col_name.index("studno")
                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if value_list[0] not in self.data:
                    if len(value_list) == 5:
                        self.data.update({value_list[0]: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4]}})
                    else:
                        print("Column values are lacking")
                        error1 = True
                else:
                    print("Already in BTree")
                    error1 = True

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.replace(" ", "")
                value_list = (value_list + " ").split(',')
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    else:
                        value_list[i] = value_list[i].rstrip('\'')
                        value_list[i] = value_list[i].lstrip('\'')

                        value_list[i] = value_list[i][1:]

                    if not value_list[i].isdigit() and value_list[i] != "NULL":
                        value_list[i] = value_list[i][:-1]
                    print(value_list[i])

                key_index = col_name.index("studno")
                value_list[key_index] = "'" + value_list[key_index].split("'")[1] + "'"
                col_name = col_name.split(',')
                if "studno" not in col_name:
                    print("No primary key")
                    error1 = True
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

                    if key_value_list not in self.data:
                        self.data.update({key_value_list: dict_cols_vals})
                    else:
                        print("Already in BTree")
                        error1 = True

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(',')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    col_ext = split_list[0].replace(" ","")
                    val_ext = split_list[1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    else:
                        val_ext = split_list[1][1:-1]
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if "studno" not in col_name:
                    print("No primary key")
                    error1 = True
                else:
                    key_index = col_name.index("studno")
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

                    if key_value_list not in self.data:
                        self.data.update({key_value_list: dict_cols_vals})
                    else:
                        print("Already in BTree")
                        error1 = True

        elif self.tablename == 'course':
            if value_list_bool and not column_name_bool: #first case input
                value_list = (value_list + " ").split(',')
                for i in range(0, len(value_list)):
                    value_list[i] = value_list[i].rstrip('\'')
                    value_list[i] = value_list[i].lstrip('\'')
                    value_list[i] = value_list[i][1:]
                    if re.search("'null'",value_list[i]):
                        value_list[i] = "NULL"
                    if not value_list[i].isdigit() and value_list[i] == "NULL":
                        value_list[i] = value_list[i][:-1]
                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if value_list[0] not in self.data:
                    if len(value_list) == 6:
                        self.data.update({value_list[0]: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4], self.columns[5]: value_list[5]}})
                    else:
                        print("Column values are lacking")
                        error1 = True
                else:
                    print("Already in BTree")
                    error1 = True

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.replace(" ", "")
                value_list = (value_list + "  ").split(',')
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    else:
                        value_list[i] = value_list[i].rstrip('\'')
                        value_list[i] = value_list[i].lstrip('\'')
            
                        value_list[i] = value_list[i][1:]

                    if not value_list[i].isdigit() and value_list[i] != "NULL":
                        value_list[i] = value_list[i][:-1]
                    print(value_list[i])
                key_index = col_name.index("cno")
                value_list[key_index] = "'" + value_list[key_index].split("'")[1] + "'"
                col_name = col_name.split(',')
                if "cno" not in col_name:
                    print("No primary key")
                    error1 = True
                else:
                    key_value_list = value_list[key_index]
                    dict_cols_vals = dict(zip(col_name,value_list))

                    if 'ctitle' not in dict_cols_vals:
                        dict_cols_vals['ctitle'] = "NULL";
                    if 'cdesc' not in dict_cols_vals:
                        dict_cols_vals['cdesc'] = "NULL";
                    if 'noofunits' not in dict_cols_vals:
                        dict_cols_vals['noofunits'] = "NULL";
                    if 'haslab' not in dict_cols_vals:
                        dict_cols_vals['haslab'] = "NULL";
                    if 'semoffered' not in dict_cols_vals:
                        dict_cols_vals['semoffered'] = "NULL";

                    if key_value_list not in self.data:
                        self.data.update({key_value_list: dict_cols_vals})
                    else:
                        print("Already in BTree")
                        error1 = True

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(',')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    col_ext = split_list[0].replace(" ","")
                    val_ext = split_list[1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    else:
                        val_ext = split_list[1][1:-1]
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if "cno" not in col_name:
                    print("No primary key")
                    error1 = True
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
                    if 'haslab' not in dict_cols_vals:
                        dict_cols_vals['haslab'] = "NULL";
                    if 'semoffered' not in dict_cols_vals:
                        dict_cols_vals['semoffered'] = "NULL";

                    if key_value_list not in self.data:
                        self.data.update({key_value_list: dict_cols_vals})
                    else:
                        print("Already in BTree")
                        error1 = True

        elif self.tablename == 'courseoffering':
            if value_list_bool and not column_name_bool: #first case input
                value_list = (value_list+ " ").split(',')
                for i in range(0, len(value_list)):
                    value_list[i] = value_list[i].rstrip('\'')
                    value_list[i] = value_list[i].lstrip('\'')
                    value_list[i] = value_list[i][1:-1]
                    if re.search("'null'",value_list[i]):
                        value_list[i] = "NULL"
                    if not value_list[i].isdigit() and value_list[i] == "NULL":
                        value_list[i] = value_list[i][:-1]

                value_list[0] = "'" + value_list[0].split("'")[1] + "'"

                print(value_list[0:4])
                if (value_list[0:4]) not in self.data.keys():
                    if len(value_list) == 6:
                        str123 = ",".join(value_list[0:4])
                        self.data.update({",".join(value_list[0:4]): {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3], self.columns[4]: value_list[4], self.columns[5]: value_list[5]}})
                    else:
                        print("Column values are lacking")
                        error1 = True
                else:
                    print("Already in BTree")
                    error1 = True

            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.replace(" ", "")
                value_list = value_list.split(',')
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    else:
                        value_list[i] = value_list[i].rstrip('\'')
                        value_list[i] = value_list[i].lstrip('\'')
            
                        value_list[i] = value_list[i][1:]

                    if not value_list[i].isdigit() and value_list[i] != "NULL":
                        value_list[i] = value_list[i][:-1]
                    print(value_list[i])
                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                col_name = col_name.split(',')

                if ("semester" not in col_name) or ("acadyear" not in col_name) or ("cno" not in col_name) or ("section" not in col_name):
                    print("No primary key/s")
                    error1 = True
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
                        dict_cols_vals['time'] = "NULL";
                    if 'maxstud' not in dict_cols_vals:
                        dict_cols_vals['maxstud'] = "NULL";

                    primary_key_string = key_value_list[0] + "," + key_value_list[1] + "," + key_value_list[2] + "," + key_value_list[3]
                    if primary_key_string not in self.data:
                        new_dict_container = {key_col_name[0]: key_value_list[0], key_col_name[1]: key_value_list[1], key_col_name[2]: key_value_list[2], key_col_name[3]: key_value_list[3]}
                        new_dict_container.update(dict_cols_vals)
                        self.data.update({primary_key_string: new_dict_container})
                    else:
                        print("Already in BTree")
                        error1 = True

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(',')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    col_ext = split_list[0].replace(" ","")
                    val_ext = split_list[1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    else:
                        val_ext = split_list[1][1:-1]
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                if ("semester" not in col_name) or ("acadyear" not in col_name) or ("cno" not in col_name) or ("section" not in col_name):
                    print("No primary key")
                    error1 = True
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
                        dict_cols_vals['time'] = "NULL";
                    if 'maxstud' not in dict_cols_vals:
                        dict_cols_vals['maxstud'] = "NULL";

                    primary_key_string = key_value_list[0] + "," + key_value_list[1] + "," + key_value_list[2] + "," + key_value_list[3]

                    if primary_key_string not in self.data:
                        new_dict_container = {key_col_name[0]: key_value_list[0], key_col_name[1]: key_value_list[1], key_col_name[2]: key_value_list[2], key_col_name[3]: key_value_list[3]}
                        new_dict_container.update(dict_cols_vals)
                        self.data.update({primary_key_string: new_dict_container})
                    else:
                        print("Already in BTree")
                        error1 = True

        elif self.tablename == 'studcourse':
            if value_list_bool and not column_name_bool: #first case input
                value_list = (value_list + " ").split(',')
                for i in range(0, len(value_list)):
                    value_list[i] = value_list[i].rstrip('\'')
                    value_list[i] = value_list[i].lstrip('\'')
                    value_list[i] = value_list[i][1:-1]

                    if re.search("'null'",value_list[i]):
                        value_list[i] = "NULL"
                    if not value_list[i].isdigit() and value_list[i] == "NULL":
                        value_list[i] = value_list[i][:-1]
                    print(value_list[i] + "-val")

                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                if len(value_list) == 4:
                    #btreelen = self.counter + 1
                    #print(btreelen + "-btreelen")
                    #for k in self.data.keys():
                    #print(k + "-dsa")
                    self.data.update({self.counter: {self.columns[0]: value_list[0], self.columns[1]: value_list[1], self.columns[2]: value_list[2], self.columns[3]: value_list[3]}})
                    self.counter = self.counter + 1
                else:
                    print("Column values are lacking")
                    error1 = True



            elif value_list_bool and column_name_bool: #second case input
                col_name = col_name.replace(" ", "")
                value_list = (value_list + " ").split(',')
                for i in range(0, len(value_list)):
                    print(value_list[i])
                    if re.search("'null'",value_list[i]):# == " 'null'":
                        value_list[i] = "NULL"
                    else:
                        value_list[i] = value_list[i].rstrip('\'')
                        value_list[i] = value_list[i].lstrip('\'')
            
                        value_list[i] = value_list[i][1:]

                    if not value_list[i].isdigit() and value_list[i] != "NULL":
                        value_list[i] = value_list[i][:-1]
                    print(value_list[i])
                col_name = col_name.split(',')
                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                dict_cols_vals = dict(zip(col_name,value_list))

                if 'studno' not in dict_cols_vals:
                        dict_cols_vals['studno'] = "NULL";
                if 'cno' not in dict_cols_vals:
                        dict_cols_vals['cno'] = "NULL";
                if 'semester' not in dict_cols_vals:
                        dict_cols_vals['semester'] = "NULL";
                if 'acadyear' not in dict_cols_vals:
                        dict_cols_vals['acadyear'] = "NULL";


                self.data.update({self.counter: dict_cols_vals})
                self.counter = self.counter + 1

            elif not value_list_bool and not column_name_bool: #third case input
                assignment_list = (assignment_list + " ").split(',')
                insert_list = []
                col_name = []
                value_list = []

                for i in range(0,len(assignment_list)):
                    split_list = assignment_list[i].split("=")
                    col_ext = split_list[0].replace(" ","")
                    val_ext = split_list[1]
                    if re.search("'null'",val_ext):
                        val_ext = "NULL"
                    else:
                        val_ext = split_list[1][1:-1]
                    col_name.append(col_ext)
                    value_list.append(val_ext)

                value_list[0] = "'" + value_list[0].split("'")[1] + "'"
                dict_cols_vals = dict(zip(col_name,value_list))

                if 'studno' not in dict_cols_vals:
                        dict_cols_vals['studno'] = "NULL";
                if 'cno' not in dict_cols_vals:
                        dict_cols_vals['cno'] = "NULL";
                if 'semester' not in dict_cols_vals:
                        dict_cols_vals['semester'] = "NULL";
                if 'acadyear' not in dict_cols_vals:
                        dict_cols_vals['acadyear'] = "NULL";


                self.data.update({self.counter + 1: dict_cols_vals})
                self.counter = self.counter + 1

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
            col_name = col_name[1:-1]
            comp_operator = comp_operator[1:-1]
            if not isinstance(cond_exp, int):
                cond_exp = cond_exp[1:-1]


        if columns[0] == "*":
            if withcondition and where_column: #If True lang, print all pa din
                #return
                print("cas")
            else:
                for i in self.columns:
                      cols.append(i)
                     # print(i)
                retdata.append(cols)
 
                for j in self.data:
                    row = []
                    for i in self.columns:
                        print(self.data[j][i])
                        row.append(self.data[j][i])
                    retdata.append(row)

        else:
            #print(columns)
            if withcondition:
                return
            else:
                for i in columns:
                    cols.append(i)
                    # print(i)
                retdata.append(cols)
 
                for j in self.data:
                    row = []
                    for i in columns:
                        i = i.strip(" ")
                        print(self.data[j][i])
                        row.append(self.data[j][i])
                    retdata.append(row)
        return retdata

    def delete(self, columns, withcondition, condition):
        retdata = []
        colNames = []
        row = []

        for col in self.columns:
            colNames.append(col)    
        retdata.append(colNames)

        if withcondition:
            print('condition')
        else:            
            self.data.clear()
            for pk in self.data:
                for col in self.columns:
                    col = col.strip(" ")
                    row.append(self.data[pk][col])
                retdata.append(row)
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
