# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open("Input/Names/invited_names.txt", "r")
letter = open("Input/Letters/starting_letter.txt", "r")
content = letter.read()
a = names.readlines()

for name in a:
    l = len(name)
    real = name[:l-1]
    output = content.replace("[name]", real)
    output.strip()
    # either use .strip or slicing to remove \n
    f_name = "Output/ReadyToSend/letter_to_"+real+".txt"
    with open(f_name, "w") as file:
        file.write(output)
names.close()
letter.close()
