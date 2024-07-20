import os
import datetime
import tarfile
from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
import time
import dropbox

load_dotenv()
mongoUri = os.getenv('mongo_uri')
dbnames = os.getenv('db_names').split(',')
dropbox_key = os.getenv('dropbox_key')
interval = int(os.getenv('interval'))

def run_backup():
    client = MongoClient(mongoUri)
    for dbname in dbnames:
        db = client[dbname]
        collections = db.list_collection_names()
        files_to_compress = []
        directory = create_folder_backup(dbname)
        
        for collection in collections:
            db_collection = db[collection]
            cursor = db_collection.find({})
            filename = f'{directory}/{collection}.json'
            files_to_compress.append(filename)
            
            with open(filename, 'w') as file:
                file.write('[')
                first = True
                for document in cursor:
                    if not first:
                        file.write(',')
                    file.write(dumps(document))
                    first = False
                file.write(']')
        
        tar_file = f'{directory}.tar.gz'
        make_tarfile(tar_file, files_to_compress)
        upload_to_dropbox(tar_file)

def make_tarfile(output_filename, files_to_compress):
    with tarfile.open(output_filename, "w:gz") as tar:
        for filename in files_to_compress:
            tar.add(filename)

def create_folder_backup(dbname):
    dt = datetime.datetime.now()
    directory = f'backups/bk_{dbname}_{dt.month}-{dt.day}-{dt.year}__{dt.hour}_{dt.minute}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def upload_to_dropbox(filepath):
    dbx = dropbox.Dropbox(dropbox_key)
    with open(filepath, 'rb') as f:
        dbx.files_upload(f.read(), '/' + os.path.basename(filepath))
    print(f'Uploaded {filepath} to Dropbox')

if __name__ == '__main__':
    print('Starting backup')
    while True:
        try:
            run_backup()
            print('Backup complete')
            time.sleep(interval)
        except Exception as e:
            print(e)
            print('Backup failed, retrying in 10 seconds')
            time.sleep(10)
