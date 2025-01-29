import random

coin_flip = random.randint(1, 100)
coin_flip = int(coin_flip)
if coin_flip > 50:
    print("Heads")
else:
    print("Tails")

