#NAME: select.py
#DATE: 31/03/2019

import json
import time
import random

#Open Movie File
marvelMovies = open('movies.json').read()
marvel = json.loads(marvelMovies)

#Select Random Phase
print("Selecting a Marvel Phase.")
time.sleep(4)
phases = len(marvel['marvel'])
phase = random.randint(0, phases-1)
print("Selecting a movie from Phase "+str(marvel['marvel'][phase]['phase'])+".")

#Select Movie from phase
phaseTitles = marvel['marvel'][phase]['movies']
titles = len(phaseTitles)
title = random.randint(0, titles-1)
time.sleep(4)
print("You should watch "+str(phaseTitles[title]['title'])+".")


