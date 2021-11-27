"""
Call in Order:
Suppose we have the following code:
    public class Foo {
        public Foo() { ... }
        public void first() { ... }
        public void second() { ... }
        public void third() { ... }
    }

The same instance of Foo will be passed to three different threads. ThreadA will call first, threads will call second, and thread( will call third. Design a mechanism to ensure that first is called before second and second is called before third.
"""

import logging
from threading import Thread, Semaphore

class Foo:
    def __init__(self):
        logging.info("Initialize foo")
        self.lock1 = Semaphore(1)
        self.lock2 = Semaphore(1)

        self.lock1.acquire()
        self.lock2.acquire()

    def first(self):
        logging.info("Running first")
        self.lock1.release()

    def second(self):
        self.lock1.acquire()
        self.lock1.release()
        logging.info("Running second")
        self.lock2.release()

    def third(self):
        self.lock2.acquire()
        self.lock2.release()
        logging.info("Running third")

def thread_function(name, target_function):
    logging.info("Thread %s: starting", name)
    target_function()

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Creating foo object")
    foo = Foo()

    logging.info("Creating threads")
    t1 = Thread(target=thread_function, args=(1, foo.first, ))
    t2 = Thread(target=thread_function, args=(2, foo.second, ))
    t3 = Thread(target=thread_function, args=(3, foo.third, ))
    t1.start()
    t2.start()
    t3.start()


if __name__ == "__main__":
    main()
