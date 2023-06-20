import pandas as pd
import numpy as np
import matplotlib_inline as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('max_columns',200)

def get_monthly_revenue():
    raw_data = pd.read_csv('schoolproformainvoicedatesandexamcount.csv',
                           usecols=['School Name', 'Creation Date', 'Proforma Amount', 'Proforma Date',
                                    'Invoice Amount', 'Invoice Date', 'Exam Series Created'])
    date_column = pd.DatetimeIndex(raw_data['Invoice Date'], dayfirst=True)
    raw_data['Month'] = date_column.month
    # raw_data['Invoice Date'].replace(to_replace=lambda x: 0 if x == 'NULL' else x, inplace=True)
    # raw_data['Invoice Amount'].replace(to_replace=lambda x: 0 if x == 'NULL' else x, inplace=True)
    pd.set_option('display.max_columns', 8)
    sales_by_month = raw_data.groupby('Month').agg({'Proforma Amount':sum,'Invoice Amount':sum})
    print(sales_by_month)
    print(f'Total Invoice Amount: ',raw_data['Invoice Amount'].sum())
    return

if __name__ == '__main__':
    # datafile = get_raw_data()
    print(get_total_invoice_amounts())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
