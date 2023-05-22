import polars as pl
# import re

def get_raw_data():
    df = pl.scan_csv(r'C:\Users\benar\OneDrive\Documents\schoolproformainvoicedatesandexamcount.csv', try_parse_dates=True)
    df.with_columns('Invoice Date')
    return df

def get_read_from_csv():
    sourcefile = r'C:\Users\benar\OneDrive\Documents\schoolproformainvoicedatesandexamcount.csv'
    with open(sourcefile, encoding='utf-8') as data_file:
        reader = csv.reader(data_file)
        next(reader, None)
        data = []
        for row in reader:
            mydict = {"School": row[0], "Code": row[1], "ValidityStatus": row[2], "CreationDate": row[3],
                      "Country": row[4], "BoardingStatus": row[9] if  row[9] == 'NULL' else None,
                      "Ownership": row[11], "SchoolGender": row[12],
                      "ProformaAmt": row[13], "ProformaDate": row[14], "InvoiceAmt": row[15], "InvoiceDate": row[16],
                      "ExamsProcessed": row[17]}
            data.append(mydict)
    return data
