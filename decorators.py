#Decorators

def outer(func):
    def inner():
        print("inside decorator")
        func()
    return inner
    
@outer
def fun():
    print('this is a function')
    
fun()
#output:
inside decorator
this is a function


#example2

import time

def count_time(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter() 
        run_time = end_time - start_time
        print(f"{run_time:.4f} secs")
    return wrapper_timer

@count_time
def fun(num_times):
    for i in range(num_times):
        sum=[i*2 for i in range(100000)]
        
fun(1000)

#output
5.1934
