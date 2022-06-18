lst = []
for i in range (1, 11):
    lst.append(i)
print(lst)
# Or do a list comprehension in one line
lst = [i for i in range(1, 11)]
print(lst)

lst = [i for i in range(2, 11, 2)]
print(lst)

# or
lst_even = [i for i in range(1, 11) if i % 2 == 0]
print(lst)
# To use and if_else in list comprehension

lst = [i if i % 2 == 0 else i ** 2 for i in range(1, 11)]
print(lst)

lst_input = [int(input("Enter a number: ")) for num in range(1, 4)]
print(lst_input)

# Nest for list in one line
list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
print(list_nested_for)

# upper case in list
upper_names = [name.upper() for name in ["dolapo", "tolani", "florence"]]
print(upper_names)

# check lengths of elements in list
list_length = [name.upper() for name in ["dolapo", "tolani", "florence"]]
print(upper_names)

# lists of dictionary
list_of_dicts = [{key: value} for key, value in zip(upper_names, lst_even)]
print(list_of_dicts)

# generator expression
lst = [numbers for numbers in range(1, 11)]
gen = (numbers for numbers in range(1, 11))

print(lst)
print(gen)
print(list(gen))

# sets
s1 = {1, 2, 3, 5}
s2 = {4, 3, 2, 5}

s1.pop()
print("pop", s1)

# intersection
print(s1 & s2)

# intersection update
s1 &= s2
# or
s1 = s1 & s2
print(s1)

# union
print(s1 | s2)

#update
s1 |= s2
print(s1)

# difference
print(s1 - s2)

s1 = {1, 3, 4, 2, 3, 5}
s2 = {4, 3, 2, 5}

print(s1 - s2)
# symmetric
print(s1 ^ s2)

# super sets and sub sets

print(s1 >= s2)
print(s1 <= s2)

dict_play = {"name": "Tolani", "age": 32, "influenced": "Samson"}
print(dict_play["name"])

# if name not found, return argument in get
dict = { "age": 32, "influenced": "Samson"}
print(dict.get("name", "Samson"))

dict = {"name": "care", "age": 32, "influenced": "Samson"}
print(dict.pop("name"))

# iterating keys for empty dictionary {}
print({}.fromkeys("hello", "UNKNOWN"))

def get_first(s: str) -> str:
    return s[0]

# more on list comprehension
l = [get_first(val) for val in ["Hello", "How", "Are", "You"]]
print(l)

