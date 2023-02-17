#Task 1

word = input('Enter your name. Input only letters:')
name = len(word)
if word.isalpha():
    print(f'Name {word} consist of {name} letters')
else:
    print('You should input letters')




#Task 2

age = input('Enter you age! it should be a number:')

if age.isdigit():
    if '7' in (age):
        print('You are lucky')
    elif 7 < int(age) < 16:
        print('It is film for adult')
    elif int(age) > 65:
        print('Show your pension certificate')
    elif int(age) < 7:
        print('Where is your parents?')
    else:
        print('There are no tickets')
else:
    print ('There is not a number')
