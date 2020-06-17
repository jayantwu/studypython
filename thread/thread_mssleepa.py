import _thread
from time import sleep, ctime

def loop0(a):
    print(a)
    print("start loop0 at time :{}".format(ctime()))
    sleep(2)
    print("end loop0 at time :{}".format(ctime()))

def loop1(b):
    print(b)
    print("start loop1 at time :{}".format(ctime()))
    sleep(1)
    print("end loop1 at time :{}".format(ctime()))

def loop2(c):
    print(c)
    print("start loop2 at time :{}".format(ctime()))
    sleep(3)
    print("end loop2 at time :{}".format(ctime()))

def main():
    print("start at {}".format((ctime())))
    _thread.start_new_thread(loop0, ('a',))   #元组里是loop0的参数，
    _thread.start_new_thread(loop1, ('b',))
    _thread.start_new_thread(loop2, ('c',))
    sleep(6)   #需要有这个sleep，不然会出现主线程结束，子线程没执行玩被中断，threading中有join方法达到这个作用
    print("end at {}".format((ctime())))

if __name__ == '__main__':
    main()


"""
start at Wed Jun 17 21:45:01 2020
a
start loop0 at time :Wed Jun 17 21:45:01 2020
c
start loop2 at time :Wed Jun 17 21:45:01 2020
b
start loop1 at time :Wed Jun 17 21:45:01 2020
end loop1 at time :Wed Jun 17 21:45:02 2020
end loop0 at time :Wed Jun 17 21:45:03 2020
end loop2 at time :Wed Jun 17 21:45:04 2020
end at Wed Jun 17 21:45:07 2020

"""