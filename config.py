import os

class Config:

    def __init__(self):
        self.mysql_hostname = os.environ.get('MYSQL_HOSTNAME')
        self.mysql_username = os.environ.get('MYSQL_USERNAME')
        self.mysql_password = os.environ.get('MYSQL_PASSWORD')

config = Config()