# coding=utf-8
import re
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'

m = re.match(patt, data)
print(m.group())
#Thu
patt = '\d+-\d+-\d+'
m2 = re.search(patt, data).group()
print(m2)
#1171590364-6-8
patt = '.+\d+-\d+-\d+'
m3 = re.match(patt, data).group()
print(m3)
#Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8
patt = '.+(\d+-\d+-\d+)'  #贪婪模式
m4 = re.match(patt, data).group(1)
print(m4)
#4-6-8

patt = '.+?(\d+-\d+-\d+)'    #非贪婪模式
m5 = re.match(patt, data).group(1)
print(m5)
#1171590364-6-8

patt = '-(\d+)-'
m6 = re.search(patt, data)
print(m6)   #<re.Match object; span=(57, 60), match='-6-'>
print(m6.group())  #-6-
print(m6.group(1))  #6

print(re.match(r'([a-zA-Z]+)( )([a-zA-Z]+)', 'Katy Parry').group())

print(re.match(r'\d+([a-zA-Z ]+)', '1180 Bordeaux Drive').group())
print(re.match(r'\d+([a-zA-Z ]+)', '3120 De la Cruz Boulevard').group())


m7 = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print(m7)
##X的地方用Mr.  Smith替换

##############
################exercise time###################
"""
1-1 识别后续的字符串：“bat”、“bit”、“but”、“hat”、“hit”或者“hut”。
'b.t'
1-2 匹配由单个空格分隔的任意单词对，也就是姓和名。
'[a-zA-Z]+ [a-zA-Z]+'
1-5 根据读者当地的格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数
量的街道单词，包括类型名称）。例如，美国街道地址使用如下格式：1180 Bordeaux
Drive。使你的正则表达式足够灵活，以支持多单词的街道名称，如 3120 De la Cruz
Boulevard。
'\d+([a-zA-Z ]+)'    有很大缺陷，当字母中再出现数字时，会匹配一部分字母，这种情况下实际应该不要匹配才对
"""

