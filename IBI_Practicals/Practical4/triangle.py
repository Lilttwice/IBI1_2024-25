try:
    time = int(input())
    if time < 1:
        print("input 1 or greater")
    else:
        # Use the formula of sum of arithmetic sequences：S = n * (n + 1) / 2
        num = time * (time + 1) // 2
        print(num)
except ValueError:
    print("Error. Please enter a valid number.")
except Exception as e:
    print(f"Error: {e}")