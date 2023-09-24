def triangle(row, column=0):
    if row == 0:
        return
    if column < row:
        print("*", end=" ")
        triangle(row, column + 1)
    else:
        print()
        triangle(row - 1, 0)


triangle(5)
