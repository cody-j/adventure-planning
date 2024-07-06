from datetime import datetime
from peewee import *
from .base import Base

class Adventure(Base):
    name =  CharField(max_length=255)
    description = TextField()
    created_at = DateTimeField(default=datetime.now)

