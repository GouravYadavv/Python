def triangle(row, column=0):
    if row == 0:
        return
    if column < row:
        triangle(row, column + 1)
        print("*", end=" ")
    else:
        triangle(row - 1, 0)
        print()


triangle(5)
