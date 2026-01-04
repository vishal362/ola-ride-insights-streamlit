This project is an end-to-end data analytics application built using Python and Streamlit to analyze and visualize OLA ride data for the month of July.

The Streamlit app acts as an interactive analytical dashboard that presents key business insights derived from cleaned ride-level data.
It enables users to explore ride patterns, booking outcomes, revenue distribution, cancellations, and rating behavior in a simple web interface.# ola-ride-insights-streamlit.
The main goals of this Streamlit application are:

To present insights visually from the cleaned OLA dataset

To bridge the gap between data analysis and storytelling

To provide a lightweight alternative to Power BI dashboards

To make insights accessible via a web interface
Key Insights Covered in the App
The Streamlit dashboard includes the following analytical sections:

Ride Volume Over Time (daily trends)

Booking Status Breakdown (Success vs Cancellations)

Revenue by Payment Method

Top Vehicle Types by Usage

Ride Distance Distribution

Driver Ratings Distribution

Customer vs Driver Ratings Comparison

Each section is built using Python visualizations rendered live in Streamlit.
Tools & Technologies Used
Python

Streamlit – for web app development

Pandas & NumPy – data manipulation

Matplotlib / Seaborn / Altair – data visualization

CSV Dataset – cleaned OLA ride data


Dataset Used
File Name: OLA_July_Cleaned.csv

The dataset is a cleaned version of raw OLA ride data.

Cleaning and preprocessing were performed separately using Python (Jupyter Notebook).

