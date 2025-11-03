from time import sleep

from select import select
import numpy
from copy import copy, deepcopy
import sys


class NQPosition:

    def __init__(self, N):

        # choose some internal representation of the NxN board
        # put queens on it
        if N < 4:
            sys.exit("Dimension is too small")

        # 4D tests

        #N = 4
        #self.Dimension = N

        #self.field = [[0, 0, 1, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 4, 0, 0]]
        #elf.queens = [(0, 2), (1, 1), (2, 2), (3, 1)]

        #self.field = [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        #self.queens = [(0, 0), (0, 1), (0, 2), (0, 3)]

        # unslolveable
        # self.field = [[1, 0, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 4]]
        # self.queens = [(0, 0), (0, 3), (3, 0), (3, 3)]

        ###########################################################
        N = 8
        self.Dimension = N
        # solveable
        self.field = [
            [
                1, 2, 3, 4, 5, 6, 7, 0], [
                0, 0, 0, 0, 0, 0, 0, 0], [
                0, 0, 0, 0, 0, 0, 0, 0], [
                    0, 0, 0, 0, 0, 0, 0, 0], [
                        0, 0, 0, 0, 0, 0, 0, 0], [
                            0, 0, 0, 0, 0, 0, 0, 0], [
                                0, 0, 0, 0, 0, 0, 0, 0], [
                                    0, 0, 0, 0, 0, 0, 0, 0]]
        self.queens = [(0, 0), (0, 1), (0, 2), (0, 3),
                       (0, 4), (0, 5), (0, 6)]  # , (0, 7)]

        #not solveable
        # self.field = [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        #             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        #             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        # self.queens = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0,
        # 6)], (0, 7)]

    def value(self):
        value = 0
        for i in self.queens:
            for x in self.queens:
                if i != x:
                    if i[0] == x[0] or i[1] == x[1]:
                        value = value + 1
                    if (i[0] - i[1]) == (x[0] - x[1]):
                        value = value + 1
                    if (i[0] + i[1]) == (x[0] + x[1]):
                        value = value + 1

        return value / 2

    def all_possible_moves(self, queen):
        i = 0
        possible_moves = []
        # check left and right
        while (i < queen[0]):
            if self.field[i][queen[1]] == 0:
                possible_moves.append((i, queen[1]))
            i += 1

        i = queen[0] + 1
        while (i < self.Dimension):
            if self.field[i][queen[1]] == 0:
                possible_moves.append((i, queen[1]))
            i += 1

        # check up and down
        i = 0
        while (i < queen[1]):
            if self.field[queen[0]][i] == 0:
                possible_moves.append((queen[0], i))
            i += 1

        i = queen[1] + 1
        while (i < self.Dimension):
            if self.field[queen[0]][i] == 0:
                possible_moves.append((queen[0], i))
            i += 1

        # check diagonal from up left to down right \
        i = 1
        while queen[0] - i >= 0 and queen[1] - i >= 0:
            if self.field[queen[0] - i][queen[1] - i] == 0:
                possible_moves.append((queen[0] - i, queen[1] - i))
            i += 1

        i = 1
        while queen[0] + i < self.Dimension and queen[1] + i < self.Dimension:
            if self.field[queen[0] + i][queen[1] + i] == 0:
                possible_moves.append((queen[0] + i, queen[1] + i))
            i += 1

        # check diagonal from up right to down left \
        i = 1
        while queen[1] - i >= 0 and queen[0] + i < self.Dimension:
            if self.field[queen[0] + i][queen[1] - i] == 0:
                possible_moves.append((queen[0] + i, queen[1] - i))
            i += 1

        i = 1
        while queen[1] + i < self.Dimension and queen[0] - i >= 0:
            if self.field[queen[0] - i][queen[1] + i] == 0:
                possible_moves.append((queen[0] - i, queen[1] + i))
            i += 1

        return possible_moves

    def evaluate_poss_moves(self, possible_moves, queen):
        #Just a random number that should be high enough :D
        score = 256
        restore_field = deepcopy(self.field)
        restore_queen = (queen[0], queen[1])
        local_best_move = (-1, -1)
        for move in possible_moves:
            which_queen = restore_field[queen[0]][queen[1]]
            restore_field[queen[0]][queen[1]] = 0
            restore_field[move[0]][move[1]] = which_queen
            self.queens[which_queen - 1] = move
            local_score = self.value()
            if local_score < score:
                score = local_score
                local_best_move = move
            restore_field = deepcopy(self.field)
            self.queens[which_queen - 1] = restore_queen[0], restore_queen[1]

        return local_best_move, score

    def best_move(self):
        # find the best move and the value function after making that move
        best_move = ((-1, -1), -1)
        score = 256
        i = 1
        for queen in self.queens:
            possible_moves = self.all_possible_moves(queen)

            helper0 = self.evaluate_poss_moves(possible_moves, queen)[0]
            helper1 = self.evaluate_poss_moves(possible_moves, queen)[1]

            if helper1 < score:
                best_move = (helper0, i)
                score = helper1
            i += 1
        return best_move, score

    def make_move(self, move):
        x_queen = self.queens[move[1] - 1][0]
        y_queen = self.queens[move[1] - 1][1]
        self.field[x_queen][y_queen] = 0
        self.queens[move[1] - 1] = move[0]
        x_queen = self.queens[move[1] - 1][0]
        y_queen = self.queens[move[1] - 1][1]
        self.field[x_queen][y_queen] = move[1]

        # actually execute a move (change the board)

        return 0


if __name__ == '__main__':
    pos = NQPosition(1)
    # print(pos.value())
    # print(pos.all_possible_moves(pos.queen2))
    # print(pos.best_move())  # check third node
    pos.make_move(((0, 0), 1))
