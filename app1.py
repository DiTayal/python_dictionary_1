import json
import difflib
from difflib import get_close_matches 

# can use ratio mathod to calculate ratio of numbers given in input

data=json.load(open('data.json'))

# print(type(data))

def translate(word):
    word=word.lower()

    if word in data.keys():
        return data[word] 

    # possible words can be tuple or list anything
    elif len(get_close_matches(word,data.keys())) > 0 :

        possible_word=get_close_matches(word,data.keys())[0]
        choice=input(f'Did you mean {possible_word} this? Press Y for yes and N for No : ' )

        if(choice=='Y'):
            return data[possible_word]
        elif(choice =='N'):
            return "The word does not exist , kindly double check it! "
        else:
            return "Not a valid choice"
        
    else:
        return "No such word found!"






word=input('\nEnter word: ')

output=translate(word)

if type(output)==list:
    print("\n".join(output))
else:
    print(output)
