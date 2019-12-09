"""
Running things concurrently is known as multithreading.
Running things in parallel is known as multiprocessing.

I/O bound tasks: 
    - Waiting for input and output to be completed,
        reading and writing from file system,
        and network operations.
    - These all benefit more from threading.
    - You get the illusion of running code at the same time,
        however other code starts running while other code is waiting.

CPU bound tasks:
    - Good for number crunching.
    - Using CPU
    - Data crunching
    - These benefit more from multiprocessing and running in parallel.
    - Using multiprocessing might be slower if you have
        overhead from creating and destroying files.
"""
import multiprocessing
import time


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping.')

if __name__ == "__main__":
    start = time.perf_counter()
    # create 2 processes
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # start the threads
    p1.start()
    p2.start()

    # make sure the threads are complete before moving on to calculate finish time
    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Finished in {finish-start} seconds(s)')