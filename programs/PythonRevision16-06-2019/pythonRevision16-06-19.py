# Python Revision from scratch no more JAVA or Android Focus

def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'bonjour'
    elif lang == 'en':
        return 'Hello'
    else:
        return 'Try Again'
print(greet('en'))
print(greet('es'))
print(greet('bdbcs'))
print(greet('fr'))
print('\n\n')

while False:
    line = input("> ")
    if line == 'done':
        break
    print(line)

while False:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)

for i in [4,56,412,45,2,1,6]:
    print(i)
print('\n\n')

name = 'Akshay Bengani'
name.lower()
name.upper()

for i in name:
    if i == i.upper():
        i = i.lower()
    if i == i.lower():
        i = i.upper()
print(name)