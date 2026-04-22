import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Sahyadri Bank", page_icon="🏦")

# 2. Design the Header
st.title("🏦 Sahyadri Digital Bank")
st.markdown("### *Your Secure Online Portal*")
st.divider()

# 3. Create Navigation
menu = ["Login", "Apply for Account", "About Our Bank"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Login":
    st.subheader("Customer Login")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Access Dashboard"):
        st.success(f"Welcome back! Logged in as: {acc}")

elif choice == "Apply for Account":
    st.subheader("Join Us")
    st.text_input("Full Name")
    st.number_input("Initial Deposit", min_value=1000)
    st.button("Submit Application")

elif choice == "About Our Bank":
    st.write("Sahyadri Digital Bank is a 2nd Year AI & DS project.")
    st.info("Note: This is the web interface. Core transactions are handled by the Java Engine.")
