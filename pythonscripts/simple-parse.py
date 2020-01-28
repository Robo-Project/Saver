
import sys
import xml.etree.ElementTree as ET

filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()

for testElement in root.iter('test'):
    statusElement = testElement.find('status')
    ## FIXME: Add protection against sql injection
    name = testElement.attrib['name']
    status = 0
    if statusElement.attrib['status'] == 'PASS':
        status = 1
    print('INSERT INTO tasks (name, result, date, epoch) VALUES (\'{}\', {}, NOW(), EXTRACT(EPOCH FROM NOW()));'.format(name, status))
