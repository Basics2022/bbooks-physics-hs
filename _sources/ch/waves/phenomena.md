(physics-hs:waves:phenomena)=
# Caratteristiche dei fenomeni ondulatori

(physics-hs:waves:equation:solutions)=
## Soluzioni elementari
Vengono qui discusse alcune soluzioni elementari dell'[equazione lineare delle onde](physics-hs:waves:equation:example). In un problema lineare, una soluzione qualsiasi può essere ottenuta come somma di soluzioni elementari, sfruttando il principio di sovrapposizione delle cause e degli effetti (**todo-list:**[**PSCE**](physics-hs:todo:psce)): un segnale generico e la sua evoluzione può quindi essere studiato come somma di segnali semplici che evolvono in maniera indipendente l'uno dall'altro (**todo-list:**[**analisi di Fourier**](physics-hs:todo:fourier))

In particolare, vengono alcune soluzioni elementari in domini 1-dimensionali, nella forma di onde stazionarie o onde viaggianti, e in domini 3-dimensionali, nella forma di onde piane e onde sferiche.

Per ognuna di queste perturbazioni elementari[^eikonal-approx] prese singolarmente è possibile definire una lunghezza d'onda (o in 3d un vettore d'onda locale che indica la direzione della propagazione), una frequenza e la velocità della perturbazione.

### Dominio 1-dimensionale

**Onde stazionarie.** Una soluzione generica dell'equazione delle onde può essere scritta come somma di onde stazionarie nella forma

$$f_n(x) = \cos(k_n x + \phi_n) \ ,$$

modulate da un'ampiezza

$$g_n(t) = \cos(\omega_n t + \gamma_n) \ ,$$

con $\omega_n = c k_n$. Una funzione $u_n(x,t) = f_n(x) g_n(t)$ è soluzione dell'equazione delle onde.

```{dropdown} Dimostrazione
Per dimostrare che la funzione $f_n(x) g_n(t)$ è una soluzione dell'equazione delle onde, è sufficiente valutarne le derivate seconde rispetto al tempo e allo spazio, e sostituirne le espressioni nell'equazione delle onde per ottenere un'identità,

$$\begin{aligned}
  \partial_{tt} u & = \partial_{tt} \left( f_n(x) g_n(t) \right) = f_n(x) \ddot{g}_n(t) = - \omega_n^2 u \\
  \partial_{xx} u & = \partial_{xx} \left( f_n(x) g_n(t) \right) = f''_n(x) g_n(t) = - k_n^2 u \\
\end{aligned}$$

così che $\partial_{tt} u - c^2 \partial_{tt} u = \left( -\omega_n^2 + c^2 k_n^2 \right) u = 0$ se è soddisfatta la relazione tra la pulsazione $\omega_n$ e il vettore d'onda $k_n$, $\omega_n = c k_n$.
```

**Onde viaggianti.** Utilizzando le proprietà delle funzioni trigonometriche, la funzione $u_n(x,t) = f_{n}(x) g_n(t)$ può essere scritta come somma di due onde viaggianti con velocità $c$,

$$u_n(x,t) = f_n(x) g_n(t) = A_n^{-}(x+ct) + A_n^{+}(x-ct) \ .$$ (travelling-waves)

```{dropdown} Dimostrazione
$$\begin{aligned}
u_n(x,t) 
  & = f_n(x) g_n(t) = \\
  & = \cos(k_n x + \phi_n) \cos (\omega_n t + \gamma_n) = \\
  & = \frac{1}{2} \cos(k_n x + \omega_n t + \phi_n + \gamma_n) + \frac{1}{2} \cos(k_n x - \omega_n t + \phi_n - \gamma_n) = \\
  & = \frac{1}{2} \cos(k_n( x + c t) + \theta^-_n) + \frac{1}{2} \cos(k_n( x - c t) + \theta^+_n) = \\
  & = A_n^-(x+ct) + A_n^{+}(x+ct)
\end{aligned}$$
```

