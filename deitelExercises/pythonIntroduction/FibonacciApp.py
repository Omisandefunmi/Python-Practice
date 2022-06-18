user_input = int(input('Enter a number: '))
a, b = 0, 1
if user_input <= 0:
    print('Enter a positive integer')
elif user_input == 1:
    print('The Fibonacci sequence for', user_input, 'is: ')
count = 0
while count < user_input:
    c = a + b
    print(a, end=' ')
    a = b
    b = c
    count += 1
