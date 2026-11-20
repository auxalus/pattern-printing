# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n = 5 #5 start pyramids

for i in range(n):
    for j in range(n):
        # Print '*' on the first row, last row, first column, or last column
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()