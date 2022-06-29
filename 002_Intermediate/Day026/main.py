import pandas

data = pandas.read_csv("./Day026/nato_phonetic_alphabet.csv")

letters = { row.letter : row.code for (index, row) in data.iterrows()}

word = input("Enter a word? ").upper()

result = [letters[letter] for letter in word]

print(result)