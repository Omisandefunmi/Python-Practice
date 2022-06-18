user_input = int(input('enter a number: '))

total = 0
while user_input >= 1:
    total += user_input
    print(user_input, ' + ', end='')
    user_input -= 1
print(0, ' = ', total)
