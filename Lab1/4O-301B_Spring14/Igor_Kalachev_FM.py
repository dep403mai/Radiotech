# -*- coding: UTF-8 -*-
__author__ = 'igor kalachev 4O-301B'
# Во избежание сохранения нервной системы в дальнейшем файл рекомендуется закрыть.

import pylab
from numpy import *

t = 4.0
F = 2000.0    # несущая
A1 = 1        # исходная амплитуда
A2 = 5        # амплитуда несущей
F1 = 200.0    # first harmonic
F2 = 300.0    # second harmonic
FD = 6000.0   # дискретизация
FFTL = 8192   # Количество линий спектра
wd = 0.2      # девиация частоты

# угловые частоты
w = F * math.pi * 2
w1 = F1 * math.pi * 2
w2 = F2 * math.pi * 2

S0 = [A1 * math.sin(w1 * x) + A1 * math.sin(w2 * x) for x in arange(0, t, (1.0/FD))]

SM = [A2 * math.sin(w1 * x) * math.sin(w * x) + A2 * math.sin(w2 * x) * math.sin(w * x) for x in arange(0, t, (1.0/FD))]

FM = [A1 * sin(w * t + wd * (wd * A1 * math.cos(w1 * x) + wd * A1 * math.cos(w2 * x))) for x in arange(0, t, (1.0/FD))]

# бепефе
FFT_FM = fft.rfft(FM, FFTL)
FFT_S = fft.rfft(S0, FFTL)
FFT_M = fft.rfft(SM, FFTL)

def plot_signal(x, y, title, labelx, labley, position):
    print len(x)  # Для проверки
    print len(y)  # Для проверки
    pylab.subplot(9, 1, position)
    pylab.plot(x, y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)

plot_signal(arange(0, (3.0 / 200.0), (1.0 / FD)), S0[0:(int(3 * FD / F1))], 'Source signal', 'Time (s)', 'Amplitude', 1)
plot_signal(arange(0, ((FD / 2) + (FD / FFTL)), (FD / FFTL)), abs(FFT_S) / len(arange(0, t / 3, (1.0 / FD))),
            'Spectrum of source signal', 'Frequency (Hz)', 'Amplitude', 3)
plot_signal(arange(0, (10 / F1), (1.0 / FD)), FM[0:(int(10 * FD / F1))], 'Frequence modulation', 'Time (s)',
            'Amplitude', 5)
plot_signal(arange(0, ((FD / 2) + (FD / FFTL)), (FD / FFTL)), abs(FFT_M) / len(arange(0, t / 3, (1.0 / FD))),
            'Spectrum of carrier signal', 'Frequency (Hz)', 'Amplitude', 7)
plot_signal(arange(0, ((FD / 2) + (FD / FFTL)), (FD / FFTL)), abs(FFT_FM) / len(arange(0, t / 3, (1.0 / FD))),
            'Spectrum of FM signal', 'Frequency (Hz)', 'Amplitude', 9)

pylab.show()
