user_input = int(input("Enter any number "))

while user_input != 1:
    if user_input % 2 != 0:
        user_input = ((user_input * 3) + 1)
    elif user_input % 2 == 0:
        user_input = (user_input // 2)
        print(user_input, end=" ")


