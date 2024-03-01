# 1:
from math import comb
from random import sample

# a)
countA = 0
countAB = 0

for i in range(100000):
    lst = sample(['red', 'blue', 'green'], counts=[5, 3, 2], k=3)
    if 'red' in lst:
        countA += 1
        if len(set(lst)) == 1:
            countAB += 1
            
print(countAB / countA)

# b)
PA = 1 - comb(5, 3) / comb(10, 3)
PAB = comb(5, 3) / comb(10, 3)
print(PAB / PA)


# 2:
from random import randrange
from matplotlib.pyplot import bar, hist, grid, show, legend

data = [randrange(1, 7) for x in range(500)]
bin_edges = [k+0.5 for k in range(7)]
hist(data, bin_edges, density = True, rwidth = 0.9, color = 'green', edgecolor = 'black',
    alpha = 0.5, label = 'frecvente relative')

distribution = dict([(i, 1/6) for i in range(1,7)])
bar(list(distribution.keys()), distribution.values(), width = 0.85, color = 'red', edgecolor = 'black',
    alpha= 0.6, label = 'probabilitati')

legend(loc = 'lower left')
grid()
show()


# 3:
from scipy.stats import binom
from random import randrange
from matplotlib.pyplot import bar, hist, grid, show, legend

# a)
data = binom.rvs(5, 6/10, size = 1000)
#print(data)

# b)
bin_edges = [k+0.5 for k in range(6)]
hist(data, bin_edges, density = True, rwidth = 0.9, color = 'green', edgecolor = 'black',
    alpha = 0.5, label = 'frecvente relative')

distribution = dict([(i, binom.pmf(i, 5, 6/10)) for i in range(0, 6)])
bar(list(distribution.keys()), distribution.values(), width = 0.85, color = 'red', edgecolor = 'black',
    alpha= 0.6, label = 'probabilitati')

legend(loc = 'lower left')
grid()
show()
