def max2(l):
    m1, m2 = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for index in range(3, len(l)):
        if l[index] > m1:
            m2 = m1
            m1 = l[index]
        elif l[index] > m2:
            m2 = l[index]

    return (m1, m2)



