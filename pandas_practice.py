import pandas as pd


def get_monthly_revenue():
    raw_data = pd.read_csv('schoolproformainvoicedatesandexamcount.csv',
                           usecols=['School Name', 'Creation Date', 'Proforma Amount', 'Proforma Date',
                                    'Invoice Amount', 'Invoice Date', 'Exam Series Created'])
    invoice_date = pd.to_datetime(raw_data['Invoice Date'])
    raw_data['Invoice Month']=invoice_date.month
    raw_data['Invoice Year']=invoice_date.year
    return raw_data['Invoice Month']
