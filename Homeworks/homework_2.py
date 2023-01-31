#Task 1

word = input('Enter your name:')
name = len(word)
print('Word \'', word,'\' consists of', name, 'letters')

#Task 2

age = int(input('Enter you age:'))

if age < 7:
    print('Where is your parents?')
elif age < 16 and age > 7:
    print('It is film for adult')
elif age > 65 and age < 100:
    print('Show your pension certificate')
elif age == 7:
    print('You are lucky')
else:
    print('There are no tickets')