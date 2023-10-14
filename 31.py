import random

def gencode(codelen:int = 6):
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    last_pos = len(chars) - 1
    code = ''
    for i in range(codelen):
        pos = random.randint(0, last_pos)
        code += chars[pos]
    return code


def getmax2(l:list):
    m1, m2 = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for idx in range(2, len(l)):
        if l[idx] > m1:
            m2 = m1
            m1 = l[idx]
        elif l[idx] > m2:
            m2 = l[idx]
        
    
    return (m1, m2)


def main():
    code = gencode()
    print(code)

    l = [3,7,2,46,432,35,646,355,235]
    print(getmax2(l))

if __name__ == '__main__':
    main()



