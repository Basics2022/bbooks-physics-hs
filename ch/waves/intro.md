(physics-hs:waves:intro)=
# Introduzione ai fenomeni ondulatori

- Onde meccaniche nei mezzi continui:
  - nei solidi
    - elastici
    - onde sismiche
  - nei fluidi
    - onde di pressione (densità e altre proprietà meccaniche) e suono
- Onde EM; lo spettro EM comprende
  - onde radio, micro, IR, luce visibile, UV, $\gamma$, $X$

(physics-hs:waves:equation:examples)=
## Equazione delle onde in diversi sistemi
In questa sezione viene discussa la comparsa dell'equazione delle onde in diversi ambiti della fisica.

(physics-hs:waves:equation:examples:mechanics)=
### Sistemi meccanici

(physics-hs:waves:equation:examples:mechanics:axial)=
#### Azione assiale - catena di molle lineari

$$M_j \ddot{U}_j(t) = F_{j,j-1} + F_{j,j+1} + F_j^{ext}(t) = K_{j,j-1} \left( U_{j-1}(t) - U_j(t) \right) + K_{j,j+1} \left( U_{j+1}(t) - U_{j}(t) \right) + f_j^{ext}$$

...

Se le molle hanno tutte la stessa rigidezza, $K$,

$$M_j \ddot{U}_j(t) - K \left( U_{j-1}(t) - 2 U_j(t) + U_{j+1}(t) \right) =  F^e_j(t) \ .$$ (eq:axial:discrete:index)

**Condizioni iniziali e condizioni al contorno.**

**Forma matriciale.** Il problema può essere riscritto usando il formalismo matriciale come

$$\begin{aligned}
  \mathbf{M} \ddot{\mathbf{U}} + \mathbf{K} \mathbf{U} = \mathbf{F}^e \ ,
\end{aligned}$$

con le matrici

$$\mathbf{K} = K \begin{bmatrix}
   2    & -1    &  0    &  0    & 0     & \dots & 0     \\
  -1    &  2    & -1    &  0    & 0     & \dots & 0     \\ 
   0    & -1    &  2    & -1    & 0     & \dots & 0     \\
  \dots & \dots & \dots & \dots & \dots & \dots & \dots \\
   0    & 0     & \dots & 0     &    2  & -1    &  0    \\  
   0    & 0     & \dots & 0     &   -1  &  2    & -1    \\  
\end{bmatrix}$$

$$\mathbf{M} = \begin{bmatrix}
   M_1  &  0    &  0    &  \dots   & 0     \\
   0    &  M_2  &  0    &  \dots   & 0     \\ 
   0    &  0    &  M_3  &  \dots   & 0     \\
  \dots & \dots & \dots &  \dots   & \dots \\
   0    & 0     & \dots &  M_{n-1} & 0     \\  
   0    & 0     & \dots &  0       & M_n   \\  
\end{bmatrix}$$

$$\mathbf{U}(t) = \begin{bmatrix} U_0(t) & U_1(t) & \dots & U_n(t) \end{bmatrix}^T$$
$$\mathbf{F}(t) = \begin{bmatrix} F_0(t) & F_1(t) & \dots & F_n(t) \end{bmatrix}^T$$

**Approssimazione di un problema continuo.** Gli elementi del vettore $\mathbf{U}$ possono essere interpretati come i valori di una funzione del tempo e dello spazio, $u(x,t)$, per determinati valori della variabile indipendente $x$,

$$U_j(t) = u(x_j, t) \ .$$

Se i punti di coordinata $x_j$ hanno intervalli regolari,

$$x_j = x_{j-1} + \Delta x \qquad , \qquad x_j = j \, \Delta x \qquad j = 0:n \ ,$$

con $\Delta x$ "sufficientemente piccolo", allora l'approssimazione in serie di Taylor

$$\begin{aligned}
  & u(x_i,t) \\
  & u(x_i+\Delta x, t) = u(x_i,t) + \Delta x \partial_x u(x_i,t) + \dfrac{1}{2} \Delta x^2 \partial_{xx} u(x_i,t) + o(\Delta x^2) \\
  & u(x_i-\Delta x, t) = u(x_i,t) - \Delta x \partial_x u(x_i,t) + \dfrac{1}{2} \Delta x^2 \partial_{xx} u(x_i,t) + o(\Delta x^2) \\
\end{aligned}$$

permette di riconoscere l'approssimazione centrata della derivata seconda $\partial_{xx} u(x_i, t)$ valutata in $x = x_i$,

$$\partial_{xx} u(x_i,t) = \dfrac{u(x_i-\Delta x,t) - 2 u(x_i,t) + u(x_i+\Delta x,t)}{\Delta x^2}$$


$$M_j \partial_{tt} u(x_j,t) - \Delta x^2 K \partial_{xx} u(x_j,t) = F_j(t) $$


(physics-hs:waves:equation:examples:mechanics:torsion)=
#### Torsione - catena di molle rotazionali

