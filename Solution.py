import os
import sys
import math
from random import randint

input_file=sys.argv[1]
output_file=sys.argv[2]


f = open(input_file)

program_time = float(f.readline())

size_v = int(f.readline())
v = f.readline()

k = int(f.readline())

strings = []
max_length = 0

for i in range(k):
    l=list(f.readline())
    l = l[:-1]
    strings += [l]
    length = len(l)
    if (length >= max_length):
        max_length = length

cc = int(f.readline())

mc = [[0]*5]*5
for i in range(5):
    l=f.readline().strip().split(' ')
    for j in range(5):
        mc[i][j] = int(l[j])



def make_strings_equal(arr,k,max_length):
    for i in range(k):
        original_len = len(arr[i])
        to_be_added = max_length - original_len
        for j in range(to_be_added):
            arr[i] = arr[i] + ['-']

make_strings_equal(strings, k , max_length)

print(strings)



# def cost(string_arr, mc):
#     # string arr is a 2d array of dimensions:- k*max_length
#     # mc is 2d matrix of dim 5*5. (ACTG*ACTG)
