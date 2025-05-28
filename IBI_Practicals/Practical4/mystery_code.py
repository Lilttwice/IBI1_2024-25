# What does this piece of code do?
# Answer: Simulates rolling two dice until they show the same number, then reports the number of rolls taken.

# Import libraries
# randint allows drawing a random integer between two endpoints (inclusive)
from random import randint

# ceil takes the ceiling of a number (not used in this code)
from math import ceil

# workflow:
# 1. Initialize a counter for the number of rolls
# 2. Continuously roll two dice until they match:
#    - Increment the roll counter
#    - Generate two random numbers between 1 and 6
#    - Check if the numbers are identical
#    - If they match, print the counter and exit the loop

progress = 0  # Counter for the number of rolls
while progress >= 0:  # Loop indefinitely until a match is found
    progress += 1  # Increment the roll counter
    first_n = randint(1, 6)  # Roll the first die
    second_n = randint(1, 6)  # Roll the second die
    if first_n == second_n:  # Check if both dice show the same number
        print(progress)  # Print the number of rolls taken
        break  # Exit the loop once a match is found

    # Library needed:
from random import randint

def count_rolls_until_match():
    """
    Simulates rolling two dice until they show the same number.
    Returns the number of rolls taken to achieve this.
    
    workflow:
    1. Initialize a counter for the number of rolls
    2. Repeat the following until a match is found:
       - Increment the roll counter
       - Roll two dice (generate two random numbers)
       - Check if the results are identical
       - If they match, return the counter value
    """
    roll_count = 0
    while True:  # Loop until a match is found
        roll_count += 1  # Increment the roll counter
        # Roll two dice simultaneously to reduce function call overhead
        first_dice, second_dice = randint(1, 6), randint(1, 6)
        if first_dice == second_dice:  # Check for a match
            return roll_count  # Return the number of rolls taken

if __name__ == "__main__":
    try:
        result = count_rolls_until_match()
        print(f"After {result} rolls, we got two identical numbers.")
    except Exception as e:
        print(f"Error: {e}")