import xml.etree.ElementTree as ET


clientprofiles = ET.parse('C:\\Users\\andre\\Desktop\\Perf_C200_01_1x_4x100GigE_BW\\userprofiles\\FTP_BANDWIDTH.xml')
root = clientprofiles.getroot()

for child in root:
    print(child.tag, end=" ")
    if child.attrib != {}:
        print(child.attrib, end="")
    print()
