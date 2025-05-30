import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numpy as np
import pandas as pd
from datetime import datetime

cred = credentials.Certificate("/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Visualization/healthcare_bigdata_playbook_chap11/healthcare-bigdata-chap11-firebase-adminsdk-fbsvc-53891efc43.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://healthcare-bigdata-chap11-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


def calc_dist(df):
  """
  calculation of distance
  """
  x_d = df['X'] - df['p_x']
  y_d = df['Y'] - df['p_y']
  z_d = df['Z'] - df['p_z']
  return np.sqrt(x_d**2 + y_d**2 + z_d**2)

def calc_timediff(df):
  """
  The time difference is calculated and then stored in the d_time column.
  """
  d1 = datetime.strptime(str(df['timestamp']), "%Y-%m-%d %H:%M:%S.%f")
  d2 = datetime.strptime(str(df['p_timestamp']), "%Y-%m-%d %H:%M:%S.%f")
  return (d1 - d2).total_seconds()

def calc_act(df):
  """
  Calculate the velocity and store it in the calc_act column.
  """
  if df['d_time'] != 0:
    return np.abs(df['dist'] / df['d_time'])
  else:
    # 정상적인 수가 아님.
    return 0


dbRef = db.reference()

act = pd.read_csv('/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Visualization/healthcare_bigdata_playbook_chap11/OTg6QzA_activities.csv')

# 22년1월2일 데이터만 추출해서, 가시화를 해보자
data220102 = act[ (act['timestamp'] >= '2022-01-02 00:00:00.000') & (act['timestamp'] < '2022-01-03 00:00:00.000') ].copy()

data220102['p_timestamp'] = data220102.timestamp.shift(1)
data220102['p_x'] = data220102['X'].shift(1)
data220102['p_y'] = data220102['Y'].shift(1)
data220102['p_z'] = data220102['Z'].shift(1)

# NaN 값이 있는 행을 삭제하자. NaN가 있으면 거리 및 속도 계산할 수 없다.
# 첫번째 행이 삭제될 것이다.
tenmin = data220102.dropna().copy()

tenmin['dist'] = tenmin[["X","p_x", "Y", "p_y", "Z", "p_z"]].apply(calc_dist, axis=1)
tenmin['d_time'] = tenmin[["timestamp", "p_timestamp"]].apply(calc_timediff, axis=1)
tenmin['calc_act'] = tenmin[["dist", "d_time"]].apply(calc_act, axis=1)
tenmin['timestamp'] = tenmin['timestamp'].astype('datetime64[ns]')

cleaned = tenmin[['timestamp', 'calc_act']]
cleaned = cleaned.set_index('timestamp')

# 10분단위로 리샘플링
tenmin = cleaned.resample('10min')
result = tenmin['calc_act'].agg(['mean'])

# 칼럼 이름 변경하기
result['hm'] = result.index.values
result['hm'] = result['hm'].dt.strftime('%H:%M')

# NaN값을 zero로 채우기
result.fillna(0, inplace=True)

updates = result.to_dict(orient='records')

# device 노드 찾기
dbDevice = dbRef.child('OTg6QzA')
dbDevice.child('2022-01-02').set( updates )