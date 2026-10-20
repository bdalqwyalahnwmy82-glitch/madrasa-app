import streamlit as st
import pandas as pd
from datetime import datetime
st.set_page_config(page_title="Madrasa App", layout="wide")
st.title("Madrasa School App")
st.markdown("### Smart School Management System")
with st.sidebar:
    st.header("Menu")
    page = st.radio("Select Page", ["Home", "Students", "Teachers", "Grades"])
if page == "Home":
    col1, col2, col3 = st.columns(3)
    col1.metric("Students", "245")
    col2.metric("Teachers", "18")
    col3.metric("Attendance", "92%")
    st.success("App updated successfully!")
    st.balloons()
if page == "Students":
    st.header("Students Management")
    df = pd.DataFrame({"Name": ["Ahmed Mohamed", "Salem Ali"], "Class": ["10th", "11th"], "GPA": [95, 88]})
    st.dataframe(df, use_container_width=True)
if page == "Teachers":
    st.header("Teachers")
    st.write("Teachers list")
if page == "Grades":
    st.header("Grades")
    st.write("Enter grades")
