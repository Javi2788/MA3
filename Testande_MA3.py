""" MA3.py

Student:
Mail:
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
    xlst = []
    ylst = []
    for i in range(n):
         xlst.append(random.uniform(-1, 1))
         ylst.append(random.uniform(-1, 1))
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
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
     return

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
     return 
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    
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
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	main()
