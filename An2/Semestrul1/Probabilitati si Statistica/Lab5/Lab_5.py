# 1:
from scipy.stats import uniform
from random import randrange
from matplotlib.pyplot import bar, hist, grid, show, legend, xticks

nr = ['0', 'A', 'B', 'AB']
pb = [0.46, 0.4, 0.1, 0.04]

lst = []
for i in range(100):
    u = uniform.rvs()
    s = 0
    for index, p in enumerate(pb):
        s += p
        if u < s:
            lst.append(nr[index])
            break
            
#print(lst)
    
bin_edges = [k+0.5 for k in range(-1, 4)]
hist(lst, bin_edges, density = True, rwidth = 0.9, color = 'green', edgecolor = 'black',
    alpha = 0.5, label = 'frecvente relative')
xticks(range(4))

legend(loc = 'lower left')
grid()
show()


# 2:
from scipy.stats import uniform
from matplotlib.pyplot import bar, hist, grid, show, legend, xticks, plot
from math import log
from scipy.stats import expon

alpha = 1/12

def f_invers(x):
    return (-1) / alpha * log(1 - x)

lst = []
for i in range(1000):
    u = uniform.rvs()
    lst.append(f_invers(u))
            
#print(lst)
    
hist(lst, bins=12, density = True, range=(0, 60))

x = range(60)
plot(x,expon.pdf(x, loc=0, scale=1/alpha),'r-')

xticks(range(0, 60, 5))
grid()
show()

p = 1 - expon.cdf(5, loc=0, scale=1/alpha)
print(p)
