import streamlit as st
import os

# Input
input_program = st.text_area('最初のメッセージです')
input_error = st.text_area('次のメッセージです')
msgFinal=''

# Process
if st.button('結合'):
  msgFinal='結合結果は「'+input_program+'」と「'+input_error+'」でした'
  

# Output
  #st.write(completion.choices[0].message.content)
  st.write(msgFinal)
