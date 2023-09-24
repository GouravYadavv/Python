def Print_List(n):
    if n == 0:
        print(n)
        return n
    Print_List(n - 1)
    print(n)


def reverse_print_list(n):
    if n == 0:
        print(n)
        return n
    print(n)
    reverse_print_list(n - 1)


def sum_of_n_numbers(n):
    if n == 1:
        return n
    return n + sum_of_n_numbers(n - 1)


def Sum_of_digits(n):
    if n == 0:
        return n
    return n % 10 + Sum_of_digits(n // 10)


def Product_of_digits(n):
    if n % 10 == n:
        return n
    return n % 10 * Product_of_digits(n // 10)


Print_List(5)
reverse_print_list(5)
print(sum_of_n_numbers(5))
print(Sum_of_digits(129))
print(Product_of_digits(326))
