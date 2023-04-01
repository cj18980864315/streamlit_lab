#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/4/1 下午5:06
# @Author  : Tianyi
# @Email   : 8363777@qq.com
# @File    : streamlit_app.pyx
# @Software: VSCode
# @Desc    : streamlit 应用。

# ----------------------------------------------------------------------------------------------------------------------
import os
import sys

# ----------------------------------------------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
print(BASE_DIR)

# ----------------------------------------------------------------------------------------------------------------------
import streamlit as st

st.write('Hello world')