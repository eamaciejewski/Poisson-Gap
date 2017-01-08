#! /usr/bin/python

# Usage ./Poisson_Gap.py seed sampling_points total_points
# Ex: ./Poisson_Gap.py 1234 64 512

from __future__ import division
import random
import math
import string
import sys


def poisson(lmbd):
    L = math.exp(-lmbd)
    k = 0
    p = 1

    while p >= L:
        u = random.random()
        p *= u
        k += 1

    return k-1

def main():
    initial_seed = string.atof(sys.argv[1])
    sampling_points = string.atoi(sys.argv[2])
    total_size = string.atoi(sys.argv[3])
    ld = total_size/sampling_points
    weight = 2.0
    current_num_points = 0
    random.seed(initial_seed)
    

    while current_num_points != sampling_points:
        gap_size = 0
        current_num_points = 0
        vector_smpl_points = []

        while gap_size < total_size:
            vector_smpl_points.append(gap_size)
            gap_size += 1
            current_num_points += 1

            gap_size += poisson((ld-1.0)*weight*math.sin(gap_size/(total_size+1)*math.pi))

        if current_num_points > sampling_points:
            weight *= 1.02
       
        if current_num_points < sampling_points:
            weight /= 1.02
    
    for num in range(len(vector_smpl_points)):
        print vector_smpl_points[num]

main()

