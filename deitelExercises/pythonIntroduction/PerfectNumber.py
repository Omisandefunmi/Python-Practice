user_input = int(input("Enter number: "))
factor = 2
sum_of_factor = 0
count = 0
while factor < user_input:
    if user_input % factor == 0:
        print(factor, " is a factor ", user_input)
        sum_of_factor = sum_of_factor + factor
        count += 1
    factor += 1

print(sum_of_factor)
if sum_of_factor == user_input:
    print(user_input, " is a perfect number")
elif sum_of_factor < user_input:
    print(user_input, " is a deficient number")
elif sum_of_factor > user_input:
    print(user_input, " is an abundant number")

