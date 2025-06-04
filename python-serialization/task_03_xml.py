#!/usr/bin/python3
"""
task_03_xml

this module contains 2 functions
serialize_to_xml and deserialize_from_xml
and import xml.etree.ElementTree
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    this function serialize dictionary in to
    xml file and handle the indentation
    """
    root = ET.Element("root")
    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)
    ET.indent(root, space="    ")
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    this function deserialize xml file
    in to dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dic = {}
    for child in root:
        dic[child.tag] = child.text
    return dic
