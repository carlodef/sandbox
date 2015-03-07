#!/usr/bin/env python
import multiprocessing
import time
import sys

def slowly_square(i):
    time.sleep(1)
    return i*i

def main():
    pool = multiprocessing.Pool(8)
    processes = []
    results = []
    try:
        #results = pool.map_async(slowly_square, range(40)).get(9999999)
        #results = pool.map(slowly_square, range(40))
        for i in range(20):
            processes.append(pool.apply_async(slowly_square, (i,)))
        for p in processes:
            results.append(p.get(3600))  # wait at most one hour

    except KeyboardInterrupt:
        pool.terminate()
        print "You stopped the program!"
        sys.exit(1)

    print "\nFinally, here are the results: ", results

if __name__ == '__main__':
    main()
