import yfinance as yf
import pandas as pd

def download_asset_returns(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

def load_ff_factors(filepath):
    ff = pd.read_csv(filepath, skiprows=3)
    ff = ff.rename(columns=lambda x: x.strip())
    ff['Date'] = pd.to_datetime(ff['Date'], format='%Y%m%d')
    ff.set_index('Date', inplace=True)
    ff = ff / 100  # FF factors are usually in percent
    return ff
