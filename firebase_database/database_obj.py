from firebase_database import firestore_database as database

db = database.FireData().db

db_users = db.collection(u'users')
