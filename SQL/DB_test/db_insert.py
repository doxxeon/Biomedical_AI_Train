import pandas as pd
from sqlalchemy import create_engine

def insert_to_db(csv_file_path):
    # SQLAlchemy를 사용하여 데이터베이스 엔진 생성
    engine = create_engine('mysql+pymysql://root:1436@192.168.0.187:3306/test')

    # CSV 파일을 Pandas DataFrame으로 읽기
    try:
        df = pd.read_csv(csv_file_path, nrows=1)  # 첫 줄은 컬럼으로 사용하고 두 번째 줄부터 데이터
        df.iloc[0, 1] = 2024  # 설립연도에 정수값을 넣기
        df.iloc[0, 0] = '김도현'  # ID에 이름 넣기

        # 데이터베이스에 DataFrame 삽입
        df.to_sql('company', con=engine, if_exists='append', index=False)
        print('Data inserted successfully.')
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    csv_file = '/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/SQL/DB_test/train.csv'  # 실제 CSV 파일 경로로 업데이트
    insert_to_db(csv_file)