n = input("Enter the size ")
i=2
hold = 0
a=0
b=1
print("0", end=" ")

while i<=int(n):
    hold = a+b
    print(hold, end=" ")
    a=b
    b=hold
    i=i+1
print("\n")



