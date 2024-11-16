import random

def guessing_game(list):
    #used to check for integer inputs by user
    int_checker = [f"{i}" for i in range(10)]
    
    #picks random word from list passed in
    secret_word = random.choice(list)

    #creating an 'empty' word with underscores per letter in the secret_word
    placeholder = ["_" for i in secret_word]
    
    #prints length of secret_word
    print(f"The word I'm thinking of has {len(secret_word)} letters. Start guessing letters!\n")

    #initializing correct and incorrect guesses into empty lists
    correct_guesses = []
    incorrect_guesses = []

    #while loop for going through guesses till correct word is formed 
    while secret_word != "".join(placeholder):
        guess = input("Enter guess: ").lower().strip()
        if guess == '':
            break
        elif len(guess) > 1:
            print("Sorry, only one letter guesses, okay?")
        elif guess in int_checker:
            print("Sorry, please only use letters, not integers.")
        elif guess in correct_guesses or guess in incorrect_guesses:
            print("You already guessed that letter! And don't worry, there are no duplicate letters in these words.")
        elif guess in secret_word:
            correct_guesses.append(guess)
            index = index_finder(secret_word, guess)
            placeholder[index] = guess
            print(f"Nice that's correct! Here's what you got from the word so far: {"".join(placeholder)}\nThese are the letters you've guessed correctly:\n{correct_guesses}\n")
            print(f"Your total guesses: {len(correct_guesses) + len(incorrect_guesses)}\nYour correct guess count is: {len(correct_guesses)}\nYour inccorect guess count is: {len(incorrect_guesses)}\n")
        elif guess not in secret_word:
            incorrect_guesses.append(guess)
            print(f"Oof! Sorry that's not in the word, here are your incorrect guesses:\n{incorrect_guesses}\nThis is what the word looks like right now:{"".join(placeholder)}\n")
            print(f"Your total guesses: {len(correct_guesses) + len(incorrect_guesses)}\nYour correct guess count is: {len(correct_guesses)}\nYour inccorect guess count is: {len(incorrect_guesses)}\n")
    
    print(f"Woot! Woot! You got it! Here are your final results:\nWord was: {secret_word}")
    print(f"Your total guesses: {len(correct_guesses) + len(incorrect_guesses)}\nYour correct guess count is: {len(correct_guesses)}\nYour inccorect guess count is: {len(incorrect_guesses)}\n")
    question = input("Would you like to go again? [Y/N]").lower().strip()
    if question == "" or question == "y":
        print("Sweet! Let's go again.")
        guessing_game(list)
    else:
        print("Thanks for playing! Come back anytime.")

#returns index position for swapping underscore with guess
def index_finder(word, letter):
    location = 0
    for i in word:
        if i == letter:
            break
        else:
            location += 1
    return location

def main():
    #list of words for program to choose from
    word_bank = ["mario", "metroid", "zelda", "nes", "sega", "sony", "dk", "sekiro", "darksoul", "zombies"]
    
    #welcome message
    print("Welcome to the Video Game edition of Hangman!\nHere are some rules to be aware of:\n   1. Please only enter 1 letter at a time.\n   2. There will be no punctuation or integers in these words.\n   3. Don't worry about being case sensitive! We'll cover that for you.\n   4. Please have fun!\nWith that out of the way, let's begin!")
    guessing_game(word_bank)


if __name__ == '__main__':
    main()