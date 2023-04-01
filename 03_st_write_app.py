#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/4/1 下午5:06
# @Author  : Tianyi
# @Email   : 8363777@qq.com
# @File    : streamlit_app.pyx
# @Software: VSCode
# @Desc    : 使用 st.write 方法显示文本，数字，数据帧和绘图的示例。

# ----------------------------------------------------------------------------------------------------------------------
import os
import sys

# ----------------------------------------------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
print(BASE_DIR)

# ----------------------------------------------------------------------------------------------------------------------
import streamlit as st

# ----------------------------------------------------------------------------------------------------------------------
import altair as alt
import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------
st.header('st.write 应用示例')

# Example 1: Its basic use case is to display text and Markdown-formatted text.
st.subheader('Display Text')
st.write('Hello, :red[**World!**] :sunglasses:')

# Example 2: Its basic use case is to display text and Markdown-formatted text.
st.subheader('Display Number')
st.write(123456)

# Example 3: DataFrames can also be displayed as follows.
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})
st.subheader('Display DataFrame')
st.write(df)

# Example 4: You can pass in multiple arguments.
st.subheader('Accept multiple arguments')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5: Finally, you can also display plots as well by passing it to a variable as follows.
st.subheader('Display Charts')
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['A', 'B', 'C']
)
c = alt.Chart(df).mark_circle().encode(
    x='A', y='B', size='C', color='C', tooltip=['A', 'B', 'C']
)
st.write(c)

# Example 6: Display mathematical expressions formatted as LaTeX.
st.subheader('Display Latex Expressions')
st.latex(r'''
    a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} =
    \sum_{k=0}^{n-1} ar^k = 
    a \left(\frac{1-r^{n}}{1-r}\right)
''')

# Example 7: Display Code
st.subheader('Display Python Code')
code = r'''
def hello():
    print("Hello, Streamlit!")
'''
st.code(code, language='python')
