# Vendor Performance Analysis

📊 End-to-end analytics pipeline to evaluate vendor performance using Python, SQLite, and Power BI.

## 🧠 Project Overview

This project focuses on analyzing vendor sales and procurement data to measure vendor performance. It ingests raw CSV data into a SQLite database, performs cleaning and exploratory data analysis (EDA), computes vendor performance summaries, and delivers an interactive dashboard with key KPIs and insights.

The outputs include:
- A cleaned and merged vendor performance summary (`vendor_sales_summary.csv`)
- Python scripts and Jupyter Notebooks for ingestion and analysis
- A Power BI dashboard file (`Vendor_Analysis_Dashboard.pbix`) to visualize key metrics

## 🗂️ Repository Structure

Vendor-Performance-Analysis/
├── Data_Ingestion_sqlite.ipynb # Notebook to ingest raw data into SQLite

├── EDA.ipynb # Notebook for exploratory data analysis

├── Ingestion_DB.ipynb # Notebook showing ingestion process

├── Ingestion_DB.py # Python script for ingestion into database

├── getvendorsumscript.py # Script to generate vendor summary outputs

├── vendor_sales_summary.csv # Generated summary output file

├── Vendor_Performance_Analysis.ipynb # Main analysis notebook

├── Vendor_Analysis_Dashboard.pbix # Power BI dashboard file

├── logging.log # Log output from database ingestion or scripts

├── LICENSE # MIT License

└── README.md # This documentation


## 🛠️ Tools & Technologies

- **Python** — Data cleaning, database ingestion, EDA (Pandas, NumPy)
- **SQLite** — Relational database for storing and querying sourced data
- **Jupyter Notebooks** — Interactive analysis environments
- **Power BI** — Interactive dashboard visualization
- **CSV** — Data interchange format

## 🚀 How to Use

### 1. Clone the Repository
git clone https://github.com/AbhiiisheK990/Vendor-Performance-Analysis.git
cd Vendor-Performance-Analysis

2. Install Dependencies
Make sure you have Python (3.7+) and the required libraries installed:
pip install pandas numpy sqlite3 jupyter

3. Data Ingestion
Run the Ingestion_DB.py script or open Data_Ingestion_sqlite.ipynb to ingest your raw CSV data into a SQLite database.
Ensure your raw data files are available in the expected format.

4. Exploratory Data Analysis
Open and run EDA.ipynb and Vendor_Performance_Analysis.ipynb to explore trends, patterns, and insights.
Compute descriptive statistics and visualize key metrics.

5. Vendor Summary
Use getvendorsumscript.py to generate a consolidated vendor_sales_summary.csv file summarizing vendor performance.

7. Visualize
Open Vendor_Analysis_Dashboard.pbix in Power BI to explore the insights via interactive dashboards.
Customize visualizations for more reporting or presentation use.

📌 What You’ll Find

📍 Data Ingestion
The ingestion notebooks and script load raw datasets into a SQLite database for easier querying and consistent processing.

📍 EDA & Analysis
The EDA and analysis notebooks perform cleansing, aggregation, and visualization of performance metrics such as sales, orders, and vendor contribution.

📍 Dashboard
The Power BI file provides rich visuals to:

Compare vendor performance over time
Highlight top vendors by sales
Drill down into specific performance metrics

📈 Expected Outcomes
With this project you can:
Identify top-performing vendors
Compare vendor efficiency and sales metrics
Monitor vendor contributions over time
Build data-driven insights for supplier management
