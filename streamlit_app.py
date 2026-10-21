import streamlit as st
from PIL import Image
import sympy as sp

st.set_page_config(page_title="حل واجب رياضيات", page_icon="✅", layout="centered")

st.markdown("## ✅ حل واجب رياضيات")

uploaded = st.file_uploader("📸 ارفع صورة الواجب", type=["jpg","png","jpeg"])

def احل_المعادلة(نص):
    try:
        x = sp.symbols('x')
        clean = نص.replace('س','x').replace('×','*').replace('÷','/').lower()
        if '=' in clean:
            left, right = clean.split('=')
            eq = sp.Eq(sp.sympify(left), sp.sympify(right))
            sol = sp.solve(eq, x)
        else:
            sol = sp.solve(sp.sympify(clean), x)
        return sol
    except:
        return None

سؤال = st.text_input("اكتب المسألة هنا:", value="x+5=15")

if سؤال:
    حل = احل_المعادلة(سؤال)
    if حل is not None:
        st.markdown("### 1. فهم السؤال:")
        st.write(f"السؤال: حل المعادلة {سؤال}")
        st.markdown("### 2. خطوات الحل:")
        st.write("• نحدد المطلوب\n• ننقل الرقم\n• نحسب")
        st.markdown("### 3. الحل الكامل:")
        st.success(f"x = {حل[0] if حل else حل}")
        st.markdown("### 4. الشرح المبسط:")
        st.write(f"يا بطل، {سؤال} نخلي x لحالها ونطير الرقم للجهة الثانية")
        st.markdown("### 5. الإجابة النهائية:")
        st.markdown(f"<div style='background:#1e4620;padding:15px;border-radius:10px;color:#8ef08e;font-size:20px'>✅ x = {حل[0] if حل else حل}</div>", unsafe_allow_html=True)

if uploaded:
    st.image(Image.open(uploaded), caption="صورة الواجب")

st.divider()
st.caption("قابل للتثبيت | صنع في زبيد لطلاب السعودية")
