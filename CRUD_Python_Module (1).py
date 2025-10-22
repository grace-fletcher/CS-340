# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU2025' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            try:
                insert_result = self.collection.insert_one(data)  # data should be dictionary  
                return True if insert_result.acknowledged else False# Returns True if insertion is successful
            except Exception as e:
                # Handles errors that can occur during insertion
                print(f"An error occured while inserting data: {e}")
                return False # Returns False if an error occurs
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                # This will find the documents in the collection that match the query
                documents = list(self.database.animals.find(query))
                return documents # Returns the list of documents
            except errors.PyMongoError as e:
                # Handles errors that can occur during the reading process
                print(f"An error occurred while reading data: {e}")
                return [] # Returns an empty list if an error occurs
        else:
            raise Exception("Query parameter is empty")
            
    # Create method to implement the U in CRUD.
    def update(self, query, update_data):
        try:
            result = self.database.animals.update_many(query, {'$set' : update_data})
            return result.modified_count # Returns a count of updated items
        except Exception as e:
            print(f"An error occurred while updating data: {e}")
            return 0
    
    # Create method to implement the D in CRUD.
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting data: {e}")
            return 0
    