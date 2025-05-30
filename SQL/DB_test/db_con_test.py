from sqlalchemy import create_engine
import pandas as pd

def getdata_from_db(query):
    # 데이터베이스 연결
    try:
        engine = create_engine('mysql+pymysql://root:doxxeon@127.0.0.1:3306/')
        df = pd.read_sql(query, engine)
        return df
        
    except Exception as e:
        print("An error occurred while getting data:", e)
        return None

def main():
    query = 'SELECT * FROM test.patient'
    df = getdata_from_db(query)
    
    if df is not None:
        print(df)
        print(f"Number of records: {len(df)}")

if __name__ == '__main__':
    main()