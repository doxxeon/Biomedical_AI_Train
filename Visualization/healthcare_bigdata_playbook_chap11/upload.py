import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Visualization/healthcare_bigdata_playbook_chap11/healthcare-bigdata-chap11-firebase-adminsdk-fbsvc-53891efc43.json")  # api key
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://healthcare-bigdata-chap11-default-rtdb.asia-southeast1.firebasedatabase.app/'  # target url
})

dbRef = db.reference()
print(dbRef.get())