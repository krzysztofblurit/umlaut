from time import sleep
import threading

class ThreadingTest():

    def __init__(self):
        pass

    x = 0
    thread_name = ""
    increment = 0

    def execute(self, thread_name, increment):
        self.thread_name=thread_name
        self.increment=increment+increment
        sleep(0.1)
        thread_name = self.thread_name
        increment = self.increment

        print(thread_name)
        print(increment)


if __name__ == "__main__":
    task = ThreadingTest()
    task.execute("zadanie1", 1)
    task.execute("zadanie2", 2)