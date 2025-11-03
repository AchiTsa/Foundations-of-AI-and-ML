import NQPos


def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


if __name__ == '__main__':
    # please adapt dimension and field/queens in NQPos constructor
    pos = NQPos.NQPosition(8)
    hill_climbing(pos)
    # for printing
    aligned = list(zip(*pos.field))
    for row in aligned:
        print(row)
