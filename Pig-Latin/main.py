#
# Name Vincent Leahy
# Date 4/13/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#Function to convernt words into pig latin utilizing the "AY"
def to_pig_latin(word):
    if len(word) > 1:
        return word[1:] + word[0] + "AY"
    else:
        return word + "AY"

#Function to convert sentence into pig latin
def convernt_sentence_to_pig_latin(sentence):
    words = sentence.upper().split()
    pig_latin_words = [to_pig_latin(word) for word in words]
    return " ".join(pig_latin_words)

#Function to promt the user and to take user sentence and convert into pig latin
def main():
    english_sentence = input("Enter a sentence in English: ")
    pig_latin_sentence = convernt_sentence_to_pig_latin(english_sentence)
    print("Pig Latin:", pig_latin_sentence)

# Run the main function
if __name__ == "__main__":
    main()