import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd

cred = credentials.Certificate("/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Visualization/healthcare_bigdata_playbook_chap11/healthcare-bigdata-chap11-firebase-adminsdk-fbsvc-53891efc43.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://healthcare-bigdata-chap11-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


dbRef = db.reference()

df_ratio = pd.read_csv('/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Visualization/healthcare_bigdata_playbook_chap11/stacked_ratio_en.csv', encoding="CP949")
updates = df_ratio.to_dict(orient='records')

# device 노드 찾기
dbDevice = dbRef.child('stackedbar')
dbDevice.set( updates )