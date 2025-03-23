(physics-hs:waves:phenomena)=
# Caratteristiche dei fenomeni ondulatori

**todo**
- necessità di segnali coerenti (es.laser, forzanti armoniche)?
- condizioni nelle quali è lecito aspettarsi la manifestazione dei seguenti fenomeni. Es. diffrazione quando un'onda incontra ostacoli di dimensioni "paragonabili" alla lunghezza d'onda della perturbazione...

(physics-hs:waves:effects:interference)=
## Interferenza

- distinguere tra PSCE di segnali, e pattern di interferenza che compare nel quadrato del segnale, spesso associato alle grandezze percepite con i sensi e/o misurate da strumenti di misura (es. intensità luminosa della radiazione elettromagnetica)

(physics-hs:waves:effects:reflection)=
## Riflessione

(physics-hs:waves:effects:refraction)=
## Rifrazione

(physics-hs:waves:effects:diffraction)=
## Diffrazione

La diffrazione è una conseguenza dell'intereferenza di un'onda con un ostacolo o un'apertura di dimensione parabonabile alla lunghezza d'onda ({prf:ref}`wave-length`) della perturbazione.

Per alcune geometrie semplici, sono note alcune soluzioni approssimate dei pattern di interferenza in seguito alla diffrazione:
- **near-field**: approssimazione di Fresnel
- **far-field**: approssimazione di Fraunhofer

**todo** 
- Limiti di diffrazione: quando è lecito aspettarsi diosservare diffrazione?
- Aggiungere esempi di soluzione esatta calcolata con script, e confronto con le approssimazioni di Fresnel e Fraunhofer; distinguere tra soprapposizione segnali, e pattern di [interferenza nell'intensità media](physics-hs:waves:effects:intereference). Riferimeni: [video di 3B1B - How re hologram possible?](physics-hs:extra:waves-optics)

- Fare esempi pratici: lato posteriore di un DVD, doppia fenditura, reticoli di diffrazione, diaframma di una macchina fotografica con apertura ridotta,...

**Applicazioni ed esempi.** Spettroscopia

```{prf:example} Doppia fenditura
Modello: diffrazione dovuta a due fessure sufficientmente ridotte da poter essere considerate sorgenti puntiformi (in fase, o no? discutere)
```

```{prf:example} Singola fenditura
Modello: diffrazione dovuta alla sovrapposizione degli effetti di una distribuzione di sorgenti punti. 
```

```{prf:example} Reticolo di diffrazione
```

(physics-hs:waves:effects:polarization)=
## Polarizzazione
- Onde sismiche S, shear, di taglio
- Onde EM

(physics-hs:waves:effects:doppler)=
## Effetto Doppler
Quando la sorgente e l'osservatore sono in moto relativo, la frequenza percepita dall'osservatore è diversa dalla frequenza emessa dalla sorgente.

$$A(t) = F \cos(\Omega t )$$

<!--
$$f(x, t) = A_+(x-x_s(t_{ret}) - c(t-t_{ret}))$$
-->

con $t_{ret}$ l'istante di tempo in cui è stato emesso il segnale dalla sorgente che raggiunge il punto $x$ nell'istante $t > t_{ret}$ (causalità)

$$\begin{aligned}
 | x - x_s(t_{ret}) | & = \quad  c (t - t_{ret}) \\
   x - x_s(t_{ret})   & = \pm c (t - t_{ret}) = \begin{cases} \quad c ( t-t_{ret} ) & , \quad x \ge x_s(t_{ret}) \\ - c ( t-t_{ret} ) & , \quad  x \le x_s(t_{ret}) \\ \end{cases}
\end{aligned}$$

Nel caso di sorgente a velocità costante, $x_s(t) = x_{s,0} + v_s t$, e ricettore a velocità costante $x_r(t) = x_{r,0} + v_r t$.

$$\begin{aligned}
  x_r(t) -x_s(t_{ret}) & = \pm c ( t - t_{ret} ) \\
  x_{r,0} + v_r t - x_{s,0} - v_s t_{ret} & = \pm c ( t - t_{ret} ) \\
\end{aligned}$$


$$(v_s \mp c) t_{ret} = (v_r \mp c) t + x_{r,0} - x_{s,0}$$

$$t_{ret} = \dfrac{v_r \mp c}{v_s \mp c} t + \dfrac{x_{r,0} - x_{s,0}}{v_s \mp c}$$

<!--
$$x - x_{s,0} - v_s t_{ret} = c \left( t - t_{ret} \right)$$

$$t_{ret} = \dfrac{c}{c - v_s} t - \dfrac{x - x_{s,0}}{c}$$
-->
