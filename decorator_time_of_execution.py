import time


def time_of_execution(func):
    def time_wrapper(*args, **kwargs):
        print("The runtime is >>>",  time.ctime(time.time()))
        start_time = time.time()
        multiply_result = func(*args, **kwargs)
        end_time = time.time()
        duration_of_execution = end_time - start_time
        print(f"The start time is >>> {start_time} sec.")
        print(f"The end time is >>> {end_time} sec.")
        print(f"Duration of execution >>> {duration_of_execution} sec.")
        return multiply_result
    return time_wrapper


@time_of_execution
def multiply_num(a, b):
    print("The result of function >>>", a * b**a)
    return a * b**a


multiply_num(8217, 153)