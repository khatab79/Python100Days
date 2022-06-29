import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():

    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError as error:
        print(error)
        print("Accept only text. Please, no numbers, no space and no symbols.")
        generate_phonetic()

    else:
        print(output_list)


generate_phonetic()

# word = input("Enter a word: ").upper()

# is_text = True
#
# while is_text:
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#
#     except KeyError as error:
#         print("Accept only text. Please, no numbers and no symbols.")
#         word = input("Enter a word: ").upper()
#
#     else:
#         print(output_list)
#         is_text = False
