import streamlit as st
import pandas as pd 
import psycopg2
from datetime import datetime


# connection

def get_connection():
    return psycopg2.connect(
    host = 5432,
    database = zoho,
    user =  postgres,
    password = Iphone14pro
    )

# create user
def create_user(username,password):
    conn = get_connection()
    cursor = conn.cursor()
    

# st pg

st.title("user authentication ")


menu = ("signup","login","profile")
choice = st.slidebar.selectbox("Menu",menu)

if choice == "signup":
    st.subheader("creat a new Account")
    new_user = st.text_input("user_name")
    new_password = st.text_input("password", type = "password")
    if st.button("signup"):
        create_user(new_user,new_password)
        st.success("Already registered")


elif choice == "login":
    st.subheader("login your Account")
    username = st.text_input("username")
    password = st.text_input("password",type = "password")
    if st.button("login"):
        login_user("username","password")
        st.success("login successfully")
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.checking_rerun()

else:
    st.error("username or password incorrect")

if"logged_in" in st.session_state and st.session_state["logged_in"]:
    st.slidebar.subheader("Welcome")(st.session_state["username"])
    if st.slidebar.button("Logout"):
     