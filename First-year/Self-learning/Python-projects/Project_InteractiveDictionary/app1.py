
# My first Python project :

import json
from difflib import get_close_matches

data=json.load(open("data.json"))
print("\n*************************  WELCOME TO MINI DICTIONARY ************************************\n")
while True:
    print("\nEnter \end to end the program otherwise\n ")
    word=input("Enter any word: ")
    if word=="\end":
        break
    else:
        def dic(word):
            word=word.lower()
            if word in data:
                return (data[word])
            elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
                return data[word.title()]
            elif word.upper() in data: #in case user enters words like USA or NATO
                return data[word.upper()]
            elif len(get_close_matches(word,data.keys()))>0:
                print("\nDid you mean %s instead ?\n "%get_close_matches(word,data.keys())[0])
                ans=input("Press (y/n): ")
                if ans=='y':
                    print("\nThe meaning of %s is:\n "%get_close_matches(word,data.keys())[0])
                    return (data[get_close_matches(word,data.keys())[0]])
                elif ans=='n':
                    return "\nSorry! This word doesn't exists. Please double check it.\n "
                else:
                    return "\nWe didn't understand your request. Please try again.\n"
            else:
                return "\nSorry! This word doesn't exists. Please double check it.\n "

        output=dic(word)

        if type(output)==list:
            for item in output:
                print(item)
        else:
            print(output)

        continue
