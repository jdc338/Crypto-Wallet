import pymongo
from app.controllers.user_controller import add_user
# Add this at the top of your test_user_functions.py
import sys
sys.path.insert(0, '/Users/jdc338/Crypto-Wallet/backend')


def test_add_user():
    user_id = add_user('James', 'james@gmail.com', 'Password12')
    assert user_id is not None
