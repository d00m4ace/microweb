import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml_as_str = reparsed.toprettyxml(indent="  ")
    # Remove the first line which contains the XML declaration without encoding
    lines = pretty_xml_as_str.split('\n')
    return '\n'.join(lines[1:])

def build(sitemap_urls):
    # Create the file structure
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url_info in sitemap_urls:
        url = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(url, 'loc')
        loc.text = url_info["loc"]
        lastmod = ET.SubElement(url, 'lastmod')
        lastmod.text = url_info["lastmod"]
        
    # Convert the ElementTree to a string
    xml_string = prettify(urlset)
    
    # Write the XML string to a file, manually adding the correct XML declaration
    with open("output\sitemap.xml", "w", encoding="utf-8") as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write(xml_string)
    
    print("Sitemap generated successfully.")
    
