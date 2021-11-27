import threading
import logging
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: stopping")

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main: before creating thread")
    x = threading.Thread(target = thread_function, args = (1, ))
    logging.info("Main: before running thread")
    x.start()
    logging.info("Main: wait for thread to finish")
    x.join()
    logging.info("Process finished")


if __name__ == "__main__":
    main()