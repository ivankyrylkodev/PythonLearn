import random

while True:
    try:
        level = int(input("Level: ").strip())
        if level < 1:
            raise ValueError
        break
    except ValueError:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: ").strip())
        if guess < 1:
            raise ValueError
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue

