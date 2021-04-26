from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import math

def ModulatinggraphFM(vm,fm):
    x = []
    y = []
    vm = float(vm)
    fm = float(fm)
    time = float(0)
    for i in range(2000):
        wave = float(vm * math.sin(2*math.pi*fm*time))
        x.append(time)
        y.append(wave)
        time += 0.001
    print(":=")
    fig, ax = plt.subplots()
    ax.set_title('Señal Moduladora (Frecuencia)')
    ax.set_xlabel('Tiempo')
    plt.grid()
    plt.plot(x,y)
    plt.plot(x,y,'orange')
    plt.savefig("img/graphicModraFM.png", bbox_inches='tight')

def ModulatinggraphPM(vm,fm):
    x = []
    y = []
    vm = float(vm)
    fm = float(fm)
    time = float(0)
    for i in range(2000):
        wave = float(vm * math.cos(2*math.pi*fm*time))
        x.append(time)
        y.append(wave)
        time += 0.001
    print(":=")
    fig, ax = plt.subplots()
    ax.set_title('Señal Moduladora (Fase)')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Vm')    
    plt.grid()
    plt.plot(x,y)
    plt.savefig("img/graphicModraPM.png", bbox_inches='tight')

def Carriergraph(vc,fc):
    x = []
    y = []
    vc = float(vc)
    fc = float(fc)
    time = float(0)
    for i in range(2000):
        wave = float(vc * math.cos(2*math.pi*fc*time))
        x.append(time)
        y.append(wave)
        time += 0.001
    print(":)")
    CarriergraphFM(x,y)
    CarriergraphPM(x,y)
    

def CarriergraphFM(x,y):
    fig, ax = plt.subplots()
    ax.set_title('Señal Portadora (Frecuencia)')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Vm')    
    plt.grid()
    plt.plot(x,y)
    plt.plot(x,y,'orange')
    plt.savefig("img/graphicPorFM.png", bbox_inches='tight')

def CarriergraphPM(x,y):
    fig, ax = plt.subplots()
    ax.set_title('Señal Portadora (Fase)')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Vm')    
    plt.grid()
    plt.plot(x,y)
    plt.savefig("img/graphicPorPM.png", bbox_inches='tight')