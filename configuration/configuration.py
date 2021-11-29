import sqlalchemy as alch
import dotenv
import os

dotenv.load_dotenv()

password=os.getenv("password")

db_name = "project_friends"
connectionData = f"mysql+pymysql://root:{password}@localhost/{db_name}"
engine = alch.create_engine(connectionData)