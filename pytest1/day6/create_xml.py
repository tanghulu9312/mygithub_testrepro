#!/usr/bin/env python
#Author:TangHu
import xml.etree.ElementTree as ET
#person info

new_xml=ET.Element("Students")
student=ET.SubElement(new_xml,"student",attrib={"heigh":"175cm","weight":"65kg","sex":"male"})
id=ET.SubElement(student,"id")
id.text='10001'
name=ET.SubElement(student,"name")
name.text="zhangsan"
classes=ET.SubElement(student,"classes")
classes.text="六年级（一）班"

student=ET.SubElement(new_xml,"student",attrib={"heigh":"165cm","weight":"45kg","sex":"fmale"})
id=ET.SubElement(student,"id")
id.text='10002'
name=ET.SubElement(student,"name")
name.text="李四"
classes=ET.SubElement(student,"classes")
classes.text="六年级（二）班"
et=ET.ElementTree(new_xml)
et.write("test.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)