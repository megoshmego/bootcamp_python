main.py

import random

import requests


def get_list_of_words():
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=10
    )

    string_of_words = response.content.decode('utf-8')

    list_of_words = string_of_words.splitlines()
    print(list_of_words)

    return list_of_words


words = get_list_of_words()

random_word = random.choice(words)
print(random_word)
