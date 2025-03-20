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

(physics-hs:waves:optics:geometric:lenses:thin)=
## Lenti sottili

(physics-hs:waves:optics:geometric:lenses:equation)=
### Equazione delle lenti sottili sferiche

Raggi paralleli incidenti su una lente sferica covessa sottile convergono in un unico punto sull'asse della lente, chiamato **fuoco della lente**, a una distanza $f$ dalla lente, chiamata **lunghezza focale**. Per una lente sottile esiste una relazione tra i raggi di curvatura $R_1$, $R_2$ delle superficie della lente, gli indifici di rifrazione del mezzo $n_1$ e della lente $n_L$ e la lunghezza focale $f$,

$$\frac{1}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{1}{R_1} + \frac{1}{R_2} \right) \ .$$

```{dropdown} Dimostrazione

Nel limite degli angoli piccoli da poter ritenedere buona l'approssimazione $\theta \sim \sin \theta \sim \tan \theta$, gli angoli dei versori normali alle lenti nei punti per i quali passa il raggio luminoso, a distanza $h$ dall'asse della lente sono

$$\phi_1 \sim \frac{h}{R_1} \qquad , \qquad \phi_2 \sim \frac{h}{R_2} \ .$$

Nel limite di piccoli angoli, gli angoli formati dai raggi luminosi entrante $\xi_1$ e uscente $\xi_2$ con l'asse della lente sono

 $$\xi_1 = \frac{h_o - h}{d_0} \qquad , \qquad \xi_2 = \frac{h_i + h}{d_i} \ , $$ (eq:lens:angles:approx)

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

Quindi segue la relazione tra l'angolo $\xi_2$ del raggio luminoso trasmesso dalla lente e l'angolo $\xi_1$ incidente sulla lente,

$$\begin{aligned}
  \xi_2
  & = \theta_2 - \phi_2 = \frac{n_L}{n_1} \theta_{L2} - \phi_2 = \\
  & = \frac{n_L}{n_1} \left( \phi_2 + \phi_1 - \frac{n_1}{n_L} \theta_1 \right) - \phi_2 = \\
  & = \frac{n_L}{n_1} \left( \phi_2 + \phi_1 - \frac{n_1}{n_L} \left( \phi_1 - \xi_1 \right) \right) - \phi_2 = \\
\end{aligned}$$
  
$$
  \xi_2 = \left( \frac{n_L}{n_1} - 1 \right) \left( \phi_2 + \phi_1 \right) + \xi_1 
$$ (eq:lens:angles:relation)

**Lunghezza focale.** La lunghezza focale si ottiene per raggi incidenti paralleli $\xi_1 = 0$, $h_0 = h$. Il fuoco della lente si trova sull'asse, e quindi $h^*_i = 0$. La distanza del fuoco dalla lente è definita **lunghezza focale**, $d^*_i = f$. Utilizzando l'approssimazione per piccoli angoli, $\xi_2 = \frac{h}{f}$, e quindi

$$\frac{h}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{h}{R_2} + \frac{h}{R_1} \right) \ ,$$

ed è quindi valida per ogni valore di $h$ e quindi per ogni raggio parallelo l'equazione delle lenti sottili

$$\frac{1}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{1}{R_1} + \frac{1}{R_2} \right) \ .$$

```

(physics-hs:waves:optics:geometric:lenses:image-focus)=
### Formazione dell'immagine

Dato un **piano dell'oggetto** $\pi_o$ a distanza $d_o$ dalla lente, i raggi luminosi provenienti da ogni punto $P_o$ del piano $\pi_o$ passanti per la lente sottile convergono in un unico punto $P_i$ di un piano $\pi_i$, detto **piano dell'immagine**, a distanza $d_i$ dalla lente con

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \ .$$

Questa condizione è la condizione di **messa a fuoco**, e comporta un rapporto di magnificazione dell'immagine

$$\frac{h_i}{h_o} = \frac{d_i}{d_o} \ ,$$

