from blockstack.lib.client import BlockstackAPI

import math
import sys
import requests
import json
import hashlib
import hmac
import ecdsa


private_key = sys.argv[3]
sender_wallet = sys.argv[1]
receiver_wallet = sys.argv[2]

# Define the amount of tokens you want to send
amount = 100

# Define an optional memo describing the transfer
memo = "Transfer of" + str(amount) + "tokens to wallet abcd1234"


class HiroWallet:
    def __init__(self, secret_key):
        self.api = BlockstackAPI()
        self.secret_key = secret_key

    def send(self, recipient):
        # Construct the transaction
        tx = {
            "recipient": recipient,
            "amount": amount,
            "secret_key": self.secret_key
        }

        # Send the transaction
        # response = self.api.send_transaction(tx)

        return response


# Initialize wallets
wallet1 = HiroWallet('your_secret_key_1')
wallet2 = HiroWallet('your_secret_key_2')

# Send funds from wallet1 to wallet2
response = wallet1.send(wallet2.secret_key)

print(response)


def extract_account_number(path: str) -> int:
    segments = path.split('/')
    account_num = int(segments[3].replace("'", ''), 10)
    if math.isnan(account_num):
        raise ValueError('Cannot parse account number from path')
    return account_num


def generate_signature(transaction_hash):
    # Prepare the secp256k1 curve
    curve = ecdsa.SECP256k1

    # Load the origin's private key
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=curve)

    # Sign the transaction hash
    signature = sk.sign(bytes.fromhex(transaction_hash))

    # Return the generated signature
    return signature.hex()


def transfer():
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
    signature = hmac.new(
        private_key.encode(), msg=data_json.encode(), digestmod=hashlib.sha256
    ).hexdigest()
    headers["X-Hiro-Wallet-Signature"] = signature
    response = requests.post(url, headers=headers, data=data_json)
    return response.json()


if transfer():
    print("Transfer successful!")
else:
    print("Transfer failed")
