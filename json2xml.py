import ijson
import xml.etree.ElementTree as ET

def json_to_xml(input_file, output_file, root_tag='root'):
    with open(input_file, 'r') as f_in:
        root = ET.Element(root_tag)
        current_element = root
        elements_stack = []

        parser = ijson.parse(f_in)
        for prefix, event, value in parser:
            if event == 'start_map':
                if prefix.endswith('.item'):
                    element = ET.Element(prefix.split('.')[-2])
                    current_element.append(element)
                    elements_stack.append(current_element)
                    current_element = element
            elif event == 'map_key':
                key = value
            elif event == 'string' or event == 'number':
                child_element = ET.Element(key)
                child_element.text = str(value)
                current_element.append(child_element)
            elif event == 'end_map':
                if elements_stack:
                    current_element = elements_stack.pop()

        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Example usage
input_file = 'large.json'
output_file = 'output.xml'
json_to_xml(input_file, output_file)
