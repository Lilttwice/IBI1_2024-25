# Calculate the value of a, b, c, d, e, f and print the result of c > e to decide quicker way.
a = 15
b = 60 + 15
c = a + b
d = 60 + 30
e = 5
f = d + e
print(f>c)
print(c>e)
# Output: True \n True
# Q1: Look at the second output. c is longer.
# Q2: Look at the first output. f is longer. So, c (walk to the bus stop and take the bus) is quicker.

# 4.2 Booleans
# initialize the booleans X and Y
X = True
Y = False

# create boolean W，W is only true when both X and Y are true.
W = X and Y

# print the result
print(f"The value of X: {X}")
print(f"The value of Y: {Y}")
print(f"The value of W (X and Y): {W}")

# The truth table for the boolean operation W (X and Y) is as follows:
# | X     | Y     | W (X and Y) |
# |-------|-------|-------------|
# | True  | True  | True        |
# | True  | False | False       |
# | False | True  | False       |
# | False | False | False       |