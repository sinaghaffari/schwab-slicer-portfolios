from SchwabPortfolio import Equity, Portfolio

account_hash = 'E45C0F3D0F6E404DD3B9282DC702FE11E61805ABEFA6340231D68AD57389B416'
portfolio = Portfolio(
  name='US',
  children={
    Equity(ticker='VOO'): '0.5',
    Equity(ticker='VXF'): '0.1',
    Portfolio(
      name='US Stocks',
      children={
        Equity(ticker='AAPL'): '0.22',
        Equity(ticker='AMD'): '0.22',
        Equity(ticker='AMZN'): '0.04',
        Equity(ticker='MSFT'): '0.05',
        Equity(ticker='NVDA'): '0.23',
        Equity(ticker='RIVN'): '0.12',
        Equity(ticker='TSLA'): '0.04',
        Equity(ticker='TSM'): '0.08'
      }
    ): '0.4'
  }
)