import xml.etree.ElementTree as ET
tree = ET.parse('RecorderConfig.xml')
root = tree.getroot()

print(root.tag)

for item in root:
    print(item.tag)
    print(item.text)

