from threading import Thread
import os

print("start main")


def square_numbers():
    for i in range(1000):
        i * i


if __name__ == " __main__":
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        thread = Threds(target=square_numbers)
        threads.append(threads)

    # start threads
    for thread in threads:
        thread.start()

    # wait for all processes to finish
    # block the mail program until these processes are finished
    for thread in threads:
        threads.join()

print("end main")
