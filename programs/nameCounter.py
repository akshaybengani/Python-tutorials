#counts = {}
#names = ['akshay','shivank','yash','akshay','naman','shivank','akshay','yash','shivank']
#for name in names:
#    if name not in counts:
#        counts[name] = 1
#    else:
#        counts[name] = counts[name] + 1
#print(counts)

counts = {}
names = ['akshay','shivank','yash','akshay','naman','shivank','akshay','yash','shivank']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)
