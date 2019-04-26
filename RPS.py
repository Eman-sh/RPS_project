import random


moves = ["rock", "paper", "scissors"]


class Player:

    def __init__(self):
        self.points = 0

    def move(self):
        return "rock"

    def learn(self, the_move):
        pass


class HumanPlayer(Player):

    def move(self):
        make_move = input("rock, paper, scissors? \n")
        while make_move != "rock" and make_move != "paper" \
                and make_move != "scissors":
            print(" *** Invalid option, try again ***\n")
            make_move = input("rock, paper, scissors? \n")
        return make_move


class RandomPlayer(Player):
    def move(self):
        make_move = random.choice(moves)
        return make_move


class ReflectPlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.the_move = None

    def move(self):
        if self.the_move is None:
            make_move = moves[0]
        else:
            make_move = self.the_move
            return make_move

    def learn(self, the_move):

        self.the_move = the_move


class CyclePlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        if self.step == 0:
            make_move = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            make_move = moves[1]
            self.step = self.step + 1
        else:
            make_move = moves[2]
            self.step = self.step + 1
        return make_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_single(self):
        print("Rock Paper Scissors, Start Game!\n")
        print(f"Round 1 of 1:")
        self.play_round()
        if self.p1.points > self.p2.points:
            print("*** YOU WON -_-' ***")
        elif self.p1.points < self.p2.points:
            print("*** COMPUTER WON ^-^ ***")
        else:
            print("***** TIE *****")
        print(" FINAL SCORE " + str(self.p1.points) +
              " To " + str(self.p2.points))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        count = Game.game_rules(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_game(self):
        print("Rock Paper Scissors, Start Game!\n")
        for round in range(3):
            round += 1
            print("Round: " + str(round))
            self.play_round()
        if self.p1.points > self.p2.points:
            print("*** YOU WON -_-' ***")
        elif self.p1.points < self.p2.points:
            print("** GAME OVER! **")
        else:
            print("***** TIE *****")
        print(" You:" + str(self.p1.points) + " X " +
              "Computer:"+str(self.p2.points))

    def game_rules(self, move1, move2):
        print(f"You: {move1} \n")
        print(f"Computer: {move2} \n")
        if beats(move1, move2):
            print("** you got a point **")
            print(f"YOU:{move1} \nCOMPUTER:{move2} \n")
            self.p1.points += 1

        elif beats(move2, move1):
            print("** GAME OVER! **")
            print(f"YOU:{move1} \nCOMPUTER:{move2} \n")
            self.p2.points += 1

        else:
            print("***** TIE *****")
            print(f"YOU:{move1} \nCOMPUTER:{move2} \n")
            return 0


if __name__ == '__main__':
    Players = [Player(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    p2 = input("Game mode: [1]Easy, [2]Normal, [3]Hard " +
               "\n" + "or Enter any key for Random: " + "\n")

    while True:
        if p2 == '1':
            p2 = Player()
        elif p2 == '2':
            p2 = CyclePlayer()
        elif p2 == '3':
            p2 = ReflectPlayer()
        else:
            p2 = random.choice(Players)
        break

    game = input("Enter [1] for Single game or [2] for Multiple: \n")
    Game = Game(p2)
    while True:
        if game == "1":
            Game.play_single()
            break
        elif game == "2":
            Game.play_game()
            break
        else:
            print(" *** Invalid option, try again ***\n")
            rounds = input("Enter [1] for Single game or [2] for Multiple: \n")
