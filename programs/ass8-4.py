fname = input("Enter the file name: ")
fhand = open(fname)
mylist = list()
mytext = list()
for line in fhand:
    myline = line.split()
    for word in myline:
        if not word in mytext:
            mytext.append(word)
mytext.sort()
print(mytext)        
