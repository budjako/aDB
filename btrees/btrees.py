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
