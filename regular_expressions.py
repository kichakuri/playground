import csv
import polars as pl
#from datetime import date.datetime

def get_raw_data():
    df = pl.scan_csv(r'C:\Users\benar\OneDrive\Documents\schoolproformainvoicedatesandexamcount.csv', try_parse_dates=True)
    df.with_columns('Invoice Date')
    return df

# import re

'''def get_first_regex():
    my_string = 'hello world. you are the best world'
    pattern = re.compile(r'Hello', re.I)
    matches = pattern.finditer(my_string)
    for match in matches:
        print(match)


#    subbed_urls = pattern.sub(r"\2\3",urls)
#    print(subbed_urls)

#        print(match.group(0))
#        print(match.group(1))
#        print(match.group(2))
#        print(match.group(3))
#        print(match.start(), match.end())
#        print(match.span)
#        print(match.group()[0])
'''


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
