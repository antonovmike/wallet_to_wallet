import sys
import ecdsa
import requests


private_key = sys.argv[3]
sender_wallet = sys.argv[1]
receiver_wallet = sys.argv[2]
url = "https://wallet.hiro.so/api/v1/transactions"
transaction_hash = "123"

# Define the amount of tokens you want to send
amount = 100

transaction_data = {
    "from_address": sender_wallet,
    "to_address": receiver_wallet,
    "transaction_hash": transaction_hash,
    "amount": amount,
    "currency": "XRP",
    "fee": 0.000012,
    "nonce": 1,
    "timestamp": 1626580000
}

# Define an optional memo describing the transfer
memo = "Transfer of" + str(amount) + "tokens to wallet abcd1234"


def generate_signature():
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    signature = sk.sign(transaction_hash)
    return signature


def send_transaction():
    signature = generate_signature()
    headers = {
        "Signature": signature,
        "Content-Type": "application/json",
        "X-Hiro-Wallet-Application-Id": "YOUR_APP_ID",
        "X-Hiro-Wallet-Client-Id": "YOUR_CLIENT_ID"
    }
    response = requests.post(url, headers=headers, json=transaction_data)
    return response.json()


if send_transaction():
    print("Transfer successful!")
else:
    print("Transfer failed")
