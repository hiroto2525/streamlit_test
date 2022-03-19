import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

import datetime

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteraton {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'完了しました'

# st.title('streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.dataframe(df)

# st.map(df)


# if st.checkbox('show image'):
#     img = Image.open('/Users/hiroto-ikuta/Downloads/santorini-416136_1920.jpg')
#     st.image(img, caption='kireina kesiki', use_column_width=True)

# left_column, right_column = st.columns(2)

# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('表示')

# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')



# option = st.text_input('あなたの趣味を教えてください。')
# st.write('あなたの趣味:', option)

# condition = st.slider('あなたの調子は', 0, 100000, 1000)
# 'あなたの調子は', condition



