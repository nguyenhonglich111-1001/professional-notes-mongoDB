import pymongo
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
load_dotenv()

mongodb_password = os.environ['mongodb_password']
mongodb_password = quote_plus(mongodb_password)

connect_string = f'mongodb+srv://hdttuan:{mongodb_password}@cluster0.h09da4d.mongodb.net/?retryWrites=true&w=majority'

crawlClient = pymongo.MongoClient(connect_string)
crawlClient = crawlClient['TRACKINGINVESTMENT_CRAWL']

personal_mongodb_password = os.environ['personal_mongodb_password']
personal_mongodb_password = quote_plus(personal_mongodb_password)

personal_connection_string = f'mongodb+srv://lichnh:{personal_mongodb_password}@personal.r7jxpl0.mongodb.net/?retryWrites=true&w=majority'

personal_client = pymongo.MongoClient(personal_connection_string)
codingDB = personal_client['coding']









