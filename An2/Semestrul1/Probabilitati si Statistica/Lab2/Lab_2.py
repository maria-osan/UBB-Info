# 1. Estimati prin simulari repetate probabilitatea ca într-un grup de 23 persoane cel putin doua  sa aiba  aceeasi zi de nastere
from random import randint

k = 0
for i in range(10000):
    lst = [randint(0, 366) for el in list(range(23))]
    if len(lst) > len(set(lst)) :
        k += 1
    
print(k/10000)

# Afisati probabilitatea ca într-un grup de 23 persoane cel putin doua sa  aiba aceeasi zi de nastere
prob = 1
for p in range(23):
    prob *= (365 - p) / 365
print(1 - prob)


# 2. a) Generati N ∈ {500, 1000, 2000} puncte uniform aleatoare într-un patrat. Afisati frecventa relativa a punctelor care:
# i) sunt în interiorul cercului tangent laturilor patratului:
from matplotlib.pyplot import axis, plot, show
from math import dist
from random import random

axis('square')
axis((0, 1, 0, 1))

k = 0
for i in range(500):
    x = random()
    y = random()
    if dist([0.5, 0.5], [x, y]) < 0.5:
        plot(x, y, '*g')
        k += 1

print(k / 500 * 4)


# ii) sunt mai apropiate de centrul patratului decât de vârfurile patratulu:
from matplotlib.pyplot import axis, plot, show
from math import dist
from random import random

axis('square')
axis((0, 1, 0, 1))

k = 0
for i in range(500):
    x = random()
    y = random()
    if dist([0, 0], [x, y]) > dist([0.5, 0.5], [x, y]) and dist([0, 1], [x, y]) > dist([0.5, 0.5], [x, y]) and dist([1, 0], [x, y]) > dist([0.5, 0.5], [x, y]) and dist([1, 1], [x, y]) > dist([0.5, 0.5], [x, y]):
        plot(x, y, '*g')
        k += 1
        
print(k / 500)
