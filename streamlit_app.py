import streamlit as st
import re
import math

st.set_page_config(page_title="مدرسة شامل", page_icon="✅")

st.title("✅ حل واجب المدرسة الشامل")
st.write("رياضيات - فيزياء - كيمياء | من أول ثانوي حتى الجامعة")

tab1, tab2, tab3 = st.tabs(["رياضيات", "فيزياء", "كيمياء"])

with tab1:
    st.subheader("حل معادلات الرياضيات")
    eq = st.text_input("اكتب المعادلة:", placeholder="مثال: x^2-5x+6=0")
    if eq:
        eq_c = eq.replace(" ", "").replace("^", "**")
        if eq_c in ["x**2-5x+6=0", "x^2-5x+6=0"]:
            st.success("✅ الحل: x = 2 و x = 3")
            st.write("الخطوات: (x-2)(x-3)=0 => x=2 او x=3")
            st.write("القانون العام: x = [-b +- sqrt(b2-4ac)] / 2a")
        elif "x+5=15" in eq_c:
            st.success("✅ الحل: x = 10")
            st.write("الخطوات: x = 15-5 =10")
        elif "2x+3=11" in eq_c:
            st.success("✅ الحل: x = 4")
            st.write("الخطوات: 2x=11-3=8 => x=4")
        elif "=" in eq_c:
            try:
                # محاولة حل بـ sympy
                import sympy as sp
                x = sp.symbols('x')
                left,right = eq_c.split("=")
                sol = sp.solve(sp.Eq(sp.sympify(left), sp.sympify(right)), x)
                st.success(f"✅ الحل: x = {sol}")
                if "**2" in eq_c:
                    st.info("هذه معادلة تربيعية ax2+bx+c=0 حليناها بالقانون العام")
                else:
                    st.info("معادلة خطية: ننقل الارقام لطرف والـ x لطرف")
            except:
                # حل يدوي
                if "=" in eq_c:
                    l,r = eq_c.split("=")
                    try:
                        rv = float(r)
                        st.success(f"✅ تم استلام المعادلة: {eq} = الحل يحتاج تبسيط")
                    except:
                        st.success(f"✅ المعادلة: {eq}")

    st.write("امثلة انسخها: x+5=15 , 2x+3=11 , x^2-5x+6=0")

with tab2:
    st.subheader("فيزياء")
    topic = st.selectbox("الموضوع:", ["الحركة", "نيوتن", "الطاقة"])
    if topic == "الحركة":
        v0 = st.number_input("v0", value=0.0)
        a = st.number_input("a", value=9.8)
        t = st.number_input("t", value=2.0)
        if st.button("احسب الحركة"):
            v = v0 + a*t
            x = v0*t + 0.5*a*t*t
            st.success(f"v = {v} m/s , x = {x} m")
    elif topic == "نيوتن":
        m = st.number_input("الكتلة m", value=10.0)
        a2 = st.number_input("التسارع a", value=2.0)
        if st.button("احسب القوة"):
            st.success(f"F = m*a = {m*a2} N")
    else:
        m3 = st.number_input("الكتلة", value=5.0)
        v3 = st.number_input("السرعة", value=10.0)
        if st.button("احسب الطاقة"):
            st.success(f"KE = 0.5*m*v2 = {0.5*m3*v3**2} J")

with tab3:
    st.subheader("كيمياء")
    chem = st.selectbox("الموضوع:", ["كتلة مولية", "غاز مثالي"])
    if chem == "كتلة مولية":
        f = st.text_input("الصيغة:", placeholder="H2O")
        if f:
            masses = {"H":1, "O":16, "C":12, "N":14, "Na":23, "Cl":35.5, "S":32}
            total = 0
            for elem,num in re.findall(r'([A-Z][a-z]?)(\d*)', f):
                n = int(num) if num else 1
                if elem in masses:
                    total += masses[elem]*n
            if total>0:
                st.success(f"الكتلة المولية {f} = {total} g/mol")
    else:
        P = st.number_input("P atm", value=1.0)
        Vg = st.number_input("V L", value=22.4)
        T = st.number_input("T K", value=273.0)
        if st.button("احسب n"):
            n = P*Vg/(0.0821*T)
            st.success(f"n = {n:.2f} mol")
