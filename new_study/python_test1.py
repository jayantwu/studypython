def fun1(var1, *args, **kv):
    print(var1)
    print('afaaafafa')
    for arg in args:
        print(arg)

    print('-'*40)
    for k, v in kv.items():
        print(k, end=': ')
        print(v)
        print('\n')



def fun2(var1, /, var2, var3, *, var4, var5):
    print(var1, var2, var3, var4, var5)




def fun3(a, b):
    return lambda x : x + 3 

fun1("hello", "how are you", "im good.", a="first", b="second", c="third")


fun2('hello world', 'jiayang', var3='wu', var4='beijing', var5='shanghai')

#fun2(var1='hello world', 'jiayang', var3='wu', var4='beijing', var5='shanghai')



squares = [x**2 for x in range(10)]



print(squares)




matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]


matrix2 = [[row[i] for row in matrix] for i in range(4)]


print(matrix2)


questions = ['name', 'quest', 'favorite color']

answers = ['lancelog', 'the holy grail', 'blue']


print(zip(questions, answers))

for q, a in zip(questions, answers):
    print('what is your {0}? it is {1}'.format(q, a))




















