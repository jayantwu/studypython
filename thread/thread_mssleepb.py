import _thread
from time import sleep, ctime

loops = [4, 2]
def loop(nloop, nsec, lock):
    print('start loop {} at {}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at {}'.format(nloop, ctime()))
    lock.release()  #执行完之后释放锁

def main():
    print('starting at {}'.format(ctime()))
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire() #获取每个锁
        locks.append(lock)
    print(locks)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))   #创建线程

    for i in nloops:  #所有锁都被释放时才会结束主线程，可能会出现第1个线程已经释放锁，而第0个还没有释放的情况
        while locks[i].locked():   #锁状态下，返回True
            pass

    print('all done at : {}'.format(ctime()))

if __name__ == '__main__':
    main()


"""
starting at Wed Jun 17 21:33:16 2020
[<locked _thread.lock object at 0x00000189A86AFD50>, <locked _thread.lock object at 0x00000189A86AF540>]
start loop 0 at Wed Jun 17 21:33:16 2020
start loop 1 at Wed Jun 17 21:33:16 2020
loop 1 done at Wed Jun 17 21:33:18 2020
loop 0 done at Wed Jun 17 21:33:20 2020
all done at : Wed Jun 17 21:33:20 2020

"""