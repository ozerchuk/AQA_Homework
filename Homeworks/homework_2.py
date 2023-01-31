#Task 1

word = input('Enter your name. Input only letters:')
name = len(word)
result = f'Name {word} consist of {name} letters'
print(result)




#Task 2

age = input('Enter you age! it should be a number:')

if age.isdigit():
    if int(age) < 7:
        print('Where is your parents?')
    elif int(age) < 16:
        print('It is film for adult')
    elif 65 < int(age) < 100:
        print('Show your pension certificate')
    elif '7' in age:
        print('You are lucky')
    else:
        print('There are no tickets')
else:
    print ('There is not a number')
