#
# openai==1.XXで実行する(0.28ではダメ)
#

import streamlit as st
import os
import openai

os.environ["OPENAI_API_KEY"] = "XXXX" #適切なAPIキーを記述する
openai.api_key = os.getenv("OPENAI_API_KEY")

# Input
input_program = st.text_area('最初のメッセージです')
input_error = st.text_area('次のメッセージです')
msgFinal=''

# Process
if st.button('結合'):
  #msg_text='My C program is '+input_program+'. '
  #msg_text=msg_text+'I got the following error message: '+input_error+'. '
  #msg_text=msg_text+'Please show me a hint to correct my program, in Japanese. '
  ##msg_text=msg_text+'But do not show the corrected program. '
  #msg_text=msg_text+'And please show the corrected program. '
  #completion = openai.chat.completions.create(
  #  model="gpt-3.5-turbo",
  #  temperature=1.0,
  #  messages=[
  #    {"role": "user", "content": msg_text}
  #]
  #)
  msgFinal='結合結果は「'+input_program+'」と「'+input_error+'」でした'
  

# Output
  #st.write(completion.choices[0].message.content)
  st.write(msgFinal)
