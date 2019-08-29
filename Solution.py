import os
import sys
import math
from random import randint

input_file=sys.argv[1]
output_file=sys.argv[2]


f = open(input_file)

program_time = float(f.readline())

size_v = int(f.readline())
v = f.readline().strip().split(', ')

a_index = v.index('A')
c_index = v.index('C')
g_index = v.index('G')
t_index = v.index('T')

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


cc_arr = 0 #total cost of extending all strings and making length equal

#takes in the array of original strings and makes their length equal by inserting hyphens in the end(except for the biggest strings)
def make_strings_equal(arr,k,max_length):
    for i in range(k):
        original_len = len(arr[i])
        to_be_added = max_length - original_len
        for j in range(to_be_added):
            arr[i] = arr[i] + ['-']
            cc_arr+=1


# make_strings_equal(strings, k , max_length)
# print(strings)

# maintains original order of characters and changes the position of the first hyphen randomly, keeping the total length same
def swappy(string):
    #pos is the position at which the hyphen is to be inserted
    pos = randint(0,max_length-1)
    #if string has no hyphens, then just return the same string
    if (len(string) == max_length):
        return string
    #exch is the occurenc of the first hyphen in the string    
    exch = string.index('-')
    if (pos<= exch):
        #if the position where the hyphen is to be inserted is less than(or equal to) the index of first hyphen, do this
        string_new = string[:pos] + ['-'] + string[pos:exch] + string[exch+1:]
    else:
        #if index of the first hyphen is less than the position where the hyphen is to be inserted, do this
        string_new = string[:exch] + string[exch+1:pos] + ['-'] + string[pos:]
    return string_new




#matching cost between 2 any characterz a1 and a2
def matching_cost(a1, a2):
    if (a1 == a2): #diagonals are 0
        return 0
    # if either a1 or a2 are 0, check 5th column or row, because '-' is not there in v    
    elif (a1 == '-'): 
        return mc[4][v.index(a2)]
    elif (a2 == '-'):
        return mc[v.index(a1)][4]

    # else return the value at the appropriate index from given matrix mc
    return mc[v.index(a1)][v.index(a2)]


def cost(string_arr, mc):
    # string arr is a 2d array of dimensions:- k*max_length
    # mc is 2d matrix of dim 5*5. (ACTG*ACTG)
    cost1 = 0
    for i in range(k):
        for j in range(k):
            if (i!=j):
                for m in range(max_length):
                    cost1 += matching_cost(string_arr[i][m], string_arr[j][m])

    # adding the                
    total_cost = cost1 + cc_arr
    return total_costs

# matching cost of one string against the entire array of strings which will be subtracted if the string
def cost_against_one(string, string_arr):
    cost = 0
    for i in range(k):
        if(string != string_arr[i]):
            for j in range(max_length):
                cost += matching_cost(string_arr[i][j], string_arr[j][j])

    return cost



def local_search():
    eval = 100000
    value = cost

    #evaluate cost of a random string
    #change a string
    #evaluate 






