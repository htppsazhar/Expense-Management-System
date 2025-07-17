import streamlit as st
import requests
from datetime import date

API_URL = "http://localhost:8000"


def add_update_tab():
    st.header("Add / Update Expense")

    selected_date = st.date_input("Date", value=date.today())

    # Example static categories
    categories = ["Food", "Utilities", "Entertainment", "Transport", "Other"]
    default_category = "Transport"
    if default_category not in categories:
        default_category = categories[0]

    with st.form("expense_form"):
        expenses = []

        for i in range(5):  # 5 rows
            col1, col2, col3 = st.columns(3)

            amount = col1.number_input(
                "Amount", min_value=0.0, step=0.5, format="%.2f", key=f"amount_{i}"
            )

            category = col2.selectbox(
                "Category", options=categories, index=categories.index(default_category), key=f"category_{i}"
            )

            notes = col3.text_input("Notes", key=f"notes_{i}")

            if amount > 0.0:
                expenses.append({
                    "expense_date": str(selected_date),
                    "amount": amount,
                    "category": category,
                    "notes": notes
                })

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not expenses:
                st.warning("Please enter at least one expense with a non-zero amount.")
            else:
                try:
                    for expense in expenses:
                        response = requests.post(f"{API_URL}/expenses/", json=expense)
                        response.raise_for_status()
                    st.success("Expenses added/updated successfully!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error submitting expenses: {e}")
