import pandas

data = pandas.read_csv('morse_code.csv')
new_dict = {row.character:row.code for (index, row) in data.iterrows()}
morse_codes = list(new_dict)
print(morse_codes)

def code_morse():
    phrase = input('Enter phrase to transform into Morse code: ').upper()
    for character in phrase:
        if character in morse_codes:
            print(character, new_dict[character])
        else:
            print("Sorry, that's not a valid Morse code.")

code_morse()