import numpy as np
from adcutils import frequency as fq
from matplotlib import pyplot as plt

def main():
    # Sampling parameters
    sample_rate = 500  # samples per second (Hz)
    duration = 1.0     # seconds
    freq_true = 5      # fq of the sine wave in Hz

    # Generate time vector and sine wave signal
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * freq_true * t)

    # Estimate fq using zero-crossings method
    freq_zc = fq.get_freq(signal, sample_rate, mode="zero-crossings")
    print(f"Estimated fq (zero-crossings): {freq_zc:.2f} Hz")

    # Estimate fq using FFT method
    freq_fft = fq.get_freq(signal, sample_rate, mode="fft")
    print(f"Estimated fq (FFT): {freq_fft:.2f} Hz")

    plt.plot(signal)
    plt.show()

if __name__ == "__main__":
    main()
