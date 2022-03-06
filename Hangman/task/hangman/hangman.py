import random
import sys


def find_indexes(string, character):
    return [i for i, v in enumerate(string) if v == character]


def main():
    print('H A N G M A N')
    while True:
        jogar = input('Type "play" to play the game, "exit" to quit: ')
        if jogar == "exit":
            sys.exit()
        elif jogar == "play":
            break
    list_of_words = ["python", "java", "kotlin", "javascript"]
    choice = random.choice(list_of_words)
    hidden_word = choice.replace(choice[:], "-" * len(choice))
    guessed_letters = set()
    lives = 8
    while lives > 0:
        if "-" not in hidden_word:
            print(hidden_word)
            print("You guessed the word!\nYou survived!")
            sys.exit()
        print()
        print(hidden_word)
        letter = input(f'Input a letter: ')
        if not len(letter) == 1:
            print('You should input a single letter')
            continue
        if not letter.islower():
            print('Please enter a lowercase English letter')
            continue
        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue
        elif letter in choice:
            indexes = find_indexes(choice, letter)
            hidden_word_list = list(hidden_word)
            for index in indexes:
                hidden_word_list[index] = letter
            hidden_word = "".join(hidden_word_list)
            guessed_letters.add(letter)
        elif letter not in choice:
            lives -= 1
            print("That letter doesn't appear in the word")
            guessed_letters.add(letter)
    print("You lost!")
    main()


if __name__ == '__main__':
    main()
