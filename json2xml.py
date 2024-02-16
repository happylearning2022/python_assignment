import ijson
import xml.etree.ElementTree as ET

def json_to_xml(input_file, output_file, root_tag='root'):
    with open(input_file, 'r') as f_in:
        root = ET.Element(root_tag)

        parser = ijson.parse(f_in)
        for prefix, event, value in parser:
            if prefix.endswith('.item') and event == 'start_map':
                parent_element = root
                element = ET.Element(prefix.split('.')[-2])
                parent_element.append(element)
            elif event == 'map_key':
                key = value
            elif event == 'string':
                child_element = ET.Element(key)
                child_element.text = value
                element.append(child_element)
            elif event == 'number':
                child_element = ET.Element(key)
                child_element.text = str(value)
                element.append(child_element)

        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Example usage
input_file = 'large.json'
output_file = 'output.xml'
json_to_xml(input_file, output_file)
