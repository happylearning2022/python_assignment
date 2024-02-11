import xml.etree.ElementTree as ET


def xml_to_html_table(xml_string):
    # Parse XML string
    root = ET.fromstring(xml_string)

    # Initialize HTML table
    html_table = """<html>
    <head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>

<h2>Collapsed Borders</h2>
<p>If you want the borders to collapse into one border, add the CSS border-collapse property.</p>

<table style="width:100%">"""

    # Extract headers
    headers = []
    for child in root:
        for subchild in child:
            if subchild.tag not in headers:
                headers.append(subchild.tag)

    # Add headers to HTML table
    html_table += "<tr>\n"
    for header in headers:
        html_table += f"<th>{header}</th>\n"
    html_table += "</tr>\n"

    # Add data rows to HTML table
    for child in root:
        html_table += "<tr>\n"
        for header in headers:
            data = child.find(header)
            if data is not None:
                html_table += f"<td>{data.text}</td>\n"
            else:
                html_table += "<td></td>\n"
        html_table += "</tr>\n"

    # Close HTML table
    html_table += "</table></body></html>"

    return html_table


# Example XML string
xml_string = """
<data>
    <row>
        <name>John</name>
        <age>30</age>
        <city>New York</city>
    </row>
    <row>
        <name>Alice</name>
        <age>25</age>
        <city>Los Angeles</city>
    </row>
    <row>
        <name>Bob</name>
        <age>35</age>
        <city>Chicago</city>
    </row>
</data>
"""

# Convert XML to HTML table
html_table = xml_to_html_table(xml_string)
print(html_table)
