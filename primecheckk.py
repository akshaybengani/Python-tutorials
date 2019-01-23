value = int(input("Enter a value "))
i=2
flag = "Yes it is a prime number"
while i<value:
    if value%i==0:
        flag = "No it is not a prime number"
    i=i+1

print(flag)