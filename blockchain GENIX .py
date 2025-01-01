import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        required_prefix = '0' * difficulty
        while not self.hash.startswith(required_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = 50

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Sistemul va cădea, dar GENIX niciodată - 0000")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), self.pending_transactions)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [{"to": mining_reward_address, "amount": self.mining_reward}]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Example Usage
if __name__ == "__main__":
    genix = Blockchain()

    # Create some transactions
    genix.create_transaction({"from": "address1", "to": "address2", "amount": 100})
    genix.create_transaction({"from": "address2", "to": "address1", "amount": 50})

    # Mine block
    genix.mine_pending_transactions("miner_address")

    # Check blockchain validity
    print(f"Blockchain valid: {genix.is_chain_valid()}")

    # Print the blockchain
    for block in genix.chain:
        print(block.__dict__)