$$I \partial_{tt} \theta(x_j,t) - \Delta x^2 K_t \partial_{xx} \theta(x_j,t) = M_j(t)$$


(physics-hs:waves:equation:examples:mechanics:string)=
#### Filo teso

$$M_j \partial_{tt} u(x_j,t) - \Delta x^2 N_0 \partial_{xx} u(x_j,t) = F_j(t)$$

Esempio: corde di strumenti musicali.

(physics-hs:waves:equation:examples:fluids)=
### Fluidi

(physics-hs:waves:equation:examples:fluids:sound)=
#### Suono

La percezione umana dell'udito è legata alla trasduzione di perturbazioni di pressione di ampiezza limitata da parte del nostro sistema di misura che va dall'orecchio al nostro cervello, capace di percepire perturbazioni di frequenza compresa qualitativamente tra $20 \, \text{Hz}$ e $20.000 \, \text{Hz}$.

**Suono in un tubo.** 

Poi da cancellare o riscrivere meglio per il livello

$$P(\rho,s)$$ 

$$d P = \left( \dfrac{\partial P}{\partial \rho} \right)_s \, d \rho + \left( \dfrac{\partial P}{\partial s} \right)_{\rho} \, ds $$

$$
\begin{cases}
  \dfrac{1}{c^2} \partial_t P + \rho_0 \partial_x u = 0 \\
  \rho_0 \partial_t u + \partial_x P = 0 \\
\end{cases}
$$

$$\dfrac{1}{c^2} \partial_{tt} P - \partial_{xx} P = 0$$


**Suono nello spazio.**

$$\dfrac{1}{c^2} \partial_{tt} P - \nabla^2 P = 0$$

(physics-hs:waves:equation:examples:fluids:surface)=
#### Onde su superficie libera


(physics-hs:waves:equation:examples:em)=
### Campo elettromagnetico

(physics-hs:waves:equation:solutions)=
## Soluzioni particolari

- Onde stazionarie
- Onde viaggianti

### Frequenza, lunghezza d'onda e relazione con velocità di propagazione della perturbazione

```{prf:definition} Frequenza
:label: wave-length

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

(physics-hs:waves:optics)=
## Ottica

**todo**
- Equazione delle onde per il campo EM

```{prf:definition} Indice di rifrazione
:label: refraction-index

L'indice di rifrazione $n_i$ di un materiale omogeneo è una proprietà del materiale che può essere definita come rapporto della velocità di propagazione della luce nel vuoto $c$ e nel materiale $c_i$,

$$n_i = \frac{c_0}{c_i} \ .$$

```

(physics-hs:waves:optics:geometric)=
### Ottica geometrica

**Approssimazione con raggi di luce.** I raggi luminosi sono qualitativamente delle linee geometriche che indicano la propagazione della luce. Essi possono essere definiti come delle curve perpendicolari in ogni punto ai fronti d'onda del campo elettromagnetico.

**todo** 
- *discutere approssimazione geometrica, con raggi luminosi; quando vale?*
- *aggiungere immagini per questa approssimazione: bridging EM field and geometrical optics, some examples: free space homogeneous medium; discontinuous medium; continuously varying in-homogeneous medium: miraggio e fata morgana*

(physics-hs:waves:optics:geometric:principles)=
#### Princìpi dell'ottica geometrica
**Propagazione rettilinea in un mezzo omogeneo.** In un mezzo omogeneo, con indice di rifrazione $n$ ({prf:ref}`refraction-index`) uniforme, i raggi luminosi si propagano su traiettorie rettilinee.

**Legge di Snell - riflessione e rifrazione tra mezzi discontinui.** Per soddisfare le condizioni di continuità del campo elettromagnetico in corrispondenza di una discontinuità di proprietà fisiche, un raggio che si propaga nel mezzo 1 e incidente su una discontinuità con il mezzo 2 con un angolo $\theta{1,i}$ con la direzione normale, in generale:
- viene riflesso con lo stesso angolo 

   $$\theta_{1,r} = \theta_{1,i}$$

- viene trasmesso con angolo $\theta_{2,t}$, tale che

   $$\frac{\sin \theta_{2,t}}{\sin \theta_{1,i}} = \dfrac{n_1}{n_2} = \dfrac{c_2}{c_1} \ .$$

**todo** *Stabilire i coefficienti di riflessione e trasmissione. Scrivere sezione in physics-electromagnetism*

**Riflessione totale.** Quando $\frac{c_2}{c_1} > 1$ esiste un angolo di incidenza limite oltre al quale non avviene trasmissione nel secondo mezzo. Il valore massimo della funzione $\sin$ è 1; la condizione limite, di riflessione totale si ottiene quando 

$$1 = \sin \theta_{2,t} = \frac{c_2}{c_1} \sin \theta_{1,i} \qquad \rightarrow \qquad $$


(physics-hs:waves:optics:geometric:lenses)=
#### Lenti


