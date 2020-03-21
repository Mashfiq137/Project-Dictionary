import json
from difflib import get_close_matches as gcm 

data = json.load(open("Data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(gcm(word,data.keys()))> 0:
		decision = input("Did you mean %s instead?Enter Y if yes, or N if no: " %gcm(word,data.keys())[0])
		if decision == "Y":
			return data[gcm(word,data.keys())[0]]
		elif decision == "N":
			return "The word doesn't exist. Please double check it."
		else :
			return "Invalid query. Try again" 	

	else:
		
		return "The word you entered does not exist. Please try again."

word = input("Enter a word : ")
output = translate(word)
if type(output) == list:
	for item in output:
		print(item)
else :
	print(output) 