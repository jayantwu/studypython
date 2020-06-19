# -*- coding: utf-8 -*-
#创建thread的实例，传给它一个可调用的类实例
import threading
from time import sleep, ctime

loops = [4, 2]
class ThreadFunc():
    def __init__(self, func, args, name=''):  #args用来存func的参数，这里是个元组
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):    #可以让一个类实例像一个函数一样执行，具体以后详细学习一下这个call
        self.func(*self.args)   #执行func

def loop(nloop, nsec):
    print('start loop {} at:{}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at:{}'.format(nloop, ctime()))

def main():
    print('starting at:{}'.format(ctime()))
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__)) #
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 起线程

    for i in nloops:
        threads[i].join()

    print('all done at:{}'.format(ctime()))

if __name__ == '__main__':
    main()