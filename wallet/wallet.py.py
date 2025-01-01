from eth_account import Account
import secrets

def create_wallet():
    # Generare cheie privată
    private_key = secrets.token_hex(32)
    private_key = "0x" + private_key
    # Creare cont folosind cheia privată
    account = Account.from_key(private_key)
    
    # Afișare informații despre portofel
    print(f'Address: {account.address}')
    print(f'Private Key: {account._private_key.hex()}')

# Creare portofel nou
if __name__ == "__main__":
    create_wallet()
