# GCD is we take two numbers and check that the highest number which divides both the values is called as GCD

v1 = input("Enter 1st value ")
v2 = input("Enter 2nd value ")

v1 = int(v1)
v2 = int(v2)

i=1

while i<v1 and i<v2:
    if v1%i==0 and v2%i==0:
        gcd = i
    i = i+1
print("GCD is ",gcd)