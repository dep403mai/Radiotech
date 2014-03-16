# -*- coding: UTF-8 -*-
import pylab
import math
from numpy import *

# Входные данные #

Tm=4.0 #Длительность сигнала
Fd=25000.0 #Частота дискретизации
FFTL=8192 #Количество линий спектра
F1=200.0 #Частота исходного сигнала
F2=2000.0 #Частота несущей
A=1 #Амплитуда исходного сигнала
A1=5 #Амплитуда несущего сигнала
g1=200.0 #Первая гармоника
g2=300.0  #Вторая гармоника

w=2*math.pi*F1 #Угловая частота исходного сигнала
w1=2*math.pi*F2 #Угловая частота 
G1=2*math.pi*g1 #Первая гармоника
G2=2*math.pi*g2 #Вторая гармоника

# Формирование списков значений сигналов #

# Формирование списков значений исходного сигнала, длительностью Tm, с шагом 1/Fd #
S=[A*math.cos((G1)*x)+A*math.cos((G2)*x) for x in arange(0,Tm,(1.0/Fd))]

# Формируем список значений несущего сигнала, длительностью Tm, с шагом 1/Fd # 
M=[A1*math.cos((w1)*x) for x in arange(0,Tm,(1.0/Fd))]

# Модулируем #
DSB=[A*math.cos((w1+G1)*x)+A*math.cos((w1-G1)*x)+A1*math.cos((w1+G2)*x)+A1*math.cos((w1-G2)*x) for x in arange(0,Tm,(1.0/Fd))]


# Выполняем FFT для списка значений исходного сигнала, несущего сигнала и амплитудо-модулировонного сигнала
FFT_DSB=fft.rfft(DSB,FFTL)
FFT_S=fft.rfft(S,FFTL)
FFT_M=fft.rfft(M,FFTL)
#  Определение функции построения графиков  #

def plot_signal(x,y,title,labelx,labley,position):
    pylab.subplot (9, 1, position)
    pylab.plot(x,y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)           

#Построение исходного сигнала
plot_signal(arange(0,(3/F1),(1.0/Fd)),S[0:(int(3*Fd/F1))],'Source signal','Time (s)','Amplitude',1)
#Построение спектра исходного сигнала
plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_S)/len(arange(0,Tm/3,(1.0/Fd))),'Spectrum of source signal','Frequency (Hz)','Amplitude',3)
#Построение DSB сигнала
plot_signal(arange(0,(10/F1),(1.0/Fd)),DSB[0:(int(10*Fd/F1))],'DSB modulation','Time (s)','Amplitude',5)
#Построение спектра несущего сигнала
plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_M)/len(arange(0,Tm/3,(1.0/Fd))),'Spectrum of carrier signal','Frequency (Hz)','Amplitude',7)
#Построение спектра АМ сигнала
plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_DSB)/len(arange(0,Tm/3,(1.0/Fd))),'Spectrum of DSB signal','Frequency (Hz)','Amplitude',9)

#Отображение графиков
pylab.show()

