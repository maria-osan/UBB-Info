# 1. a)
from scipy.stats import bernoulli

lst = bernoulli.rvs(0.5, size=10)

poz = 0
steps = []

for i in lst:
    if i == 0:
        poz -= 1
        steps.append(poz)
    else:
        poz += 1
        steps.append(poz)
        
print(steps)


# 1. b)
from scipy.stats import binom, bernoulli
from random import randrange
from matplotlib.pyplot import bar, hist, grid, show, legend, xticks

data = []
for i in range(1000):
    lst = bernoulli.rvs(0.5, size=10)
    poz = 0
    for el in lst:
        if el == 0:
            poz -= 1
        else:
            poz += 1
    data.append(poz)

bin_edges = [k+0.5 for k in range(-10, 11)]
hist(data, bin_edges, density = True, rwidth = 0.9, color = 'green', edgecolor = 'black',
    alpha = 0.5, label = 'frecvente relative')
xticks(range(-10, 11))

legend(loc = 'lower left')
grid()
show()


# 1. c)
from scipy.stats import binom, bernoulli
from random import randrange
from matplotlib.pyplot import bar, hist, grid, show, legend, xticks

data = []
for i in range(1000):
    lst = bernoulli.rvs(0.5, size=10)
    poz = 0
    for el in lst:
        if el == 0:
            poz -= 1
        else:
            poz += 1
        if poz == 11:
            poz = 0
        if poz == -1:
            poz = 10
    data.append(poz)

bin_edges = [k+0.5 for k in range(11)]
hist(data, bin_edges, density = True, rwidth = 0.9, color = 'green', edgecolor = 'black',
    alpha = 0.5, label = 'frecvente relative')
xticks(range(11))

legend(loc = 'lower left')
grid()
show()


# 2. i)
from scipy.stats import hypergeom

print(1 - hypergeom.cdf(2, 49, 6, 6))


# 2. ii)
from scipy.stats import geom, hypergeom

p = 1 - hypergeom.cdf(2, 49, 6, 6)
print(1 - geom.cdf(9, p))
