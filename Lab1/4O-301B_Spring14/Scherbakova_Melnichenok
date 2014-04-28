import pylab 
import math  
from numpy import *
Tm=4.0 
Fd=20000.0
FFTL=8192 
F1=200.0 
F2=300.0
F3=2000.0
A=1 
A1=5 
w=2*math.pi*F1 
w1=2*math.pi*F2
w2=2*math.pi*F3
S=[A*(math.cos(w*x)+math.cos(w1*x)) for x in arange(0,Tm,(1.0/Fd))]
M=[A1*math.cos(w1*x) for x in arange(0,Tm,(1.0/Fd))]
FM=[A1*(math.cos(w2*x+math.sin(w*x)+math.sin(w1*x))) for x in arange(0,Tm,(1.0/Fd))]
FFT_AM=fft.rfft(FM,FFTL)
FFT_S=fft.rfft(S,FFTL)
FFT_M=fft.rfft(M,FFTL)
def plot_signal(x,y,title,labelx,labley,position):
    pylab.subplot (9, 1, position)
    pylab.plot(x,y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)           


plot_signal(arange(0,(3/F1),(1.0/Fd)),S[0:(int(3*Fd/F1))],'Source signal','Time (s)','Amplitude',1)

plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_S)/len(arange(0,Tm/3,(1.0/Fd))),'Spectrum of source signal','Frequency (Hz)','Amplitude',3)

plot_signal(arange(0,(10/F1),(1.0/Fd)),FM[0:(int(10*Fd/F1))],'Amplitude modulation','Time (s)','Amplitude',5)

plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_M)/len(arange(0,Tm/3,(1.0/Fd))),'Spectrum of carrier signal','Frequency (Hz)','Amplitude',7)

plot_signal(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_AM)/len(arange(0,Tm/3,(1.0/Fd))),'Spectrum of AM signal','Frequency (Hz)','Amplitude',9)


pylab.show()
