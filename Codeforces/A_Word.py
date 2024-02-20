word_array = input().split()

capital_positions = [[i for i, char in enumerate(
    word) if char.isupper()] for word in word_array]

small_positions = [[i for i, char in enumerate(
    word) if char.islower()] for word in word_array]


if len(capital_positions[0]) > len(small_positions[0]):
    word_array = [word.upper() for word in word_array]
else:
    word_array = [word.lower() for word in word_array]

print("".join(word_array))
