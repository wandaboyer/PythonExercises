#!/usr/bin/env python
import sys
import threading
from time import time
from bitarray import bitarray

NUM_THREADS = 10

mutex = threading.BoundedSemaphore(1)
thread_count = 0
count_barrier = threading.Semaphore(0)

boolean_barrier = threading.Semaphore(0)
boolean_thread_completion = bitarray(NUM_THREADS)
boolean_thread_completion.setall(0)
boolean_mask = bitarray(NUM_THREADS)
boolean_mask.setall(1)


def barrier(barrier_type='count'):
    sys.stdout.write('\nBefore Spawning Threads\n')

    def count_barrier_proc():
        global mutex
        global thread_count
        global count_barrier
        thread_name = threading.currentThread().getName()

        mutex.acquire()
        thread_count += 1
        mutex.release()

        sys.stdout.write(f"\n\tThis is thread {thread_name} just before the block")

        if thread_count == NUM_THREADS:
            count_barrier.release()
        count_barrier.acquire()
        count_barrier.release()

        sys.stdout.write(f"\n\t\tThis is thread {thread_name} past the block!\n")

    def boolean_barrier_proc():
        global mutex
        global boolean_thread_completion
        global boolean_barrier
        thread_name = threading.currentThread().getName()

        mutex.acquire()
        boolean_thread_completion = flip(boolean_thread_completion, thread_name)
        mutex.release()

        sys.stdout.write(f"\n\tThis is thread {thread_name} just before the block")
        
        if boolean_thread_completion == boolean_mask:
            boolean_barrier.release()
        boolean_barrier.acquire()
        boolean_barrier.release()

        sys.stdout.write(f"\n\t\tThis is thread {thread_name} past the block!\n")

    def flip(bitarray, b):
        """
            Modified from:
            https://github.com/Imperium-Software/resolver/blob/master/SATSolver/individual.py
            Flips the bit at position b.
        """
        try:
            b = int(b)
        except ValueError as e:
            raise ValueError(f"The value of b can't be interpreted as an integer; {e}")
        
        if b >= bitarray.length() or b < 0:
            return
        bitarray[b] = not bitarray[b]
        return bitarray

    threads = []
    try:
        thread_method = locals()[f"{barrier_type}_barrier_proc"]
    except KeyError as e:
        raise KeyError(f"Don't have a barrier type {barrier_type} to fetch method for; {e}")

    for i in range(NUM_THREADS):
        thread = threading.Thread(name=f'{i}', target=thread_method)
        threads.append(thread)
        thread.start()

    sys.stdout.write('\nDone spawning Threads\n')

    for thread in threads:
        sys.stdout.write(f"\n\tThread {thread.getName()} is joining")
        thread.join()

    sys.stdout.write('\nDone joining threads.\n')


if __name__ == "__main__":
    time_before = time()
    barrier(barrier_type='boolean')
    time_after = time()
    print(f"Total time: {time_after - time_before}")
