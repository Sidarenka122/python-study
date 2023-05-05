import time

class TribonacciGenerator:
    def __init__(self, length):
        self.length = length
        self.sequence = [0, 0, 1]

    def __iter__(self):
        for i in range(0, self.length):
            if i >= 3:
                item = sum(self.sequence)
                self.sequence[i % 3] = item

                yield item
            else:
                yield self.sequence[i]

if __name__ == '__main__':
    main_iter = TribonacciGenerator(32)

    for line in main_iter:
        print(line)
        time.sleep(0.25)