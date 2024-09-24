import requests
import streamlit as st



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")





#


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Faisal Shaikh :wave:")
    st.title("A Computer Science Graduate")
    st.write(
        "Passionate and driven Computer Science graduate with a strong foundation in software development and problem-solving. "
        "Eager to apply my knowledge and skills to contribute to innovative projects and drive technological advancements."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am driven by a passion for:
            - Software development and creating impactful solutions.
            - Problem-solving and tackling complex challenges.
            - Contributing to innovative technological advancements.

            If this resonates with you, feel free to reach out!
            """
        )
    

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
