#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/4/1 下午5:06
# @Author  : Tianyi
# @Email   : 8363777@qq.com
# @File    : st_button_app.pyx
# @Software: VSCode
# @Desc    : streamlit button 应用。

# ----------------------------------------------------------------------------------------------------------------------
import os
import sys

# ----------------------------------------------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
print(BASE_DIR)

# ----------------------------------------------------------------------------------------------------------------------
import streamlit as st

st.header('ST BUTTON')

if st.button('say hello', type="primary", use_container_width=True):
    st.write('Why hello there')
else:
    st.write('Goodbye')
