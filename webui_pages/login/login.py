import mysql.connector
import streamlit as st

# 连接到数据库
connection = mysql.connector.connect(
    host='localhost',
    database='users',
    user='root1',
    password='123456'
)

cursor = connection.cursor()

if "output" not in st.session_state:
    st.session_state.output = None


def login_page():
    with st.sidebar:
        st.title("登录")

        # 获取用户输入的用户名和密码
        username = st.text_input('用户名')
        password = st.text_input('密码', type='password')
        if "prompt_shown" not in st.session_state:
            st.session_state.prompt_shown = False
        # 验证用户凭据
        if st.button('登录'):
            query = "SELECT * FROM user_info WHERE account = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:

                st.session_state.logged_in = True
                if not st.session_state.output:

                    query = "SELECT * FROM user_info WHERE account = %s"
                    cursor.execute(query, (username,))
                    user_info = cursor.fetchone()
                    if user_info:
                        st.session_state.prompt1 = f"{user_info[0]}由于{user_info[8]}，从{user_info[5]}总共贷款了{user_info[9]}元，总利息为{user_info[10]}元。逾期{user_info[6]}天，总罚息为{user_info[11]}元。目前共欠{user_info[5]}{user_info[4]}元。"

                else:
                    return None

            else:
                st.error('Invalid username or password')
