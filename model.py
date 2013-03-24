#!/usr/bin/env python
from sqlalchemy import Column, Integer, String, Date, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import UniqueConstraint
import uuid
from hashlib import sha1
from database import Base

class Control(Base):
	__tablename__ = 'controls'
	title = Column(String)
	number = Column(String,primary_key=True)
	MAC = Column(String)
	CONF = Column(String)
	name = Column(String)
	subjectArea = Column(String)
	impactCode = Column(String)
	description = Column(String)
	threat = Column(Text)
	guidance = Column(Text)
	references = Column(Text)