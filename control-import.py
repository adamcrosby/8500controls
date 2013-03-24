#!/usr/bin/env python

import sys, pprint

reload(sys)
sys.setdefaultencoding('utf-8')
import xml.etree.ElementTree as ET

xmlns = "urn:FindingImport"

controlsXML = ET.parse(sys.argv[1])

importFile = controlsXML.getroot()

iaControls = importFile.findall("{%s}IACONTROL" % xmlns)

areas = {}
impacts = {}
count = 0
for control in iaControls:
	title = control.find("{%s}CONTROL_NUMBER" % xmlns).get('title')
	number = control.find("{%s}CONTROL_NUMBER" % xmlns).text
	MACs = [mac.text for mac in control.findall("{%s}MACCONF/{%s}MAC" % (xmlns, xmlns))]
	CONFs = [conf.text for conf in control.findall("{%s}MACCONF/{%s}CONF" % (xmlns, xmlns))]
	name = control.find("{%s}CONTROL_NAME" % xmlns).text
	area = control.find("{%s}SUBJECT_AREA" % xmlns).text
	impact = control.find("{%s}IMPACT_CODE" % xmlns).text
	desc = control.find("{%s}DESCRIPTION" % xmlns).text
	threat = control.find("{%s}THREAT" % xmlns).text
	imp = control.find("{%s}GENERAL_IMPLEMENTATION_GUIDANCE" % xmlns).text
	resources = control.find("{%s}SYSTEM_SPECIFIC_GUIDANCE_RESOURCES" % xmlns).text
	print threat
	if area in areas.keys():
		areas[area] += 1
	else:
		areas[area] = 1
	if impact in impacts.keys():
		impacts[impact] +=1
	else:
		impacts[impact] = 1
	count += 1


#print pprint.pprint(areas)
#print sum(areas.values())
#print pprint.pprint(impacts)
#print count





test = """
<IMPORT_FILE xmlns="urn:FindingImport">
  <IACONTROL>
    <CONTROL_NUMBER title="Alternate Site Designation">COAS-1</CONTROL_NUMBER>
    <MACCONF>
      <MAC>MACIII</MAC>
    </MACCONF>
    <CONTROL_NAME>Alternate Site Designation</CONTROL_NAME>
    <SUBJECT_AREA>Continuity</SUBJECT_AREA>
    <IMPACT_CODE>Medium</IMPACT_CODE>
    <DESCRIPTION>An alternate site is identified that permits the partial restoration of mission or business essential functions.</DESCRIPTION>
    <THREAT>Environmental disasters, organized disruptions, loss of utilities/services, equipment or system failures, and serious information security incidents are potential events that could disrupt mission or business essential functions.  A recovery strategy should be developed to include an alternate site to mitigate the impact of disruptive events.</THREAT>
    <GENERAL_IMPLEMENTATION_GUIDANCE>
datestr = benchmark.find("{%s}status" % xmlns).get("date")
"""
