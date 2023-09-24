# In this program we will be writing a code with a decorator which will not let user give an input of different type other than which is needed.


def Check_dt(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)

            else:
                raise TypeError("You have entered wrong datatype.")

        return inner_wrapper

    return outer_wrapper


@Check_dt(int)
def square(num):
    print(num**2)


square(4)
