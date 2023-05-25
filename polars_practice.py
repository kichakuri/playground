import polars as pl


# from datetime import datetime

def get_raw_data():
    # Get the data from the csv file in the Documents folder
    raw_df = pl.read_csv(r'schoolproformainvoicedatesandexamcount.csv',
                         try_parse_dates=True)

    # Add column for the month it was invoiced.
    # df_with_mm_and_yy = raw_df.with_columns([
    #     pl.col('Invoice Date').dt.month().alias('Inv_MM'),
    #     pl.col('Invoice Date').dt.year().alias('Inv_YY')
    # ]
    # )

    # Get Schools where the invoices amount is "Null" and Exam Series is more than 0
    schools_with_exam_but_no_inv = raw_df.filter(
        (pl.col('Invoice Amount') == 'NULL') & (pl.col('Exam Series Created') > 0)
    )



    return schools_with_exam_but_no_inv
