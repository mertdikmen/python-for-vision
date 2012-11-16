import multiprocessing
import os

def my_function(some_number):
    print("{}: the number is {}".format(os.getpid(), some_number))
    
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4, maxtasksperchild=2)
    
    my_array = [5, 1, 4, 10, 3, 0, 12, 6, 8]
    
    pool.map(my_function, my_array)