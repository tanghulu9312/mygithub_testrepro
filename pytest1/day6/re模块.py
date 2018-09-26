#!/usr/bin/env python
#Author:TangHu
import re
'''
#match从起始位置开始根据模型去字符串中匹配指定内容，匹配单个
res1=re.match('\d+','123434343gdft34sf*&fsd423ljjsd___fs32345dg')
print(res1)
#search根据模型去字符串中匹配指定内容，匹配单个
res2=re.search('\w+','sf*&fsd423ljjsd___fsdwe32234g')
print(res2)

a="123abc456"
res3=re.search("([0-9]*)([a-z]*)([0-9]*)",a).group()
print('res3=====>',res3)
print (re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2,3))


#上述两中方式均用于匹配单值，即：只能匹配字符串中的一个，
# 如果想要匹配到字符串中所有符合条件的元素，则需要使用 findall。
res4=re.findall('\w+','sf*&fsd4\'[]23ljg\[]\jsd___fsdwe32234g')
print(res4)


res5=re.findall('[a-z]+',a)
print(res5)
res6=re.findall('\d+','sf*&fsd4\'[]23ljg\[]\jsd___fsdwe32234g')
print(res6)

#用于替换匹配的字符串
res7=re.sub('[a-z]+','yue',a)
print(res7)

#根据指定匹配进行分组
content="'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
res8=re.split("\*",content)
print(res8)
'''
'''
a='\n\rfasd\tfs fsdf'
res1=re.findall('\s+',a)
print(res1)
print(re.findall('\S+',a))
'''
temp='dfffffaasdf231434'
print(re.findall('\Ad',temp))
print(re.findall('34\Z',temp))
print(re.match('([a-z]*)([0-9]*)',temp).group(2))

print(re.findall('dfa*',temp))
print(re.findall('dfa?',temp))
print(re.findall('s.*3',temp))
print(re.findall('s.?f',temp))
print(re.findall('s.*?3',temp))

print(re.findall('df{2,4}',temp))
print(re.findall('[f]+',temp))
print(re.findall('[^df]+',temp))

print(re.findall('3|4',temp))
register='511324199512054512'
print(re.search("(?P<ID>\d{6})(?P<birthday>\d{8})(?P<number>\d{4})",register).groupdict())