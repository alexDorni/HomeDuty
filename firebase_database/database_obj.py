from firebase_database import firestore_database as database

# DB
db = database.FireData().db

# DB -> users(col)
db_users = db.collection(u'users')

# User name after login
user_name_login = None

