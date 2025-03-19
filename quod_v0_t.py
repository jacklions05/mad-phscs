#pendolo quadrifilare alternativo
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

#array con i 3 tempi
t_1 = np.array([3.206268,17.088677,43.755925,73.582968,93.802320,116.133285,132.074624,149.070693,160.751470,184.102975,206.382201,224.411205,246.674636,272.109141,295.416063,320.833134,346.242987,394.928853,419.264950]) #tempo dall'inizio della presa dati
t_2 = np.array([]) #il periodo T dell’oscillazione corrente
t_3 = np.array([0.013812,0.014362,0.015470,0.016732,0.017624,0.018630,0.019432,0.020266,0.020872,0.022102,0.023318,0.024366,0.025652,0.027290,0.028810,0.030712,0.032674,0.036594,0.038732]) #il tempo di transito tT della bandierina
#inserisco le costanti
"""
by jack
tt=np.array([0.013812,0.014362,0.015470,0.016732,0.017624,0.018630,0.019432,0.20266,0.20872,0.022102,0.023318,0.24366,0.025652,0.027290,0.028810,0.30712,0.32674,0.036594,0.038732])
sigma_tt=np.full (t.shape, 0.00001)



t=np.array([3.206268,17.088677,43.755925,73.582968,93.802320,116.133285,132.074624,149.070693,160.751470,184.102975,206.382201,224.411205,246.674636,272.109141,295.416063,320.833134,346.242987,394.928853,419.264950])
sigma_t=np.full(t.shape, 0.00001)
"""
#costanti
#lunghezza fulcro-cm
l = 1.093 #va misurato
sl = 0.01 #errore strumento in metri

#distanza fulcro-bandiera
d =  1.16 #va misurato
sd = 0.01 #errore strumento in metri

#larghezza bandierina

w =  0.0202 #va misurata
dw = 0.01 #errore strumento in metri
#gravità
g = 9.81

#prima richiesta grafico di v0 in funzione del tempo

def v_0(t_3):
    return (w / t_3) * (l / d)
y = v_0(t_3)
plt.plot(t_1, y, label="grafico della velocità v0 nel punto più basso in funzione del tempo", color="c")
plt.scatter(t_1, y)
plt.title("Grafico della velocità v0 nel punto più basso in funzione del tempo")
plt.xlabel("tempo di transito")
plt.ylabel("v0")
plt.legend()
# Mostra il grafico
plt.show()




