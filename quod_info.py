#pendolo quadrifilare

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# carica il file con i dati
dati = np.loadtxt("tebella_pendolo_formattata.txt")#mi raccomando in fondto .txt se è quello il formato

# estrai la i-esima colonna
prima_colonna = dati[:, 0]
seconda_colonna = dati[:, 1]
terza_colonna = dati[:, 2]
"""
# Seleziona gli elementi dall'indice i all'indice k (Python usa slicing: include i ma esclude k)
i, k = 2, 5  # Cambia questi valori come ti serve
subset = seconda_colonna[i:k]
"""
#tempo dall inizio presa dati ps non credo serva
a = prima_colonna[0:10] #10 è inventato
#Periodo T delloscilalzione corrente
p = seconda_colonna[0:10] #10 è inventato
#tempo di transito della bandierina
t = terza_colonna[0:10] #10 è inventato

sigma_tempi = np.full(t.shape, 0.01) #0.01 è di prova non lo so a priori
#costanti
#lunghezza fulcro-cm
l = 60.0#va misurato
sl = 0.01 #errore strumento in metri

#distanza fulcro-bandiera
d = 65.0 #va misurato
sd = 0.01 #errore strumento in metri

#larghezza bandierina

w = 5.0 #va misurata
dw = 0.01 #errore strumento in metri
#gravità
g = 9.81

"""
prima richiesta "Si costruisca il grafico della velocità v0 nel punto
più basso in funzione del tempo" (forse è il tempo della prima colonna)
"""
#in un asse c'è il i_esimo tempo della prima colonna, nell'altro ci deve essere la funzione che descrive v0 con l' i-esimo tempo della terza collona associato a quello della prima

def funzione_del_fit(λ, w, l, t, d):
    return (w * l) / (t * d) * np.exp(-λ * t)

fit, covfit = curve_fit(funzione_del_fit, x, y, sigma=sigma_tempi)
λ, w, l, t, d,   = fit
dλ, dw, dl, dt, dd, = np.sqrt(covfit.diagonal())

plt.errorbar(t, p , dp ,dt , fmt='o' )
zz = np.linspace(0, 0.5, 200)

plt.plot(zz, funzione_del_fit(zz, funzione_del_fit, dt, dp) )

plt.show()




















