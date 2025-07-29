import numpy as np
import pytest
from adcutils.frequency import get_freq, _get_freq_fft, _get_freq_zero_crossings

def test_get_freq_fft():
    # Test FFT-based frequency estimation on a clean sine wave
    fs = 1000  # sample rate in Hz
    f = 50     # signal frequency in Hz
    t = np.linspace(0, 1, fs, endpoint=False)
    signal = np.sin(2 * np.pi * f * t)

    freq_est = _get_freq_fft(signal, fs)
    # Assert the estimated frequency is within 1 Hz of the true frequency
    assert abs(freq_est - f) < 1, f"FFT freq estimate {freq_est} differs from {f}"

def test_get_freq_zero_crossings():
    # Test zero-crossings frequency estimation on a clean sine wave
    fs = 1000
    f = 50
    t = np.linspace(0, 1, fs, endpoint=False)
    signal = np.sin(2 * np.pi * f * t)

    freq_est = _get_freq_zero_crossings(signal, fs)
    # Assert the estimated frequency is within 1 Hz of the true frequency
    assert abs(freq_est - f) < 1, f"Zero crossings freq estimate {freq_est} differs from {f}"

def test_get_freq_dispatch_fft_and_zero_crossings():
    # Test the dispatcher function for both FFT and zero-crossings modes
    fs = 1000
    f = 60
    t = np.linspace(0, 1, fs, endpoint=False)
    signal = np.sin(2 * np.pi * f * t)

    freq_fft = get_freq(signal, fs, mode="fft")
    freq_zc = get_freq(signal, fs, mode="zero-crossings")

    # Assert both methods give results within 1 Hz of the true frequency
    assert abs(freq_fft - f) < 1
    assert abs(freq_zc - f) < 1

def test_get_freq_accepts_list_input():
    # Test that get_freq can accept a Python list instead of np.ndarray
    fs = 1000
    f = 30
    t = np.linspace(0, 1, fs, endpoint=False)
    signal = np.sin(2 * np.pi * f * t)
    signal_list = signal.tolist()  # convert to Python list

    freq_fft = get_freq(signal_list, fs, mode="fft")
    freq_zc = get_freq(signal_list, fs, mode="zero-crossings")

    # Assert frequency estimates remain accurate with list input
    assert abs(freq_fft - f) < 1
    assert abs(freq_zc - f) < 1

def test_get_freq_invalid_mode():
    # Test that an invalid mode raises a ValueError
    fs = 1000
    f = 10
    t = np.linspace(0, 1, fs, endpoint=False)
    signal = np.sin(2 * np.pi * f * t)

    with pytest.raises(ValueError):
        get_freq(signal, fs, mode="invalid_mode")
