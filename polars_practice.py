import polars as pl
#from datetime import date.datetime

def get_raw_data():
    df = pl.read_csv(r'C:\Users\benar\OneDrive\Documents\schoolproformainvoicedatesandexamcount.csv', try_parse_dates=True)
    df.with_columns('Invoice Date')
    return df