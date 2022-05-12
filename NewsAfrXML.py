from gettext import install
import xml.etree.ElementTree as ET
import collections

parser = ET.XMLParser(encoding='utf-8')

tree = ET.parse('WorkWithFiles/newsafr2.xml',parser)
# tree = ET.parse('WorkWithFiles/newsafr2.xml')
xml_root = tree.getroot()
print(xml_root.text)
print(xml_root.tag)
print(xml_root.attrib)

news = xml_root.findall('channel/item/description')
# print(type(news))
description_list = []
for new in news:
    # print(new)
    description_words = [word for word in new.text.split(' ') if len(word) > 6]
    description_list.extend(description_words)
    description_counter = collections.Counter(description_list)
# print(description_counter)
print(sorted(description_counter.items(), key=lambda x: x[1][1], reverse=True))
# print(collections.Counter(description_list).most_common(10))
print()







