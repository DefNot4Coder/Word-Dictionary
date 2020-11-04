from tkinter import *
import json
from difflib import get_close_matches
data =  json.load(open("data.json"))
#Function to find the definition of word along with few more 'Features'
window=Tk()
def finder(word):
    no = 1
    if word in data.keys():
        for i in data[word]:
            print("---" + str(- no) + ") " + i)
            no +=1
    else:
        conf = input("Press 'Y' and Enter if you mean '" + get_close_matches(word, data.keys(), cutoff=0.6)[0] + "' instead or else Press 'N' or else 'Q' to 'Quit' : ").lower()
        if conf == 'y':
            word = get_close_matches(word, data.keys())[0]
            finder(word)
        elif conf == 'n':
            print("----------The word doesn't exist, try again!----------")
            finder()
        elif conf == 'q':
            print("----------Thank You for using me!----------")
        else:
            print("---------Just type 'Y' for 'Yes' & 'N' for 'No'!----------")
            finder(word)
#Function to repeat the process.
def repeater():
        try:
            word = input("Enter word to find definition: ")
            word = word.lower()
            finder(word)
        except :
            repeater()
repeater()
