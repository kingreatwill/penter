from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

Base = declarative_base()

class DBType(Enum):
    SQLITE = 'sqlite'
    MYSQL = 'mysql'
    POSTGRES = 'postgres'

class DBManager:
    def __init__(self, dbtype: DBType, dbname: str):
        engine = create_engine('sqlite:///github.db')
        Session = sessionmaker(bind=engine)

        Base.metadata.create_all(engine)
        self.session = Session()