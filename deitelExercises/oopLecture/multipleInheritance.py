import json


class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__getitem__(index - 1)

    def __setitem__(self, index, value):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__setitem__(index - 1, value)


l = CustomList()
l.append(100)
l.append(10)
l.append(1)
print(l)
l[1] = 23

print(l)


class CustomDict(dict):
    def __init__(self, *args, **kwargs):
        super(CustomDict, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        with open("custom_file.txt", mode="w", encoding="utf -8") as file:
            json.dump(dict1, file)
        return super(CustomDict, self).__setitem__(key, value)


dict1 = CustomDict()
dict1["name"] = "Olufunmi"
dict1["status"] = "single"
dict1["school"] = "semicolon"
dict1["course"] = "java"
