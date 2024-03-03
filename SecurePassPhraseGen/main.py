import json
import time
import secrets
import hashlib

from typing import Iterable

with open("worlds.json", 'r') as f:
    worlds = json.loads(f.read())['worlds']

def algorithm(worlds: Iterable = worlds) -> tuple:
    rand_number = 0
    phrase = ""

    n = secrets.choice(range(10, 30))

    while n > 1:
        rand_number = secrets.randbelow(11)

        if rand_number % 2 == 0:
            phrase += secrets.choice(worlds).title() + ' '
        else:
            phrase += secrets.choice(worlds) + ' '  

        n -= 1
    
    return phrase, hashlib.sha512(phrase.encode()).hexdigest()
