#!/usr/bin/env python3

# Usage ./Poisson_Gap.py seed sampling_points total_points
# Ex: ./Poisson_Gap.py 1234 64 512

import argparse
import random
import math
import numpy as np
import matplotlib.pyplot as plt


#helps create gap for poisson sampling
def poisson(lmbd):
    L = math.exp(-lmbd)
    k = 0
    p = 1

    while p >= L:
        u = random.random()
        p *= u
        k += 1

    return k-1

#creates a frequency array for clear display of how many times a number is selected
def frequency_array(np_array):
    freq=np.bincount(np_array)
    nums=np.arange(np.amax(np_array)+1)
    print(np.vstack((nums,freq[nums])).T)

#main poisson sampling function
def main():
#argument parser: needs initial seed, number of sampling points, and total points
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seed", required=True, type=int, help="initial seed")
    parser.add_argument("-sp", "--sampling_points", required=True, type=int, help="number of sampling points")
    parser.add_argument("-tp", "--total_points", required=True, type=int, help="total number of points")
    args = parser.parse_args()

#total = 3 used for testing purposes, how many times should the function iterate to get sufficient data?
    final = np.array([])
    count = 0
    total = 3
    initial_seed = args.seed

    while count != total:

#retrieves arguments from argument parser and initializes necessary variables
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
                vector_smpl_points = np.append(vector_smpl_points, math.floor(gap_size)) #stores point
                gap_size += 1 #puts pointer at next point
                current_num_points += 1 

                #creates the gap
                gap_size += int(poisson((ld-1.0)*weight*math.sin(gap_size/(total_size+1)*math.pi)))

            #adjusts weight to search for correct number of points
            if current_num_points > sampling_points:
                weight *= 1.02
       
            if current_num_points < sampling_points:
                weight /= 1.02
        
        #moves along main while loop and adds new schedule to final np
        initial_seed += 1
        count += 1
        final = np.append(final, vector_smpl_points)
 
#prints frequency array and creates histogram of data   
    frequency_array(final.astype(int))
    plt.hist(final.astype(int), bins=np.arange(total_size+1)-0.5)
    plt.xlim([0,total_size])
    plt.ylim([0,count])
    plt.title('Poisson Gap distribution for %s schedules; seed = %s, sampling points = %s, total points = %s'%(total, args.seed, sampling_points, total_size))
    plt.xlabel('Sampling Points')
    plt.ylabel('Frequency')
    plt.show()

    
    
main()


