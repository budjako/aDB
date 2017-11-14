from BTrees.OOBTree import OOBTree
import sys

tableName = "student"

try:
    metadata = open(tableName + ".dat", "r")
except:
    print("File not found")
    sys.exit()

counter = 0

cols = []
btree = OOBTree()

for line in metadata:
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
        counter = counter + 1
    elif(counter == 1):     # primary key/s
        print("Primary Key: ", line)
        counter = counter + 1
    else:
        nonewline = line.rstrip('\n')
        # print(nonewline)
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
            print('removed:', k)
            btree.pop(k)
    elif co == 'gthan':
        if lv > cv:
            print('removed:', k)
            btree.pop(k)
    elif co == 'leq':
        if lv <= cv:
            print('removed:', k)
            btree.pop(k)
    elif co == 'geq':
        if lv >= cv:
            print('removed:', k)
            btree.pop(k)
    elif co == 'neq':
        if lv != cv:
            print('removed:', k)
            btree.pop(k)

##################################

op = "delete" # operation
cis = True # condition is given
pkig = False # primary key is given
boig = False # binary opertaion is given
coig = True # comparative operation is given
co = "neq" # COMPARATIVE OPERATIONS: lthan, gthan, leq, geq, neq
bo = "plus"  # BINARY OPERATIONS: plus, minus, times, divide, modulo
pk = "2008-56411" # primary key
colSel = "unitsearned" # selected column name
valType = "integer" # value type
colVal = 36 # selected column value
colVal2 = 1 # 2nd value in binary operation

btreesDelete(op, cis, pkig, boig, coig, co, bo, pk, colSel, valType, colVal, colVal2)

#################################

def btreesDelete(operation, conditionIsGiven, primaryKeyIsGiven, binOpIsGiven, compOpIsGiven, comop, binop, primaryKey, colSelect, valType, colValue, colValue2):
    
    print('LIST:', list(btree), '\n')

    if operation == 'delete':
        # has condition
        if conditionIsGiven:
            # delete using primary key
            if primaryKeyIsGiven:
                if btree.has_key(primaryKey) > 0:
                    btree.pop(primaryKey)
                else:
                    print("Key not found")
            # delete using column names
            else:
                for key in list(btree.keys()):
                    listValue = list(btree.values(key))[0][colSelect]
                    if valType == 'integer':
                        listValue = int(listValue)
                        if binOpIsGiven:
                            colValue3 = binoperation(binop, colValue, colValue2)
                        else:
                            colValue3 = colValue
                        if compOpIsGiven: 
                            comoperation(comop, listValue, colValue3, key)
                        elif listValue == colValue3:
                                print('removed:', key)
                                btree.pop(key)
                    elif listValue == colValue:
                                print('removed:', key)
                                btree.pop(key)
        # no condition
        else:
            btree.clear()

        print('\nUPDATED LIST:', list(btree))