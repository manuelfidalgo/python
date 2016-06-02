import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

lista=[]
f = open('tiempos', 'r')
for line in f:
    lista.append(float(line))
    
print lista


# example data
mu = 100  # mean
sigma = 15  # stdd


num_bins = 10
# the histogram of the data
n, bins, patches = plt.hist(lista, num_bins)
# add a 'best fit' line
plt.xlabel('Time')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()


