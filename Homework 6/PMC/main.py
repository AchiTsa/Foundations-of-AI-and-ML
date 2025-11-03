import copy
import random
from enum import Enum


class Decision(Enum):
    WIN = 1
    DRAW = 0
    LOSS = -1


class Participants(Enum):
    Computer = 'O'
    Player = 'X'
    NoOne = 'F'


# will use a pair  to indicate where to put the next stone for one player
# ("playerXYZ", X: 0(left) - 6(right))


def pure_mc(pos, N=200):
    # all moves from starting position
    # my_side = pos["to_move"]
    initial_moves = moves(pos)
    # win counters per move
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            # make random moves until the game is over
            res = simulate(pos, move)
            if res == Decision.WIN:
                win_counts[move] += 1
            elif res == Decision.DRAW:
                win_counts[move] += 0.5
            elif res == Decision.LOSS:
                win_counts[move] += -1

    # find the move with the highest number of wins, return it
    return Participants.Computer, max(win_counts, key=win_counts.get)
    # ...


# TODO
def simulate(pos, move):
    comp_turn = True
    pos_sim = copy.deepcopy(pos)
    move_sim = Participants.Computer, move
    pos_sim = make_move(pos_sim, move_sim)
    while True:
        if is_over(pos_sim)[0]:
            if is_over(pos_sim)[1] == Participants.Computer:
                return Decision.WIN
            if is_over(pos_sim)[1] == Participants.NoOne:
                return Decision.DRAW
            if is_over(pos_sim)[1] == Participants.Player:
                return Decision.LOSS

        if comp_turn:
            comp_turn = False
        else:
            comp_turn = True

        sim_moves = moves(pos)

        if comp_turn:
            move = random.choice(sim_moves)
            move_sim = Participants.Computer, move
            pos_sim = make_move(pos_sim, move_sim)
        else:
            move = random.choice(sim_moves)
            move_sim = Participants.Player, move
            pos_sim = make_move(pos_sim, move_sim)

    return 0


def moves(pos):
    if "|       |" == pos[0]:
        return [1, 2, 3, 4, 5, 6, 7]
    pos_moves = []
    for i in range(len(pos[0])):
        if pos[0][i] == " ":
            pos_moves.append(i)
    # returning already right numbers from 1-7
    return pos_moves


def dump_pos(pos):
    for line in pos:
        print(line)
    return 0


# will use a pair to indicate where to put the next stone for one player
# ("playerXYZ", X: 1(left) - 7(right))
def parse_move(movestr):  # movestr is the X number

    return Participants.Player, int(movestr) + 1


def make_move(pos, move):
    for i in range(len(pos)):
        if pos[i][move[1]] != " ":
            pos[i - 1] = pos[i - 1][:move[1]] + \
                         move[0].value + pos[i - 1][move[1] + 1:]
            return pos
    return pos


def is_over(pos):
    player_won = 0
    computer_won = 0
    # check horizontal
    for i in range(len(pos[0])):  # check every section from 0 - 6 in every row
        for row in pos:
            if row[i] == "O":
                computer_won = computer_won + 1
                player_won = 0
            elif row[i] == "X":
                player_won = player_won + 1
                computer_won = 0
            else:
                computer_won = 0
                player_won = 0
            if player_won == 4 or computer_won == 4:
                if player_won == 4:
                    return True, Participants.Player
                else:
                    return True, Participants.Computer
    # check vertical
    for row in pos:
        for i in range(len(pos[0])):
            if row[i] == "O":
                computer_won = computer_won + 1
                player_won = 0
            if row[i] == "X":
                player_won = player_won + 1
                computer_won = 0
            else:
                computer_won = 0
                player_won = 0
            if player_won == 4 or computer_won == 4:
                if player_won == 4:
                    return True, Participants.Player
                else:
                    return True, Participants.Computer
    # check diagonal
    all_diagonals = [
        # lower left to upper right
        pos[3][0] + pos[2][1] + pos[1][2] + pos[0][3],
        pos[4][0] + pos[3][1] + pos[2][2] + pos[1][3] + pos[0][4],
        pos[5][0] + pos[4][1] + pos[3][2] + pos[2][3] + pos[1][4] + pos[0][5],
        pos[5][1] + pos[4][2] + pos[3][3] + pos[2][4] + pos[1][5] + pos[0][6],
        pos[5][2] + pos[4][3] + pos[3][4] + pos[2][5] + pos[1][6],
        pos[5][3] + pos[4][4] + pos[3][5] + pos[2][6],
        # upper left to lower right
        pos[0][3] + pos[1][4] + pos[2][5] + pos[3][6],
        pos[1][0] + pos[2][1] + pos[3][2] + pos[4][3] + pos[5][4],
        pos[0][0] + pos[1][1] + pos[2][2] + pos[3][3] + pos[4][4] + pos[5][5],
        pos[0][1] + pos[1][2] + pos[2][3] + pos[3][4] + pos[4][5] + pos[5][6],
        pos[0][2] + pos[1][3] + pos[2][4] + pos[3][5] + pos[4][6],
        pos[2][0] + pos[3][1] + pos[4][2] + pos[5][3]
    ]
    for word in all_diagonals:
        if "XXXX" in word:
            return True, Participants.Player
        elif "OOOO" in word:
            return True, Participants.Computer

    # any option left == any space in array left
    whole_game_table = ""
    if ' ' not in pos[0]:
        return True, Participants.NoOne
    return False, Participants.NoOne


def play_game(pos, player, player_side="X"):
    playing = True
    while playing:
        if player:
            # print the position
            dump_pos(pos)
            movestr = input("Your move? ")
            while int(movestr) > 6 or int(movestr) < 0:
                print("Value is too big or small, values between 0 up to 6 are allowed")
                movestr = input("Your move? ")
            # convert user input into the move format you are using internally
            move = parse_move(movestr)
            player = False
        else:
            move = pure_mc(pos)
            player = True

        pos = make_move(pos, move)
        # check after each move
        if is_over(pos)[0]:
            dump_pos(pos)
            print("The winner is: ", is_over(pos)[1])
            playing = False


if __name__ == '__main__':
    player = True
    starting_pos = [
        "|       |",  # 0
        "|       |",  # 1
        "|       |",  # 2
        "|       |",  # 3
        "|       |",  # 4
        "|       |",  # 5
        "|0123456|",  # 6
    ]
    starting_pos1 = [
    "| X     |",
    "| X     |",
    "| XX    |",
    "| OO    |",
    "|OXO  X |",
    "|OXOXOXO|",
    "|0123456|"]
    #print(is_over(starting_pos1))
    #pure_mc(starting_pos1)
    #print(is_over(starting_pos))
    play_game(starting_pos, player)
