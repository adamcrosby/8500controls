#!/usr/bin/env python

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import xml.etree.ElementTree as ET

xmlns = "urn:FindingImport"

controlsXML = ET.parse(sys.argv[1])

importFile = controlsXML.getroot()

iaControls = importFile.findall("{%s}IACONTROL" % xmlns)

for control in iaControls:
	title = control.find("{%s}CONTROL_NUMBER" % xmlns).get('title')
	number = control.find("{%s}CONTROL_NUMBER" % xmlns).text
	MACs = [mac.text for mac in control.findall("{%s}MACCONF/{%s}MAC" % (xmlns, xmlns))]
	CONFs = [conf.text for conf in control.findall("{%s}MACCONF/{%s}CONF" % (xmlns, xmlns))]
	name = control.find("{%s}CONTROL_NAME" % xmlns).text
	if name != title:
			print "number: %s" % number







test = """
<IMPORT_FILE xmlns="urn:FindingImport">
  <IACONTROL>
    <CONTROL_NUMBER title="Alternate Site Designation">COAS-1</CONTROL_NUMBER>
    <MACCONF>
      <MAC>MACIII</MAC>
    </MACCONF>
    <CONTROL_NAME>Alternate Site Designation</CONTROL_NAME>
datestr = benchmark.find("{%s}status" % xmlns).get("date")
"""