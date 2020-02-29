from pymongo import MongoClient
# This connects to the mongo database
client = MongoClient ("mongodb+srv://test:notepad@notepad-xgkrs.mongodb.net/test?retryWrites=true&w=majority")
 
# Tells mongo which collection and data base to store data to
note_db = client.get_database("NoteDB")
Notes_collection = note_db.get_collection("Notes")

#saves data to database
def save_note(msg):
    Notes_collection.insert_one({'_id':msg})

    save_note ("note test")