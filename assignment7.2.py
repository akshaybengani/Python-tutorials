# Use the file name mbox-short.txt as the file name
add = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.strip('X-DSPAM-Confidence: ')
        line = line.rstrip()
        add = add + float(line)
        count = count + 1
print("Average spam confidence:",add/count)

