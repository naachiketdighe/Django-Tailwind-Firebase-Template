import firebase_admin
from firebase_admin import credentials, auth as firebase_auth

cred = credentials.Certificate('login_page/firebase.json')
firebase_admin.initialize_app(cred)

auth = firebase_auth