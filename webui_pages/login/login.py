import json
import os

import mysql.connector
import streamlit as st
import pandas as pd

from get_predict_result import get_predict_result
from webui_pages.dialogue.dialogue import chat_box
from webui_pages.record.record_out import export2json
from webui_pages.record_out import ApiRequest

# 连接到数据库
connection = mysql.connector.connect(
    host='localhost',
    database='users',
    user='root1',
    password='123456'
)

cursor = connection.cursor()
username = ""


def save_db(user_name):
    user_id = user_name
    content = export2json(chat_box)
    list_str = json.dumps(content)
    is_success = get_predict_result()
    sql = "INSERT INTO mediation_record (content, is_success, user_id) VALUES (%s, %s, %s)"
    cursor.execute(sql, (list_str, is_success, user_id))

    # 提交更改并关闭连接
    connection.commit()


def login_page():
    st.image(os.path.join("img", "login_title.png"))
    with st.sidebar:
        st.title("登录")
        # 获取用户输入的用户名和密码
        global username
        username = st.text_input('用户名')
        password = st.text_input('密码', type='password')

        # 验证用户凭据
        if st.button('登录'):

            query = "SELECT * FROM user_info WHERE account = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                st.session_state.logged_in = True
                st.session_state.username = username
                query = "SELECT * FROM user_info WHERE account = %s"
                cursor.execute(query, (username,))
                user_info = cursor.fetchone()
                if user_info:
                    st.session_state.prompt1 = f"{user_info[0]}由于{user_info[8]}，从{user_info[5]}总共贷款了{user_info[9]}元，总利息为{user_info[10]}元。逾期{user_info[6]}天，总罚息为{user_info[11]}元。目前共欠{user_info[5]}{user_info[4]}元。"
                else:
                    return None
            else:
                st.error('用户名或密码错误')


def user_information_page(api: ApiRequest, is_lite: bool = None):
    global username
    st.markdown('<h1 style="text-align: center;">用户信息</h1>', unsafe_allow_html=True)
    username = st.session_state.username
    query = "SELECT * FROM user_info WHERE account = %s"
    cursor.execute(query, (username,))
    user_info = cursor.fetchone()

    if user_info is not None:
        selected_columns = [0, 8, 5, 9, 10, 6, 11, 4]  # 指定你想要选择的8个列的索引
        selected_info = [user_info[i] for i in selected_columns]  # 根据索引从user_info中选择相应的列
        index = ['当事人信息', '欠款原因', '欠款项目', '欠款金额', '总利息', '逾期天数', '总罚息', '总欠款']
        user_series = pd.Series(selected_info, index=index)
        st.table(user_series)

    else:
        st.write("未找到用户信息")

    cols = st.columns(5)

    with cols[0]:
        pass
    with cols[1]:
        pass
    with cols[3]:
        pass
    with cols[4]:
        pass
    with cols[2]:
        if st.button('退出登录'):
            save_db(username)
            st.session_state.logged_in = False  # 退出登录状态
            chat_box.reset_history()
            st.session_state.run_once = True
            st.rerun()



