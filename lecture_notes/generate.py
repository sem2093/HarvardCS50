import random

coin = random.choice(["heads", "tails"])
print(coin)

# refine import and remove random from random.choice 
from random import choice

coin = choice(["heads", "tails"])
print(coin)

# randomly generate a number between 1 and 10

import random

number = random.randint(1, 10)
print(number)

# shuffle cards
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
  
