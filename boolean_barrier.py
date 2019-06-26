#!/usr/bin/env python
#from threading import Thread, Semaphore, BoundedSemaphore
import sys
import threading
from time import time
from bitarray import bitarray

NUM_THREADS = 10

mutex = threading.BoundedSemaphore(1)
thread_count = 0
barrier = threading.Semaphore(0)

boolean_barrier = threading.BoundedSemaphore(0)
boolean_thread_completion = bitarray(2 ** NUM_THREADS)

def barrier(barrier_type='count'):
    sys.stdout.write('\nBefore Spawning Threads\n')

    def count_barrier_proc():
        global mutex
        global thread_count
        global barrier
        thread_name = threading.currentThread().getName()

        mutex.acquire()
        thread_count += 1
        mutex.release()

        sys.stdout.write(f"\n\tThis is thread {thread_name} just before the block")

        if thread_count == NUM_THREADS:
            barrier.release()
        barrier.acquire()
        barrier.release()

        sys.stdout.write(f"\n\t\tThis is thread {thread_name} past the block!\n")

    def boolean_barrier_proc():
        global mutex
        global boolean_thread_completion
        global boolean_barrier
        thread_name = threading.currentThread().getName()

        mutex.acquire()
        thread_count += 1
        mutex.release()

        sys.stdout.write(f"\n\tThis is thread {thread_name} just before the block")

        if thread_count == NUM_THREADS:
            barrier.release()
        barrier.acquire()
        barrier.release()

        sys.stdout.write(f"\n\t\tThis is thread {thread_n

    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(name=f'thread_{i}', target=count_barrier_proc)
        threads.append(thread)
        thread.start()

    sys.stdout.write('\nDone spawning Threads\n')

    for thread in threads:
        sys.stdout.write(f"\n\tThread {thread.getName()} is joining")
        thread.join()

    sys.stdout.write('\nDone joining threads.\n')





if __name__ == "__main__":
    # want total time of all threads, time for each thread; also how long does it take once you've surmounted the barrier for all the rest of the threads to finish off
    time_before = time()
    barrier(barrier_type='boolean')
    time_after = time()
    print(f"Total time: {time_after - time_before}")
