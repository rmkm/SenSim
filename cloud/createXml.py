from lxml import etree
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

root = etree.Element("root")
child1 = etree.SubElement(root, "child1")
#with open('./app_b64enc.txt', 'rt') as f:
with open(input_path, 'rt') as f:
    child1.text = etree.CDATA(f.read())
#child1.text = etree.CDATA("PIZZATIME")
tree = etree.ElementTree(root)
#with open('./package.xml', 'wb') as f:
with open(output_path, 'wb') as f:
    f.write(etree.tostring(tree))
#print (etree.tostring(root, pretty_print=True))
