import random
from IPython.display import clear_output

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

state = goal.copy()
moves = 0


def is_solvable(puzzle):
    nums = [x for x in puzzle if x != 0]
    inv = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1

    return inv % 2 == 0


def shuffle_board():
    global state, moves
    moves = 0

    while True:
        state = goal.copy()
        random.shuffle(state)

        if is_solvable(state) and state != goal:
            break


def print_board():
    clear_output(wait=True)

    print("GAME 8-PUZZLE")
    print("Mục tiêu:")
    print("1 2 3")
    print("4 5 6")
    print("7 8 _")
    print()
    print("Số bước:", moves)
    print()

    for i in range(0, 9, 3):
        row = state[i:i+3]
        for x in row:
            if x == 0:
                print("_", end=" ")
            else:
                print(x, end=" ")
        print()

    print()
    print("Điều khiển:")
    print("w = lên")
    print("s = xuống")
    print("a = trái")
    print("d = phải")
    print("q = thoát")


def move(direction):
    global moves

    zero = state.index(0)
    new_pos = zero

    if direction == "w":
        new_pos = zero + 3
    elif direction == "s":
        new_pos = zero - 3
    elif direction == "a":
        new_pos = zero + 1
    elif direction == "d":
        new_pos = zero - 1
    else:
        return

    if new_pos < 0 or new_pos >= 9:
        return

    if zero % 3 == 0 and direction == "d":
        return
    if zero % 3 == 2 and direction == "a":
        return

    state[zero], state[new_pos] = state[new_pos], state[zero]
    moves += 1


shuffle_board()

while True:
    print_board()

    if state == goal:
        print("Bạn đã thắng!")
        break

    key = input("Nhập w/a/s/d: ").lower()

    if key == "q":
        print("Đã thoát game.")
        break

    move(key)
