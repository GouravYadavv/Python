import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("Time taken by", func.__name__, "is:", time.time() - start, "seconds")

    return wrapper


@timer
def Hello():
    print("Hello World!")
    time.sleep(2)


@timer
def square(nums):
    time.sleep(2)
    print(nums**2)


Hello()
square(2)
