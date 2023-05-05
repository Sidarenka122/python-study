import time
import numpy as np

class TribonacciGenerator:
    def __init__(self, length):
        self.length = length
        self.sequence = []

    def __iter__(self):
        for i in range(0, self.length):
            arr = np.array(self.sequence)
            self.sequence.append(1 if i == 2 else sum(arr[len(arr)-2:]))

            yield self.sequence[-1]

if __name__ == '__main__':
    main_iter = TribonacciGenerator(5)

    for line in main_iter:
        print(line)
        time.sleep(0.25)