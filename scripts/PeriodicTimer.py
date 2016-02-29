import threading
import functools

# From http://stackoverflow.com/questions/8600161/executing-periodic-actions-in-python

class PeriodicTimer(object):
    def __init__(self, interval, callback):
        self.interval = interval

        @functools.wraps(callback)
        def wrapper(*args, **kwargs):
            result = callback(*args, **kwargs)
            if result:
                self.thread = threading.Timer(self.interval, self.callback)
                self.thread.start()

        self.callback = wrapper

    def start(self, *args, **kwargs):
        self.thread = threading.Timer(self.interval, self.callback, args=args, kwargs=kwargs)
        self.thread.start()

    def cancel(self):
        self.thread.cancel()