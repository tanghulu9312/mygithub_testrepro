#!/usr/bin/env python
#Author:TangHu
'''
xml是实现不同语言或程序之间进行数据交换的协议，
跟json差不多，但json使用起来更简单，不过，古时候，
在json还没诞生的黑暗年代，大家只能选择用xml呀，
至今很多传统公司如金融行业的很多系统的接口还主要是xml
'''
import xml.etree.ElementTree as ET

tree=ET.parse("xml_test.xml")
root=tree.getroot()

#遍历xml文档
'''
for child in root:
    print('==========>',child.tag,child.attrib,child.attrib['name'])
    for i in child:
        print(i.tag,i.attrib,i.text)

#只遍历year节点
for node in root.iter('year'):

    print(node.tag,node.attrib,node.text)

#修改
for node in root.iter('year'):
    new_year=int(node.text)+1
    node.text=str(new_year)
    node.set('updated','yes')
    node.set('version','2.0')
tree.write('xml_test.xml')

#删除节点
for country in root.findall('country'):

    rank=int(country.find('rank').text)
    if rank<50:
        root.remove(country)

tree.write('output2.xml')

# for country in root.iter('country'):
#     rank=int(country.find('rank').text)
#     print('***',rank)
#     if rank>50:
#         root.remove(country)
# tree.write('output3.xml')
#root.iter()全文搜索
#root.find()在root的子节点找，只找一个
#root.findall()在root子节点找，找所有
'''

'''
#添加节点
country=ET.Element('country')
country.attrib={'name':'China'}
rank=ET.Element('rank')
rank.text='3'
year=ET.Element('year')
year.attrib={'version':'3.0'}
year.text='2018'
country.append(rank)
country.append(year)
root.append(country)

tree.write('xml_test.xml')
'''

#如过country=China，则添加两个子节点gdpc和neighbor

for country in root.findall('country'):
    if  country.attrib.get('name')=='China':

        gdpc=ET.Element('gdpc')
        gdpc.text='92100'
        neighbor=ET.Element('neighbor')
        neighbor.attrib={"direction":"E","name": "korea"}

        country.append(gdpc)
        country.append(neighbor)
tree.write('xml_test.xml')
