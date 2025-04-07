#
# Name Vincent Leahy
# Date 4/6/2026
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#for the main entry point of the program
import random

#a function needed to read responses from the file 8_ball_responses.txt
def load_responses(filename):
        with open(filename, 'r') as file:
            responses = file.readlines()
        return [response.strip() for response in responses]

#Simulating the magic 8 ball
def magic_8_ball():
    responses = load_responses('8_ball_responses.txt') 
    print('I am a magic 8 ball! Try me out!!')

    while True:
        #have the user ask a question
        question = input("Ask a yes or no questions (or type 'quit' to exit): ")

        #if user types exit

        if question.lower() == 'quit':
            print('Goodbye, see you soon!')
            break

        #Display the responses from the file.
        answer = random.choice(responses)
        print(f'The magic 8 ball speaks: {answer}')

#main point of entry 
def main():
    magic_8_ball()

#Making sure the script runs the main() function when executed directly
if __name__ == '__main__':
    main()