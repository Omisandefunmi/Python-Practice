lst = list("abcde")
print(lst)

lst = ['a', 'b', 'c']
print('-->'.join(lst))

lst = list("abcdefghijk")
print(lst[4])

#ListSlicing
lst = list("abcdefghijk")
print(lst[1:5])
print(lst[::2])

print(lst * 2)

#ConcantenatingString
print(lst + [1, 2, 5, 8])

#or
lst += [1, 2, 3, 8]
print(lst)

#CheckingForElementsInList
print('a' in lst)
print('q' not in lst)
print('q' in lst)

#Dictionary
my_dict = {
    'name': "Segun",
    'age': 12,
    'sex': 'Male',
    'hobby': ['Python', 'Java'],
    'isAthlete': False

    }
print(my_dict)
for key in my_dict:
    print(key)

for key in my_dict:
    print(key, '-->', my_dict[key])

#append_adds_elements_to_the_end_of_a_list

