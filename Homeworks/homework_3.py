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

word_1 = input('Enter a couple words are ending on letter \'o\':').split(' ')
word_2 = input('Click the button on keyboard that corresponds to the letter \'o\':')
result = []

for elem in word_1:
    elem.lower()
    if elem.endswith(word_2):
        result.append(elem)

print(f'Words are ending on letter \'o\'--> {len(result)}')

