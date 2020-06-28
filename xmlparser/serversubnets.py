import xml.etree.ElementTree as ET


serversubnets = ET.parse('C:\\Users\\andre\\Desktop\\Perf_C200_01_1x_4x100GigE_BW\\wrserversubnets\\PORT_0.xml')
root = serversubnets.getroot()

for child in root:
    print(child.tag, end=" ")
    if child.attrib != {}:
        print(child.attrib, end="")
    print()
