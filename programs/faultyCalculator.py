# Design a calculator which will correctly solve all the problems except the following ones:
# 45*3=555 56+9=77 56/6=4
# Program should take operator and the two numbers as input from the user and then return the result

num1 = int(input("Enter Number 1 "))
num2 = int(input("Enter Number 2 "))
opr  = input("Enter Operator ")

def faultCheck(num1,num2,opr):
    if num1==45 and num2==3 and opr=='*':
        return '555'
    elif num1==56 and num2==9 and opr=='+':
        return '77'
    elif num1==56 and num2==6 and opr=='/':
        return '4'
    else:
        return True

if opr == '+':
    check = faultCheck(num1,num2,opr)
    if check == True:
        print(num1+num2)
    else:
        print(check)
elif opr == '-':
    check = faultCheck(num1,num2,opr)
    if check == True:
        print(num1-num2)
    else:
        print(check)
elif opr == '*':
    check = faultCheck(num1,num2,opr)
    if check == True:
        print(num1*num2)
    else:
        print(check)
elif opr == '/':
    check = faultCheck(num1,num2,opr)
    if check == True:
        print(num1/num2)
    else:
        print(check)
else:
    print('Please enter correct operator ')