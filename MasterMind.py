
import random

class Master_game:
    def __init__(self) -> None:
        self.sequence_length = 0
        self.colors =["r", "b", "g", "y"]
        self.solution = []
        self.guess = []
        self.game_won = False
        self.guess_count = 0

    def get_length(self) -> None:
        print("Please enter a number between 4 and 10 to be the length of the code.")
        while True:
            try:  
                new_length = int(input())
            except ValueError:
                print("Please enter a number.")
                continue
            if new_length >= 4 and new_length <= 10:
                break
            else:
                print("Out of range!")
        self.sequence_length = new_length

    def make_solution(self) -> None:
        self.solution = [random.choice(self.colors) for i in range(self.sequence_length)]

    def get_guess(self) -> None:
        while True:
            guess_string = input(f"Please enter a sequence of {self.sequence_length} characters. Possible characters are r, b, g, or y.\n")
            guess_list = [char for char in guess_string]
            if all(char in self.colors for char in guess_list) and len(guess_list) == self.sequence_length:
                break
            print("invalid guess.") #plan to add functionality to specify which condition is invalid
        print("Valid guess.")
        self.guess = guess_list

    def get_comparison(self) -> None:
        feedbacker = ""
        for i in range(self.sequence_length):
            if self.solution[i] == self.guess[i]:
                feedbacker += "2"
            elif self.guess[i] in self.solution:
                feedbacker += "1"
            else:
                feedbacker += "0"
        if feedbacker == "2"*self.sequence_length:
            print("Congratulations! You won!")
            self.game_won = True
        else:
            print("A 0 means your character isn't in the solution. A 1 means it's in the solution, but in the wrong position. A 2 means it's in the correct position.")
            #real sloppy. fix this
            print(feedbacker)


def play_game()-> None:
    while True:
        new_game = Master_game()
        new_game.get_length()
        new_game.make_solution()
        while not new_game.game_won:
            new_game.get_guess()
            new_game.get_comparison()
        while True:
            replay = input("Play again? y/n\n")
            if replay == "y" or replay == "n":
                break
            print("Please answer y or n")
        if replay == "n":
            return

play_game()



