import xml.etree.ElementTree as ET


clientsubnets = ET.parse('C:\\Users\\andre\\Desktop\\Perf_C200_01_1x_4x100GigE_BW\\clientsubnets\\PORT_0.xml')
root = clientsubnets.getroot()

for child in root:
    print(child.tag, end=" ")
    if child.attrib != {}:
        print(child.attrib, end="")
    print()
