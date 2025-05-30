# client.py
import requests
import pandas as pd
import time

url = 'http://localhost:9999/predict'

df = pd.read_csv('X_train_over.csv')

s_time = time.time()
fraud_count = 0

for index, row in df[:10000].iterrows():
    input_data = {'Amount_Scaled': row['Amount_Scaled'],
                  'V1': row['V1'],
                  'V2': row['V2'],
                  'V3': row['V3'],
                  'V4': row['V4'],
                  'V5': row['V5'],
                  'V6': row['V6'],
                  'V7': row['V7'],
                  'V8': row['V8'],
                  'V9': row['V9'],
                  'V10': row['V10'],
                  'V11': row['V11'],
                  'V12': row['V12'],
                  'V13': row['V13'],
                  'V14': row['V14'],
                  'V15': row['V15'],
                  'V16': row['V16'],
                  'V17': row['V17'],
                  'V18': row['V18'],
                  'V19': row['V19'],
                  'V20': row['V20'],
                  'V21': row['V21'],
                  'V22': row['V22'],
                  'V23': row['V23'],
                  'V24': row['V24'],
                  'V25': row['V25'],
                  'V26': row['V26'],
                  'V27': row['V27'],
                  'V28': row['V28'],
                  }
    try:
        start_time = time.time()
        res = requests.post(url, json=input_data)
        print('result: ', res.json())

        result = res.json()['prediction'][0]
        if result == 1:
            fraud_count += 1

        if res.status_code == 200:
            print('ok')
        else:
            print(res.status_code)

    except requests.exceptions.RequestException as e:
        print('요청 중 오류 발생:', e)

    time.sleep(0.01)

end_time = time.time()
print('소요시간: ', end_time - s_time)
print('사기 건수: ', fraud_count)