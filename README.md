# IG-markets REST and Streaming APIs combined python library

This is a combinination of REST and Streaming APIs for IG markets.

#### Streaming API for data streaming and download
- Source of download_previous_bars.py - https://pypi.python.org/pypi/trading_ig
- Source of streaming_data.py - https://github.com/femtotrader/ig-markets-stream-api-python-library

#### REST API for order mamangement and account queries
Source of REST api - https://github.com/lewisbarber/ig-markets-rest-api-python-library. I had to drop a parameter from the market order function to make it work on my ig demo account. I have also set out the various different paramenters required to send an order through via the api for sending a market order and also a limit/stop order.

REST API can be used to get 
- account information
- order management


### How To Use The Library
--------------------------

Using this library to connect to the IG Markets API is extremely easy. All you need to do is import the IGService class, create an instance, and call the methods you wish to use. There is a method for each endpoint exposed by their API. The code sample below shows you how to connect to the API, switch to a secondary account and retrieve all open positions for the active account.

**Note:** The secure session with IG is established when you create an instance of the IGService class.

```python
from utils_igmarkets.ig_service import IGService
from utils_igmarkets.trading_ig_config import Config

c = Config()
ig_service = IGService(c.username, c.password, c.api_key, c.acc_type)
ig_service.create_session()

response = ig_service.fetch_accounts()
print(response)

######## Create a market order via the api ########

response = ig_service.create_open_position(currency_code='USD', direction='BUY', epic='CS.D.AUDUSD.MINI.IP', expiry='-', force_open='false', guaranteed_stop='false', level='', limit_distance='', limit_level='', order_type='MARKET', size=3, stop_distance='', stop_level='')

######## Create an working order via the api  ########

response = ig_service.create_working_order(currency_code='USD', direction='SELL', epic='CS.D.AUDUSD.MINI.IP', expiry='-', good_till_date="2016/02/06 20:00:44", guaranteed_stop='true', level=0.7850, limit_distance=200.0, limit_level='', size=1, stop_distance=45.0, stop_level='', time_in_force='GOOD_TILL_CANCELLED', order_type='LIMIT')
```

with `ig_service_config.py`

```python
username = "DEMO-*******-LIVE"
password = "*********"
api_key = "******************************************"
acc_type = "DEMO"  # LIVE / DEMO
acc_number = "*******"
```
