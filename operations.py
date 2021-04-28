from bessel import getn 
from bessel import getlateral
import numpy as np
#FM
freq_sens= 0
freq_dev= 0
freq_rat= 0
freq_per= 0
freq_band_real= 0
freq_band_min= 0
#PM
pha_sens = 0
pha_dev= 0
pha_ind= 0
pha_per= 0
pha_band_real= 0
pha_band_min= 0
#SPECTRUM
paresF_freq=[]
paresF_phas=[]
#LATERALS
lateralF_freq=[]
lateralF_phas=[]
comp_freq=0
comp_phas=0
carrierF_freq=0
carrierF_phas=0
#POWER
carrierp=0
total_power_phas=0
total_power_freq=0
power_freq=[]
power_phas=[]

def calculationsFM(m,vm,fm,vc,RL):
    vm = float(vm)
    fm = float(fm)
    m = float(m)
    vc= float(vc)
    RL= float(RL)
    getSensitivity(1,m,vm,fm)
    getDeviation(1,vm)
    getDeviationRatio(fm)
    getPercent(1,fm)
    getBandwidthMin(1,fm)
    getBandwidthReal(1,m,fm)
    getFrequency(1,m)
    getPc(vc,RL)
    getPower(1,m,vc,RL)

def calculationsPM(m,vm,fm,vc,RL):
    vm = float(vm)
    fm = float(fm)
    m = float(m)    
    getSensitivity(2,m,vm,fm)
    getDeviation(2,vm)
    getPercent(2,fm)
    getBandwidthMin(2,fm)
    getBandwidthReal(2,m,fm)
    getFrequency(2,m)
    getPower(2,m,vc,RL)

def getFrequency(aux,m):
    global lateralF_freq, lateralF_phas,carrierF_freq, carrierF_phas,comp_freq, comp_phas
    if aux==1:
        array= getlateral(m)
        carrierF_freq=array[0]
        comp_freq = (getn(m))-1
        for i in range(len(array)-1):
            if i < len(array):
                lateralF_freq.append(array[i+1])
    elif aux==2:
        array= getlateral(m)
        carrierF_phas=array[0]
        comp_phas=(getn(m))-1
        for i in range(len(array)-1):
            if i < len(array):
                lateralF_phas.append(array[i+1])

def getPower(aux,m,vc,RL):
    m=float(m)
    vc= float(vc)
    RL=float(RL)
    global total_power_phas, total_power_freq, power_freq, power_phas
    if aux==1:
        array= getlateral(m)
        for i in range(len(array)):
            if(i==0):
                power_freq.append(float("{:.3f}".format((((array[i]*vc)**2)/(2*RL)))))
            else:
                power_freq.append(float("{:.3f}".format((2*((array[i]*vc)**2)/(2*RL)))))
            total_power_freq += power_freq[i]
        total_power_freq = (float("{:.3f}".format(total_power_freq)))
    elif aux==2:
        array= getlateral(m)
        for i in range(len(array)):
            if(i==0):
                power_phas.append(float("{:.3f}".format((((array[i]*vc)**2)/(2*RL)))))
            else:
                power_phas.append(float("{:.3f}".format((2*((array[i]*vc)**2)/(2*RL)))))
            total_power_phas =+power_phas[i]
        total_power_phas = (float("{:.3f}".format(total_power_phas)))

def getSensitivity(aux,m,Vm,fm):
    global pha_sens, freq_sens, pha_ind
    if aux==1:
        freq_sens= float("{:.3f}".format((m*Vm)/fm))
    elif aux==2:
        pha_ind = m
        pha_sens= m*Vm

def getDeviation(aux,Vm):
    global pha_dev, freq_dev, pha_sens, freq_sens
    if aux==1:
        freq_dev= freq_sens*Vm
    elif aux==2:
        pha_dev= pha_sens*Vm

def getDeviationRatio(fm):
    global freq_rat, freq_dev
    freq_rat= float("{:.3f}".format(freq_dev/fm))

def getPercent(aux,fm):
    global pha_dev, freq_dev, freq_per,pha_per
    if aux==1:
        freq_per= round(((fm/freq_dev)*100),2)
    elif aux==2:
        pha_per= round(((fm/pha_dev)*100),2)

def getBandwidthMin(aux,fm):
    global pha_band_min, freq_band_min, pha_dev, freq_dev
    if aux==1:
        freq_band_min= float("{:.3f}".format(2*(freq_dev+fm)))
    elif aux==2:
        pha_band_min= float("{:.3f}".format(2*(pha_dev+fm)))

def getBandwidthReal(aux,m,fm):
    global freq_band_real, pha_band_real
    if aux==1:
        n=(getn(m))-1
        freq_band_real= float("{:.3f}".format(2*(n*fm))) 
    elif aux==2:
        n=(getn(m))-1
        pha_band_real= float("{:.3f}".format(2*(n*fm)))

def getPc(vc, RL):
    global carrierp
    carrierp=float("{:.2f}".format((vc**2)/(2*RL)))

#Fuctions Get
def getSensitivityFM():
    return freq_sens

def getSensitivityPM():
    return pha_sens

def getDeviationFM():
    return freq_dev

def getDeviationRatioFM():
    return freq_rat

def getPercentFM():
    return freq_per

def getBandwidthRealFM():
    return freq_band_real

def getBandwidthMinFM():
    return freq_band_min

def getDeviationPM():
    return pha_dev

def getIndexPM():
    return pha_ind

def getPercentPM():
    return pha_per

def getBandwidthRealPM():
    return pha_band_real

def getBandwidthMinPM():
    return pha_band_min

def getCarrierFM():
    return carrierF_freq

def getCarrierPM():
    return carrierF_phas

def getComponentsFM():
    return comp_freq

def getComponentsPM():
    return comp_phas

def getLateralFM():
    return lateralF_freq

def getLateralPM():
    return lateralF_phas

def getCarrierPower():
    return carrierp

def getTotalPowerFM():
    return total_power_freq

def getTotalPowerPM():
    return total_power_phas
    
def getLateralPowerFM():
    return power_freq

def getLateralPowerPM():
    return power_phas

if __name__ == '__main__':
    getPower(2,3,20,12)