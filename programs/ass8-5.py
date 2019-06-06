fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
words = list()
for line in fhand:
    if line.startswith('From:'):
        words = line.split()
        print(words[1])
        count = count + 1
print("There were ",count," lines in the file with From as the first word")
