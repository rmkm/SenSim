from lxml import etree
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

parser = etree.XMLParser(huge_tree=True)
#xml = open('./package.xml', 'rb').read()
tree = etree.parse(input_path, parser)
root = tree.getroot()
#root = etree.XML(xml)
#links = root.xpath('//root')
#for link in links:
#    print(link.text)
child1 = root[0]
#print(child1.tag)
#print(child1.text)
#for children in root:
#    print(children.tag)
#with open('./app_b64enc2.txt', 'wt') as f:
with open(output_path, 'wt') as f:
    f.write(child1.text)
#xml.close()
