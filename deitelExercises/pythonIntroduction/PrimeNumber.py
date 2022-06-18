import math

user_input = int(input("Enter number: "))
ceil_number = math.ceil(math.sqrt(user_input))
counter = 2
while counter <= ceil_number:
    result = user_input % counter
    if result == 0:
        print("It is not a prime number")
        break
    counter += 1
else:
    print("It is a prime number")


