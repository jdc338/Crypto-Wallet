from app.database import get_db
from pymongo.errors import DuplicateKeyError

def add_wallet(user_id, wallet_name, wallet_address):
    db = get_db()
    user = db.users.find_one({'_id': user_id})
    if not user:
        return "User not found."

    if any(wallet['address'] ==  wallet_address for wallet in user.get('wallets', [])):
        return "Wallet address already added."

    if any(wallet['name'] == wallet_name for wallet in user.get('wallets', [])):
        return "Wallet named {name} already taken"

    new_wallet = {'name': wallet_name, 'address': wallet_address}
    db.users.update_one({'_id': user_id}, {'$push': {'wallets': new_wallet}})
    return "Wallet added successfully."

def remove_wallet_address(user_id, wallet_address):
    db = get_db()
    result = db.users.update_one({'_id': user_id}, {'$pull': {'wallets': {'address': wallet_address}}})
    if result.modified_count:
        return "Wallet address removed successfully."
    else:
        return "Wallet address not found or removal failed."

def list_wallet_addresses(user_id):
    db = get_db()
    user = db.users.find_one({'_id': user_id}, {'wallets': 1})
    if user:
        return user.get('wallets', [])
    else:
        return "User not found."

import requests

def get_wallet_balance(wallet_address):
    api_url = "https://api.blockchain.com/v3/exchange"
    headers = {"X-API-Token": "Your-API-Key"}
    # Add any required parameters for the API call
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        # Process the successful response
        data = response.json()
        # Extract and return the wallet balance
        return data['balance']
    else:
        # Handle errors or unsuccessful responses
        return "Error: " + response.text
