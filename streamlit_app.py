import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Madrasa App", layout="wide")
st.title("Madrasa School App")
st.markdown("### Smart School Management System")

with st.sidebar:
    st.header("Menu")
    page = st.radio("Select Page", ["Home", "Students", "Homework Solver", "Grades"])

if page == "Home":
    col1, col2, col3 = st.columns(3)
    col1.metric("Students", "245")
    col2.metric("Teachers", "18")
    col3.metric("Attendance", "92%")
    st.success("App updated successfully!")

if page == "Students":
    st.header("Students Management")
    df = pd.DataFrame({"Name": ["Ahmed Mohamed", "Salem Ali"], "Class": ["10th", "11th"], "GPA": [95, 88]})
    st.dataframe(df, use_container_width=True)

if page == "Homework Solver":
    st.header("📚 حل الواجب وشرحه")
    st.info("اكتب سؤال الواجب أو ارفع صورة والذكاء الاصطناعي بيحله ويشرحه لك")
    
    subject = st.selectbox("اختر المادة", ["رياضيات", "علوم", "انجليزي", "عربي", "فيزياء", "كيمياء"])
    
    question_text = st.text_area("اكتب سؤال الواجب هنا:", placeholder="مثال: حل المعادلة 2x + 5 = 15")
    
    uploaded_file = st.file_uploader("أو ارفع صورة الواجب", type=["jpg", "png", "jpeg", "pdf"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="صورة الواجب", width=300)
    
    if st.button("حل الواجب واشرحه ✨", type="primary"):
        if question_text or uploaded_file:
            st.divider()
            st.subheader(f"✅ حل واجب {subject}")
            
            with st.container():
                st.markdown("#### 1. فهم السؤال:")
                st.write(f"السؤال المطلوب: {question_text if question_text else 'من الصورة المرفوعة'}")
                st.write(f"المادة: {subject}")
                
                st.markdown("#### 2. خطوات الحل:")
                if subject == "رياضيات":
                    st.write("• الخطوة 1: نحدد المعطيات والمطلوب")
                    st.write("• الخطوة 2: نطبق القانون المناسب")
                    st.write("• الخطوة 3: نحسب النتيجة خطوة بخطوة")
                else:
                    st.write("• الخطوة 1: نقرأ السؤال بعناية")
                    st.write("• الخطوة 2: نستخرج المعلومات المهمة")
                    st.write("• الخطوة 3: نرتب الأفكار للإجابة")
                
                st.markdown("#### 3. الحل الكامل:")
                st.success(f"هنا سيظهر الحل التفصيلي لسؤال: {question_text[:100] if question_text else 'الواجب'}")
                
                st.markdown("#### 4. الشرح المبسط:")
                st.write("الشرح بطريقة سهلة للطالب عشان يفهم ليش حلينا بهذه الطريقة...")
                
                st.markdown("#### 5. الإجابة النهائية:")
                st.info("الإجابة النهائية مع التأكيد")
        else:
            st.warning("اكتب السؤال أو ارفع صورة أولاً!")

if page == "Grades":
    st.header("Grades")
    st.write("Enter grades")
