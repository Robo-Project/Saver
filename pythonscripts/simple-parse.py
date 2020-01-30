
import sys
import xml.etree.ElementTree as ET

filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()


for testElement in root.iter('test'):
    statusElement = testElement.find('status')
    name = testElement.attrib['name']
    status = statusElement.attrib['status']
    print('INSERT INTO tasks (name, status) VALUES (\'{}\', \'{}\');'.format(name, status))
