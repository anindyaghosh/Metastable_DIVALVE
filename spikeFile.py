import numpy as np
import os

currDir = os.path.dirname(os.path.abspath(__file__))

foldername = 'Cori_2016-12-14'
filename = 'clusters.templateWaveforms.npy'

file = os.path.join(currDir, 'spikeAndBehavioralData\\allData', foldername, filename)

data = np.load(file)