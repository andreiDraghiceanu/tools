import xml.etree.ElementTree as ET


serverprofiles = ET.parse('C:\\Users\\andre\\Desktop\\Perf_C200_01_1x_4x100GigE_BW\\wrserverprofiles\\FTP_BANDWIDTH.xml')
root = serverprofiles.getroot()

for child in root:
    print(child.tag, end=" ")
    if child.attrib != {}:
        print(child.attrib, end="")
    print()
