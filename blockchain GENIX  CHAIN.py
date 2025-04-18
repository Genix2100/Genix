ython
import time

class Block:
    def _init_(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data

    def _repr_(self):
        return f"Block(index={self.index}, timestamp={self.timestamp}, data='{self.data}')"

Creează blocul genesis
genesis_block = Block(0, int(time.time()), "Sistemul va cădea, dar GENIX niciodată - 0000")

print(genesis_block)

