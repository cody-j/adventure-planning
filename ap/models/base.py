from peewee import *

db = SqliteDatabase('database/data/ap.db')

class Base(Model):
    class Meta:
        database = db  # Specify the database to use
