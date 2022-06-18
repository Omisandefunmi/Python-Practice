entries = []
numberOfEntries = 0
def createUserName():
    username = input('Enter username: ')
    return username

def createPassword():
    password = input('Enter password: ')
    return password

def validatePassword(passwordEntered):
    return passwordEntered == createPassword()

def createEntry():
    date, title = input('date: '), input('title: ')
    key = {'date', 'title', 'body'}
    value = {date, title, input(f"{date}\n{title}\n\nHey diary:\n")}
    entry = dict(zip(key, value))
    return entry

def addEntry(password):
    if validatePassword(password):
        entries.append(createEntry())
        return numberOfEntries + 1
    return False

def findEntryByIndex(entryId, password):
    if validatePassword(password):
        print(entries[entryId-1])
    else:
        print("Entry not found")