import requests
import random
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("The Dad 2.0")
header = colored(header, color = "green")
print(header)
url = "https://icanhazdadjoke.com/search"

name = input("Want to hear a joke? About what? ")


response = requests.get(
	url,
	headers = {"Accept":"application/json"},
	params={"term":name}
)

data = response.json()

if len(data["results"]) == 0:
	print ("Sorry, I don't know any jokes about that... Try something else.")
elif len(data["results"]) == 1:
	print (data["results"][0]["joke"])
else:
	a = random.randint(0,len(data["results"]))	
	print (data["results"][a]["joke"])
