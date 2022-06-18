users_profile = [{"username": "Olufunmi", "password": "1111"},
                 {"username": "ademi", "password": "0000"}]


def list_checker(username, password):
    for user in users_profile:
        if user["username"] == username and user["password"] == password:
            return True
    return False


print(list_checker("Olufunmi", "1111"))

if __name__ == "__main":
    pass

user_access_details = {
    "favourite_food": ["rice", "beans", "dodo"],
    "favourite_players": {"Arsernal": "Bukayo", "Chelsea": "Lukaku", "Dekanorbs": "Shege"},
    "favourite_girls": "Funke",
    "favourite_language": {"Programming": "Python", "Dialect": "Yoruba", "Slang": "Breakfast"}
}


def type_checker(value_type):
    return [True if type(value) == value_type else False for value in user_access_details.values()]


def type_checker_again(value_type):
    for value in user_access_details.values():
        if type(value) == value_type:
            print(f"{value} is of type {type(value)}")


print(type_checker(dict))
type_checker_again(dict)

contact_detail = {
    "fullName": "Yem",
    "class": {"cohort 10": "dekanorbs", "cohort 11": "luminaries"},
    "phoneNumber": ["09099009900"]
}


def add_details(item):
    for detail in contact_detail.values():
        if type(detail) == list:
            detail.append(item)


add_details("909090")
print(contact_detail)


def add_details_again(phone_num):
    for key, value in contact_detail.items():
        if key == "phoneNumber" and type(value) == list:
            value.append(phone_num)


add_details_again("808080")
print(contact_detail)
