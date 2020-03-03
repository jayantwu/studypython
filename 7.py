from time import sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0
                    self._minute = 0

    def show(self):
        """格式化输出，右对齐，不足2位最左边填充0"""
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self._hour, self._minute, self._second)



def main():
    clock = Clock(22, 59, 59)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == "__main__":
    main()

