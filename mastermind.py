import copy
import random


class Mastermind:
    def __init__(self):
        self.positions = 10
        self.colors = 8

    def set_positions(self, positions):
        self.positions = positions

    def set_colors(self, colors):
        self.colors = colors

    def play(self):
        list_col = [str(i) for i in range(1, self.colors + 1)]
        code_list = []
        rounds = 0
        for i in range(self.positions):
            ball = random.choice(list_col)
            code_list.append(ball)

        print(f"Playing Mastermind with {self.colors} colors "
              f"and {self.positions} positions")

        while True:
            guess = str(input("What is your guess?: "))
            print(f"Your guess is {guess}")
            guess_list = [i for i in guess]
            star_count = 0
            o_count = 0
            rounds += 1
            code_list_copy = copy.deepcopy(code_list)
            for i in range(len(guess_list)):
                if guess_list[i] in code_list_copy:
                    if guess_list[i] == code_list[i]:
                        star_count += 1
                    else:
                        o_count += 1
                    code_list_copy.remove(guess_list[i])
            print(("*" * star_count) + ("o" * o_count))
            print()
            if star_count == 4:
                print(f"You solve it after {rounds} rounds")
                break


game = Mastermind()
print("Welcome to The Mastermind Game! (˶ᵔ ᵕ ᵔ˶)₊˚⊹♡")

adjust_or_not = str(input("Do you want to adjust the game?(y/n): "))
if adjust_or_not == "y":
    positions = int(input("Numbers of positions: "))
    colors = int(input("Numbers of colors: "))
    game.set_positions(positions)
    game.set_colors(colors)

while True:
    play_or_not = str(input("Do you want to play the game?(y/n): "))
    if play_or_not == "y":
        game.play()
        print()
    else:
        print("Thank you for playing! (˵ •̀ ᴗ - ˵ ) ✧")
        break


