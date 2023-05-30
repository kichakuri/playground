import pandas as pd


def get_monthly_revenue():
    raw_data = pd.read_csv('schoolproformainvoicedatesandexamcount.csv',
                           usecols=['School Name', 'Creation Date', 'Proforma Amount', 'Proforma Date',
                                    'Invoice Amount', 'Invoice Date', 'Exam Series Created'])
    date_column = pd.DatetimeIndex(raw_data['Invoice Date'], dayfirst=True)
    raw_data['Month'] = date_column.month
    pd.set_option('display.max_columns', 8)
    raw_data = raw_data.groupby('Month')['Invoice Amount'].sum()
    return raw_data


if __name__ == '__main__':
    # datafile = get_raw_data()
    print(get_monthly_revenue())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
