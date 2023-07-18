import requests
import json
import hashlib
import hmac
import ecdsa

# Authentication
private_key = "qwerty"

# Define the address of the wallet you want to send tokens to
sender_wallet = "sender_wallet_address"
receiver_wallet = "receiver_wallet_address"

# Define the amount of tokens you want to send
amount = 100

# Define an optional memo describing the transfer
memo = "Transfer of 100 tokens to wallet abcd1234"


def generate_signature(transaction_hash):
    # Prepare the secp256k1 curve
    curve = ecdsa.SECP256k1

    # Load the origin's private key
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=curve)

    # Sign the transaction hash
    signature = sk.sign(bytes.fromhex(transaction_hash))

    # Return the generated signature
    return signature.hex()


def transfer(sender_wallet, receiver_wallet, amount):
    url = "https://wallet.hiro.so/api/v1/transactions"
    headers = {
        "Content-Type": "application/json",
        "X-Hiro-Wallet-Application-Id": "YOUR_APP_ID",
        "X-Hiro-Wallet-Client-Id": "YOUR_CLIENT_ID"
    }
    transaction_hash = "123"
    data = {
        "from_address": sender_wallet,
        "to_address": receiver_wallet,
        "transaction_hash": transaction_hash,
        "amount": amount,
        "currency": "XRP",
        "fee": 0.000012,
        "nonce": 1,
        "timestamp": 1626580000
    }
    data_json = json.dumps(data)
    signature = hmac.new(private_key.encode(), msg=data_json.encode(), digestmod=hashlib.sha256).hexdigest()
    headers["X-Hiro-Wallet-Signature"] = signature
    response = requests.post(url, headers=headers, data=data_json)
    return response.json()


if transfer(sender_wallet, receiver_wallet, amount, private_key):
    print("Transfer successful!")
else:
    print("Transfer failed")