```{prf:definition} Pulsazione $\omega_n$ e frequenza $f_n$
:label: wave-frequency

Il parametro $\omega_n$ di una soluzione elementare viene definita **pulsazione**. La **frequenza** della soluzione elementare è definita come l'inverso del periodo della soluzione elementare $f_n = \frac{1}{T_n}$, e può essere espresso in funzione della pulsazione come $f_n = \frac{\omega_n}{2\pi}$.

```
```{prf:definition} Vettore d'onda $k_n$ e lunghezza d'onda $\lambda_n$
:label: wave-length

Il parametro $k_n$ di una soluzione elementare viene definita **vettore d'onda**. La **lunghezza d'onda** rappresenta la distanza tra due massimi consecutivi di soluzione elementare e la sua relazione con il vettore d'onda è $\lambda_n = \frac{2 \pi }{k_n}$.

Il carattere vettoriale del vettore d'onda appare evidente nei domini multi-dimenisonali, nei quali le soluzioni elentari possono essere espresse come funzione dell'argomento $\vec{k} \cdot \vec{r} - \omega t$. Il vettore d'onda $\vec{k}$ è un'indicazione della direzione locale di propagazione della perturbazione elementare.

```
```{prf:definition} Velocità di propagazione delle perturbazioni
:label: wave-speed

La velocità di propagazione delle perturbazioni governate dall'equazione delle onde {eq}`eq:wave-eqn:1d` è $c$. Il suo significato è evidente nell'espressione {eq}`travelling-waves` delle onde viaggianti, ed è uguale al rapporto tra la lunghezza d'onda e la frequenza di una soluzione elementare $c = \frac{\omega_n}{k_n}$.

```

La frequenza di una perturbazione in un problema lineare è tipicamente determinata dalla frequenza della sorgente della perturbazione (**todo-list:**[**analisi di Fourier**](physics-hs:todo:fourier)), poiché i sistemi lineari rispondono con la stessa frequenza della forzante. La velocità delle perturbazioni è una caratteristica del mezzo. La lunghezza d'onda del sistema è quindi lo spazio percorso da una perturbazione, in un periodo della forzante $T$ (intervallo di tempo che separa due massimi del disturbo esterno, e quindi della perturbazione),

$$\lambda = c T \ .$$

Usando le relazioni tra lunghezza d'onda e vettore d'onda $\lambda = \frac{2 \pi}{k_n}$, e tra periodo e puslazione $T_n = \frac{2 \pi}{\omega_n}$, si ottiene di nuovo

$$\omega_n = c k_n \ .$$


### Dominio 3-dimensionale

[^eikonal-approx]: In generale, questa operazione può essere svolta localmente per una soluzione qualisasi delle onde, nel limite di lunghezza d'onda molto minore delle dimensioni caratteristiche del problema. Questa approssimazione viene definita *approssimazione eikonale* ed è all'origine dell'approccio geometrico ai fenomeni ondulatori, come l'acustica geometrica o l'[ottica geometrica](physics-hs:waves:optics:geometric).

<!--
### Frequenza, lunghezza d'onda e relazione con velocità di propagazione della perturbazione
-->


**Onde sferiche.** Un'onda sferica prodotta da una sorgente puntiforme in un dominio 3-dimensionale può essere rappresentata usando un sistema di coordinate sferiche come

  $$f(r,t) = \dfrac{A(r-ct)}{r}$$

avendo scelto l'origine del sistema di coordinate, $r=0$, in corrispondenza della sorgente puntiforme.

```{admonition} Causalità e direzione di propagazione delle perturbazioni
A differenza dell'espressione delle onde viaggianti nel caso 1-dimesnionale, nell'espressione delle onde sferiche prodotte da una sorgente puntiforme è presente solo un tipo di onda
```

(physics-hs:waves:effects)=
## Effetti associati

(physics-hs:waves:effects:interference)=
### Interferenza

(physics-hs:waves:effects:reflection)=
### Riflessione

(physics-hs:waves:effects:refraction)=
### Rifrazione

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
