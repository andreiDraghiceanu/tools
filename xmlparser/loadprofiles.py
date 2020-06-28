import xml.etree.ElementTree as ET


loadprofiles = ET.parse('C:\\Users\\andre\\Desktop\\Perf_C200_01_1x_4x100GigE_BW\\loadprofiles\\FTP_BANDWIDTH.xml')
root = loadprofiles.getroot()


def lp_elements(root):
    for child in root:
        print(type(child.tag))
        yield child.tag


child = lp_elements(root)

def lpsub_elements(sub_child):
    for sub_child in lp_elements(root):
        yield child



for item in lpsub_elements(child):
    print(item)