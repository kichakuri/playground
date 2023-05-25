# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from polars_practice import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = get_read_from_csv()
    datafile = get_raw_data()
#    print(data)
    print(datafile.head(2))
#    print (get_first_regex())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
