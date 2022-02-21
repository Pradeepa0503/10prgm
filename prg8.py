#8.	Write a program to convert lowercase vowel to uppercase in string.
def convowtoupp(phrase):
    new_phrase = ""
    for letter in phrase:
        if letter in ['a', 'e', 'i', 'o', 'u'] :
            new_phrase += letter.upper()
        else:
            new_phrase += letter.lower()
    return new_phrase
print(convowtoupp(input("Enter a phrase: ")))
 