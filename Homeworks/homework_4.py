
# Task 1

# first case
list_1 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
print('Current list', list_1)
list_2 = list_1.copy()

for num in list_2:
    if num < 21 or num > 74:
        list_1.remove(num)
print('Updated list', list_1)

# second case (using List Comprehension)
list_1 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
print('Current list', list_1)
list_1 = [num for num in list_1 if 21 < num < 74]
print('Updated list', list_1)

# Task 2

dict = {
      'cito' : 47.999,
      'BB_studio':42.999,
      'momo': 49.999,
      'main-service': 37.245,
      'buy.now': 38.324,
      'x-store': 37.166,
      'the_partner': 38.988,
      'store': 37.720,
      'rozetka': 38.003
}

min_val = min(dict.values())
print('Minimal price is', min_val)
max_val = max(dict.values())
print('Maximal price is', max_val)

price = [keys for keys, values in dict.items() if min_val < values < max_val]
print('The name of stores between min and max price are', price)


