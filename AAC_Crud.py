from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 32834
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary
                print("Document inserted with ID:", result.inserted_id)
                return True
            except Exception as e:
                raise Exception(f"Error inserting document: {e}")
        else:
            raise ValueError("Nothing to save, because data parameter is empty")
            return False
    
# Method to implement the R in CRUD.
    def read(self, data):
        try:
            result = list(self.collection.find(data))
            return result
        except Exception as e:
            print(f"Error querying documents: {e}")
            return []
                
# Implementation of the U in CRUD (update)
    def update(self, filter, data):
        if filter is not None and data is not None:
            try:
                result = self.collection.update_one(filter, {'$set' : data})
                print(f'Document updated: {result.modified_count}')
                return result.modified_count
            except Exception as e:
                print(f'Error updating documents {e}')
                return 0
        else:
            raise ValueError('Filter and Data must not be None')
            
# Implementation of the D in CRUD (delete)
    def delete(self, data):
        if data is not None:
            try: 
                result = self.collection.delete_one(data)
                print(f'{data} deleted successfully. {result.deleted_count}')
                return result.deleted_count
            except Exception as e:
                print(f'Error deleteing {data}: {e}')
                return 0
        else: 
            raise ValueError("Data must not be None")
    
