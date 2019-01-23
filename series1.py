# 1/1 + 1/2 + 1/3 + n
# sum 
sum = 0
n = int(input("Enter value "))
for i in range(1,n):
    print("1/",i," +",end=" ")
    sum = sum + 1/i
   
print("\nsum is ",sum)