from multiprocessing import Pool

def go(x):
    print(1)
    raise Exception("Hi, I'm an exception from a child process.")
    print(2)
    return x**2

p = Pool()
results = []
for x in range(5):
    results.append(p.apply_async(go, [x]))

p.close()

# with the join method, exceptions raised in child processes are handled
# silently
#p.join()

# with the get method, exceptions are passed then raised
for r in results:
    r.get()
