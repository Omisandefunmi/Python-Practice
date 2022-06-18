# try:
#     numerator = int(input("Enter numerator: "))
#     denominator = int(input("Enter denominator: "))
#     result = numerator / denominator
# except ZeroDivisionError as a:
#     print(a)
#     print("Cannot divide by zero")
# else:
#     print(result)
# finally:
#     print("Calculator session has ended")


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("You can see its a divide function")
    return num1 / num2


print(divide(3, 1))

numerator = input("Enter numerator: ")
denominator = input("Enter denominator: ")
while True:
    try:
        print(divide(numerator, denominator))
        break
    except (ZeroDivisionError, ValueError, TypeError):
        print("Wrong value input")
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
