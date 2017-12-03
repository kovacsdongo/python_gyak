import xml.etree.ElementTree as et
import pprint

#with open("worldpop.xml","r") as pop:
with open("cd_catalog.xml","r") as pop:
    data = pop.read()
    #print data

    xml_data = et.fromstring(data)

    country_list = xml_data.findall("CD")
    cd_title = []

    for records in country_list:
        cd_title.append(records.find("TITLE").text)
    pprint.pprint(cd_title)
