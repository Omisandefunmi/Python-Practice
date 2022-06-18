# brackets = (input("Enter set of brackets"))

def bracket_pair_checker(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '{':
            stack.append(bracket)
        if bracket == '[':
            stack.append(bracket)
        if bracket == '(':
            stack.append(bracket)
        if bracket in '}])':
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
    else:
        return False


print(bracket_pair_checker("(}{}){{}})"))
print(bracket_pair_checker("{(){}[]}"))
