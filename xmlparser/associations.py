import xml.etree.ElementTree as ET


associations = ET.parse('C:\\Users\\andre\\Desktop\\Perf_C200_01_1x_4x100GigE_BW\\tests\\FTP_BANDWIDTH.xml')
root = associations.getroot()

for child in root:
    print(child.tag, end=" ")
    if child.attrib != {}:
        print(child.attrib, end="")
    print()

# all items data
# print('Expertise Data:')
#
# for elem in root:
#    for subelem in elem:
#       print(subelem.text)
