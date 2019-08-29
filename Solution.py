import os
import sys
import math
from random import randint
import time

start_time=time.time()
input_file=sys.argv[1]
output_file=sys.argv[2]

f = open(input_file)

program_time = float(f.readline())
seconds = 60*program_time
seconds *= 0.97

size_v = int(f.readline())
v = f.readline().strip().split(', ')

# a_index = v.index('A')
# c_index = v.index('C')
# g_index = v.index('G')
# t_index = v.index('T')

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

mc = []

for i in range(size_v+1):
    l=list(f.readline().strip().split(' '))
    mc += [l]

print(mc)

mc = [[int(n )for n in row]for row in mc]

print(mc)

# for i in range(size_v+1):
#     for j in range(size_v+1):
#         print(mc[i][j])


cc_arr = 0 #total cost of extending all strings and making length equal

#takes in the array of original strings and makes their length equal by inserting hyphens in the end(except for the biggest strings)
def make_strings_equal(arr,k,max_length, cc_arr):
    for i in range(k):
        original_len = len(arr[i])
        to_be_added = max_length - original_len + 1
        for j in range(to_be_added):
            arr[i] = arr[i] + ['-']
            cc_arr += 1 #incrementing the extending cost by one, every time a hyphen is introduced


make_strings_equal(strings, k , max_length, cc_arr)
# print(strings)

# maintains original order of characters and changes the position of the first hyphen randomly, keeping the total length same
def swappy(string):
    #pos is the position at which the hyphen is to be inserted
    pos = randint(0,max_length-1)
    #if string has no hyphens, then just return the same string
    if ('-' not in string):
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

# print(swappy(strings[3]))


#matching cost between 2 any characterz a1 and a2
def matching_cost(a1, a2):
    if (a1 == a2): #diagonals are 0
        return 0
    # if either a1 or a2 are 0, check 5th column or row, because '-' is not there in v    
    elif (a1 == '-'): 
        return mc[size_v][v.index(a2)]
    elif (a2 == '-'):
        return mc[v.index(a1)][size_v]

    # else return the value at the appropriate index from given matrix mc
    return mc[v.index(a1)][v.index(a2)]


def cost(string_arr, mc, cc_arr):
    # string arr is a 2d array of dimensions:- k*max_length
    # mc is 2d matrix of dim 5*5. (ACTG*ACTG)
    cost1 = 0
    for i in range(k):
        for j in range(i+1,k):
            for m in range(max_length):
                cost1 += matching_cost(string_arr[i][m], string_arr[j][m])

    # adding the         
    total_cost = 0     
    total_cost = cost1 + cc_arr
    return total_cost

# print cost(,mc,cc_arr)

# matching cost of one string against the entire array of strings
def cost_against_one(string, string_arr):
    cost = 0
    for i in range(k):
        if(string != string_arr[i]):
            for j in range(max_length):
                cost += matching_cost(string[j], string_arr[i][j])

    return cost


# print (cost_against_one(strings[1],strings))

def local_search():
    value = cost(strings, mc, cc_arr)

    while(time.time()-start_time < seconds):
        maint_arr = [0]*10
        pointer_old = []
        pointer_new = []
        evalu = 100000
        ind = 0
        ind_final = 0

        for i in range(10):
            #choose a random string
            ind = randint(0,k-1)
            chosen= strings[ind]

            #create new string by changing(swappy) the chosen string
            new_string = swappy(chosen)
            # print('---')
            # print(new_string)
            # print('---')

            #evaluate the cost of it with the rest, after changing
            new_cost = cost_against_one(new_string, strings)
            print(new_cost)

            maint_arr[i] = new_cost
            if (new_cost < evalu):
                evalu = new_cost
                pointer_old = chosen
                pointer_new = new_string
                ind_final = ind

        strings[ind_final] = pointer_new



def convert(s): 
    # initialization of string to "" 
    new = "" 
    # traverse in the string  
    for x in s: 
        new += x  
    # return string  
    return new


def print_result(string_arr):
    for i in string_arr:
        print(convert(i))

# print_result(strings)

local_search()

print('final cost:')
print (cost(strings,mc,cc_arr))

# print_result('strings')
print_result(strings)