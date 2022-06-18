count = 1
while count <= 100:
    if count % 15 == 0:
        print("fizz buzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)
    count += 1
