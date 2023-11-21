# create folders
# create starting letter
# create invited names
# for each name construct a letter


### Create folders
# import os
#
# letters_folder_path = "Input/Letters" # if a parent folder doesn't exist, it will be created
# names_folder_path = "Input/Names"
# output_folder_path = "Output/ReadyToSend"
#
# os.makedirs(letters_folder_path, exist_ok=True)
# os.makedirs(names_folder_path, exist_ok=True)
# os.makedirs(output_folder_path, exist_ok=True)

### Read from files
with open("Input/Letters/starting_letter.txt") as start_file:
    start_letter = start_file.read()

with open("Input/Names/invited_names.txt") as name_file:
    names = [line.strip() for line in name_file.readlines()]

for name in names:
    letter_text = start_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as output_letter:
        output_letter.write(letter_text)



