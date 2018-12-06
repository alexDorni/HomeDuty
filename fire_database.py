import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


""" Using Cloud Firestore from Firebase it will have (Beta):

    Stored data             1 GB total 
    Bandwidth               10GB/month 
    Document writes         20K/day 
    Document reads          50K/day 
    Document deletes        20K/day 

"""
"""
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "homeduty-19661207",
})

db = firestore.client()
"""