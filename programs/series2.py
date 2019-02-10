# 1+2-3+4-5+6-7+n
size = int(input("Enter size "))
sum =0
for i in range(1,size):
    if(i%2==0):
        print(i,"-",end=" ")
        sum = sum - i
    else:
        print(i,"+",end=" ")
        sum = sum + i
        
print("\nSum is ",sum)