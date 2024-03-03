import threading
from datetime import datetime
import time
import streamlit as st
from webui_pages.record_out import *
from streamlit_option_menu import option_menu
from webui_pages.dialogue.dialogue import dialogue_page
from webui_pages.knowledge_base.knowledge_base import knowledge_base_page
from webui_pages.login.login import login_page, save_db, username
from webui_pages.login.login import user_information_page
import os
import sys
from configs import VERSION
from server.utils import api_address

api = ApiRequest(base_url=api_address())
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()
my_time = st.session_state.start_time


if __name__ == "__main__":
    if not st.session_state.logged_in:
        login_page()
        st.session_state.start_time = datetime.now()
    else:
        is_lite = "lite" in sys.argv
        st.set_page_config(
            "Langchain-Chatchat WebUI",
            os.path.join("img", "login_title.png"),
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
                'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
                'About': f"""欢迎使用 Langchain-Chatchat WebUI {VERSION}！"""
            }
        )
        sidebar = st.sidebar
        # 通过侧边栏添加菜单项和帮助链接等
        pages = {
            "对话": {
                "icon": "chat",
                "func": dialogue_page,
            },
            "知识库管理": {
                "icon": "hdd-stack",
                "func": knowledge_base_page,

            },
            "个人信息": {
                "icon": "hdd-stack",
                "func": user_information_page,
            },
        }

        with st.sidebar:
            st.image(
                os.path.join(
                    "img",
                    "login_title.png"
                ),
                use_column_width=True
            )
            options = list(pages)
            icons = [x["icon"] for x in pages.values()]

            default_index = 0
            selected_page = option_menu(
                "",
                options=options,
                icons=icons,
                # menu_icon="chat-quote",
                default_index=default_index,
            )

        if selected_page in pages:
            pages[selected_page]["func"](api=api, is_lite=is_lite)


def my_function():
    global my_time
    end_time = datetime.now()
    time_difference = end_time - st.session_state.start_time
    if time_difference.seconds >= 60 and my_time != st.session_state.start_time:
        save_db(username)
        my_time = st.session_state.start_time
    while True:
        time.sleep(60)  # 暂停60秒钟后再次执行


if 'thread' not in st.session_state:
    st.session_state.thread = threading.Thread(target=my_function)
    st.session_state.thread.start()
