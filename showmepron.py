#!/usr/bin/env python3
import random
import requests

COLLECTION_URL = "https://www.roysac.com/asciinudes/NudeArray.txt"
NUDE_URL_FMT = "https://www.roysac.com/asciinudes/{}"

if __name__ == "__main__":
    r = requests.get(COLLECTION_URL)
    lines = [l.strip() for l in r.text.split('\n')]
    line = random.choice(lines[1:])
    name = line.split('|')[5]
    r = requests.get(NUDE_URL_FMT.format(name))
    print(r.text.strip())
