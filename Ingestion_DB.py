import pandas as pd 
import os
from sqlalchemy import create_engine
import time
import logging

logging.basicConfig(
    filename='logging.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')

engine = create_engine('sqlite:///vendor_analytics.db')

def ingest_db(df, table_name, engine):
    '''This function ingests the data into the database.'''
    try:
        df = pd.read_csv(df)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Data ingested successfully into table '{table_name}'.")
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")

def load_data():
    '''This function loads the data from the database.'''
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join('data', file))
            table_name = file.split('.')[0]
            ingest_db(os.path.join('data', file), table_name, engine)
    end = time.time()
    logging.info(f"Data loading completed in {(end - start)/60:.2f} minutes.")

if __name__ == "__main__":
    load_data()
