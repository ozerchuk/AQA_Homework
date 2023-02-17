# Task 1

def arguments_compare(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        result1 = arg1 * arg2
        print(result1)

        return result1
    elif isinstance(arg1, str) and isinstance(arg2, str):
        result2 = arg1 + arg2
        print(result2)

        return result2
    else:
        result3 = (arg1, arg2)
        print(result3)

        return result3

arguments_compare(10, 2.5)
arguments_compare('Python is ', 'top')
arguments_compare('age', 22)

# Task 2

def cinema_cash():
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
    if age.isalpha():
        print('There is not a number. Enter only numbers')

cinema_cash()