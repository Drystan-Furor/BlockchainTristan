from blockchain.block import Block
from multiprocessing import Pool, TimeoutError
import time

def create_hash(x:int) -> str:
    block = Block(1, [], 0, '1234567890', x)

    return block.create_hash()

def calculate_hashrate() -> float:
    max_hashes = 10000000
    max_workers = 4
    
    pool = Pool(processes=max_workers)     
    
    start_time = time.time()

    # execute workers and print sequence
    pool.map(create_hash, range(max_hashes))

    end_time = time.time()   

    perf = (end_time - start_time, max_hashes)
    
    hash_rate = perf[1] / perf[0];

    print("Hashes per second: {}".format(hash_rate))

    return hash_rate