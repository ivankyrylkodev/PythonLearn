import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        answer = a + b
        print(f"{a} + {b} = ", end="")
        for i in range(3):
            try:
                user_answer = int(input().strip())
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        print(f"{a} + {b} = {answer}")
                    else:
                        print(f"{a} + {b} = ", end="")
            except ValueError:
                print("EEE")
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level < 1 or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    return random.randint(1, 10 ** level)


if __name__ == "__main__":
    main()