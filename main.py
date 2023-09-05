import sys
import ecdsa
import requests
import binascii
import json
import hashlib

# Generate
# Validate and sign
# Broadcast

private_key = sys.argv[3]
private_key = bytes(private_key, 'utf-8')
sender_wallet = sys.argv[1]
receiver_wallet = sys.argv[2]
url = "https://wallet.hiro.so/api/v1/transactions"
amount = 22

transaction_data = {
    "tx_type": "token_transfer",
    "sender_address": sender_wallet,
    "token_transfer": {
        "recipient_address": receiver_wallet,
        "amount": amount,
        "memo": ""
    },
    "fee_rate": "180",
    "sponsored": False,
    "post_condition_mode": "deny",
    "nonce": 1
}

serialized_tx = binascii.hexlify(json.dumps(transaction_data).encode()).decode()
hash_object = hashlib.new('sha512_256')
hash_object.update(serialized_tx.encode())
transaction_hash = hash_object.hexdigest()

# Define an optional memo describing the transfer
# memo = "Transfer of" + str(amount) + "tokens to wallet" + str(receiver_wallet)


def generate_signature():
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    signature = sk.sign(transaction_hash.encode())
    return signature


def send_transaction():
    signature = generate_signature()
    headers = {
        "Signature": signature,
        "Content-Type": "application/json",
        "X-Hiro-Wallet-Application-Id": "YOUR_APP_ID",
        "X-Hiro-Wallet-Client-Id": "YOUR_CLIENT_ID"
    }
    # response = requests.post(url, headers=headers, json=transaction_data)
    response = requests.post(url, headers=headers, data=serialized_tx)
    return response.json()


if send_transaction():
    print("Transfer successful!")
else:
    print("Transfer failed")
