from threading import Thread
from math import sqrt
from random import randint
from time import time

N = 5000

def calculate_r(qi,pi):
    return sqrt(abs(qi-pi))
def fill_r(q,p):
    r = []
    for i in range(N):
        cur = []
        for j in range(N):
            r.append(calculate_r(q[j],p[i]))
        r.append(cur)

Q = []
P = []
for i in range(N):
    Q.append(randint(-5,5))
    P.append(randint(-5,5))
start = time()
fill_r(Q, P)
fill_r(Q, P)
print("Without threading: " + str(time()-start)+ " seconds")
start = time()
t1 = Thread(target=fill_r, args=(Q,P,))
t1.start()
t2 = Thread(target=fill_r, args=(Q,P,))
t2.start()
t1.join()
t2.join()
print("With threading: " + str(time()-start)+ " seconds")