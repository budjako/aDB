from BTrees.OOBTree import OOBTree

class TableBTree:

    def __init__(self, tablename, tablespecs):
        self.tablename = tablename
        self.primarykey = []
        self.tablespecs = tablespecs
        self.data = OOBTree()
        self.counter = 0

        print("Initialize "+tablename)
        self.loadData()
        print("tablespecs")
        print(tablespecs)
        self.printData()

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
                column_names = nonewline.split(";")
                for i in range(0,len(column_names)):
                    if(column_names[i] != ""):
                        column = column_names[i].split(",")
                        for i in range(0,len(column)):
                            name = column[i].split(" ")
                            cols.append(name[0])
                            datatypes.append(name[1])
                counter = counter + 1

            elif(counter == 1):     # primary key/s
                nonewline = line.rstrip('\n')
                keys = nonewline.split(";")
                if(len(keys) == 0):
                    self.counter = 0
                else:
                    for i in range(0,len(keys)):
                        if(keys[i] != ''):  # table has one or more primary keys
                            keyset = keys[i].split(",")
                            for i in range(0,len(keyset)):
                                if i != '':
                                    self.primarykey.append(keyset[i])
                counter = counter + 1
            else:
                nonewline = line.rstrip('\n')
                rows = nonewline.split(";")
                for i in range(0,len(rows)):
                    if(rows[i] != ""):
                        data = rows[i].split("^")
                        value = {}
                        for i in range(0, len(data)):
                            data[i] = data[i].rstrip('\'')
                            data[i] = data[i].lstrip('\'')
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
        tabledata.close()

    def printData(self):
        for i in self.data.keys():
            print(str(i))
            print(self.data[str(i)])


    # def saveToFile(self):
