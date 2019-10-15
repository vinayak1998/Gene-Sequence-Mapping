import os
import sys
import math
import random
from random import randint
import time
import copy

start_time=time.time()
input_file=sys.argv[1]
output_file=sys.argv[2]

f = open(input_file)

program_time = float(f.readline())
seconds = 60*program_time
seconds *= 0.6

size_v = int(f.readline())
v = f.readline().strip().split(', ')

# a_index = v.index('A')
# c_index = v.index('C')
# g_index = v.index('G')
# t_index = v.index('T')

k = int(f.readline())

strings = []
input_strings = []
max_length = 0

for i in range(k):
    l=list(f.readline())
    l = l[:-1]
    strings += [l]
    input_strings += [l]
    length = len(l)
    if (length >= max_length):
        max_length = length


cc = int(f.readline())

mc = []

for i in range(size_v+1):
    l=list(f.readline().strip().split(' '))
    mc += [l]

# print(mc)

mc = [[int(n )for n in row]for row in mc]

# print(mc)

# for i in range(size_v+1):
#     for j in range(size_v+1):
#         print(mc[i][j])


cc_arr = 0 #total cost of extending all strings and making length equal
l = [0]*k
#takes in the array of original strings and makes their length equal by inserting hyphens in the end(except for the biggest strings)
def make_strings_equal(arr,k,max_length):
    for i in range(k):
        original_len = len(input_strings[i])
        to_be_added = max_length - original_len
        global l
        l[i]=to_be_added
        for j in range(to_be_added):
            arr[i] = arr[i] + ['-']
            global cc_arr
            cc_arr += 1 #incrementing the extending cost by one, every time a hyphen is introduced


make_strings_equal(strings, k , max_length)
# print(strings)

def extend(arr, num):
    new_arr = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(num):
            new_arr[i] += ['-'] 

    return new_arr


# maintains original order of characters and changes the position of the first hyphen randomly, keeping the total length same
def swappy(string,ind):
    #pos is the position at which the hyphen is to be inserted
    # pos = randint(0,max_length)
    #if string has no hyphens, then just return the same string
    if ('-' not in string):
        return string
    #exch is the occurenc of the first hyphen in the string    
    global l
    no_dash = 0
    for i in string:
        if i=='-':
            no_dash+=1
    # no_dash += num
    orig_sting = input_strings[ind]
    indices = [i for i in range(len(string))]
    ind_dash = random.sample(indices,no_dash)
    new_string = ['a']*(len(string))

    for i in ind_dash:
        new_string[i] = '-'

    count = 0
    for i in range(len(string)):
        if new_string[i]!='-':
            new_string[i] = orig_sting[count]
            count+=1
    # exch = string.index('-')
    # if (pos<= exch):
    #     #if the position where the hyphen is to be inserted is less than(or equal to) the index of first hyphen, do this
    #     string_new = string[:pos] + ['-'] + string[pos:exch] + string[exch+1:]
    # else:
    #     #if index of the first hyphen is less than the position where the hyphen is to be inserted, do this
    #     string_new = string[:exch] + string[exch+1:pos] + ['-'] + string[pos:]
    return new_string
def neighbor(strings):
    for i in range(len(strings)):
      strings[i] = swappy(strings[i],i)


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
    for i in range(len(string_arr)):
        for j in range(i+1,len(string_arr)):
            for m in range(len(string_arr[0])):
                cost1 += matching_cost(string_arr[i][m], string_arr[j][m])

    # adding the         
    total_cost = cost1 + cc_arr*cc
    return total_cost
# print cost(,mc,cc_arr)
# print(cc_arr)

# matching cost of one string against the entire array of strings
def cost_against_one(string, string_arr):
    cost = 0
    for i in range(k):
        if(string != string_arr[i]):
            for j in range(len(string_arr[0])):
                cost += matching_cost(string[j], string_arr[i][j])

    return cost


# print (cost_against_one(strings[1],strings))
num = 0
local_arr = extend(strings,num)
cc_arr_final = cc_arr
cc_arr_opt = cc_arr
evalu_cost = 100000
final_string = copy.deepcopy(local_arr)
def local_search():
    # value = cost(strings, mc, cc_arr)
    global count
    count = 0 
    
    while(time.time()-start_time < seconds):
        count +=1
        # maint_arr = [0]*100
        pointer_old = []
        pointer_new = []
        evalu = 100000
        
        ind = 0
        ind_final = 0
        global num
        global strings
        global k
        global max_length
        global local_arr
        global final_string
        global cc_arr_final
        global cc_arr_opt
        global evalu_cost
        
        global local_arr
        if (evalu_cost>cost(local_arr,mc,cc_arr_final)):
            final_string = copy.deepcopy(local_arr)
            evalu_cost = cost(local_arr,mc,cc_arr_final)
            cc_arr_opt = cc_arr_final

        num = randint(0,max_length)
        neighbor(strings)
        local_arr = extend(strings,num)
        cc_arr_final = cc_arr + (num)*k
        # print (local_arr)
        # while((time.time()-start_time)<(num+1)*(seconds/(max_length+1))):
        for j in range(1000):
            if (time.time()-start_time < seconds):
                break
            for i in range(10):
                if (time.time()-start_time < seconds):
                    break
                #choose a random string
                ind = randint(0,k-1)
                chosen= local_arr[ind]

                #create new string by changing(swappy) the chosen string
                new_string = swappy(chosen,ind)
                # print(new_string)
                print
                # print('---')
                # print(new_string)
                # print('---')

                #evaluate the cost of it with the rest, after changing
                new_cost = cost_against_one(new_string, local_arr) - cost_against_one(chosen,local_arr)

                # print(new_cost)

                # maint_arr[i] = new_cost
                if (new_cost < evalu):
                    evalu = new_cost
                    pointer_old = chosen
                    pointer_new = new_string
                    ind_final = ind



            local_arr[ind_final] = pointer_new

        if (time.time()-start_time > seconds):
            file=open(output_file,'w')
            n = len(final_string[0])
            for i in range(k):
                for j in range(n):
                    file.write(final_string[i][j])
                file.write("\n")
            break

        # num += 1



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


# print_result('strings')
# print_result(final_string)
# print_result(input_strings)

file=open(output_file,'w')
n = len(final_string[0])
for i in range(k):
    for j in range(n):
        file.write(final_string[i][j])
    file.write("\n")
