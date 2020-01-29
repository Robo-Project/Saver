
import sys
import xml.etree.ElementTree as ET

filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()

for testElement in root.iter('test'):
    statusElement = testElement.find('status')
    name = testElement.attrib['name']
    status = 0
    if statusElement.attrib['status'] == 'PASS':
        status = 1
    print('PREPARE addtask (varchar(255), int, timestamptz, int) AS INSERT INTO tasks VALUES ($1, $2, $3, $4)')
    print('EXECUTE addtask (\'{}\', \'{}\', now(), extract(epoch from now()))'.format(name, status))
