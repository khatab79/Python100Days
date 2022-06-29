
new_letter = ""

with open("./Day024/MailMergeProjectStart/Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()

with open("./Day024/MailMergeProjectStart/Input/Names/invited_names.txt") as names:    
    list_of_names = names.readlines()

for name in list_of_names:
    new_name = name.strip()
    # print(starting_letter) 
    new_letter = starting_letter.replace("[name]", new_name)   
    # print(new_letter)

    with open(f"./Day024/MailMergeProjectStart/Output/ReadyToSend/{new_name}.txt", mode="w") as letter:
        letter.write(new_letter)