import streamlit as st
import pandas as pd
import os
import openai


#------- 타이틀, 헤더, 서브헤더
st.title('우리는 꽃팀 :sunflower: :hibiscus:	:cherry_blossom: :tulip:')
#st.header('어떤 꽃을 찾으세요? 지금의 계절과 꽃말을 기반으로 당신만의 꽃을 추천드립니다!')
st.subheader('어떤 꽃을 찾으세요? ')

# ----- 페이지 레이아웃
menu = ['프로그램1', '프로그램2']

choice = st.sidebar.selectbox('프로그램', menu)
# 사이드에 list의 선택박스를 생성한다.

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

#------1. 꽃말 정보 가져오기
df  = pd.read_csv('./flower_category_final3.csv')

# with col1 :
#   st.text('계절을 선택하세요')  
#   checkbox_btn = st.checkbox('봄')
#   checkbox_btn = st.checkbox('여름')
#   checkbox_btn = st.checkbox('가을')
#   checkbox_btn = st.checkbox('겨울')
  
# with col2 :
#   # column 2 에 담을 내용
#   st.text('꽃말을 선택하세요')  
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[0])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[1])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[2])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[3])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[4])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[5])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[6])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[7])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[8])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[9])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[10])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[11])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[12])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[13])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[14])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[15])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[16])
#   checkbox_btn = st.checkbox(cluster_lan['Language'].iloc[17])


##---- 클러스터 목록 가져오기
cluster = df['cluster'].unique()
 
## 선택 상자 생성
selected_cluster = st.selectbox('꽃말 선택:', cluster)
 
##----  계절 목록 가져오기
season= ['봄','여름','가을','겨울']
 
## 선택 상자 생성
selected_season = st.selectbox('계절 선택:', season)
 
## 데이터 필터링
filtered_data = df[(df['cluster'] == selected_cluster) &  (df['계절'].str.contains(selected_season) == True)]

## 필터링된 데이터 표시
st.write(filtered_data[['Name_kor', 'Name_eng', 'Language']])


# ---- 2. 꽃 장소 가져오기
# openai API 키 인증
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# 질문 작성하기
region = "대한민국"
flower_name = filtered_data['Name_kor'][0]
num = '3'
query = str(region) + "에서 " + str(flower_name) + "을 볼 수 있는 장소" + str(num)+"개를 알려줘. 설명은 빼줘."

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

# 메시지 설정하기
messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
]


# ChatGPT API 호출하기
response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)

answer = response['choices'][0]['message']['content']
answer = answer.replace('1. ','$').replace('2. ','$').replace('3. ','$')
answer_list = answer.split('$')

st.write(answer_list[1])
st.write(answer_list[2])
st.write(answer_list[3])


# ## 옵션 정의
# cluster_lan_list = list(cluster_lan['Language'])
 
# ## 선택 상자 생성
# checkbox_option = st.checkbox('옵션을 선택하세요:', cluster_lan_list)
 
# ## 선택한 옵션 표시
# st.write('선택한 옵션:', checkbox_btn)



# if st.button("click button"):
#     st.write("Data Loading..")
#     # 데이터 로딩 함수는 여기에!

# # 텍스트, 마크다운
# st.text('title *Markdown* 인식 못함')
# st.markdown('*Markdown* 출력')

# # 텍스트 또는 다양한 Python 변수/객체 출력
# st.text('This is some text.')
# x = 10
# y = 20
# st.write('x =', x, 'y =', y)

# # 데이터프레임
# df = pd.DataFrame({'col1': [1,2,3]})
# df
# st.write('데이터프레임', df)

# # 그래프 출력
# import matplotlib.pyplot as plt
# import numpy as np
# arr = np.random.normal(1,1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)
# fig

# # 코드 출력
# code = '''def hello():
# print("Hello Streamlit!")'''

# st.code(code, language='python')

# # 캡션 출력
# st.caption('This is :blue[blue]')
# st.caption('This is :red[red]')
# st.caption('This is :green[green]')
# st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# # 이모티콘 삽입

# ':100:점~ :smile:'
# ':100:점! :smile:ㅎㅎ  :thumbsup:최고!!'


# agree = st.checkbox('I agree')

# if agree:
#     st.write('Great!')
