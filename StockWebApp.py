import streamlit as st
import pandas as pd
from PIL import Image

# ADD title and image
st.write("""
# Stock Market Web Application 
**Stock price data** , date range from Jan 22,2020 to Jan 22, 2021
""")


image = Image.open(
    "logodesign1.png")

st.image(image, use_column_width=True)


# ADD side bar header
st.sidebar.header('User Input')

# Create a function to get user imput


def get_input():
    start_date = st.sidebar.text_input("Start date", "2020-01-22")
    end_date = st.sidebar.text_input("End date", "2021-01-22")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

# Create a function to get the comapny name


def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'AMZN'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == 'GOOG':
        return 'Alphabat'
    else:
        'Not Avaliable'

# Create a function to get the comapny price data and selected timeframe


def get_data(symbol, start, end):

    # Load the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv('AMZN.csv')
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("TSLA.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("GOOG.csv")
    elif symbol.upper() == 'AAPL':
        df = pd.read_csv("AAPL.csv")
    else:
        "Not Found"

    # Get the data range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rown to 0
    start_row = 0
    end_row = 0

    # Match the user selection (date) to the date in dataset (search start date)
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    # Match the user selection (date) to the date in dataset (search end date)
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break
    # Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]


# Set the index to be the date
start, end, symbol = get_input()
# Get the data
df = get_data(symbol, start, end)
# Get the company name
company_name = get_company_name(symbol.upper())


# Display the close prices
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

# Display the volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

# Get statistica on the data
st.header('Data Statistics')
st.write(df.describe())
