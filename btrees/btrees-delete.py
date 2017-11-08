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

operation = "delete" # delete
conditionIsGiven = False
primaryKeyGiven = False
primaryKey = "2011-29712"
colName = "degree"
valType = "varchar"
colValue = "BSCS"

print('LIST:')
for key in btree.keys():
    print(btree.values(key)[0][colName])

print('\n')

if operation == 'delete':
    # has condition
    if conditionIsGiven:
        # delete using primary key
        if primaryKeyGiven:
            if btree.has_key(primaryKey) > 0:
                btree.pop(primaryKey)
            else:
                print("Key not found")
        # delete using column names
        else:

            for key in list(btree.keys()):
                listValue = list(btree.values(key))[0][colName]

                if valType == 'integer':
                    listValue = int(listValue)
                
                if listValue == colValue:
                    print(key, ':', listValue, 'removed')
                    btree.pop(key)

    # no condition
    else:
        btree.clear()

    print('\nUPDATED LIST:')
    print(list(btree))

else:
    print("No such key")