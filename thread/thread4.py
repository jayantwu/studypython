# -*- coding: utf-8 -*-
#单线程和多线程执行对比
from myThread import MyThread
from time import ctime, sleep

def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)

def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x-1)

def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x-1)


funcs = [fib, fac, sum]
n = 12
def main():
    nfuncs = range(len(funcs))

    print('***single thread')
    for i in nfuncs:
        print('starting {} at {}'.format(funcs[i].__name__, ctime()))
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('***multiple threads')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print('all done')

if __name__ == '__main__':
    main()



"""
***single thread
starting fib at Fri Jun 19 23:00:37 2020
233
fib finished at: Fri Jun 19 23:00:39 2020
starting fac at Fri Jun 19 23:00:39 2020
479001600
fac finished at: Fri Jun 19 23:00:40 2020
starting sum at Fri Jun 19 23:00:40 2020
78
sum finished at: Fri Jun 19 23:00:42 2020
***multiple threads
starting fib at Fri Jun 19 23:00:42 2020
starting fac at Fri Jun 19 23:00:42 2020
starting sum at Fri Jun 19 23:00:42 2020
fac finished at: Fri Jun 19 23:00:43 2020
sum finished at: Fri Jun 19 23:00:43 2020
fib finished at: Fri Jun 19 23:00:44 2020
233
479001600
78
all done
"""
