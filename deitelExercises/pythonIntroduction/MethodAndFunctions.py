# s = "hello"
# print(s.upper(), end='')
# print()
# n = "WELL"
# print(n.lower(), end='')
# print()
# print(s[:1] + s[1].upper() + s[2:])
#
# #findMethod
# print(s.find('l'))
# #ChainingMethod
# print(s.upper().find('E'))
# d = 'i love you'
# print(d.find('o', 2))
#
# #NestingMethod
# a_str = 'This is the bat'
# print(a_str.find('t', a_str.find('t')+1))
#
# #toFindMethod
# print(a_str.rfind('t'))
# w = 'This is the world of java'
#
# #ReplaceMethod
# print(w.replace('python', 'java'))
# print(w.replace('o', 'OO', 2))
#
# #capitalize
# print(w.title())
# print(w.capitalize())
#
# #Translate
# print('010011101110'.translate(str.maketrans('01', '10')))
#
# #CheckOutCeaserCypher
#
# #PrintFormat
# a = 3
# b = 2
# print("I read the {1} textbook {0} times in {1} days".format(a, b))
# #{} is a placeholder for print format in Python
# print(f'10: >20.2')
#
# for i in range(1, 11):
#     print(f"{ '* ' * i: ^20}")
# print()
# #Smiley
# smiley = "\U0001f600"
# for i in range(1, 21, 2):
#     print(f"{smiley * i: >20}")
#
# #PrintTriangle
# star = "*"
# for i in range(1, 11):
#     print(f"{star * i:<10}    {star *(11 - i):<10}   {star * (11 - i):>10}  {star * i:>10}")
# #PrintingIndexAndLetter
# letter = "hello every body"
# for index, letter in enumerate(letter):
#     print(f"{index} --> {letter}")
#
# #SplittingString
# name = 'John Marwood Cleese'
# transformed = first, middle, last = name.split()
# print(transformed)


