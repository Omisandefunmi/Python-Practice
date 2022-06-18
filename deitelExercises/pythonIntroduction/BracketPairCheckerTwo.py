

def bracket_pair_check(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '{':
            stack.append(bracket)
        if bracket == '[':
            stack.append(bracket)
        if bracket == '(':
            stack.append(bracket)

        if bracket in ")}]":
            peek = stack[len(stack) - 1]
            if bracket == ')' and peek == '(':
                stack.pop()
            elif bracket == '}' and peek == '{':
                stack.pop()
            elif bracket == ']' and peek == '[':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


print(bracket_pair_check(('({{[]}}')))
print(bracket_pair_check(('([])')))


num = 1
def func():
    global num
    num = 2
    print(num)
print(num)

def func2():
    num = 4
    print(num)
    def func3():
        num = 5
        print(num)
    print(num)

#Arbitrary Arguments

def add(* numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(add(7,8,99,56,87,3,0,1,4))
#or

def add(*numbers):
    return sum(numbers)
print(add(7,8,99,56,87,3,0,1,4))

#or
def add(* numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(add(*[7,8,99,56,87,3,0,1,4]))
#or
def add(* numbers):
    total = 0
    for num in numbers:
        total += num
    return total
lst = [7,8,99,56,87,3,0,1,4]
print(add(*lst))

def dict_pack_unpack(**kwargs):
    print(kwargs)
dict_pack_unpack(name = "remi", age = 67, sex = "Male")
