# (UniPd 2008818) Mattia Toffolon
# Matrices Generator for a QAP problem

# Function that returns the force value (used later as a distance) between two given unit locations
def force(n1, n2, r, s, t, u):
    m = 0
    for v in {-1, 0, 1}:
        for w in {-1, 0, 1}:
            try:
                m = max(m, 1/((r-t+n1*v)**2 + (s-u+n2*w)**2))
            except ZeroDivisionError:
                return 0
    return m

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

# Parameters insertion
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
    print("Insert the 'n1' and 'n2' values (must be positive integers so that n1*n2==n):")
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

# Matrix A generation and Matrix B initialization
A = [0]*n
B = [0]*n
for i in range(n):
    B[i] = [0]*n
    if(i < m):
        A[i] = [1]*m + [0]*(n-m)
    else:
        A[i] = [0]*n

# Matrix B generation
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

# Matrices printing
for row in A:
    for val in row:
        print(val, end=" ")
    print()
for row in B:
    for val in row:
        print(val, end=" ")
    print()

# Matrices validity check
check(n, A, B)