import os
import multiprocessing


def hello() -> None:
    print(f'hello from {os.getpid()}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=hello)
    p1.start()
    print(f'hello form process {os.getpid()}')
    p1.join()
