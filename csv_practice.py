import csv

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
