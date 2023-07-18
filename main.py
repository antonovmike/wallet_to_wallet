import requests
import json
import hashlib
import hmac

# Authentication

# Define the address of the wallet you want to send tokens to
sender_wallet = "sender_wallet_address"
receiver_wallet = "receiver_wallet_address"

# Define the amount of tokens you want to send
amount = 100

# Define an optional memo describing the transfer
memo = "Transfer of 100 tokens to wallet abcd1234"


def transfer_funds(sender_wallet, receiver_wallet, amount):
    url = "https://wallet.hiro.so/transfer"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "sender_wallet": sender_wallet,
        "receiver_wallet": receiver_wallet,
        "amount": amount
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred during the transfer:", e)
        return False


if transfer_funds(sender_wallet, receiver_wallet, amount):
    print("Transfer successful!")
else:
    print("Transfer failed")
