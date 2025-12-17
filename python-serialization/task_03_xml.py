import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = value
    tree = ET.ElementTree(root)
    tree.write(
            filename,
            encoding='utf-8',
            xml_declaration=True
            )


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    dictionary = {}
    root = tree.getroot()
    for d in root.attrib:
        dictionary(d.key) = d.value
    return dictionary
