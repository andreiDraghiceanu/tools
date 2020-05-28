from xml_parser import *


xml = ManageXML("FTP_BANDWIDTH.xml")

xml.search_for_element('<TestSpec>', '<Version>')
