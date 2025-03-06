(physics-hs:waves:optics:geometric:lenses)=
# Lenti e strumenti ottici

- Lenti sottili sferiche:
  - caratteristiche
  - tipi: conv
  
- Strumenti ottici e caratteristiche:
  - distanza focale
  - ingrandimento
  - messa a fuoco
  - apertura - diaframma
  - tempi di esposizione - otturatore
  - profondità di campo
  
- Problemi:
  - aberrazione
  - ...
  
- L'occhio umano

(physics-hs:waves:optics:geometric:lenses)=
## Lenti sottili

(physics-hs:waves:optics:geometric:lenses:equation)=
### Equazione delle lenti sottili sferiche

Raggi paralleli incidenti su una lente sferica covessa sottile convergono in un unico punto, chiamato **fuoco della lente**. L'angolo

$$\phi_1 = \frac{h}{R_1} \qquad , \qquad \phi_2i = \frac{h}{R_2} \ .$$

Nel limite di piccoli angoli, gli angoli formati dai raggi luminosi con l'asse della lente sono

 $$\xi_1 = \frac{h_o - h}{d_0} \qquad , \qquad \xi_2 = \frac{h_i + h}{d_i} \ . $$

Siano $\theta_1$, $\theta_{L1}$ gli angoli rispetto alla normale della superficie del raggio incidente entrante nella lente e trasmesso nella lente, $\theta_{L2}$, $\theta_2$ gli angoli rispetto alla normale locale rel raggio uscente dalla lente.

L'applicazione della [legge di Snell](physics-hs:waves:optics:geometric:phenomena:snell) fornisce le relazioni

  $$\begin{aligned}
    \frac{n_L}{n_1} & = \frac{\sin \theta_1}{\sin \theta_{L1}} \qquad , \qquad
    \frac{n_L}{n_1} & = \frac{\sin \theta_2}{\sin \theta_{L2}} 
  \end{aligned}$$

mentre la geometria del problema

$$\begin{aligned}
  \theta_1    & = \phi_1 - \xi_1 \\
  \xi_2       & = \theta_2 - \phi_2 \\
  \theta_{2L} & = \phi_2 + \xi_{1L} = \phi_2 + \phi_1 - \theta_{1L} 
\end{aligned}$$

Quindi

$$\begin{aligned}
  \xi_2
  & = \theta_2 - \phi_2 = \frac{n_L}{n_1} \theta_{L2} - \phi_2 = \\
  & = \frac{n_L}{n_1} \left( \phi_2 + \phi_1 - \frac{n_1}{n_L} \theta_1 \right) - \phi_2 = \\
  & = \frac{n_L}{n_1} \left( \phi_2 + \phi_1 - \frac{n_1}{n_L} \left( \phi_1 - \xi_1 \right) \right) - \phi_2 = \\
  & = \left( \frac{n_L}{n_1} - 1 \right) \left( \phi_2 + \phi_1 \right) + \xi_1 \\
\end{aligned}$$

La lunghezza focale si ottiene per raggi incidenti paralleli $\xi_1 = 0$, $h_0 = h$. Il fuoco della lente si trova sull'asse, e quindi $h^*_i = 0$. La distanza del fuoco dalla lente è definita **lunghezza focale**, $d^*_i = f$. Utilizzando l'approssimazione per piccoli angoli, $\xi_2 = \frac{h}{f}$, e quindi

$$\frac{h}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{h}{R_2} + \frac{h}{R_1} \right) \ ,$$

ed è quindi valida per ogni valore di $h$ e quindi per ogni raggio parallelo l'equazione delle lenti sottili

$$\frac{1}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{1}{R_1} + \frac{1}{R_2} \right) \ .$$


(physics-hs:waves:optics:geometric:lenses:image-focus)=
### Formazione dell'immagine

Dato un **piano dell'oggetto** $\pi_o$ a distanza $d_o$ dalla lente, i raggi luminosi provenienti da ogni punto $P_o$ del piano $\pi_o$ passanti per la lente sottile convergono in un unico punto $P_i$ di un piano $\pi_i$, detto **piano dell'immagine**, a distanza $d_i$ dalla lente con

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \ .$$

Questa condizione è la condizione di **messa a fuoco**, e comporta un rapporto di magnificazione dell'immagine

$$-\frac{h_i}{h_o} = \frac{d_i}{d_o} \ ,$$

dove $h_o$, $h_i$ sono le distanze dall'asse della lente nel piano dell'oggetto e dell'immagine.




<!--
- Piano dell'immagine e **messa a fuoco**.
  - Dimostrazione che tutti i raggi luminosi provenienti da un punto convergono in un unico punto nel piano di formazione dell'immagine - messa a fuoco.
  - Mancata messa a fuoco
-->

Esiste un piano, il piano di formazione dell'immagine, dove tutti i raggi provenienti da ogni punto di un piano, il piano dell'oggetto, convergono a un punto. In questo piano, l'immagine è a fuoco.

$$\frac{h_i + h}{d_i} = \left(\frac{n_L}{n_1} - 1 \right)\left(\frac{h}{R_1}+\frac{h}{R_2}\right) + \frac{h_o - h}{d_o} \ ,$$

$$\frac{h_i}{d_i} = \frac{h}{f} + \frac{h_o}{d_o} - h \left( \frac{1}{d_o} + \frac{1}{d_i} \right) = \frac{h_o}{d_o} + h \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right)\ .$$

e scrivendo $h = h_o - d_o \, \xi_1$,

$$\begin{aligned}
  \frac{h_i}{d_i}
  & = h_o \left( \frac{1}{d_o} + \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) - \xi_1 d_o \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \\
  & = h_o \left( \frac{1}{f} - \frac{1}{d_i} \right) - \xi_1 d_o \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \\
\end{aligned}$$

Le coordinate delle immagini del punto non dipende dall'angolo $\xi_1$ e quindi dal raggio luminoso che origina dallo stesso punto e passa per la lente se la seconda parentesi è nulla. Questo definisce la relazione tra la lunghezza focale, la distanza dall'oggetto e la distanza del piano di formazione dell'immagine dalla lente per avere la **messa a fuoco**

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \ .$$

Nelle condizioni di messa a fuoco, si può quindi scrivere

$$h_i = h_o \left( \frac{d_i}{f} - 1 \right) = d_i \frac{h_o}{d_o} \ ,R$$

o in termini della magnificazione

 $$\frac{h_i}{h_o} = \frac{d_i}{d_o} \ .$$



```{prf:example} Lente di ingrandimento
```

```{prf:example} Auto-focus

- Per convoluzione
- Per contrasto
```

## Lenti sempici

## Lenti
- Zoom: sistema afocale (modifica l'ingrandimento angolare) + lente focale (si occupa della generazione dell'immagine)

## Lenti spesse
[Lenti spesse, wikipedia](https://it.wikipedia.org/wiki/Lente_spessa)
