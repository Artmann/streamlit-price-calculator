import pandas as pd
import streamlit as st

# Title of the app
st.title("Price Calculator")

# st.text("Hello World", help="This is a greeting")

# random_df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})

# st.table(random_df)


# Input for the amount of requests
requests = st.number_input(
    "Enter the number of requests:", min_value=1, value=1, step=1
)

# Radio button to select customer type
customer_type = st.radio("Select customer type:", ("Business", "Individual"), index=0)

# If the customer is an Individual, show VAT input
if customer_type == "Individual":
    vat_percentage = st.number_input(
        "Enter VAT percentage (%):", min_value=0.0, value=25.0, step=0.1
    )
else:
    vat_percentage = 0.0  # No VAT for businesses

# Base price per request (adjust as needed)
price_per_request = 10.0  # Example price per request in dollars

# Calculate the subtotal
subtotal = requests * price_per_request

# Calculate VAT amount
vat_amount = subtotal * (vat_percentage / 100)

# Calculate total price
total_price = subtotal + vat_amount

# Display the results
st.markdown("### Price Breakdown")
st.write(f"Subtotal: ${subtotal:,.2f}")
if vat_percentage > 0:
    st.write(f"VAT ({vat_percentage}%): ${vat_amount:,.2f}")
st.write(f"**Total Price: ${total_price:,.2f}**")
