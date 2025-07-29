import numpy as np
from typing import Union, Sequence, Literal

def _get_freq_fft(signal: np.ndarray, sample_rate: float) -> float:
    """
    Estimate frequency using FFT peak detection.

    Parameters:
        signal (np.ndarray): The sampled signal (1D array).
        sample_rate (float): Samples per second.

    Returns:
        float: Estimated frequency in Hz.
    """
    n: int = len(signal)
    spectrum: np.ndarray = np.fft.fft(signal)
    freqs: np.ndarray = np.fft.fftfreq(n, d=1 / sample_rate)
    idx: int = int(np.argmax(np.abs(spectrum[: n // 2])))
    return abs(freqs[idx])


def _get_freq_zero_crossings(signal: np.ndarray, sample_rate: float) -> float:
    """
    Estimate frequency by counting zero crossings.

    Parameters:
        signal (np.ndarray): The sampled signal (1D array).
        sample_rate (float): Samples per second.

    Returns:
        float: Estimated frequency in Hz.
    """
    zero_crossings: np.ndarray = np.where(np.diff(np.signbit(signal)))[0]
    num_cycles: float = len(zero_crossings) / 2
    duration: float = len(signal) / sample_rate
    return num_cycles / duration if duration > 0 else 0.0


def get_freq(
    signal: Union[np.ndarray, Sequence[float]],
    sample_rate: float,
    mode: Literal["fft", "zero-crossings"] = "fft",
) -> float:
    """
    Estimate the dominant frequency of an ADC signal.

    Parameters:
        signal (Union[np.ndarray, Sequence[float]]): The sampled signal (1D array or list).
        sample_rate (float): Samples per second.
        mode (Literal['fft', 'zero-crossings']): Estimation method.

    Returns:
        float: Estimated frequency in Hz.
    """
    if not isinstance(signal, np.ndarray):
        signal = np.array(signal, dtype=float)

    if mode == "fft":
        return _get_freq_fft(signal, sample_rate)
    elif mode == "zero-crossings":
        return _get_freq_zero_crossings(signal, sample_rate)
    else:
        raise ValueError(f"Unknown mode '{mode}'. Use 'fft' or 'zero-crossings'.")


__all__ = [
    "get_freq"
]
