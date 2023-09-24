def reverse_num(arr):
    reverse = 0
    while arr > 0:
        number = arr % 10
        reverse = (reverse * 10) + number
        arr = arr // 10

    return reverse


print(reverse_num(1238934))
