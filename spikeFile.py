import matplotlib.pyplot as plt
import numpy as np
import os

currDir = os.path.dirname(os.path.abspath(__file__))

foldername = 'Cori_2016-12-14'
filename = ['spikes.times.npy', 'spikes.clusters.npy']

data = np.zeros((10017476, 2))

for i in np.arange(len(filename)):
    file = os.path.join(currDir, 'spikeAndBehavioralData\\allData', foldername, filename[i])
    data[:,i] = np.load(file).flatten()

# [times, spikes]

plt.scatter(data[:100, 0], data[:100, 1])