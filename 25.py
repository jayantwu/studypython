from multiprocessing import Process
from time import sleep
from random import randint
from threading import Thread
def task(name):
    print("{}下载中....".format(name))
    sleep(randint(3, 6))
    print("{}下载完成！".format(name))


def main():
    #"""
    t1 = Thread(target=task, args=("波多野ji衣.avi",))
    t2 = Thread(target=task, args=("one peace.mp4",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    #"""
    """
    p1 = Process(target=task, args=("小泽玛丽亚.rmvb",))
    p2 = Process(target=task, args=("苍jin空.avi",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()  """

    print("全部下载完成！")
if __name__ == "__main__":
    main()


"""
当不使用join()的时候，主进程可能已经先结束了。。。。下面是输出结果

全部下载完成！
小泽玛丽亚.rmvb下载中....
苍jin空.avi下载中....
小泽玛丽亚.rmvb下载完成！
苍jin空.avi下载完成！
"""
"""
线程不加join()也是一样的

波多野ji衣.avi下载中....
one peace.mp4下载中....
全部下载完成！
波多野ji衣.avi下载完成！
one peace.mp4下载完成！
"""