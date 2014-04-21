# -*- coding: UTF-8 -*-
import pylab #Для графиков
import math  #Для sin(), cos()
import random
from numpy import * #Для функции arange(), функция поддерживает тип float для аргументов

########## Входные данные ##############

Fd=60000.0 #Частота дискретизации аналогового несущего сигнала
Fdd=500.0 #Частота дискретизации цифрового исходного сигнала
Fc=18.0 #Частота несущейдающихся символов
FFTL=8192 #Количество линий спектрая скорость (частота символов)ность импульса
N=30 #Количество передающихся символов
speed=10.0 #Символьная скорость (частота символов)
duration=1/speed #Длительность импульса
time_signal=N*duration #Длительность исходного сигнала из N импульсов
M=3 #Количество уровней модуляции
# Формируем исходную последовательность символов
sequence=[random.choice([-1,1]) for x in range(0,N)]
 
Wc=2*math.pi*Fc #Угловая частота несущей
T=1/Fc
# Формируем список значений исходного сигнала
signal=[]
for x in range(0,N):
    signal+=[sequence[x] for y in arange(0,duration,(1.0/Fdd))]

# Формируем список значений модулированного сигнала
ASK=[]
for x in xrange(0,N):
    ASK+=[math.cos(Wc*t+sequence[x]*math.pi*t*Fc) for t in arange(0,duration,(1.0/Fd))]
FM2=[]
for x in xrange(0,N):
    FM2+=[math.cos(Wc*t+(sequence[x]*math.pi)/2)for t in arange(0,duration,(1.0/Fd))]
FM4=[]
for x in xrange(0,N,2):
    if (sequence[x]==1) and (sequence[x+1]==1):
        FM4+=[sequence[x]*math.cos(Wc*t+math.pi*1/4) for t in arange(0,duration*2,(1.0/Fd))]
    elif (sequence[x]==-1) and (sequence[x+1]==1):
        FM4+=[sequence[x]*math.cos(Wc*t+math.pi*3/4) for t in arange(0,duration*2,(1.0/Fd))]
    elif (sequence[x]==-1) and (sequence[x+1]==-1):
        FM4+=[sequence[x]*math.cos(Wc*t+math.pi*5/4) for t in arange(0,duration*2,(1.0/Fd))]
    elif (sequence[x]==1) and (sequence[x+1]==-1):
        FM4+=[sequence[x]*math.cos(Wc*t+math.pi*7/4) for t in arange(0,duration*2,(1.0/Fd))]
FM8=[]
for x in xrange(0, N, 3):
    if (sequence[x] == 1) & (sequence[x + 1] == 1) & (sequence[x + 2] == 1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 15 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == 1) & (sequence[x + 1] == 1) & (sequence[x + 2] == -1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 13 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == 1) & (sequence[x + 1] == -1) & (sequence[x + 2] == 1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 11 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == 1) & (sequence[x + 1] == -1) & (sequence[x + 2] == -1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 9 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == -1) & (sequence[x + 1] == 1) & (sequence[x + 2] == 1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 7 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == -1) & (sequence[x + 1] == 1) & (sequence[x + 2] == -1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 5 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == -1) & (sequence[x + 1] == -1) & (sequence[x + 2] == 1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 3 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
    elif (sequence[x] == -1) & (sequence[x + 1] == -1) & (sequence[x + 2] == -1):
        FM8 += [sequence[x] * math.cos(Wc * t + math.pi * 1 / 8) for t in arange(0, duration * 3, (1.0 / Fd))]
        
#пределение функции построения графиков  #####################
FFT_AM=fft.rfft(ASK,FFTL)
FFT_FM2=fft.rfft(FM2,FFTL)
FFT_FM4=fft.rfft(FM4,FFTL)
FFT_FM8=fft.rfft(FM8,FFTL)
def plot_signal(x,y,title,labelx,labley,position):
    pylab.subplot(8,1, position)
    pylab.plot(x,y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)

plot_signal(arange(0,time_signal,(1.0/Fdd)),signal,'Digital sequence','time','',1)
plot_signal(arange(0,time_signal,(1.0/Fd)),ASK,'ASK','time','',2)
plot_signal(arange(0,time_signal,(1.0/Fd)),FM2,'FM2','time','',3)
plot_signal(arange(0,time_signal,(1.0/Fd)),FM4,'FM4','time','',4)
plot_signal(arange(0,time_signal,(1.0/Fd)),FM8,'FM8','time','',5)
print len(arange(0,((Fd/20)+(Fd/FFTL)),(Fd/FFTL)))
plot_signal(arange(0,((Fd/20)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_FM2[:411])/len(arange(0,time_signal/3,(1.0/Fd))),
'Spectrum of FM2','Frequency (Hz)','Amplitude', 6)
plot_signal(arange(0,((Fd/20)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_FM4[:411])/len(arange(0,time_signal/3,(1.0/Fd))),
            'Spectrum of FM4','Frequency (Hz)','Amplitude',7)
plot_signal(arange(0,((Fd/20)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_FM8[:411])/len(arange(0,time_signal/3,(1.0/Fd))),
            'Spectrum of FM8','Frequency (Hz)','Amplitude',8)
#Отображение графиков
pylab.show()

