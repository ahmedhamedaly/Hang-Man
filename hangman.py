import random

# printHangman(state)
# @parameters: state
# @return: Hangman Board
# This method prints out the Hangman board based on state


def printHangman(state):
    hangman = {
        0:       "   ____\n"
                 "  |    |\n"
                 "  |    \n"
                 "  |   \n"
                 "  |    \n"
                 "  |   \n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",

        1:       "   ____\n"
                 "  |    |\n"
                 "  |    o\n"
                 "  |   \n"
                 "  |    \n"
                 "  |   \n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",

        2:       "   ____\n"
                 "  |    |\n"
                 "  |    o\n"
                 "  |    |\n"
                 "  |    |\n"
                 "  |    \n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",

        3:       "   ____\n"
                 "  |    |\n"
                 "  |    o\n"
                 "  |   /|\n"
                 "  |    |\n"
                 "  |    \n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",

        4:       "   ____\n"
                 "  |    |\n"
                 "  |    o\n"
                 "  |   /|\\\n"
                 "  |    |\n"
                 "  |    \n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",

        5:       "   ____\n"
                 "  |    |\n"
                 "  |    o\n"
                 "  |   /|\\\n"
                 "  |    |\n"
                 "  |   /\n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",

        6:       "   ____\n"
                 "  |    |\n"
                 "  |    o\n"
                 "  |   /|\\\n"
                 "  |    |\n"
                 "  |   / \\\n"
                 " _|_\n"
                 "|   |______\n"
                 "|          |\n"
                 "|__________|\n",
    }
    return hangman.get(state, "Game Over")

# printGuess(word, correct)
# @parameters: word, correct
# @return: word
# Takes in the word to guess and the correct guesses and returns the word revealed in the right format


def printGuess(word, correct):
    output = "Word: "
    for i in range(len(word)):
        guessNotThere = 1
        for j in range(len(correct)):
            if word[i] == correct[j]:
                output += word[i] + " "
                guessNotThere = 0
                break
        if guessNotThere:
            output += "_ "
    return output

# handleInput(word)
# @parameters: word
# @return: guess, valid
# Takes a letter guess from the user and returns 1 if its in the word and 0 if its not


def handleInput(word):
    guess = input("Enter a letter: ")

    for i in word:
        if guess[0] is i:
            return guess, 1
    return guess, 0


def main():
    state = 0
    correct = ""
    wrong = ""
    game = 1

    dictionary = open("words.txt").readlines()
    word = dictionary[random.randint(0, len(dictionary))][:-1]
    print("The word is " + word)

    while game:
        print(printHangman(state))
        print("Wrong: " + wrong)
        print(printGuess(word, correct))

        newGuess, correctGuess = handleInput(word)

        if not correctGuess:
            state += 1
            wrong += newGuess
        else:
            correct += newGuess

        if len(word) == len(correct):
            print("\n-----------------------------\n"
                  "You have won, Congratulations\n"
                  "-----------------------------")
            exit(0)

        if state == 6:
            print("\n-------------------------------------\n"
                  "You have lost, The word was " + word + "\n" +
                  "-------------------------------------")
            exit(0)


if __name__ == '__main__':
    main()
