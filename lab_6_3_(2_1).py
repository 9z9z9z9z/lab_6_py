from multiprocessing import Process, Value
import time
from random import randint


N = 5000


def filling(Q, P, N):
    ret = []
    for i in range(N // 5):
        tmp = []
        for j in range(N // 5):
            tmp.append(func(Q[j], P[i]))
        ret.append(tmp)


def func(q, p):
    return 1 / (1 + (q - p) ** 2)


def generate(N):
    ret = []
    for i in range(N):
        ret.append(randint(0, 10))
    return ret


if __name__ == "__main__":
    Q = generate(N)
    P = generate(N)
    start = time.time()
    filling(Q, P, N * 5)
    print(f"Without multiprocessing: {round(time.time() - start, 5)} seconds")
    start = time.time()
    for _ in range(5):
        p = Process(target=filling, args=(Q[::5], P[::5], N))
        p.start()
    print(f"With multiprocessing: {round(time.time() - start, 5)} seconds")
