#!/usr/bin/env python

import sys, sqlalchemy
from sqlalchemy.exc import IntegrityError
from database import db_session, init_db
from model import Control


reload(sys)
sys.setdefaultencoding('utf-8')
import xml.etree.ElementTree as ET

xmlns = "urn:FindingImport"

controlsXML = ET.parse(sys.argv[1])

importFile = controlsXML.getroot()

iaControls = importFile.findall("{%s}IACONTROL" % xmlns)
init_db()

for control in iaControls:
	c = Control()
	c.title = control.find("{%s}CONTROL_NUMBER" % xmlns).get('title')
	c.number = control.find("{%s}CONTROL_NUMBER" % xmlns).text
	c.MAC = '|'.join([mac.text for mac in control.findall("{%s}MACCONF/{%s}MAC" % (xmlns, xmlns))])
	c.CONF = '|'.join([conf.text for conf in control.findall("{%s}MACCONF/{%s}CONF" % (xmlns, xmlns))])
	c.name = control.find("{%s}CONTROL_NAME" % xmlns).text
	c.subjectArea = control.find("{%s}SUBJECT_AREA" % xmlns).text
	c.impactCode = control.find("{%s}IMPACT_CODE" % xmlns).text
	c.description = control.find("{%s}DESCRIPTION" % xmlns).text
	c.threat = control.find("{%s}THREAT" % xmlns).text
	c.guidance = control.find("{%s}GENERAL_IMPLEMENTATION_GUIDANCE" % xmlns).text
	c.references = control.find("{%s}SYSTEM_SPECIFIC_GUIDANCE_RESOURCES" % xmlns).text


	db_session.add(c)
db_session.commit()


test = u"""
<IMPORT_FILE xmlns="urn:FindingImport">
  <IACONTROL>
    <CONTROL_NUMBER title="Alternate Site Designation">COAS-1</CONTROL_NUMBER>
    <MACCONF>
      <MAC>MACIII</MAC>
    </MACCONF>
    <CONTROL_NAME>Alternate Site Designation</CONTROL_NAME>
    <SUBJECT_AREA>Continuity</SUBJECT_AREA>
    <IMPACT_CODE>High</IMPACT_CODE>
    <DESCRIPTION>An alternate site is identified that permits the restoration of all mission or business essential functions.</DESCRIPTION>
    <THREAT>Environmental disasters, organized disruptions, loss of utilities/services, equipment or system failures, and serious information security incidents are potential events that could disrupt mission or business essential functions.  A recovery strategy should be developed to include an alternate site to mitigate the impact of disruptive events.</THREAT>
    <GENERAL_IMPLEMENTATION_GUIDANCE/><SYSTEM_SPECIFIC_GUIDANCE_RESOURCES/>"""