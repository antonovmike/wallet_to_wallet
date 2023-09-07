# wallet_to_wallet
Demo app for transfer from wallet to wallet via https://wallet.hiro.so now it's called https://leather.io/

![Hiro docs](https://docs.hiro.so/get-started/transactions)

Generate signature by signing the transaction hash with the origin's private key with the curve set to secp256k1.

Install and activate Python virtual environment:
```bash
apt install python3.10-venv
```
```bash
source venv/bin/activate
```
Upgrade package installer for Python and install packages:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install ecdsa
```
```bash
pip install blockstack-client
```
Start with args
```bash
source venv/bin/activate
python3 main.py SENDER_WALLET RECEIVER_WALLET PRIVATE_KEY
```
