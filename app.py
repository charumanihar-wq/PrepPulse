import streamlit as st

st.set_page_config(page_title="PrepPulse", layout="centered")

st.title("PrepPulse – Interview Readiness Checker")
st.write("Check your interview readiness in under 2 minutes.")

name = st.text_input("Your Name")
role = st.selectbox("Target Role", ["Software Developer", "Data Analyst", "Student"])

tech = st.slider("Technical Skills Confidence", 0, 10, 5)
comm = st.slider("Communication Confidence", 0, 10, 5)
resume = st.slider("Resume Strength", 0, 10, 5)
portfolio = st.slider("Portfolio / Projects", 0, 10, 5)

if st.button("Check My Readiness"):
    score = tech*3.5 + resume*2.5 + comm*2 + portfolio*2

    st.subheader("Your Interview Readiness Score")
    st.success(f"{int(score)} / 100")

    if score < 40:
        level = "Beginner"
    elif score < 70:
        level = "Intermediate"
    else:
        level = "Interview Ready"

    st.write(f"Level: **{level}**")

    st.subheader("Suggestions")
    if tech < 6:
        st.write("- Improve technical fundamentals.")
    if comm < 6:
        st.write("- Practice mock interviews.")
    if resume < 6:
        st.write("- Improve resume structure.")
    if portfolio < 6:
        st.write("- Build or polish projects.")
