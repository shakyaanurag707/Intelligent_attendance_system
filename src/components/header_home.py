import streamlit as st




def header_home():

    logo_url = "https://img.icons8.com/stickers/1200/attendance-mark.jpg"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src = '{logo_url}' style='height:100px;'/> 
            <h1 style = 'text-align:center; color:#E0E3FF'>Intelligent Attendance<br/>System</h1>
        </div>                        


                """, unsafe_allow_html=True)



def header_dashboard():

    logo_url = "https://img.icons8.com/stickers/1200/attendance-mark.jpg"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src = '{logo_url}' style='height:100px;'/> 
            <h4 style = 'text-align:left; color:#5865F2'>Intelligent Attendence<br/>System</h4>
        </div>                        


                """, unsafe_allow_html=True)