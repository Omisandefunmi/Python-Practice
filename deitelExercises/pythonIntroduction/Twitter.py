tweeps = [{"username": "missy", "age": 23, "tweets": ["hey people","end sars"],"verify": False},
          {"username": "pope", "age": 26, "tweets":["everyone"], "verify": True},
          {"username": "winnie", "age": 16, "tweets": [], "verify": False},
          {"username": "twinnie", "age": 19, "tweets": ["learning lists in python"], "verify": False},
          {"username": "uriel", "age": 20, "tweets": ["unity is key"], "verify": True},
          {"username": "nick", "age": 32, "tweets": ["Asuu biko ooo"], "verify": False},
          {"username": "quinn", "age": 29, "tweets": ["no one is invincible", "i am strong"], "verify": False},
          {"username": "king", "age": 30, "tweets": ["i need urgent 2k", "who will respond to my plea"], "verify": False},
          {"username": "judy", "age": 27, "tweets": [], "verify": False},
          {"username": "aproko_doctor", "age": 29, "tweets": ["Emeka stop brushing with salt"], "verify": False}
          ]



verifiedUsers = [tweep["username"] for tweep in tweeps if tweep["verify"]]
print("The list of verified twitter users is ", verifiedUsers)

verifiedUsers2 = map(lambda y: y['username'], filter(lambda x: x['verify'], tweeps))
print(list(verifiedUsers2))

nonVerifiedTweeps = map(lambda x: x['username'], filter(lambda y: y['verify'] if y['verify'] == False else True, tweeps))
print(list(nonVerifiedTweeps))

activeUsers = [tweep['username'] for tweep in tweeps if len(tweep['tweets']) > 0]
print(list(activeUsers))
youngerTweeps = [tweep["username"] for tweep in tweeps if tweep["age"] < 25]
print(youngerTweeps)

youngAndVerifiedTweeps = [tweep["username"] for tweep in tweeps if tweep["age"] < 25 and tweep['verify']]
print(youngAndVerifiedTweeps)

oldestTweep = max(tweep['age'] for tweep in tweeps)
print(oldestTweep)

averageAgeOfTweeps = sum(tweep['age'] for tweep in tweeps) / len(tweeps)
print(averageAgeOfTweeps)

youngestTweep = min(tweep['age'] for tweep in tweeps)
print(youngestTweep)

oldestAndVerifiedTweep = max(tweep['age'] for tweep in tweeps if tweep['verify'])
print(oldestAndVerifiedTweep)


