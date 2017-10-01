metadata = open("metadata.txt", "r")
tables = {}

for line in metadata:
    nonewline = line.rstrip('\n')
    print(nonewline);
    tokens = nonewline.split(" ")
    tokens.reverse()
    tablename = tokens.pop()
    tokens.reverse()
    for i in range(0,len(tokens)):
        tokens[i] = str.lower(tokens[i])
    tables[str.lower(tablename)] = tokens
print(tables)
