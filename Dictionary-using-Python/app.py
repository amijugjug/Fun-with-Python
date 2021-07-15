#Application making python dictionary
import json
#json is a standard library that comes by-default on installation
#By this module we will loadt the data.json file
#data.jsom file contains all the data that is required for this project
#data of data.json file is loaded into a dictionary.

from difflib import get_close_matches
'''As json difflib is also a standard library,
here we use get_close_matches from diffib for data matching purpose
For example(user entered data as rainn but we have rain then
by methods of this module we work to give closest data possible)'''

data=json.load(open("data.json"))
#load is the method which takes the file object of the json file which we want to use.
#data is a dict variable which will load all the data of json file to it.

def translate(word):	
#The word which is passed as arguement will be searched in data dictionary
#And the value corresponding to that key(word) is returned.
	if word.lower() in  data:
		return data[word.lower()]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
#The get_close_matches() functions have 4 arguement 2 of them are default
#we need to pass a word(string) as first and second a list of string.
#optional arguements are n(number of closest matcing element in list)
#and the search ratio
#It returns a list of words which are closer to the searched arguements. 
#If not any word is foud it return an empty list
#It uses matching ratio to search for similar words
	elif len(get_close_matches(word,data.keys()))>0:
		yn= input("Did you mean %s instead?\nPress Y if yes,or N if no :" % get_close_matches(word,data.keys())[0])
		if yn.upper() == 'Y':
			return data[get_close_matches(word,data.keys())[0]]
		elif yn.upper() == 'N':
			return "The word doesn't exist please re-check it."
		else:
			return "We doesn't understand your entry."
#otherwise the else part is executed and the message is returned.
	else:
		return "This word doesn't exist."


word=input("Enter Data :")

#Here, word is a global varriable that takes input from user

output=translate(word)
if type(output) == list:
	for item in output:
		print(f"{word.title()}: "+item+"\n")
else:
	print(output)