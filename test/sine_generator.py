import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def seno(N, amplitud):
    samples = np.linspace(0, 1, N)
    return [hex(int(i)) for i in ((2**(amplitud-1))*np.sin(np.pi*2*samples)+(2**(amplitud-1)))]

# def chip(N, amplitud):
#     samples = np.linspace(0, 1, N)
#     w = (2**(amplitud-1))*(chirp(samples, f0=1, f1=8, t1=1, method='linear')+1)
#     return [hex(int(i)) for i in w]

if __name__=="__main__":
    
    sen = chirp(100,8)
    # cont = 0
    # for t in sen:
    #     if len(t) < 5:
    #         aux = t[0:1] 
    #         for h in range(5-len(t)):
    #             aux += "0"
    #         aux += t[2:-1]
    #         sen[cont] = aux
    #     cont = cont +1
            
    print(sen)
    plt.plot(sen)
    plt.show()