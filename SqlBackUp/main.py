from webdav4.client import Client
#TODO:not add webdav4 to requirements.txt yet
client = Client(base_url='https://dav.jianguoyun.com/dav/',auth=('ksxmyqj@gmail.com', '')) #add passwd

fileNmae = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
client.upload_file(from_path='../db.sqlite3', to_path=f/SQL/{fileNmae}.sqlite3', overwrite=False)
