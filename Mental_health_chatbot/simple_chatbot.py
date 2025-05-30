import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('jhgan/ko-sroberta-multitask')

sentences = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트 모델입니다."]
embeddings = model.encode(sentences)

df = pd.read_excel('감성대화말뭉치(최종데이터)_Training.xlsx')

common_cols = ['상황키워드', '감정_대분류', '감정_소분류']

df1 = df[common_cols + ['사람문장1', '시스템문장1']].rename(columns={'사람문장1': '사람문장', '시스템문장1': '시스템문장'})
df2 = df[common_cols + ['사람문장2', '시스템문장2']].rename(columns={'사람문장2': '사람문장', '시스템문장2': '시스템문장'})
df3 = df[common_cols + ['사람문장3', '시스템문장3']].rename(columns={'사람문장3': '사람문장', '시스템문장3': '시스템문장'})

df_combined = pd.concat([df1, df2, df3], ignore_index=True)

df_combined = df_combined.dropna(subset=['사람문장', '시스템문장'], how='all')

df_combined['embedding'] = df_combined['사람문장'].map(
    lambda x: list(model.encode(x)) if isinstance(x, str) else None
)
query_embedding = embeddings[0]  # 첫 번째 문장 기준으로 유사도 계산
df_combined['distance'] = df_combined['embedding'].map(
    lambda x: cosine_similarity([query_embedding], [x]).squeeze() if x is not None else None
)

df_combined.to_csv('flattened_dialogue.csv', index=False)