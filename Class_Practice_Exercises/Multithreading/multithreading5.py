"""
Prove that these are actually coming in as they are completed,
    let's pass in a range of seconds

Start 5 second thread first, but since we use as_completed() method, it prints
    the results in the order they are completed

With the submit method, it submits each function one at a time,
    so we can use submit method on an entire list by using map
"""
import concurrent.futures
import time

# set start time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

# using a context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    
    # create list of seconds
    seconds_list = [5, 4, 3, 2, 1]

    # map will apply the function do_something to every item in the seconds_list
    # instead of running the results as they complete, map returns in the order
    # that they were started.
    results = executor.map(do_something, seconds_list)

    for result in results:
        print(result)

finish = time.perf_counter()


print(f'Finished in {finish-start} seconds(s)')