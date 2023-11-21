from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.environ.get('DBUSER')
db_pass = os.environ.get('DBPASS')
db_svr = os.environ.get('DBSERVER')
db_port = os.environ.get('DBPORT')
db_name = os.environ.get('DBNAME')


engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_pass}@{db_svr}:{db_port}/{db_name}?charset=utf8mb4')

# Create a SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()