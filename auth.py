import streamlit as st
from database import login_user, register_user, verify_pin

def login_ui():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state["user"] = username
            st.session_state["pin_verified"] = False
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

def register_ui():
    st.subheader("📝 Register")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Register"):
        register_user(username, password, pin)
        st.success("Account created successfully")

def pin_ui():
    pin = st.text_input("🔢 Enter PIN", type="password")
    if st.button("Verify PIN"):
        if verify_pin(st.session_state["user"], pin):
            st.session_state["pin_verified"] = True
            st.success("PIN verified")
        else:
            st.error("Wrong PIN")
