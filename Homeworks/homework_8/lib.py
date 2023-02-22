def calculator(arg1, arg2, operation):
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