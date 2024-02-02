
import sys

with open(r"C:\Users\Cihan\Downloads\input.txt", 'r') as file:
   lines = file.readlines()
   split_result = lines[0].split('=')  # Assuming G1 is in the first line
   G1 = split_result[1].strip().split(',')
   G1 = [int(elem) for elem in G1]

   split_result = lines[1].split('=')  # Assuming G2 is in the second line
   G2 = split_result[1].strip().split(',')
   G2 = [int(elem) for elem in G2]
#%%

x1_peak = -G1[1]/(2*G1[0])

def pol1(x):

    return G1[0]*x**2 + G1[1]*x + G1[2]

def R1find_interval():
    interval_start = x1_peak
    interval_end = x1_peak + 0.7

    while pol1(interval_start) * pol1(interval_end) > 0:
        interval_start += 0.7
        interval_end += 0.7

    return interval_start, interval_end

def L1find_interval():
    interval_start = x1_peak
    interval_end = x1_peak - 0.7

    while pol1(interval_start) * pol1(interval_end) > 0:
        interval_start += -0.7
        interval_end += -0.7

    return interval_start, interval_end
#%%
[a,b] = L1find_interval()
[c,d] = R1find_interval()

print(f"{a:.3f} T {b:.3f}")
# Method: Bisection
 # interval
iteration=100
tolerance = 1e-6
def bisection1(z, y):

    if pol1(z) * pol1(y) > 0:
        print('No root exists within the given interval')
        sys.exit()

    for i1 in range(0, iteration+1):
        xh1 = (z + y) / 2
        if abs(pol1(xh1)) < tolerance:
            break
        elif pol1(z) * pol1(xh1) < 0:
            y = xh1
        else:
            z = xh1

    return xh1, i1
#%%

[xh1,i1] = bisection1(a,b)


print('The root: %.3f' % xh1)
print('Number of bisections: %d' % i1)

print(f"{c:.3f} T {d:.3f}")
[xh2,i2] = bisection1(c,d)

print('The root: %.3f' % xh2)
print('Number of bisections: %d' % i2)
#%%
x2_peak = -G2[1]/(2*G2[0])

def pol2(x):

    return G2[0]*x**2 + G2[1]*x + G2[2]

def R2find_interval():
    interval_start = x2_peak
    interval_end = x2_peak + 0.7

    while pol2(interval_start) * pol2(interval_end) > 0:
        interval_start += 0.7
        interval_end += 0.7

    return interval_start, interval_end

def L2find_interval():
    interval_start = x2_peak
    interval_end = x2_peak - 0.7

    while pol2(interval_start) * pol2(interval_end) > 0:
        interval_start += -0.7
        interval_end += -0.7

    return interval_start, interval_end
#%%
[e,f] = L2find_interval()
[g,h] = R2find_interval()

print(f"{e:.3f} T {f:.3f}")
# Method: Bisection
 # interval
iteration=100
tolerance = 1e-6
def bisection2(z, y):

    if pol2(z) * pol2(y) > 0:
        print('No root exists within the given interval')
        sys.exit()

    for i3 in range(0, iteration+1):
        xh3 = (z + y) / 2
        if abs(pol2(xh3)) < tolerance:
            break
        elif pol2(z) * pol2(xh3) < 0:
            y = xh3
        else:
            z = xh3

    return xh3, i3
#%%

[xh3,i3] = bisection2(e,f)


print('The root: %.3f' % xh3)
print('Number of bisections: %d' % i3)

print(f"{g:.3f} T {h:.3f}")
[xh4,i4] = bisection2(g,h)

print('The root: %.3f' % xh4)
print('Number of bisections: %d' % i4)


#%%
ff = open(r"C:\Users\Cihan\Downloads\output.txt", 'w')
ff.write(f'''Given equations:
y1= {G1[0]}x**2+{G1[1]}x+ {G1[2]}
y2= {G2[0]}x**2+{G2[1]}x+ {G2[2]}
The roots of y1:
Interval: {a:.2f}-{b:.2f}
Iteration={i1}
x1={xh1:.2f}
Interval: {d:.2f}-{c:.2f}
Iteration={i2}
x2={xh2:.2f}
The roots of y2:
Interval: {f:.2f}-{e:.2f}
Iteration={i3}
x1={xh3:.2f}
Interval: {g:.2f}-{h:.2f}
Iteration={i4}
x2={xh4:.2f}''')


ff.close()  # Don't forget to close the file after writing
f = open(r"C:\Users\Cihan\Downloads\output.txt", "r")
print(f.read())


    
