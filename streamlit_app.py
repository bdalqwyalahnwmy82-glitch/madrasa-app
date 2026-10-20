import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="تطبيق المدرسة", layout="wide", page_icon="🏫")

# --- تصميم ---
st.markdown("""
<style>
body { direction: rtl; }
.stApp { background-color: #f5f7fb; }
h1, h2, h3 { text-align: center; color: #1e3a8a; }
</style>
""", unsafe_allow_html=True)

st.title("🏫 تطبيق المدرسة الذكي")
st.markdown("### نظام إدارة الطلاب والمعلمين")

# --- القائمة الجانبية ---
with st.sidebar:
    st.header("القائمة")
        page = st.radio("اختر الصفحة:", ["الرئيسية", "الطلاب", "المعلمين", "الدرجات", "الحضور"])

        if page == "الرئيسية":
            col1, col2, col3 = st.columns(3)
                col1.metric("عدد الطلاب", "245", "12+")
                    col2.metric("عدد المعلمين", "18", "2+")
                        col3.metric("نسبة الحضور", "92%", "5%")
                            
                                st.success("مرحبا بك في نظام المدرسة المطور الجديد! تم تحديث التصميم بنجاح.")
                                    st.info(f"تاريخ اليوم: {datetime.now().strftime('%Y-%m-%d')}")
                                        st.balloons