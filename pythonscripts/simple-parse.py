import sys
import xml.etree.ElementTree as ET 

filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()

for test in root.iter('test'):
    status = test.find('status')
    print('INSERT INTO tasks (name, result, date, epoch) VALUES (', test.attrib['name'], ', ', status.attrib['status'], 'NOW(), EXTRACT(EPOCH FROM NOW()))' )