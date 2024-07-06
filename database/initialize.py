from playhouse.migrate import *
from ap.models import Adventure
from database.main import db
import os

def initialize():
    data_dir = 'database/data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    db.connect()
    db.create_tables([
        Adventure
    ], safe=True)
    db.close()

    ## run migrations that haven't yet been run (introspect and decide)

if __name__ == '__main__':
    initialize()
