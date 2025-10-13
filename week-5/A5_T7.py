def main():
    print("Program starting.")

    words = collectwords()
    analysewords(words)

    print("Program ending.")

def collectwords():
    words = []
    while True:
        word=input("Insert word (empty stops): ")
        if word == "":
            break
        words.append(word) #adds each inputted word into words list
    return DELIMITER.join(words) #returns words list as one string with delimiter "," between each word
    
def analysewords(wordstring):
    wordlist = wordstring.split(DELIMITER) #splits list into substrings with delimiter between each one
    wordcount = len(wordlist)
    charcount = sum(len(word) for word in wordlist) #calculates the length of each word in wordlist and adds it all up
    avg = charcount / wordcount

    print(f"- {wordcount} Words")
    print(f"- {charcount} Characters")
    print("- {:.2f} Average word length" .format(avg))
    return None

DELIMITER = ","

main()