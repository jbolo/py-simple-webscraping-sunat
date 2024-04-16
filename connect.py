from config import config
from sqlalchemy import create_engine

connection_string = f"mysql+mysqlconnector\
    ://{config.mysql_username}:\
        {config.mysql_password}@\
            {config.mysql_hostname}:3306/sunat"
engine = create_engine(connection_string, echo=True)