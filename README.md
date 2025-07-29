# adcutils

**adcutils** is a Python utility library for working with ADC (Analog-to-Digital Converter) sample arrays and lists. It provides tools for calculating signal characteristics such as frequency from sampled data, helping you analyze and process raw ADC output more effectively.

> ⚠️ **Disclaimer**: The methods and calculations provided by `adcutils` are intended for exploratory or educational use. While care has been taken to ensure reasonable functionality, results may not be suitable for critical applications. Use with discretion and validate independently for your specific use case.


## Installation

Install the latest release from [pypi](https://pypi.org/project/adcutils/):

```bash
pip install adcutils
```

## Quickstart
Check out the [examples here](https://github.com/Jamackey/adcutils/tree/main/examples) or try the following python code in a main.py:

```python
import numpy as np
from adcutils import frequency

# Create a 5 Hz sine wave sampled at 500 Hz
sample_rate = 500
t = np.linspace(0, 1, sample_rate, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)

# Estimate frequency using FFT
freq_est = frequency.get_freq(signal, sample_rate, mode="zero-crossings")
print(f"Estimated frequency: {freq_est:.2f} Hz")
```

