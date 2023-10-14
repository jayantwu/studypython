class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w:int):
        self._width=w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h:int):
        self._height=h

    @property
    def resolution(self):
        return self._width * self._height

def main():
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')


if __name__ == '__main__':
    main()