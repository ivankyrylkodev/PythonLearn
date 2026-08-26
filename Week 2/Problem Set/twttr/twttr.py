input_text = input("Input: ")

for letter in input_text:
    if letter.lower() in "aeiou":
        input_text = input_text.replace(letter, "")

print("Output: ", input_text)