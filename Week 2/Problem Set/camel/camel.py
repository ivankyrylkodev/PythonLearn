def main():
    sentense = input("camelCase: ")
    print("snake_case:", snake_case(sentense))

def snake_case(words):
    for letter in words:
        if letter.isupper():
            words = words.replace(letter, "_" + letter.lower())
    return words

main()