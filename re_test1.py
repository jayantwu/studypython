import re
m1 = re.match('foo', 'food is my favorite! ')
print(m1)
print(m1.group())
"""
<re.Match object; span=(0, 3), match='foo'>
foo
"""

bt = 'bat|bit|but'
m2 = re.match(bt, 'battle')
print(m2)
print(m2.group())   #bat#


m3 = re.search(bt, 'He bit me!')
print(m3.group())      #bit#


#match是从头开始匹配
m4 = re.match(bt, 'he bit me!')
print(m4)    #None#

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group(0))  #abc-123
print(m.group(1))  #abc
print(m.group(2))  #123
print(m.groups())  #return tupple  ('abc', '123')

m = re.findall(r'th\w+', 'this and That', re.I)
print(m)   # ['this', 'That']  return a list
m = re.finditer(r'th\w+', 'this and That', re.I)
print(m)
g = m.__next__()
print(g.group())
for g in m:
    print(g.group())
