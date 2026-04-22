import streamlit as st
import random
import pandas as pd

# Page Setup
st.set_page_config(page_title="Sahyadri Digital Bank", page_icon="🏦", layout="wide")

# Initialize Session State (Our "Web Database") [cite: 57, 97]
if 'balance' not in st.session_state:
    st.session_state.balance = 5000.0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- HEADER SECTION ---
st.title("🏦 Sahyadri Digital Bank")
st.markdown("### *AI-Powered Secure Banking Interface*")
st.divider()

# --- SIDEBAR NAVIGATION [cite: 51] ---
menu = ["Login Portal", "Transactions", "AI Financial Insights", "Support (OTP)"]
choice = st.sidebar.selectbox("Navigation Menu", menu)

# --- 1. LOGIN MODULE [cite: 47] ---
if choice == "Login Portal":
    st.subheader("Customer Authentication")
    col1, col2 = st.columns(2)
    with col1:
        acc_no = st.text_input("Account Number", value="101")
        pin = st.text_input("Enter 4-Digit PIN", type="password")
        if st.button("Login"):
            if pin == "1234": # Mock authentication logic
                st.session_state.logged_in = True
                st.success("Login Successful!")
            else:
                st.error("Invalid Credentials")

# --- 2. TRANSACTION MODULE (Deposit/Withdraw) [cite: 48, 49, 57] ---
elif choice == "Transactions":
    if not st.session_state.logged_in:
        st.warning("Please login first to perform transactions.")
    else:
        st.subheader("Manage Your Funds")
        st.metric("Current Balance", f"₹{st.session_state.balance:,.2f}")
        
        tab1, tab2 = st.tabs(["Deposit", "Withdraw"])
        
        with tab1:
            dep_amt = st.number_input("Amount to Deposit", min_value=0.0)
            if st.button("Confirm Deposit"):
                st.session_state.balance += dep_amt
                st.session_state.history.append(f"Deposited ₹{dep_amt}")
                st.success(f"₹{dep_amt} added to your account.")
                st.rerun()

        with tab2:
            with_amt = st.number_input("Amount to Withdraw", min_value=0.0)
            if st.button("Confirm Withdrawal"):
                # Enforcing Mini Project constraints (Min Balance 1000) 
                if with_amt > (st.session_state.balance - 1000):
                    st.error("Transaction Failed: Minimum balance of ₹1,000 required.")
                else:
                    st.session_state.balance -= with_amt
                    st.session_state.history.append(f"Withdrew ₹{with_amt}")
                    st.success(f"₹{with_amt} withdrawn successfully.")
                    st.rerun()

# --- 3. AI FINANCIAL INSIGHTS (Predictive Logic) [cite: 50, 70, 83] ---
elif choice == "AI Financial Insights":
    st.subheader("Smart Performance Analysis")
    # Simulation of Performance Prediction logic 
    avg_balance = st.session_state.balance
    
    if avg_balance > 10000:
        prediction = "Excellent Financial Health"
    elif avg_balance >= 5000:
        prediction = "Good Savings Pattern"
    else:
        prediction = "Improvement Needed: High Risk of Low Balance"
    
    st.info(f"AI Prediction: **{prediction}**")
    
    # Simple Chart for Analysis [cite: 51, 85]
    if st.session_state.history:
        st.write("Recent Activity Trend:")
        st.line_chart([1000, 2000, 1500, st.session_state.balance])

# --- 4. SUPPORT (OTP Simulation) [cite: 25, 44] ---
elif choice == "Support (OTP)":
    st.subheader("Security & Account Recovery")
    if st.button("Generate Security OTP"):
        otp = random.randint(100000, 999999)
        st.warning(f"Verification Code: {otp}")
        st.write("Use this code to verify your identity with the bank admin.")
