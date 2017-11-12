from BTrees.OOBTree import OOBTree

class TableBTree:

    def __init__(self, tablename, tablespecs):
        self.tablename = tablename
        self.primarykey = []
        self.columns = []
        self.tablespecs = tablespecs
        self.data = OOBTree()
        self.counter = 0

        print("Initialize "+tablename)
        self.loadData()
        print("tablespecs")
        print(tablespecs)
        # self.printData()

    def loadData(self):
        print("Loading data of "+self.tablename+" table.")
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

                    print(keyset)
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
            print(self.data[i])

    def select(self, columns, withcondition, condition):
        retdata = []
        cols = []
        row = []
        print("SELECT OPERATION ON "+self.tablename)
        if columns[0] == "*":
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
        return retdata

    # def delete(self, table_selected, columns, withcond, condition):

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
