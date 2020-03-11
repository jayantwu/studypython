import re, os
def delfile(path, pattern):
    l = os.listdir(path)
    print(l)
    for f in l:
        if re.search(pattern, f):      #如果匹配返回一个正则对象，否则为none
            os.remove(f)
            print("成功删除{}".format(f))

"""文件的复制与删除"""
def main():
    try:
        with open('tiger.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        n = int(input("你要复制几份？"))
        for i in range(1, n+1):
            with open('tiger_copy{}.jpg'.format(i), 'wb') as fs2:
                fs2.write(data)
        print("复制{}份完成！".format(n))
        ans = input("你是否想要删除刚刚复制的文件?y/n ").lower()
        while True:
            if ans in ['yes', 'y']:
                path = r"C:\Users\NING MEI\PycharmProjects\untitled"
                pattern = re.compile(r'' + input("请输入要匹配的re表达式："))     #  r'^tiger_copy[0-9]+.jpg$'
                delfile(path, pattern)
                break
            elif ans in ['no', 'n']:
                break
            else:
                print('请输入y或n！')
                ans = input()

    except FileNotFoundError as e:
            print('指定的文件无法打开.')
    except IOError as e:
            print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()