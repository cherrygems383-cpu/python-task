word = input("Enter the letters: ")
uppercase_word = ""

for characters in word:
    if 'a' <= characters <= 'z':
        uppercase_word += chr(ord(characters) -32)
    else:
        uppercase_word += characters
print(uppercase_word)
