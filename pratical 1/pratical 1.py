import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.data}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        # Start with the genesis block
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # The first block has no previous hash, so we pass "0"
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        # Get the hash of the last block to set as the previous hash for the new block
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), data, previous_hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash of the current block matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Test the blockchain

blockchain = Blockchain()

# Adding blocks to the blockchain
blockchain.add_block("First block after Genesis")
blockchain.add_block("Second block")
blockchain.add_block("Third block")

# Displaying each block's hash and data
for block in blockchain.chain:
    print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, Previous Hash: {block.previous_hash}")

# Validate the blockchain
print("Blockchain valid?", blockchain.is_valid())
