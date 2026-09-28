word = input("Enter the letters: ")
lowercase_word = ""

for characters in word:
    if 'A' <= characters <= 'Z':
        lowercase_word += chr(ord(characters) +32)
    else:
        lowercase_word += characters
print(lowercase_word)
