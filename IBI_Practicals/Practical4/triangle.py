# IBI Practical 4: Triangle Number Calculator

# input: interger n
# output the sum of the first n natural numbers
# formula：n * (n + 1) / 2
def calculate_triangle_number(n):
    """parameter: n (int): triangle numbers are integers"""
    return n * (n + 1) // 2
# displayes the first 10 values of the triangle sequence
# 1. loop from 1 to 10
# 2. calculate the triangle number for each n
# 3. print the corresponding triangle number
def display_first_ten_values():
    """display the first 10 values of the triangle sequence"""
    print("\nthe first 10 values of triangle sequence：")
    for n in range(1, 11):
        print(f"{n}. {calculate_triangle_number(n)}")

#Obtain user input and process it
# Loop until the user enters 0 to exit
# Prompt the user to enter an integer
# If the input is 0, exit the loop
# If the input is -1, display the first 10 values. Otherwise, calculate and display the number of triangles at the corresponding position
# Handle input errors
def get_user_input():
    while True:
        try:
            time = int(input("\nPlease enter an integer (enter 0 to exit, enter -1 to display the first 10 values)): "))
            
            if time < 0:
                if time == -1:
                    display_first_ten_values()
                else:
                    print("Please enter an integer of 1 or larger, or enter 0 to exit")
                continue
                
            if time == 0:
                print("Quitting the program.")
                break
                
            num = calculate_triangle_number(time)
            print(f"The {time} of triangle number is: {num}")
            
        except ValueError:
            print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"Error: {e}")

# workflow
# 1. greeting
# 2. displayes the first 10 values of the triangle sequence (1, 3, 6, 10, 15, 21, 28, 36, 45, 55)
# 3. starts the user input loop
def main():
    """main def for the triangle number calculator"""
    print("Let's calculate the triangle number！")
    display_first_ten_values()
    get_user_input()

if __name__ == "__main__":
    main()