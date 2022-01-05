import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import os

load_dotenv()

APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
BASE_PAPER_URL = os.getenv('BASE_PAPER_URL')

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, BASE_PAPER_URL)

# Get our account information.
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))