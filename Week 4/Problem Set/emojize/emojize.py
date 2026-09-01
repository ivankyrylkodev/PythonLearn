import emoji

input_emoji = input("Input: ").strip()
print("Output:", emoji.emojize(input_emoji, language='alias'))