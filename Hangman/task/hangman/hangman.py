# Write your code here
import random
from string import ascii_lowercase


class Hangman:
    dictionary = ['python', 'java', 'kotlin', 'javascript']
    no_such_letter = 'No such letter in the word'
    already_typed = 'You already typed this letter'
    not_ascii = 'It is not an ASCII lowercase letter'
    print_single = 'You should print a single letter'

    def __init__(self):
        self.title = "H A N G M A N"
        self.correct = random.choice(Hangman.dictionary)
        self.correct_set = set(self.correct)
        self.guessed_set = set()
        self.inputted_set = set()
        self.hint = None
        self.attempts = 8

    def start(self):
        print(self.title)
        self.menu()

    def menu(self):
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == "play":
            self.game()
        elif choice == "exit":
            return
        else:
            self.menu()

    def game(self):
        while self.attempts:
            self.print_guessed()
            self.attempt()
        if self.guessed_set == self.inputted_set:
            print(f"You guessed the word {self.correct}!")
            print("You survived!")
        else:
            print('You are hanged!')
        print()

    def print_guessed(self):
        self.hint = ""
        for letter in self.correct:
            self.hint += letter if letter in self.guessed_set else "-"
        print()
        print(self.hint)

    def attempt(self):
        string = input("Input a letter: ")

        if len(string) > 1:
            print(self.print_single)
        elif string in self.inputted_set:
            print(self.already_typed)
        elif string not in ascii_lowercase:
            print(self.not_ascii)
        elif string in self.correct_set:
            self.guessed_set.add(string)
            self.inputted_set.add(string)
            if self.guessed_set == self.inputted_set:
                self.attempts = 0
        else:
            self.inputted_set.add(string)
            print(self.no_such_letter)
            self.attempts -= 1


game = Hangman()
game.start()
