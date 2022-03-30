

def blackListCharacters(characterArray, word):
    for char in word:
        for bChar in characterArray:
            if char is bChar:
                return False
    return True





wordlistFile = open("Wordlist.txt", "r")

word = wordlistFile.readline()

words = [word]

while word != "":
    words.append(word)
    word = wordlistFile.readline()

blacklistCharacterArray = ['a','e','i','o','u','y']
count = 0

for word in words:
    if blackListCharacters(blacklistCharacterArray, word):
        count+=1
        print(word)
print(count)