# -*- coding: utf-8 -*-
#创建thread的实例，传给它一个函数
import threading
from time import sleep, ctime

loops = [4, 2]
def loop(nloop, nsec):
    print('start loop {} at:{}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at:{}'.format(nloop, ctime()))

def main():
    print('starting at:{}'.format(ctime()))
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))  #args为一个元组，是loop函数的参数
        threads.append(t)
    print(threads)

    for i in nloops:
        threads[i].start()    #起线程

    for i in nloops:
        threads[i].join()    #等待所有子线程结束，才继续执行主线程的代码；可以不使用join，差别就是”all done“会先打印出来

    print('all done at:{}'.format(ctime()))

if __name__ == '__main__':
    main()


"""
starting at:Thu Jun 18 22:28:50 2020
start loop 0 at:Thu Jun 18 22:28:50 2020
start loop 1 at:Thu Jun 18 22:28:50 2020
loop 1 done at:Thu Jun 18 22:28:52 2020
loop 0 done at:Thu Jun 18 22:28:54 2020
all done at:Thu Jun 18 22:28:54 2020
"""