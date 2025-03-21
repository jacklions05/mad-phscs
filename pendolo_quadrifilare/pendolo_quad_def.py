#pendolo quad definitv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# carica il file con i dati
dati = np.loadtxt(...il percorso pper arrivare ak vstro file)#ah ricordati di mettere doppia \\ quando incolli il nuovo percorso file perche python non prende la singola
#secondo me seconda30 è il miglior set di dati poi vedete anche voi sperimentate...
# estrai la i-esima colonna

t_1 = dati[:, 0]
t_2 = dati[:, 1]
t_3 = dati[:, 2]

sigma_t = np.full(t_3.shape, 0.000001,)
"""
print(f"quiesti sono i tempi 1 {t_1}")
print(f"quiesti sono i tempi 2 {t_2}")
print(f"quiesti sono i tempi 3 {t_3}")
"""
#costanti
#lunghezza fulcro-cm
l = 1.148 #ufficiale 1.140 , da variare per far tornare meglio l'ultimo grafico con i.148 viene bene poi provate a cambiare anche voi
sigma_l = 0.001 #errore strumento in metri

#distanza fulcro-bandiera
d =  1.175 # certa
sigma_d = 0.001 #errore strumento in metri

#larghezza bandierina

w =  0.021 #  0.0218
sigma_w = 0.001 #errore strumento in metri

#provate a mettere 0.0218 a w e 0.00005 a sigma_w cambia tutto,

#gravità
g = 9.81
sigma_g = 0.01

def f_velocita(t_3):
    return (w / t_3) * (l / d)
v_0 = f_velocita(t_3)
#nel grafico ci vorrebbe la crassir sugli errori di t e della velocita

#formula per trovare la sigma delle velocita
#np.abs(v_0) *
sigma_v0 = np.abs(v_0) * np.sqrt((sigma_w / w)**2 + (sigma_t / t_3)**2 + (sigma_l / l)**2 + (sigma_d / d)**2)
#v00 è la prima velocita
sigma_v00 = np.array([sigma_v0[0]])
print(f"l'incertezza di v00 è di {sigma_v00}")
#plt.plot(t_1, v_0, "o",label="v_0(t)", color="c", ls='', markersize=0.1)
#ho commentato plt.plot perche tanto non si vedeva il punto, poi se riuscite a migliorare questa cosa bene

#plt.errorbar()
plt.errorbar(t_1, v_0, xerr=sigma_t, yerr=sigma_v0, fmt='+', color='red',
             ecolor='black', elinewidth=1, capsize=3, capthick=0.001)
plt.grid(which="both") #se clicco su grafico e premo l viene il grafico in scala logaritmica
#plt.scatter(t_1, v_0, s=0.1)

plt.title("Grafico della velocità $v_0$ in funzione del tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("$v_0$ (m/s)")
#plt.legend() non so che scriverci
plt.show()

#il fit

#ora il fit della velocità

#attenzione la funzione ha come costante diciamo la prima velocita
# v00 = np.array([v_0[0]]) lho scritta prima
#print(f"la velocita iniziale è {v00}")


def funzione_del_fit(t_1 , v00, λ):
    return v00 * np.exp(-λ * t_1)

popt, pcov = curve_fit(funzione_del_fit, t_1, v_0, sigma=sigma_v0, p0=[v_0[0], 0.001])
# popt: array con i parametri ottimizzati [v0_iniziale, λ]
v00_hat = popt[0]
λ_hat = popt[1]

# pcov: Matrice di covarianza. Gli errori sono sqrt degli elementi diagonali
errori = np.sqrt(np.diag(pcov))
sigma_v00 = errori[0]
sigma_λ = errori[1]

# Grafico
plt.errorbar(t_1, v_0, yerr=sigma_v0, fmt='o',markersize=0.5, label='Dati')
t_fit = np.linspace(min(t_1), max(t_1), 100)
plt.plot(t_fit, funzione_del_fit(t_fit, *popt), 'r-',
         label=rf'Fit: $v_0(0) = {v00_hat:.3f} \pm {sigma_v00:.3f}$ m/s, $\lambda = {λ_hat:.5f} \pm {sigma_λ:.5f}$ s$^{{-1}}$')

plt.xlabel('Tempo (s)')
plt.ylabel(r'$v_0$ (m/s)')
plt.legend()
plt.show()

print(f"Parametri ottimali: v00 = {v00_hat:.5f} ± {sigma_v00:.5f}")
print(f"Lambda stimato: {λ_hat:.5f} ± {sigma_λ:.5f}")

#Si costruisca il grafico cartesiano del periodo T in funzione dell’ampiezza θ_0 di oscillazione e si verifichi la (1)
#formula (1) del tempo

def funzione_di_theta(v_0, g, l):
    return np.arccos( 1 - (v_0 **2 / (2 * g * l)))
θ_0_decrescente = funzione_di_theta(v_0, g, l)
#print(θ_0_decrescente)
angle_zero = θ_0_decrescente[0] #mi faccio dare il primo valore cioè l'angolo di partenza
angle_zero_degree = (angle_zero * 180)/np.pi
print(f"L'angolo iniziale è di {angle_zero_degree:.3f} gradi")

def periodo_pendolo(l, g, θ_0_decrescente):
    return 2 * np.pi * np.sqrt(l / g) * (1 + (1/16) * θ_0_decrescente**2 + (11/3072) * θ_0_decrescente**4)
T = periodo_pendolo(l, g, θ_0_decrescente)



#θ_0=θ_0_decrescente[::-1] #ok va bene
"""
plt.plot(θ_0, T, label="Periodo (T)", color="blue")  # Prima funzione
plt.plot(θ_0, v_0, label="Velocità iniziale (v_0)", )  # Seconda funzione (esempio)

"""
color="red"
plt.plot(θ_0_decrescente, t_2, label=r"Curva sperimentale", color="blue") #probabilmente questo comando li ordina in ordine crescente da solo senno non si spiega
plt.plot(θ_0_decrescente, T,label=r"Curva teorica", color="red")
plt.show()
#non so se i nomi curva vadano bene


#eroore di affset, nella formula di (1) probabilmente abbiamo sbagloto a misurare l, bisogna provare tutti i valori di l scalado di un cm per esmpio finche non psarisce l'offset
#abbiamo considetaro il cm il chiodino del pendolo dove ce lattacco della sonda'




