import time


class Duration:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.func(*args, **kwargs)
        t2 = time.time()
        print(t2-t1)
        return result

    