import random
import json
import requests

def handle_response(message):
    input = message.lower()

    if input == "!":
        return "Type a valid command."
    
    elif input == "!help":
        return "\nThis shows how to use the bot. Type a command with '!<command>' to get started. To send a private message, type '?!<command>'.\t\nThese are the commands below:\n\t-'hello'\n\t-'roll'\n\t-'fact'\n\t-'insult'"

    elif input == "!hello":
        return "Hey there!"

    elif input == "!roll":
        return str(random.randint(1, 6))

    elif input == "!fact":
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.request("GET", url)
        data = json.loads(response.text)

        return data['text']
    
    elif input == "!insult":
        insults = ["you're a loser", "you smell", "you stink"]
        return str(random.choice(insults))
