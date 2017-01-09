#!/usr/bin/env python3

# Usage ./Poisson_Gap.py seed sampling_points total_points
# Ex: ./Poisson_Gap.py 1234 64 512

import argparse
import random
import math
import numpy as np



def poisson(lmbd):
    L = math.exp(-lmbd)
    k = 0
    p = 1

    while p >= L:
        u = random.random()
        p *= u
        k += 1

    return k-1


def frequency_array(np_array):
    freq=np.bincount(np_array)
    nums=np.arange(np.amax(np_array)+1)
    print(np.vstack((nums,freq[nums])).T)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seed", required=True, type=int, help="initial seed")
    parser.add_argument("-sp", "--sampling_points", required=True, type=int, help="number of sampling points")
    parser.add_argument("-tp", "--total_points", required=True, type=int, help="total number of points")
    args = parser.parse_args()

    final = np.array([])
    count = 0
    total = 3
    initial_seed = args.seed

    while count != total:

        
        sampling_points = args.sampling_points
        total_size = args.total_points
        ld = total_size/sampling_points
        weight = 2.0
        current_num_points = 0
        random.seed(initial_seed)
    

        while current_num_points != sampling_points:
            gap_size = 0
            current_num_points = 0
            vector_smpl_points = np.array([])

            while gap_size < total_size:
                vector_smpl_points = np.append(vector_smpl_points, math.floor(gap_size))
                gap_size += 1
                current_num_points += 1

                gap_size += int(poisson((ld-1.0)*weight*math.sin(gap_size/(total_size+1)*math.pi)))

            if current_num_points > sampling_points:
                weight *= 1.02
       
            if current_num_points < sampling_points:
                weight /= 1.02
    
        initial_seed += 1
        count += 1
        final = np.append(final, vector_smpl_points)

    frequency_array(final)

main()

