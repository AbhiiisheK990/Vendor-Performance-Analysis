#Creating database connection
import sqlite3
import pandas as pd
import logging
from Ingestion_DB import ingest_db

logging.basicConfig(
    filename='hetvendorsum.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')

def create_vendor_summary(conn):
    ''''This function will merge the three tables and create a summary table for vendor sales analysis'''

    vendor_sales_summary = pd.read_sql_query("""With FreightSummary as (
        SELECT 
        VendorNumber, 
        SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber   
    ), 
    PurchaseSummary as (
        SELECT
        p.VendorNumber,
        p.VendorName,
        p.description,
        p.Brand,
        p.PurchasePrice,
        pp.Price as ActualPrice,
        pp.volume,
        sum(p.Quantity) as TotalPurchaseQuantity,
        sum(p.Dollars) as TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp 
            ON p.Brand = pp.Brand 
        WHERE p.PurchasePrice > 0
        group by p.VendorNumber, p.VendorName, p.description, p.Brand, p.PurchasePrice, pp.Price, pp.volume
    ),
    SalesSummary as (
        SELECT 
        VendorNo, 
        Brand, 
        sum(SalesQuantity) as TotalSalesQuantity, 
        sum(SalesDollars) as TotalSalesDollars, 
        sum(SalesPrice) as TotalSalesPrice,
        sum(ExciseTax) as TotalExciseTax
        from sales 
        group by VendorNo, Brand
    )
    SELECT 
        ps.VendorNumber,
        ps.VendorName,
        ps.description,
        ps.Brand,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss 
        ON ps.VendorNumber = ss.VendorNo 
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC""", conn)

    return vendor_sales_summary

def clean_data(df):
    '''This function will clean the data by removing leading and trailing spaces from VendorName, converting volume to float, and calculating GrossProfit, ProfitMargin, StockTurnover, and SalesToPurchaseRatio'''

#Filling missing values with 0
    df.fillna(0, inplace=True)

# Remove leading and trailing spaces from VendorName
    df['VendorName'] = df['VendorName'].str.strip()
    df['description'] = df['description'].str.strip()

# Convert volume to float
    df['volume'] = df['volume'].astype('float')

#Calculate GrossProfit, ProfitMargin, StockTurnover, and SalesToPurchaseRatio
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = df['GrossProfit'] / df['TotalSalesDollars'] * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    return df

if __name__ == "__main__":
    #Create database connection
    conn = sqlite3.connect('vendor_analytics.db')
    logging.info("Database connection created successfully.")

    #Create vendor sales summary
    vendor_sales_summary = create_vendor_summary(conn)
    logging.info("Vendor sales summary created successfully.")

    #Clean the data
    vendor_sales_summary = clean_data(vendor_sales_summary)
    logging.info("Data cleaned successfully.") 

    #Store the cleaned data in the database
    vendor_sales_summary.to_sql("vendor_sales_summary", conn, if_exists="replace", index=False)
    logging.info("Vendor sales summary stored in the database successfully.")

     #Close the database connection
    conn.close()
    logging.info("Database connection closed successfully.")
