# Task 1

while True:

    word = input('Enter word that consist upper and lower letter \'o\':')
    if 'o' in word.lower():
        print('You are super hero')
        break

# Task 2

list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list_2 = []

for item in list_1:
    if type(item) == str:
        list_2.append(item)
print(f'List with only str data: {list_2}')


# Task 3

words = input('Enter a couple words are ending on letter \'o\':').split(' ')
print('Number of inputted words:', len(words))
result = 0

for elem in words:
    if elem.endswith(('o', 'O')):
        result += 1
print(f'Words are ending on letter \'o\'--> {result}')

