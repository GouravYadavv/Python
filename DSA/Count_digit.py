def countdigits(a):
    count = 0
    while a > 0:
        count += 1
        a = a // 10
    return count


print(countdigits(12345))
