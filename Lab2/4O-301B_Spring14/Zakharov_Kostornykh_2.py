# -*- coding: UTF-8 -*-
import pylab #Для графиков
import math  #Для sin(), cos()
import random
from numpy import * #Для функции arange(), функция поддерживает тип float для аргументов

########## Входные данные ##############

Fd=200.0 #Частота дискретизации аналогового несущего сигнала
Fdd=500.0 #Частота дискретизации цифрового исходного сигнала
Fc=13.0 #Частота несущей
N=30 #Количество передающихся символов
speed=10.0 #Символьная скорость (частота символов)
duration=1/speed #Длительность импульса
time_signal=N*duration #Длительность исходного сигнала из N импульсов
M=2 #Количество уровней модуляции
T=1/Fc #Период
f=2*math.pi/N #Дельта фи
FFTL=2**20 #Количество линий спектра

# Формируем исходную последовательность символов
source_digital_sequence=[random.choice([-1,1]) for x in range(0,N)]
Wc=2*math.pi*Fc #Угловая частота несущей

# Формируем список значений исходного сигнала
source_digital_signal=[]
for x in range(0,N):
    source_digital_signal+=[source_digital_sequence[x] for y in arange(0,duration,(1.0/Fdd))]

# Формируем список значений модулированных сигналов
MSK=[]
for x in xrange(0,N):
    MSK+=[cos(Wc*t+((source_digital_sequence[x]*math.pi*t)/(T*2))) for t in arange(0,duration,(1.0/Fd))] 
FM2=[]
for x in xrange(0,N):
   FM2+=[source_digital_sequence[x]*math.cos(Wc*t+M*math.pi/2+f) for t in arange(0,duration,(1.0/Fd))]
FM4=[]
for x in xrange(0,N,2):
    if (source_digital_sequence[x]==-1)&(source_digital_sequence[x+1]==1):
        FM4+=[source_digital_sequence[x]*math.cos(Wc*t+math.pi/4) for t in arange(0,2*duration,(1.0/Fd))]
    elif (source_digital_sequence[x]==-1)&(source_digital_sequence[x+1]==-1):
        FM4+=[source_digital_sequence[x]*math.cos(Wc*t+3*math.pi/4) for t in arange(0,2*duration,(1.0/Fd))]
    elif (source_digital_sequence[x]==1)&(source_digital_sequence[x+1]==-1):
        FM4+=[source_digital_sequence[x]*math.cos(Wc*t-3*math.pi/4) for t in arange(0,2*duration,(1.0/Fd))]
    elif (source_digital_sequence[x]==1)&(source_digital_sequence[x+1]==1):
        FM4+=[source_digital_sequence[x]*math.cos(Wc*t-math.pi/4) for t in arange(0,2*duration,(1.0/Fd))]
#FM8=[]
#for x in xrange(0,N,3):
#    if (source_digital_sequence[x]==-1)&(source_digital_sequence[x+1]==1)&(source_digital_sequence[x+2]==1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t+math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==-1)&(source_digital_sequence[x+1]==1)&(source_digital_sequence[x+2]==-1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t+3*math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==-1)&(source_digital_sequence[x+1]==-1)&(source_digital_sequence[x+2]==-1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t+5*math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==-1)&(source_digital_sequence[x+1]==-1)&(source_digital_sequence[x+2]==1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t+7*math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==1)&(source_digital_sequence[x+1]==-1)&(source_digital_sequence[x+2]==1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t-7*math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==1)&(source_digital_sequence[x+1]==-1)&(source_digital_sequence[x+2]==-1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t-5*math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==1)&(source_digital_sequence[x+1]==1)&(source_digital_sequence[x+2]==-1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t-3*math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
#    elif (source_digital_sequence[x]==1)&(source_digital_sequence[x+1]==1)&(source_digital_sequence[x+2]==1):
#        FM8+=[source_digital_sequence[x]*math.cos(Wc*t-math.pi/8) for t in arange(0,3*duration,(1.0/Fd))]
  
#Преобразование Фурье
FFT_MSK=fft.rfft(MSK,FFTL)
FFT_FM2=fft.rfft(FM2,FFTL)
FFT_FM4=fft.rfft(FM4,FFTL)
#FFT_FM8=fft.rfft(FM8,FFTL)
                           

#################  Определение функции построения графиков  #####################

def plot_signal(x,y,title,labelx,labley,position):
    pylab.subplot (9, 1, position)
    pylab.plot(x,y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)
plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_MSK)/len(arange(0,time_signal/3,(1.0/Fd))),'Spectrum of MSK','Frequency (Hz)','Amplitude',6)
plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_FM2)/len(arange(0,time_signal/3,(1.0/Fd))),'Spectrum of FM2','Frequency (Hz)','Amplitude',7)
plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_FM4)/len(arange(0,time_signal/3,(1.0/Fd))),'Spectrum of FM4','Frequency (Hz)','Amplitude',8)
#plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_FM8)/len(arange(0,time_signal/3,(1.0/Fd))),'Spectrum of FM8','Frequency (Hz)','Amplitude',9)
plot_signal(arange(0,time_signal,(1.0/Fdd)),source_digital_signal,'Digital sequence','time','',1)
plot_signal(arange(0,time_signal,(1.0/Fd)),MSK,'MSK','time','',2)
plot_signal(arange(0,time_signal,(1.0/Fd)),FM2,'FM2','time','',3)
plot_signal(arange(0,time_signal,(1.0/Fd)),FM4,'FM4','time','',4)
#plot_signal(arange(0,time_signal,(1.0/Fd)),FM8,'FM8','time','',5)
#Отображение графиков
pylab.show()
