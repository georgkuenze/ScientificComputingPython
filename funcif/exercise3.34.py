# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 21:33:08 2015

@author: Georg
"""
# Prime number generation

N = 200
array = [[x, False] for x in range(2, N+1)]
prime_numbers = []
for i in range(len(array)):
    if array[i][1] == False:
        j = array[i][0]
        prime_numbers.append(j)
        array[i][1] = True
        for k in range(i+j, N-1, j):
            if array[k][1] == False:
                array[k][1] = True
            else:
                pass
    else:
        pass
print "Prime numbers from 2 to %d:" % (N)
for element in prime_numbers:
    print element,

# Prime number test function
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

for element in prime_numbers:
    test_list = []
    test_list.append(isprime(element))
print "\nResult of prime number test:"
if all(x == True for x in test_list) is True:
    print "All numbers picked are prime numbers."
else:
    print "Not all numbers picked are prime numbers."