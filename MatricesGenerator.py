# Matrices Generator for a QAP problem

while(True):
    print("Insert the 'n' value (must be a positive integer):")
    n = input()
    try:
        n = int(n)
        assert(n > 0)
        break
    except (ValueError, AssertionError):
        print("Wrong input. Retry.")

while(True):
    print("Insert the 'n1' and 'n2' values (must be positive integers so that n1xn2=n):")
    n1 = input()
    n2 = input()
    try:
        n1 = int(n1)
        n2 = int(n2)
        assert(n1>0 and n2>0 and n1*n2==n)
        break
    except (ValueError, AssertionError):
        print("Wrong input. Retry.")

while(True):
    print("Insert the 'm' value (must be a positive integer so that m<=n):")
    m = input()
    try:
        m = int(m)
        assert(m>0 and m<n)
        break
    except (ValueError, AssertionError):
        print("Wrong input. Retry.")

# test print
print(n1, " ", n2, " ", n, " ", m)

A = [0]*n
for i in range(n):
    if(i < m):
        A[i] = [1]*m + [0]*(n-m)
    else:
        A[i] = [0]*n

for row in A:
    for val in row:
        print(val, end=" ")
    print()