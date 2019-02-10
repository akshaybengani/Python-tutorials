i=2

try:
    num = input("Enter a value ")
    value = int(num)
    
    while i < value:
        if (value % i == 0):
            print(i,end=" ")
        i=i+1
    print("\n")

except:
    print("Enter a numerical value ")



