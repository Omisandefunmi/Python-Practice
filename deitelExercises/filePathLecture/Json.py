with open("file.txt", mode="a") as path:
    path.write("\nI can do without love")

with open("file.txt", mode="r") as path:
    for line in path.readlines():
        for word in line.split(" "):
            print(word)

# marshal, pickle, json, yaml - serialization/deserialization

import json

config_dict = {
    "name": "Adeola",
    "age": 21,
    1: "birthday",
    "hobby": [1, 2, 3, 4],
    "bool": True
}

with open("config.json", mode="w") as file_obj:
    json.dump(config_dict, file_obj, indent=4, separators=(",", ":"))

with open("config.json", mode="r") as file_obj:
    con = json.load(file_obj)
    print(con)

print(type(config_dict))
j = json.dumps()




