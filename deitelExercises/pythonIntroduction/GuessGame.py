counter = 1
while counter <= 15:
    user_input = int(input("Guess any number between 1 and 15: "))
    if user_input == 7:
        print("You got it RIGHT")
        break
    elif user_input < 7:
        print("Too low! TRY AGAIN!!!")
    elif 7 < user_input < 15:
        print("TOO HIGH! TRY AGAIN!!!")
    else:
        print("ALAYE CALM DOWN")
    counter += 1
