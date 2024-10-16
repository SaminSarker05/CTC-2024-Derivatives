import pandas as pd
from datetime import datetime

class Strategy:
  
  def __init__(self) -> None:
    self.capital : float = 100_000_000
    self.portfolio_value : float = 0

    self.start_date : datetime = datetime(2024, 1, 1)
    self.end_date : datetime = datetime(2024, 3, 30)
  
    self.options : pd.DataFrame = pd.read_csv("data/cleaned_options_data.csv")
    self.options["day"] = self.options["ts_recv"].apply(lambda x: x.split("T")[0])

    self.underlying = pd.read_csv("data/underlying_data_hour.csv")
    self.underlying.columns = self.underlying.columns.str.lower()

  def generate_orders(self) -> pd.DataFrame:
    """
      each order is a dictionary with:
        - Datetime (date/time of trade)
        - Option Symbol (unique identifier for option; in table)
        - Action (Buy or Sell)
        - Order size (# of contracts)
    """
    orders = []

    # index data    SPY  underlying_data_hour.csv
    # options data  SPX  cleaned_options_data.zip
    # minute level price data of options

    # trades must meet margin requirements for risk management
    # premium paid + 10% of strike price

    return pd.DataFrame(orders)
