import re

str = 'abc1abc2abcd3abcde1'

m = re.split(r'\d', str)
print(m)
#['abc', 'abc', 'abcd', 'abcde']

m2 = re.split(r'[a-z]+', str)
print(m2)
#['', '1', '2', '3', '1']   #有一个空字符

m3 = re.findall(r'[a-z]+', str)
print(m3)
#['abc', 'abc', 'abcd', 'abcde']