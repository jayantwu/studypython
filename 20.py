from multiprocessing import Process
import time
import os

def task(name):
    print('{} is running, pid is {}'.format(name, os.getpid()))
    time.sleep(2)
    print('%s is end' %(name))

def main():
    start = time.time()
    p1 = Process(target=task, args=('子进程1',))
    p2 = Process(target=task, args=('子进程2',))
    p3 = Process(target=task, args=('子进程3',))
    p4 = Process(target=task, args=('子进程4',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    """"主进程需要等子进程都结束之后才能结束"""
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    end = time.time()
    print(end - start)
    print('主', os.getpid(), os.getppid())  # 返回子进程id和父进程id

if __name__ == '__main__':
    main()