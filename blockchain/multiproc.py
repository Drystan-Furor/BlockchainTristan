from blockchain.block import Block
from multiprocessing import Pool, TimeoutError
import time

def createHash(x):
    block = Block(1, '1234567890', 0, 0)

    return block.hash()

if __name__ == '__main__':
    max_hashes = 1000000
    max_workers = 4
    
    pool = Pool(processes=max_workers)     
    
    start_time = time.time()

    # execute workers and print sequence
    print(pool.map(createHash, range(max_hashes)))

    end_time = time.time()   

    perf = (end_time - start_time, max_hashes)

    print("Hashes per second: {}".format(perf[1] / perf[0]))
  