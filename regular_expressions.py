import re
import csv
import


def get_first_regex():
    urls = """
        hello
        2020-05-20
        http://python-engineer.com
        http://www.pyeng.net
        https://gadeassociates.co.ke
        https://www.zeraki.app
        """

    #    pattern=re.compile(r'https:?://(www\.)?([a-zA-Z-]+)(\.\w+)')
    #    matches=pattern.finditer(urls)

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

def read_from_CSV(sourcefile:str):
    sourcefile="C:\Users\benar\OneDrive\Documents\Litemore Ltd\Admin and Finance\Fin Reporting\2023\Reports\RevenueLeakageAnalytics\RawData\school proforma invoice  dates and exam count"
    with open(sourcefile) as data_file:
        reader=csv.reader(data_file)
        next(reader,none)
        data = []
        for row in reader:
            mydict={"School":row[0],"Code":row[1],"ValidityStatus":row[2],"CreationDate":row[3],"Country":row[4],"BoardingStatus":row[9],"Ownership":row[11],"SchoolGender":row[12],"ProformaAmt":row[13],"ProformaDate":row[14],"InvoiceAmt",row[15],"InvoiceDate",row[16],"ExamsProcessed":row[17]}
            data.append(mydict)
        return data
