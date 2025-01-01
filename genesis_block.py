from blockchain import Block

def create_genesis_block():
    genesis_block = Block(0, "0", int(time.time()), "Sistemul va cădea, dar GENIX niciodată - 0000")
    print("Genesis Block:")
    print(genesis_block.__dict__)

if __name__ == "__main__":
    create_genesis_block()
