import multiprocessing
import time
import sys

def worker(i):
    time.sleep(i)
    return i


def example_with_map_async():
   n = 10
   pool = multiprocessing.Pool()
   result = pool.map_async(worker, range(n))

   while True:
       time.sleep(0.5)
       sys.stderr.write("%02d / %02d\r" % (n - result._number_left, n))
       if result.ready():
           break

   real_result = result.get()
   pool.close()
   pool.join()


# example with apply_async
COUNTER = 0

def f(i):
    return i

def print_progession(a):
    global COUNTER
    COUNTER += 1
    sys.stdout.write("%02d\r" % COUNTER)

if __name__ == "__main__":
    p = multiprocessing.Pool()
    for i in range(10):
        p.apply_async(f, args=(i,), callback=print_progession)

    p.close()
    p.join()
