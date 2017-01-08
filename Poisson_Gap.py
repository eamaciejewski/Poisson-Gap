#!/usr/bin/env python3

# Usage ./Poisson_Gap.py seed sampling_points total_points
# Ex: ./Poisson_Gap.py 1234 64 512

import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seed", required=True, type=int, help="initial seed")
    parser.add_argument("-sp", "--sampling_points", required=True, type=int, help="number of sampling points")
    parser.add_argument("-tp", "--total_points", required=True, type=int, help="total number of points")
    args = parser.parse_args()
    initial_seed = string.atof(args.seed)
    sampling_points = string.atoi(args.sampling_points)
    total_size = string.atoi(args.total_points)
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

