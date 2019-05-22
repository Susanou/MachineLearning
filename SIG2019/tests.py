#!/usr/bin/env python3

from multiprocessing import Pool
from . import fonctions
import sys, time

def f(x):
    time.sleep(10)
    return x

if __name__ == '__main__':
    print('\n Starting function')
    with Pool(processes=1) as pool:
        res = pool.apply_async(f, (1,))
        waiting, n = True, 0
        while waiting:
            try:
                waiting = not res.successful()
                data = res.get()
            except AssertionError:
                n = fonctions.loading_animation(n)
        sys.stdout.write('\r Function complete\n')
