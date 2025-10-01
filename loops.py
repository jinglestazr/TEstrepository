text=input('Enter a string:')
for char in text:
    print(char)

numbers=[12,4,56,17,8]
minimum=numbers[0]
for num in numbers:
    if num<minimum:
        minimum=num
print('minimum value:',minimum)