import numpy as np
import scipy.signal as signal


def hilbert_transform(signal):
    analytic_signal = signal + 1j * signal.hilbert(signal)
    return analytic_signal


def fir_windowed_sinc_filter(num_taps, cutoff, width):
    fs = 1.0  # New Nyquist frequency
    taps = signal.firwin(num_taps, cutoff, window='hamming', pass_zero=False, scale=True, fs=fs)
    return taps


def quadrature_demodulation(input_signal, num_taps, cutoff, width):
    # Design the FIR filter
    filter_taps = fir_windowed_sinc_filter(num_taps, cutoff, width)

    # Apply the filter to the input signal
    filtered_signal = np.convolve(input_signal, filter_taps,
                                  mode='valid')  # Changed from 'same' to 'valid' to avoid boundary effects

    # Perform Hilbert transform to get the imaginary part
    quadrature_signal = hilbert_transform(filtered_signal)

    return quadrature_signal


# Example usage
input_signal = np.sin(np.linspace(0, 2 * np.pi, 100))
num_taps = 6
cutoff = 0.05
width = 0.05
quadrature_signal = quadrature_demodulation(input_signal, num_taps, cutoff, width)
print(quadrature_signal)