import sys

    # search the characters in the user input and find
    # matches in the dictionary wordlist
def contains(splitUI, word):
    word = word.lower()
    letters = []
    for letter in splitUI:
        letters.append(letter)
    for char in word:
        for letter in letters:
            if char == letter:
                letters.remove(letter)
                break
    if not letters:
        return True
    else:
        return False


    # Grab string from user 
if len(sys.argv) == 2:
    uI = sys.argv[1]
    uI = uI.lower()
else:
    print("Invalid amount of arguments! Quitting...")
    quit()

    # Path to wordlist
grabWL = "/usr/share/dict/american-english"

dict = open(grabWL)
text = dict.read()
dict.close()
    # Splits the wordlist by line,
    # separating each individual word
wordList = list(text.split())

    # Separates user input into an array of
    # individual characters
splitUI = list(uI)

counter = 0

    # Lists the words
for word in wordList:
    if contains(splitUI, word):
        print(word)
        counter += 1

# print("-" * 17)
print("-----------------")
print(f'Found {counter} results')
