import datetime
import os
from steem import Steem

# grab config vars
steemPostingKey = os.environ.get('steemPostingKey')
steemAccountName = os.environ.get('steemAccountName')

s = Steem()
sbd = s.get_account(steemAccountName)['sbd_balance']
print(sbd)
