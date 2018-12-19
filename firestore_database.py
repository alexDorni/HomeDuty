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


class FireData:
    def __init__(self):
        cred = credentials.Certificate(os.getcwd() + "\path_firebase" + "\homeduty.json")
        firebase_admin.initialize_app(cred, {
          'projectId': "homeduty-eaacd",
        })

        self.db = firestore.client()


    # Must be implemented for all the data
    def get_data(self):
        users_ref = self.db.collection(u'users').document(u'roommates').\
                    collection(u'email').document(u'daily').collection(u'tasks')
        docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
    #
    # def push_data(self):
    #     task = builder.TaskDataBuilder().name(u'garbage').build()
    #     self.db.collection(u'tasks').document().set(task.to_dict())
