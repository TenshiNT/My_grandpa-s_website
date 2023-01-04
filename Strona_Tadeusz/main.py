import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie
import requests
import pandas as pd

st.set_page_config(layout='wide', page_icon='👨‍⚕️', page_title='Badania Tadeusz Zgud', )

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

image_main = 'https://scontent-waw1-1.xx.fbcdn.net/v/t31.18172-8/13064651_126716417740757_696478252405672963_o.jpg?_nc_cat=107&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=lwpOiw8V1qAAX9Rf83o&_nc_ht=scontent-waw1-1.xx&oh=00_AfBX34cs_LVmrluLIwCT1xZaTGoIgddH2vHI2PiqlaJxYw&oe=63D0E36D'
lottie_doctor = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_h55dw0gs.json')

with st.container():
    st.markdown("**<h1 style='text-align: center; color: Black, font-size: 50px;'>Badania lotniczo-lekarskie</h1>**", unsafe_allow_html=True)
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Dr n. med. Tadeusz Zgud')
        st.image(image_main, width=350)
        st.write('')
        title_css = '**<p style="font-family:Sans-serif; color:Black; font-size: 25px;">Umów się na wizytę:</p>**'
        phone_num = '<p style="font-family:Sans-serif; color:Blue; font-size: 25px;">601 425 263</p>'
        st.markdown(title_css, unsafe_allow_html=True)
        st.markdown(phone_num, unsafe_allow_html=True)
    with right_column:
        meeting_data = '<p style="font-family:Georgia; color:Black; font-size: 20px;">Szczegóły wizyty uzgadniane są telefonicznie.</p>'
        location = '<p style="font-family:Georgia; color:Black; font-size: 20px;">Gabinet nr. 201a przy ulicy Prądnickiej 10 w Krakowie.</p>'
        st.markdown(meeting_data, unsafe_allow_html=True)
        st.markdown(location, unsafe_allow_html=True)
        st.markdown('')
        if st.button('Zobacz na mapie'):
            df = pd.DataFrame(
                np.random.randn(1, 2) / [1000, 1000] + [50.082400, 19.937660],
                columns=['lat', 'lon'])
            st.map(df)
        
        st.markdown('')
        st.write('---')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st_lottie(lottie_doctor, height=300, key='Doctor')