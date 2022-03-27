
import os
import sqlalchemy as sql 
import sqlalchemy.ext.declarative as declarative 
import sqlalchemy.orm as orm 
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv('DB_URL')
engine = sql.create_engine(DATABASE_URL)

Base = declarative.declarative_base()

Session = orm.sessionmaker()

