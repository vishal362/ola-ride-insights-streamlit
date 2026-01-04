# ----------------------------------------
# PART 1: Imports & App Configuration
# ----------------------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration (must be at the top)
st.set_page_config(
    page_title="OLA Ride Insights Dashboard",
    page_icon="🚖",
    layout="wide"
)
# ----------------------------------------
# PART 2: App Title & Description
# ----------------------------------------

st.title("🚖 OLA Ride Insights Dashboard")

st.write(
    "This dashboard presents key insights from OLA ride data "
    "for the month of July. It summarizes ride trends, booking "
    "status, revenue patterns, and customer-driver behavior."
)
# ----------------------------------------
# PART 3: Load CSV Data
# ----------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("OLA_July_Cleaned.csv")

df = load_data()

# ----------------------------------------
# PART 4: Data Preview
# ----------------------------------------

st.markdown("---")
st.header("📄 OLA Ride Data Preview")

# Show first few rows of the dataset
st.dataframe(df.head(10))

# ----------------------------------------
# PART 5: Booking Status Breakdown
# ----------------------------------------

st.markdown("---")
st.header("📌 Booking Status Breakdown")

# Aggregate booking status counts
status_counts = (
    df["Booking_Status"]
    .value_counts()
    .reset_index()
)
status_counts.columns = ["Booking_Status", "Total_Rides"]

# Optional: show summary table
st.subheader("🔢 Booking Status Summary")
st.dataframe(status_counts)

# Bar chart for booking status
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(
    status_counts["Booking_Status"],
    status_counts["Total_Rides"]
)

ax.set_title("Booking Status Distribution")
ax.set_xlabel("Booking Status")
ax.set_ylabel("Number of Rides")
plt.xticks(rotation=30)

st.pyplot(fig)

# ----------------------------------------
# PART 6: Ride Volume Over Time
# ----------------------------------------

st.markdown("---")
st.header("📈 Ride Volume Over Time")

# Ensure Date column is in datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate rides per day
rides_by_date = (
    df.groupby("Date")
      .size()
      .reset_index(name="Total_Rides")
)

# Line chart for daily ride volume
fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(
    rides_by_date["Date"],
    rides_by_date["Total_Rides"],
    marker="o"
)

ax.set_title("Daily Ride Volume Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Rides")
plt.xticks(rotation=45)

st.pyplot(fig)

# =========================
# STEP 7: Revenue Analysis
# =========================

st.header("💰 Revenue Analysis")

st.write(
    """
    This section focuses on revenue-related insights from OLA ride data.
    Understanding revenue distribution helps identify high-performing
    vehicle types and customer segments.
    """
)

# ---- Total Revenue ----

total_revenue = df["Booking_Value"].sum()

st.subheader("📊 Total Revenue Generated")
st.metric(
    label="Total Booking Value (₹)",
    value=f"₹ {total_revenue:,.0f}"
)

# ---- Revenue by Vehicle Type ----

revenue_by_vehicle = (
    df.groupby("Vehicle_Type")["Booking_Value"]
    .sum()
    .reset_index()
    .sort_values(by="Booking_Value", ascending=False)
)

st.subheader("🚗 Revenue by Vehicle Type")

st.dataframe(
    revenue_by_vehicle,
    use_container_width=True
)
st.subheader("📈 Revenue Contribution by Vehicle Type")

st.bar_chart(
    data=revenue_by_vehicle,
    x="Vehicle_Type",
    y="Booking_Value"
)

# ==============================
# STEP 8: Cancellation Analysis
# ==============================

st.header("❌ Cancellation Analysis")

st.write(
    """
    This section analyzes ride cancellations to understand operational
    issues and customer behavior. Reducing cancellations directly improves
    revenue and customer satisfaction.
    """
)
# ---- Cancellation Rate ----

total_rides = len(df)
canceled_rides = df[df["Is_Canceled"] == True].shape[0]

cancellation_rate = (canceled_rides / total_rides) * 100

st.subheader("📊 Overall Cancellation Rate")

st.metric(
    label="Cancellation Rate",
    value=f"{cancellation_rate:.2f} %",
)

# ---- Booking Status Distribution ----

status_counts = df["Booking_Status"].value_counts().reset_index()
status_counts.columns = ["Booking_Status", "Total_Rides"]

st.subheader("📋 Booking Status Breakdown")

st.dataframe(status_counts, use_container_width=True)

st.subheader("📉 Booking Status Distribution")

st.bar_chart(
    data=status_counts,
    x="Booking_Status",
    y="Total_Rides"
)

# ---- Cancellation Responsibility ----

cancel_df = df[df["Is_Canceled"] == True]

cancel_reason_counts = cancel_df["Booking_Status"].value_counts().reset_index()
cancel_reason_counts.columns = ["Cancellation_Type", "Count"]

st.subheader("👤 Cancellation Responsibility")

st.dataframe(cancel_reason_counts, use_container_width=True)

st.subheader("📊 Who Cancels More?")

st.bar_chart(
    data=cancel_reason_counts,
    x="Cancellation_Type",
    y="Count"
)

# ==============================
# STEP 9: Payment Method Analysis
# ==============================

st.header("💳 Payment Method Analysis")

st.write(
    """
    This section analyzes customer payment preferences and revenue contribution
    by each payment method. Understanding this helps improve checkout experience
    and payment partnerships.
    """
)
# ---- Payment Method Usage ----

payment_counts = (
    df["Payment_Method"]
    .value_counts()
    .reset_index()
)

payment_counts.columns = ["Payment_Method", "Total_Rides"]

st.subheader("📊 Payment Method Usage")

st.dataframe(payment_counts, use_container_width=True)

st.subheader("📉 Payment Method Preference")

st.bar_chart(
    data=payment_counts,
    x="Payment_Method",
    y="Total_Rides"
)
# ---- Revenue by Payment Method ----

payment_revenue = (
    df.groupby("Payment_Method")["Booking_Value"]
    .sum()
    .reset_index()
)

payment_revenue.columns = ["Payment_Method", "Total_Revenue"]

st.subheader("💰 Revenue by Payment Method")

st.dataframe(payment_revenue, use_container_width=True)

st.subheader("📊 Revenue Contribution by Payment Method")

st.bar_chart(
    data=payment_revenue,
    x="Payment_Method",
    y="Total_Revenue"
)
# ==============================
# STEP 10: Ratings Analysis
# ==============================

st.header("⭐ Ratings Analysis")

st.write(
    """
    This section analyzes customer and driver ratings to understand service quality,
    customer satisfaction, and driver performance trends.
    """
)

# ---- Customer Ratings Distribution ----

st.subheader("👤 Customer Ratings Distribution")

customer_ratings = df["Customer_Rating"].dropna()

st.histogram = st.bar_chart(
    customer_ratings.value_counts().sort_index()
)

# ---- Driver Ratings Distribution ----

st.subheader("🚖 Driver Ratings Distribution")

driver_ratings = df["Driver_Ratings"].dropna()

st.bar_chart(
    driver_ratings.value_counts().sort_index()
)
# ---- Average Ratings Comparison ----

avg_ratings = {
    "Customer Rating": customer_ratings.mean(),
    "Driver Rating": driver_ratings.mean()
}

avg_ratings_df = (
    pd.DataFrame(list(avg_ratings.items()), columns=["Type", "Average_Rating"])
)

st.subheader("📊 Average Ratings Comparison")

st.dataframe(avg_ratings_df, use_container_width=True)

st.bar_chart(
    data=avg_ratings_df,
    x="Type",
    y="Average_Rating"
)
