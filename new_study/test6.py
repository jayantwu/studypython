def fun():
    assert 1 == 0, "not equal"

def to_int(str_n):
    return int(str_n)

ports_str:str = '1, 2, 7-10'

sub_list = ports_str.split(',')
print(sub_list)
port_list = []
for sub_num in sub_list:
    if '-' in sub_num:
        start, end = map(to_int, sub_num.split('-'))
        port_list += list(range(start-1, end))
    else:
        port_list.append(int(sub_num) - 1)


print(port_list)

#fun()