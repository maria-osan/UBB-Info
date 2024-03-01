# 1:
from scipy.stats import norm
from numpy import mean, std, linspace
from matplotlib.pyplot import hist, grid, show, legend, xticks, plot

data = norm.rvs(loc = 165, scale = 10, size = 1000)

print(data.mean())
print(data.std())

print(((160 < data) & (data < 170)).mean())
print(norm.cdf(170, loc = 165, scale = 10) - norm.cdf(160, loc = 165, scale = 10))

hist(data, bins = 16, range = (130, 210), density = True, label = "Frecventa relativa")
xticks(range(130, 210, 5))

x = linspace(130, 210, 1000)
plot(x, norm.pdf(x, loc = 165, scale = 10), 'r-', label = "Functia de densitate")

grid()
legend()
show()


# 2:
from scipy.stats import expon, uniform
from numpy import mean, std, multiply, array

data = []

for i in range(1000):
    x = uniform.rvs()
    if x < 0.4:
        data.append(expon.rvs(loc = 0, scale = 5))
    else:
        data.append(uniform.rvs(loc = 4, scale = 2))
        
print(mean(data))
print(std(data))

print(mean(numpy.array(data) < 5))

#P(x <= 5): P(x <= 5 | I1) * P(I1) + P(x <= 5 | I2) * P(I2)
print(expon.cdf(5, loc = 0, scale = 5)* 0.4 + uniform.cdf(5, loc = 4, scale = 2) * 0.6)


# 3:
from scipy.stats import uniform
from numpy import exp, mean
from scipy.integrate import quad

data = uniform.rvs(loc = -1, scale = 4, size = 10000)
g = lambda x: exp(-x ** 2)

print(mean(g(data)) * 4)
print(quad(g, -1, 3)) #calculeaza integrala
