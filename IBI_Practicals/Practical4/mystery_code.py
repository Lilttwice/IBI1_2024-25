# Library needed：
from random import randint

def count_rolls_until_match():
    roll_count = 0
    while True:
        roll_count += 1
        # intergrate twice dice count，reduce functioin calls overhead
        first_dice, second_dice = randint(1, 6), randint(1, 6)
        if first_dice == second_dice:
            return roll_count

if __name__ == "__main__":
    try:
        result = count_rolls_until_match()
        print(f"after {result} times of roll，we got two indentical count")
    except Exception as e:
        print(f"Error: {e}")
    