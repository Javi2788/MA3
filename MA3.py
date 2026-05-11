""" MA3.py

Student: Jakob Victorin
Mail: jakob.victorin@gmail.com
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
import numpy as np
from statistics import mean 
from time import perf_counter as pc


def approximate_pi(n):
    xlst = [random.uniform(-1, 1) for i in range(n)]
    ylst = [random.uniform(-1, 1) for i in range(n)]
    n_c = 0
    for i, j in zip(xlst, ylst):
         if (i**2 + j**2) <= 1:
            n_c += 1
    pi = 4 * (n_c / n)
    return pi

def sphere_volume(n, d): #Ex2, approximation
    xlst = [random.uniform(-1, 1) for i in range(n)]
    ylst = [random.uniform(-1, 1) for i in range(n)]

    points = zip(xlst, ylst)
    number_inside = list(filter(lambda p: (p[0]**2 + p[1] ** 2) <= 1, points))
    n_c = len(number_inside)
    pi = 4 * (n_c / n)

    r_d = 1
    Volume = ((pi ** (d/2)) / (m.gamma((d/2) + 1))) * r_d
    return Volume

def hypersphere_exact(n,d): #Ex2, real value
    r_d = 1
    Volume = ((np.pi ** (d/2)) / (m.gamma((d/2) + 1))) * r_d
    return Volume

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    with future.ProcessPoolExecutor() as ex:
         volumes = list(ex.map(sphere_volume,[n] * np, [d] * np))
    volume_avg = sum(volumes) / len(volumes)
    return volume_avg

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    n_per_process = n // np
    tasks = [n_per_process] * np
    dims = [d] * np    
    with future.ProcessPoolExecutor() as ex:
        volumes = list(ex.map(sphere_volume, tasks, dims))
    volume_avg = sum(volumes) / len(volumes)
    return volume_avg 
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        print(approximate_pi(n))

    print()
    
    #Ex2    
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    #Ex3
    print()
    n = 100000
    d = 11
    start = pc()
    volume_lst = []
    for y in range (10):
        volume = (sphere_volume(n,d))
        volume_lst.append(volume)
    print(sum(volume_lst) / len(volume_lst))
    stop = pc()
    print()
    print(f"Ex3: Sequential time of {d} and {n} with sequential code: {stop-start}")
    print("What is parallel time?")

    print()

    n = 100000
    d = 11
    start = pc()
    print(sphere_volume_parallel1(n, d))
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n} with parallell code: {stop-start}")
    print()



    #Ex4
    n = 1000000
    d = 11
    start = pc()
    print(sphere_volume_parallel2(n, d))
    stop = pc()
    print()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")

    
    

if __name__ == '__main__':
	main()
