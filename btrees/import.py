from BTrees.OOBTree import OOBTree

metadata = open("../gui/student.csv", "r")
counter = 0

cols = []
btree = OOBTree()

for line in metadata:
    if(counter == 0):       # column names
        # nonewline = line.rstrip('\n')
        column_names = line.split("\n")
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
    else:
        rows = line.split("\n")
        for i in range(0,len(rows)):
            if(rows[i] != ""):
                data = rows[i].split(",")
                for i in range(0, len(data)):                
                    data[i] = data[i].rstrip('\"')
                    data[i] = data[i].lstrip('\"')

                btree.update({data[0]: {cols[1]: data[1], cols[2]: data[2], cols[3]: data[3], cols[4]: data[4], cols[5]: data[5]}})

        print(list(btree))

print(btree["2020-53215"])
print(btree["2020-53215"]['Major'])
