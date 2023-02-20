
# Task 1

def get_season(date_str):

    """
    This function determines the season by date, 
    firstly splits the input string date_str into day and month components, 
    converts them to integers, 
    and then checks which season the date belongs to based on the month
    """

    data = date_str.split('.')
    day = int(data[0])
    month = int(data[1])
    if month in [3, 4, 5]:
        season = 'Spring'
    elif month in [6, 7, 8]:
        season = 'Summer'
    elif month in [9, 10, 11]:
        season = 'Autumn'
    else:
        season = 'Winter'

    return season

date_str = input(str('Enter date and month in such format \'date.month\': '))
season = get_season(date_str)
print(season)


# Task 2

def calculator(arg1, arg2, operation):

    """
    This function checks whether the values of 'arg1' and 'arg2' are integer,
    and also checks whether the passed string 'operation' is a valid operation.
    If these checks are passed, the function executes the appropriate operation and returns the result
    """
    if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
        print('Invalid data type')
        return None
    if operation not in ['+', '-', '*', '/']:
        print('Operation isn\'t supported')
        return None
    if operation == '+':
        return arg1 + arg2
    elif operation == '-':
        return arg1 - arg2
    elif operation == '*':
        return arg1 * arg2
    else:
        if arg2 == 0:
            print('Division by zero is impossible')
            return None
        else:
            return arg1 / arg2

result = calculator(11, 2, '+')
print(result)

result = calculator(10, 0, '/')
print(result)  # Division by zero is impossible

result = calculator(10, '5', '+')
print(result)  # Invalid data type

result = calculator(10, 5, '%')
print(result)  # Operation isn't supported




