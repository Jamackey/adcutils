import numpy as np
from adcutils import frequency

# Create a 5 Hz sine wave sampled at 500 Hz
sample_rate = 500
t = np.linspace(0, 1, sample_rate, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)

# Estimate frequency using FFT
freq_est = frequency.get_freq(signal, sample_rate, mode="zero-crossings")
print(f"Estimated frequency: {freq_est:.2f} Hz")
