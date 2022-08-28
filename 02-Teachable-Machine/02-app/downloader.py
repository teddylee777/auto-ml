import streamlit as st
from google_images_download import google_images_download


st.title("데이터셋 다운로더")

# 초기화
if 'input_list' not in st.session_state:
    st.session_state.input_list = []

form = st.form("my_form")
user_input = form.text_input("키워드 입력")
# Now add a submit button to the form:
form.form_submit_button("추가")


# user_input = st.text_input('입력', "")
if form or st.session_state.input_list:
    if len(user_input) > 0:
        st.session_state.input_list.append(user_input)

    st.write('추가한 키워드 목록:', list(set(st.session_state.input_list)))

def download():
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords": ','.join(st.session_state.input_list),
                "limit":99, # 최대 다운로드 사진 개수는 100장으로 제한
                "size": "medium",
                "print_urls": True, 
                "format":"jpg"}

    paths = response.download(arguments)
    print(paths) 
    st.write(paths)

collect_btn = st.button('수집 시작')

if collect_btn:
    download()