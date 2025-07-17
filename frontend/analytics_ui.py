import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta

API_URL = "http://localhost:8000"

def analytics_tab():
    st.header("Expense Analytics")

    today = date.today()
    default_start = today - timedelta(days=7)

    # Date range inputs
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value=default_start)
    with col2:
        end_date = st.date_input("End Date", value=today)

    if start_date > end_date:
        st.error("Start date cannot be after end date.")
        return

    if st.button("Generate Analytics"):
        with st.spinner("Fetching analytics..."):
            payload = {
                "start_date": str(start_date),
                "end_date": str(end_date)
            }

            try:
                response = requests.post(f"{API_URL}/analytics/", json=payload)
                response.raise_for_status()
                analytics_data = response.json()

                if not analytics_data:
                    st.warning("No expenses found for the selected date range.")
                    return

                # Convert to DataFrame
                df = pd.DataFrame(analytics_data)

                # Calculate percentages
                total_expense = df["total"].sum()
                df["percentage"] = (df["total"] / total_expense * 100).round(2)

                # Sort by total descending for better display
                df = df.sort_values(by="total", ascending=False)

                # Plotly bar chart to match screenshot style
                fig = go.Figure(
                    data=go.Bar(
                        x=df["category"],
                        y=df["total"],
                        marker_color="lightskyblue"
                    )
                )
                fig.update_layout(
                    title="Expense Breakdown by Category",
                    xaxis_title=None,
                    yaxis_title=None,
                    height=400,
                    xaxis_tickangle=-90
                )
                st.plotly_chart(fig, use_container_width=True)

                # Clean table format (rounded to 2 decimals)
                df_display = df.rename(columns={
                    "category": "Category",
                    "total": "Total",
                    "percentage": "Percentage"
                })
                df_display["Total"] = df_display["Total"].map("{:,.2f}".format)
                df_display["Percentage"] = df_display["Percentage"].map("{:.2f}".format)

                st.dataframe(df_display, use_container_width=True)

            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching analytics: {e}")
