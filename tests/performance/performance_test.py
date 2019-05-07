import linedit

def one_million():
    linedit.edit_line('test_one_million.txt', 10, '55sasd5')

def one_hundred_thousand():
    linedit.edit_line('test_one_hundred_thousand.txt', 10, '55sasd5')

def one_thousand():
    linedit.edit_line('test_one_thousand.txt', 10, '55sasd5')

import time
import random
import statistics

functions = [one_million, one_hundred_thousand, one_thousand]
times = {f.__name__: [] for f in functions}

for i in range(10): 
    func = functions[0]
    t0 = time.time()
    func()
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)

for i in range(10): 
    func = functions[1]
    t0 = time.time()
    func()
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)

for i in range(10): 
    func = functions[2]
    t0 = time.time()
    func()
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)

for name, numbers in times.items():
    print('FUNCTION:', name, 'Used', len(numbers), 'times')
    print('\tMEDIAN', statistics.median(numbers))
    print('\tMEAN  ', statistics.mean(numbers))
    print('\tSTDEV ', statistics.stdev(numbers))
