import matplotlib.pyplot as plt
import numpy as numpy

colors=["green","blue","orange","red","cyan","pink","black"]


def graphicspectrumFM(fLaterales):
    x = []
    y = []
    for i in range((len(fLaterales))):
        y.append(fLaterales[i])
        x.append(i)
    for i in range((len(fLaterales))):
        a=-i
        y.append(fLaterales[i])
        x.append(a)
    fig, ax = plt.subplots()
    ax.set_title('Espectro de frecuencias de las bandas laterales (FM-Frecuencia)')
    plt.bar(x,y, color="orange")
    plt.savefig("img\graphicspectFM.png", bbox_inches='tight')

def graphicspectrumPM(fLaterales):
    x = []
    y = []
    for i in range((len(fLaterales))):
        y.append(fLaterales[i])
        x.append(i)
    for i in range((len(fLaterales))):
        a=-i
        y.append(fLaterales[i])
        x.append(a)
    fig, ax = plt.subplots()
    ax.set_title('Espectro de frecuencias de las bandas laterales (PM-Fase)')
    plt.bar(x,y)
    plt.savefig("img\graphicspectPM.png", bbox_inches='tight')