dove $h_o$, $h_i$ sono le distanze dall'asse della lente nel piano dell'oggetto e dell'immagine.

<!--
- Piano dell'immagine e **messa a fuoco**.
  - Dimostrazione che tutti i raggi luminosi provenienti da un punto convergono in un unico punto nel piano di formazione dell'immagine - messa a fuoco.
  - Mancata messa a fuoco
-->

```{dropdown} Piano dell'immagine

Esiste un piano, il piano di formazione dell'immagine, dove tutti i raggi provenienti da ogni punto di un piano, il piano dell'oggetto, convergono a un punto. In questo piano, l'immagine è a fuoco. Introducendo le approssimazioni {eq}`eq:lens:angles:approx` nella relazione {eq}`eq:lens:angles:relation` tra gli angoli dei raggi incidente e trasmesso dalla lente, si ottiene la relazione

$$\frac{h_i + h}{d_i} = \left(\frac{n_L}{n_1} - 1 \right)\left(\frac{h}{R_1}+\frac{h}{R_2}\right) + \frac{h_o - h}{d_o} \ ,$$

$$\frac{h_i}{d_i} = \frac{h}{f} + \frac{h_o}{d_o} - h \left( \frac{1}{d_o} + \frac{1}{d_i} \right) = \frac{h_o}{d_o} + h \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right)\ .$$

Esprimendo la distanza $h$ in funzione dell'angolo del raggio incidente $\xi_1$,

 $$h = h_o - d_o \, \xi_1 \ ,$$

si ottiene una relazione tra la distanze dall'asse dei punti dell'oggetto $h_o$ e dell'immagine formata $h_i$, la distanza dalla lente dell'oggetto e del piano di formazione dell'immagine $d_o$, $d_i$, della lunghezza focale e dell'angolo $\xi_1$ dei raggi incidenti passanti per la lente dei raggi incidenti passanti per la lente,,

$$\begin{aligned}
  \frac{h_i}{d_i}
  & = h_o \left( \frac{1}{d_o} + \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) - \xi_1 d_o \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \\
  & = h_o \left( \frac{1}{f} - \frac{1}{d_i} \right) - \xi_1 d_o \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \\
\end{aligned}$$

e quindi esprimere $h_i$ come funzione degli altri parametri

$$h_i(\xi_1; f; d_o, d_i, h_o) = h_o \left( \frac{d_i}{f} - 1 \right) - \xi_1 d_o d_i \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \ .$$

In generale, i raggi provenienti da un oggetto arrivano in punti differenti su un piano generico a distanza $d_i$ dalla lente, poiché la distanza $h_i$ dipende dall'angolo $\xi_i$, tenendo costanti gli altri parametri.

Nel caso in cui $h_i$ non dipende da $x_i$, tutti i raggi provenienti dallo stesso punto dell'oggetto convergono nello stesso punto del piano. Questa è la condizione di **messa a fuoco**, e definisce la relazione tra lunghezza focale, distanza dell'oggetto e distanza del piano di formazione dell'immagine,

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \ .$$

```

```{dropdown} Magnificazione

Nelle condizioni di messa a fuoco, si può quindi scrivere

$$h_i = h_o \left( \frac{d_i}{f} - 1 \right) = d_i \frac{h_o}{d_o} \ ,$$

o in termini della magnificazione

 $$\frac{h_i}{h_o} = \frac{d_i}{d_o} \ .$$

```

## Lenti sempici

## Lenti

```{prf:example} Lente di ingrandimento
```

```{prf:example} Messa a fuoco
```

```{prf:example} Auto-focus

- Per convoluzione
- Per contrasto
```

```{prf:example} Zoom
Zoom: sistema afocale (modifica l'ingrandimento angolare) + lente focale (si occupa della generazione dell'immagine)
```

## Lenti spesse
[Lenti spesse, wikipedia](https://it.wikipedia.org/wiki/Lente_spessa)
