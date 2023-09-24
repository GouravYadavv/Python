def mera_khudka_for_loop(iterator):
    iterator = iter(iterator)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


a = [1, 2, 3, 4, 5]
b = range(1, 11)
c = (1, 2, 3)
d = {1, 2, 3, 4}
e = {1: 0, 2: 1, 3: 2, 4: 3}

mera_khudka_for_loop(a)

mera_khudka_for_loop(b)

mera_khudka_for_loop(c)

mera_khudka_for_loop(d)

mera_khudka_for_loop(e)
