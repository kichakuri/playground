# This is a sample Python script.
from polars import DataFrame

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from polars_practice import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hello Kich')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # datafile = get_raw_data()
    revenue_by_month: DataFrame = get_revenue_by_month()
    print(revenue_by_month)  # Press Ctrl+F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
