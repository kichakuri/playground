import pandas as pd


def get_monthly_revenue():
    raw_data = pd.read_csv('schoolproformainvoicedatesandexamcount.csv',
                           index_col='Registration',
                           usecols=['School Name', 'Creation Date', 'Proforma Amount', 'Proforma Date',
                                    'Invoice Amount', 'Invoice Date', 'Exam Series Created'])
    return raw_data
