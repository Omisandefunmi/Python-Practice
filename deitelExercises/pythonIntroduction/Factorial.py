user_input = int(input('Enter a number: '))
factorial = 1
count = 1
while count <= user_input:
    factorial = factorial * count
    count += 1
print(factorial)
