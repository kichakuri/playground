import polars as pl


def get_revenue_by_month():
    raw_data = pl.read_csv(r'schoolproformainvoicedatesandexamcount.csv', try_parse_dates=True)
    filtered_by_amount = raw_data.filter(pl.col('Invoice Amount') != 'NULL')
    data = filtered_by_amount.with_columns(pl.col('Invoice Amount').cast(pl.Float64))
    raw_data_with_mm_col = data.with_columns(pl.col('Invoice Date').dt.month().alias('Inv_MM'))
    revenue_grouped_by_month = raw_data_with_mm_col.groupby('Inv_MM')
    revenue_amt_by_month = revenue_grouped_by_month.agg(pl.sum('Invoice Amount')).sort(by='Inv_MM', ascending=False)
    return revenue_amt_by_month
