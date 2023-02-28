import numpy as np

# Generate random EEG data
eeg_data = np.random.rand(100, 2)

# Save EEG data to a file
np.save('eeg_data.npy', eeg_data)
