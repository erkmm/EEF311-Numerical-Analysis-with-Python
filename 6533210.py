import numpy as np
from numpy.linalg import matrix_rank
from numpy import array, shape, empty, full, copy, newaxis, concatenate

# # Open the file
with open(r"C:\Users\Cihan\Downloads\input.txt", 'r') as file:
    # Read the first line to get the size
    size = int(file.readline().split('=')[-1])
    
    # Read the remaining lines and process each line
    data = [list(map(int, line.split())) for line in file.readlines()]

# Display the read data
print(f"Size: {size}")
for row in data:
    print(row)
    
# Coefficients of the linear equations
coeff= np.array(data[:2])
const = np.array([data[2]])
const = const.reshape(-1)

# Solve the system of linear equations
solution = np.linalg.solve(coeff, const)

# Display the solution
print(f"Solution: x0 = {solution[0]}, x1 = {solution[1]}")
ff = open(r"C:\Users\Cihan\Downloads\output.txt", 'w')
ff.write(f"{coeff[0,0]}xo + {coeff[1,0]}x1 = {const[0]}\n{coeff[0,1]}xo + {coeff[1,1]}x1 = {const[1]}")
ff.close()  # Don't forget to close the file after writing
f = open(r"C:\Users\Cihan\Downloads\output.txt", "r")
print(f.read())
const = const[:,newaxis] #vector to matrix conversion, new dimension added
A_y = concatenate((coeff, const), axis = 1)
print(f"Rank of matrix:{matrix_rank(coeff)}, augmented matrix:{matrix_rank(A_y)}")


n = shape(const)[0]
x = full(n, -1.0, float)  #initial guess of "x" is important
g = np.zeros(n, float) #solution array for the unknown values
xnew = empty(n, float)
iterlimit = 100; tolerance = 1.0e-6

#%% Jacobian Method
xnew = empty(n, float)
iterlimit = 100; tolerance = 1.0e-6

for iteration in range(iterlimit):
     for i in range(n): # for all the rows of matrix, xnew is calc.
         s = 0
         for j in range(n): 
             if j != i:
                 s += coeff[i, j]*x[j] #matrix multiplication for each row
         xnew[i] = (const[i]-s) / coeff[i,i]
     
     if (abs(xnew - x) < tolerance).all(): break
     else: x = copy(xnew)
     

#%% Gauss elimination
n = len(const) #number of unknown parameters
y = np.zeros(n, float) #solution array for the unknown values
for k in range(n-1): #except last column
    for p in range(k+1, n): #for each row
        fctr = coeff[k, k] / coeff[i, k]
        # k value also indicates diagonal element's row
        # current row is substracted from the diagonal element's row
        const[i] = fctr*const[i] - const[k]
        for j in range(k, n):
            coeff[i, j] = fctr*coeff[i, j] - coeff[k, j]
            
g[n-1] = const[n-1] / coeff[n-1, n-1] # from the bottom row unknown x[n-1] value is cal.

for i in range(n-2, -1, -1): #from (n-2)th row all x values are cal. 
    terms = 0
    for j in range(i+1, n):
        terms += coeff[i, j]*g[j]
    g[i] = (const[i] - terms)/coeff[i, i]
    # from bottom to top each "x" value is calculated

print('\nThe solution of the system:')
for i in range(len(x)): print("%.2f" %x[i], end=' ')            
#%%
g4 = np.round(g, 4)
x4 = np.round(x, 4)

print('\nNumber of iterations: %d '% (iteration+1))
print('The solution of the system:\n', x)

cc = open(r"C:\Users\Cihan\Downloads\output_results.txt", 'w')
cc.write(f"The solution of the system by Gauss Elimination:\nx1 = {g4[0]}\nx2 = {g4[1]}\nThe solution of the system by Jacobi Method:\nx1 = {x4[0]}\nx2 = {x4[1]}")
cc.close()
c = open(r"C:\Users\Cihan\Downloads\output_results.txt", 'r')
print(c.read())