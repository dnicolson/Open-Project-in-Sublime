import os, sys
import re, glob
import xml.etree.ElementTree as ET

projects = os.path.join(os.path.expanduser("~"),sys.argv[1])
items = []
sites = [d for d in os.listdir(projects) if not d.startswith(".")]

if (len(sys.argv) > 2):
    sites = [s for s in sites if re.search(sys.argv[2],s)]

for site in sites:
    path = os.path.join(projects,site)
    icon = glob.glob(path + "*/favicon.ico")
    if len(icon):
        icon = icon[0]
    else:
        icon = "icon.png"
    items.append({'uid': path,
                  'arg': path,
                  'title': site,
                  'subtitle': path,
                  'icon': icon,
                  'valid': "yes"})

if not len(items):
    items = [{'uid': "none",
              'arg': "arg",
              'title': "No Sites Found",
              'subtitle': "No sites matching your query were found",
              'icon': "icon.png",
              'valid': "no"}]

xml = ET.Element("items")

for item in items:
    xml_item = ET.SubElement(xml,"item",{'uid':item['uid'],'arg':item['arg']})
    xml_title =  ET.SubElement(xml_item,"title").text = item['title']
    xml_subtitle =  ET.SubElement(xml_item,"subtitle").text = item['subtitle']
    xml_icon =  ET.SubElement(xml_item,"icon").text = item['icon']
    xml_valid =  ET.SubElement(xml_item,"valid").text = item['valid']

print ET.tostring(xml)
