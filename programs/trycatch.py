max = 0
min = None

while True:
    value = input("Enter a Number: ")
    if value == "done":
        break
    try:
        num = int(value)
    except:
        print ('Invalid Input')
        continue
    if num > max:
        max = num
    if min is None:
        min = num    
    elif num < min:
        min = num
print('Maximum is ',max)
print('Minimum is ',min)

    