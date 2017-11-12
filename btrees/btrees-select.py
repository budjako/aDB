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

#################################

operation = "select"
primaryKeyIsGiven = False
binOpIsGiven = True
compOpIsGiven = True
comop = "leq" # lthan, gthan, leq, geq, neq
binop = "minus"  # plus, minus, times, divide, modulo
primaryKey = "2007-12345" # sample primary key
colSelect = "unitsearned" # *, <column names>
valType = "integer" # integer, other types
colValue = 144 # sample column value
colValue2 = 1 # add to column value (if colValue = 'integer')

# get column names
colNames = list(btree.values()[0])

#################################

def binoperation(bo, v1, v2):
    if bo == 'plus':
        v1 = v1 + v2
    elif bo == 'minus':
        v1 = v1 - v2
    elif bo == 'times':
        v1 = v1 * v2
    elif bo == 'divide':
        v1 = v1 / v2
    elif bo == 'modulo':
        v1 = v1 % v2
    
    return v1

def comoperation(co, lv, cv, k):
    if co == 'lthan':
        if lv < cv:
            selectCol = list(btree.values(k))[0]
            for colName in colNames:
                print(colName, selectCol[colName])
            print('')
    elif co == 'gthan':
        if lv > cv:
            selectCol = list(btree.values(k))[0]
            for colName in colNames:
                print(colName, selectCol[colName])
            print('')
    elif co == 'leq':
        if lv <= cv:
            selectCol = list(btree.values(k))[0]
            for colName in colNames:
                print(colName, selectCol[colName])
            print('')
    elif co == 'geq':
        if lv >= cv:
            selectCol = list(btree.values(k))[0]
            for colName in colNames:
                print(colName, selectCol[colName])
            print('')
    elif co == 'neq':
        if lv != cv:
            selectCol = list(btree.values(k))[0]
            for colName in colNames:
                print(colName, selectCol[colName])
            print('')

##################################

if operation == 'select':
    # has no condition, print all
    if colSelect == '*':
        for key in list(btree.keys()):
            for i in range(0, len(btree.keys())):
                selectCol = list(btree.values(key)[0])[i]
                selectVal = list(btree.values(key))[0][selectCol]
                print(selectCol, selectVal)
            
            print('')

    else:
        # has condition, print data with selected primary key
        if primaryKeyIsGiven:
            selectPK = (list(btree.values(primaryKey))[0])
            for colName in colNames:
                print(colName, selectPK[colName])
        # has condition, print data with selected column
        else:
            for key in list(btree.keys()):
                listValue = list(btree.values(key))[0][colSelect]
                # change to integer for comparison
                if valType == 'integer':
                    listValue = int(listValue)
                    if binOpIsGiven:
                        colValue3 = binoperation(binop, colValue, colValue2)
                    if compOpIsGiven: 
                        comoperation(comop, listValue, colValue3, key)
                    elif listValue == colValue3:
                        selectCol = list(btree.values(key))[0]
                        for colName in colNames:
                            print(colName, selectCol[colName])
                        print('')
                elif listValue == colValue:
                    selectCol = list(btree.values(key))[0]
                    for colName in colNames:
                        print(colName, selectCol[colName])
                    print('')