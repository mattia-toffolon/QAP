# (UniPd 2008818) Mattia Toffolon
# Matrices Generator for a QAP problem

##!/usr/bin/env python
# encoding: utf-8

# (Density of grey)
# Function that returns the force value (used later as a distance) between two given unit locations of the matrix: n1 x n2
def force(n1, n2, r, s, t, u):
    m = 0
    for v in {-1, 0, 1}:
        for w in {-1, 0, 1}:
            try:
                m = max(m, 1/((r-t+n1*v)**2 + (s-u+n2*w)**2))
            except ZeroDivisionError:
                return 0
    assert(m >= 0)
    return m

"""
# Function that checks if the given matrices coincide with the ones saved in the relative file
def check(n, A, B):
    try:
        f = open("Tai" + str(n) + "c")
        f.readline()
        f.readline()
        for i in range(n*2):
            line = f.readline()
            j=0
            for num in line.split(' '):
                try:
                    if(i < n):
                        assert(int(num) == A[i][j])
                    else:
                        assert(int(num) == B[i-n][j])
                    j += 1
                except ValueError:
                    continue       
                except AssertionError:
                    if(i < n):
                        print("AssertionError: ", int(num), " != ", A[i][j], " at position [", i,"][", j, "] of matrix A")   
                    else:
                        print("AssertionError: ", int(num), " != ", B[i-n][j], " at position [", i-n,"][", j, "] of matrix B")                 
                    return
        f.close
        print("The generated matrices and the ones saved in the file match!")
    except FileNotFoundError as e:
        print(e)
"""

def A_generator(n, n1, n2, m):
    # Parameters check (n, n1, n2, m)
    while(True):
        try:
            n = int(n)
            assert(n > 0)
            n1 = int(n1)
            n2 = int(n2)
            assert(n1>0 and n2>0 and n1*n2==n)
            m = int(m)
            assert(m>0 and m<n)
            break
        except (ValueError, AssertionError):
            print("Wrong parameters format. Retry.")
    # Matrix A generation (A is the flows matrix)
    A = [0]*n
    for i in range(n):
        if(i < m):
            A[i] = [1]*m + [0]*(n-m)
        else:
            A[i] = [0]*n
    return A

def B_generator(n, n1, n2, m):
    # Parameters check (n, n1, n2, m)
    while(True):
        try:
            n = int(n)
            assert(n > 0)
            n1 = int(n1)
            n2 = int(n2)
            assert(n1>0 and n2>0 and n1*n2==n)
            m = int(m)
            assert(m>0 and m<n)
            break
        except (ValueError, AssertionError):
            print("Wrong parameters format. Retry.")
    # Matrix B generation (B is the distances matrix)
    B = [0]*n
    for i in range(n):
        B[i] = [0]*n
    # (note: B is always simmetric)
    scale = 100000
    for r in range(n1):
        for s in range(n2):
            for t in range(n1):
                for u in range(n2):
                    i = n2*(r-1)+s
                    j = n2*(t-1)+u
                    if(B[i][j] != 0):
                        continue
                    else:
                        B[i][j] = round(force(n1, n2, r, s, t, u)*scale)
                        B[j][i] = B[i][j]
    return B

"""
# Matrices printing
for row in A:
    for val in row:
        print(val, end=" ")
    print()
for row in B:
    for val in row:
        print(val, end=" ")
    print()

# Matrices validity check (available only for certain matrix formats)
if (n, n1, n2, m)==(64, 8, 8, 13) or (n, n1, n2, m)==(256, 16, 16, 92):
    check(n, A, B)
"""