#!/usr/bin/env python

import sys, pprint

reload(sys)
sys.setdefaultencoding('utf-8')
import xml.etree.ElementTree as ET

checklistXML = ET.parse(sys.argv[1])

importFile = checklistXML.getroot()

vulns = importFile.findall("VULN")

vulnlist = []

for vuln in vulns:
	info = {}
	for stigdata in vuln.findall("STIG_DATA"):
		
		info [stigdata.find("VULN_ATTRIBUTE").text] = stigdata.find("ATTRIBUTE_DATA").text
	vulnlist.append(info)	
	#print stigdata.find("VULN_ATTRIBUTE")

pprint.pprint(vulnlist[2])
#print vulnlist[2].keys()

test = """    <VULN>
        <STIG_DATA>
            <VULN_ATTRIBUTE>Vuln_Num</VULN_ATTRIBUTE>
            <ATTRIBUTE_DATA>V-756</ATTRIBUTE_DATA>
        </STIG_DATA>
        <STIG_DATA>
            <VULN_ATTRIBUTE>Severity</VULN_ATTRIBUTE>
            <ATTRIBUTE_DATA>medium</ATTRIBUTE_DATA>
        </STIG_DATA>"""


