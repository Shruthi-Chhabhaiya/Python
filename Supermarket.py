import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Supermarket Daily Sales Tracker")

# Initialize session state for sales DataFrame
if "sales" not in st.session_state:
    st.session_state.sales = pd.DataFrame(columns=["Product", "Quantity", "Price", "Revenue"])

# Sales form
with st.form("sales_form"):
    product = st.text_input("Enter Product Name")
    quantity = st.number_input("Enter Quantity", min_value=1, step=1)
    price = st.number_input("Enter Price per Unit", min_value=0.0, step=0.5)
    submitted = st.form_submit_button("Add Sale")

# Add new sale record
if submitted and product:
    revenue = quantity * price
    new_row = {"Product": product, "Quantity": quantity, "Price": price, "Revenue": revenue}
    st.session_state.sales = pd.concat([st.session_state.sales, pd.DataFrame([new_row])], ignore_index=True)
    st.success(f"Added {product} - Revenue: ₹{revenue}")

# Display sales records
st.subheader("Sales Records")
st.dataframe(st.session_state.sales, use_container_width=True)

# Total revenue
total_revenue = st.session_state.sales["Revenue"].sum()
st.metric("Total revenue today", f"₹{total_revenue}")

# Plot revenue by product
if not st.session_state.sales.empty:
    fig = px.bar(
        st.session_state.sales,
        x="Product",
        y="Revenue",
        title="Revenue by Product",
        color="Product"
    )
    st.plotly_chart(fig, use_container_width=True)
