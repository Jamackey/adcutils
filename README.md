# adcutils

**adcutils** is a Python utility library for working with ADC (Analog-to-Digital Converter) sample arrays and lists. It provides tools for calculating signal characteristics such as frequency from sampled data, helping you analyze and process raw ADC output more effectively.

> ⚠️ **Disclaimer**: The methods and calculations provided by `adcutils` are intended for exploratory or educational use. While care has been taken to ensure reasonable functionality, results may not be suitable for critical applications. Use with discretion and validate independently for your specific use case.


---

## 📦 Installation

Install the latest release from [pypi](https://pypi.org/project/adcutils/):

```bash
pip install adcutils
```

---

## 🚀 Quickstart

```python
import numpy as np
from adcutils import frequency as fq

# Generate a 5 Hz sine wave sampled at 500 Hz
samples = 500  # sampling frequency in Hz
sps = 10_000 # 10 MS/s 
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)

# Estimate the frequency
freq_zc = frequency.get_freq(signal, sps, mode="zero-crossings")
freq_fft = frequency.get_freq(signal, sps, mode="fft")
print(f"Estimated frequency: {freq:.2f} Hz")
```

