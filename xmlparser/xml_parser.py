import xml.etree.ElementTree as xml
from xml.etree import ElementTree
from xml.dom import minidom
import os


class ManageXML:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = None
        self.root = None

    def xml_read(self):
        """Read root element"""
        self.tree = xml.parse('%s' % self.xml_file)
        self.root = self.tree.getroot()

    def prettify(self, fname, path):
        """ Return a pretty-printed XML string for the Element """
        rough_string = ElementTree.tostring(self.root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        xml_name = fname + '.xml'
        filename = os.path.join(path, xml_name)
        if not filename is None:
            f = open(filename, 'w')
            reparsed.writexml(f, indent="    ", addindent="    ", newl="\n")
            f.close()
        return xml_name

    @staticmethod
    def search_for_element(parent, child):
        for element in parent:
            if element.tag == child:
                return element

    @staticmethod
    def add_element(parent_elem, new_elem, **kwargs):
        child_elem = xml.SubElement(parent_elem, new_elem, kwargs)
