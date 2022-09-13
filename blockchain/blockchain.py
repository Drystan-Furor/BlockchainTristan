from datetime import datetime

class Blockchain:
    def __init__(self) -> None:
        pass
    
    def create_genesis_block():
            block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
    return block