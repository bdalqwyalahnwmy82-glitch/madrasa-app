import streamlit as st
from PIL import Image

st.set_page_config(page_title="واجب رياضيات")

st.markdown("## ✅ حل واجب رياضيات")
st.write("ارفع صورة واجبك أو اكتب المعادلة")

uploaded = st.file_uploader("📸 صورة الواجب", type=["jpg","png","jpeg"])
text = st.text_input("اكتب المعادلة:", placeholder="مثال: x+5=15")

def احل(نص):
    try:
        c = نص.replace('س','x').replace(' ', '')
        if '=' in c:
            l, r = c.split('=')
            # حل معادلة x+b=a
            # نفترض شكل بسيط: 2x+3=11
            # نحولها لـ x = ...
            if 'x' in l:
                # مثال: x+5=15 => x = 15-5
                r_val = float(eval(r))
                # نحسب قيمة l عند x=0
                l0 = float(eval(l.replace('x','0').replace('2*0','0').replace('++','+')))
                # معامل x
                l1 = float(eval(l.replace('x','1')))
                a = l1 - l0
                sol = (r_val - l0) / a
                return f"✅ الحل: x = {sol}"
        return "اكتب مثل: x+5=15"
    except:
        return "اكتب المعادلة بشكل صحيح: x+5=15"

if text:
    st.success(احل(text))

if uploaded:
    st.image(Image.open(uploaded))
    st.info("تم رفع الصورة ✅")
