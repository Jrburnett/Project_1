import os
import requests
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

load_dotenv()

alpaca_api_key = os.getenv("ALPACA_API")
alpaca_secret_key = os.getenv("ALPACA_API_SECERT")


alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2"
)

tickers = ["AGG", "VCIT", "HYG", "BNDX", "EMB", "VTV", "VUG", "IJH", "VB", "VXUS", "VWO"]

start_date = pd.Timestamp("2019-02-09", tz="America/New_York").isoformat()
today = pd.Timestamp("2022-02-09", tz="America/New_York").isoformat()

timeframe = "1D"

df_portfolio = alpaca.get_barset(
    tickers,
    timeframe,
    start = start_date,
    end = today
)
