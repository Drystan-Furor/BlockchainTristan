from blockchain.block import Block
from multiprocessing import Pool
import os
import time
import sys

class Blockchain:
    difficulty = 5
    max_workers = 4
    pool = None
    batch_size = int(2.5e5)

    def __init__(self) -> None:
        self.pool = Pool(processes=Blockchain.max_workers)     

    def createProof(block:Block, start_nonce:int, end_nonce:int):
        block.nonce = start_nonce

        hash = ''
        
        print('Searched from %d to %d' % (start_nonce, end_nonce))

        for nonce in range(start_nonce, end_nonce):
            block.nonce = nonce
            hash = block.hash()
            if hash.startswith('0' * Blockchain.difficulty):
                return hash
        
        return None    
    
    def startProcess(args):
        block, nonce_range = args
        return Blockchain.createProof(block, nonce_range[0], nonce_range[1])

    def mineAsync(self, block:Block) -> str:
        
        nonce = 0

        while True:    
            nonce_ranges = [
                (nonce + i * self.batch_size, nonce + (i+1) * self.batch_size)
                for i in range(self.max_workers)
            ]

            params = [
                (block, nonce_range) for nonce_range in nonce_ranges
            ]
            
            for result in self.pool.imap_unordered(Blockchain.startProcess, params):
                if result is not None: return result

            nonce += self.max_workers * self.batch_size