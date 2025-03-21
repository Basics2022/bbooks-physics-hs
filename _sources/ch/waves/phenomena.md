(physics-hs:waves:phenomena)=
# Caratteristiche dei fenomeni ondulatori

(physics-hs:waves:equation:solutions)=
## Soluzioni elementari
Vengono qui discusse alcune soluzioni elementari dell'[equazione lineare delle onde](physics-hs:waves:equation:example). In un problema lineare, una soluzione qualsiasi può essere ottenuta come somma di soluzioni elementari, sfruttando il principio di sovrapposizione delle cause e degli effetti (**todo-list:**[**PSCE**](physics-hs:todo:psce)): un segnale generico e la sua evoluzione può quindi essere studiato come somma di segnali semplici che evolvono in maniera indipendente l'uno dall'altro (**todo-list:**[**analisi di Fourier**](physics-hs:todo:fourier))

In particolare, vengono alcune soluzioni elementari in domini 1-dimensionali, nella forma di onde stazionarie o onde viaggianti, e in domini 3-dimensionali, nella forma di onde piane e onde sferiche.

Per ognuna di queste perturbazioni elementari[^eikonal-approx] prese singolarmente è possibile definire una lunghezza d'onda (o in 3d un vettore d'onda locale che indica la direzione della propagazione), una frequenza e la velocità della perturbazione.

### Dominio 1-dimensionale

### Dominio 3-dimensionale

[^eikonal-approx]: In generale, questa operazione può essere svolta localmente per una soluzione qualisasi delle onde, nel limite di lunghezza d'onda molto minore delle dimensioni caratteristiche del problema. Questa approssimazione viene definita *approssimazione eikonale* ed è all'origine dell'approccio geometrico ai fenomeni ondulatori, come l'acustica geometrica o l'[ottica geometrica](physics-hs:waves:optics:geometric).

<!--
### Frequenza, lunghezza d'onda e relazione con velocità di propagazione della perturbazione
-->

```{prf:definition} Frequenza
:label: wave-frequency

```
```{prf:definition} Lunghezza d'onda
:label: wave-length

```
```{prf:definition} Velocità della perturbazione
:label: wave-speed

```

Per i fenomeni fisici governati da problemi lineari, vale il **principio di sovrapposizione delle cause e degli effetti**. ...

- Soluzione generale 1-dimensionale

  $$f(x,t) = A_{+}(x - c t) + A_{-}(x + ct)$$

```{dropdown} Verifica della soluzione

$$\begin{aligned}
\partial_x    f & = A'_+(x-ct) + A'_-(x+ct) \\
\partial_{xx} f & = A''_+(x-ct) + A''_-(x+ct) \\
\partial_t    f & = - c \, A'_+(x-ct) + c \, A'_-(x+ct) \\
\partial_{tt} f & = c^2 \, A''_+(x-ct) + c^2 \,  A''_-(x+ct) \\
\end{aligned}$$

```


- Soluzione generale 3-dimensionale

  $$f(r,t) = \dfrac{A(r-ct)}{r}$$

(physics-hs:waves:effects)=
## Effetti associati

(physics-hs:waves:effects:reflection)=
### Riflessione

(physics-hs:waves:effects:refraction)=
### Rifrazione

(physics-hs:waves:effects:interference)=
### Interferenza

(physics-hs:waves:effects:diffraction)=
### Diffrazione

La diffrazione è una conseguenza dell'incontro di un'onda con un ostacolo o un'apertura di dimensione parabonabile alla lunghezza d'onda ({prf:ref}`wave-length`) della perturbazione.

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
### Polarizzazione
- Onde sismiche S, shear, di taglio
- Onde EM

(physics-hs:waves:effects:doppler)=
### Effetto Doppler
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
