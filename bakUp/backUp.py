from datetime import datetime

from webdav4.client import Client
import pathlib
from dotenv import load_dotenv, find_dotenv
import os 

load_dotenv(find_dotenv())
PASSWD = os.environ['PASSWD']
# TODO:not add webdav4 to requirements.txt yet
client = Client(base_url='https://dav.jianguoyun.com/dav/bak',
                auth=('ksxmyqj@gmail.com', PASSWD))  # add passwd

fileName = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.sqlite3'
pathlike = pathlib.Path('../db.sqlite3')
client.upload_file(from_path=pathlike, to_path=fileName, overwrite=False)
print('Success\n')
