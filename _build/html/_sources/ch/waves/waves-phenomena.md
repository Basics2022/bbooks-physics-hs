(physics-hs:waves:phenomena)=
# Caratteristiche dei fenomeni ondulatori

**todo**
- necessità di segnali coerenti (es.laser, forzanti armoniche)?
- condizioni nelle quali è lecito aspettarsi la manifestazione dei seguenti fenomeni. Es. diffrazione quando un'onda incontra ostacoli di dimensioni "paragonabili" alla lunghezza d'onda della perturbazione...

(physics-hs:waves:effects:interference)=
## Interferenza

- distinguere tra PSCE di segnali, e pattern di interferenza che compare nel quadrato del segnale, spesso associato alle grandezze percepite con i sensi e/o misurate da strumenti di misura (es. intensità luminosa della radiazione elettromagnetica)

```{list-table}
:header-rows: 0
* - ![](../../media/psce-0.png)
* - ![](../../media/psce-1.png)
```

<span style="color:red">Studio sistematico della diffrazione, con esempi: di limite di Fresnel e Fraunhofer; limite di diffrazione; pattern di diffrazione in funzione della forma dell'apertura,...</span>

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

(physics-hs:waves:effects:reflection)=
## Riflessione

(physics-hs:waves:effects:refraction)=
## Rifrazione


(physics-hs:waves:effects:polarization)=
## Polarizzazione
- Onde sismiche S, shear, di taglio
- Onde EM

(physics-hs:waves:effects:doppler)=
## Effetto Doppler
Quando la sorgente e l'osservatore sono in moto relativo, la frequenza percepita dall'osservatore è diversa dalla frequenza emessa dalla sorgente. 

In questo paragrafo viene valutato solo l'effetto della propagazione 1-dimensionale di disturbi piani, lungo la direzione del moto relativo di sorgente e osservatore (ricevitore). Per evitare complicazioni algebriche e avere un problema risolvibile in forma chiusa senza troppe difficoltà, ci si limita al moto relativo uniforme.
Le leggi del moto di sorgente e osservatore sono rispettivamente,

$$\begin{aligned}
  x_s(t) & = x_{s,0} + v_s \, t \\
  x_r(t) & = x_{r,0} + v_r \, t \\
\end{aligned}$$

Il segnale emesso dalla sorgente  $A_s(t) = F \cos(\Omega_s t)$ si propaga come due [onde viaggianti](physics-hs:waves:equation:solutions:1d:travelling) in direzione opposta,

$$\begin{aligned}
  u(x,t) = \dots 
\end{aligned}$$
<!--
  & = \frac{1}{2} A\left(x-x_s(t_{ret})-c(t-t_{ret})\right) + \frac{1}{2} A\left(x-x_s(t_{ret})+c(t-t_{ret})\right) = \\
  & = \dots
& = \frac{1}{2} A\left(x-x_{s,0}-(c+v_s)t\right) \cdot H(x-x_s(t)-ct > 0) + \\
  & + \frac{1}{2} A\left(x-x_{s,0}+(c-v_s)t\right) \cdot H(x-x_s(t)+ct < 0) \ ,
-->

con la funzione $H(y) = 1$ per $y = \text{True}$, $H(y)=0$ se $y= \text{False}$ necessaria a limitare la soluzione al dominio di influenza.

Quando l'osservatore si trova a destra della sorgente, $x_r(t) > x_s(t)$ (**todo** ruolo di $t_{ret}$, onde d'urto,...) esso è raggiunto al tempo $t$ dalla parte di segnale che si propaga verso destra emesso nell'istante di tempo $t^+_{ret}$

$$\begin{aligned}
  c( t - t^+_{ret} ) 
  & = x_r(t) - x_s(t^+_{ret}) = \\ 
  & = v_r \, t  - v_s \, t^+_{ret} + x_{r,0} - x_{s,0} 
  \quad \rightarrow \quad t^+_{ret} = \frac{1- \frac{v_r}{c}}{1 - \frac{v_s}{c}} t - \frac{x_{r,0} - x_{s,0}}{c - v_s}
\end{aligned}$$

L'osservatore registra un segnale precedente emesso dalla sorgente uguale a

$$U_R(t) = u(x_r(t), t) = U_s( t_{ret}^+ ) = U_S \left( \frac{1- \frac{v_r}{c}}{1 - \frac{v_s}{c}} t - \frac{x_{r,0} - x_{s,0}}{c - v_s} \right) \ ,$$

quindi nel caso di segnale armonico, la pulsazione della frequenza registrata è

$$\Omega_r = \frac{1- \frac{v_r}{c}}{1 - \frac{v_s}{c}} \, \Omega_s$$ (eq:doppler:right:freq)

Quando l'osservatore si trova a sinistra della sorgente, $x_r(t) < x_s(t)$ (**todo** ruolo di $t_{ret}$, onde d'urto,...) esso è raggiunto al tempo $t$ dalla parte di segnale che si propaga verso sinistra emesso nell'istante di tempo $t^-_{ret}$

$$\begin{aligned}
  c( t - t^-_{ret} ) 
  & = - x_r(t) + x_s(t^-_{ret}) = \\ 
  & = - v_r \, t  + v_s \, t^-_{ret} - x_{r,0} + x_{s,0} 
  \quad \rightarrow \quad t^-_{ret} = \frac{1+ \frac{v_r}{c}}{1 + \frac{v_s}{c}} t - \frac{x_{s,0} - x_{r,0}}{c + v_s}
\end{aligned}$$

L'osservatore registra un segnale precedente emesso dalla sorgente uguale a

$$U_R(t) = u(x_r(t), t) = U_s( t_{ret}^- ) = U_S \left( \frac{1+ \frac{v_r}{c}}{1 + \frac{v_s}{c}} t - \frac{x_{s,0} - x_{r,0}}{c - v_s} \right) \ ,$$

quindi nel caso di segnale armonico, la pulsazione della frequenza registrata è

$$\Omega_r = \frac{1 + \frac{v_r}{c}}{1 + \frac{v_s}{c}} \, \Omega_s$$ (eq:doppler:left:freq)

<!--
$$f(x, t) = A_+(x-x_s(t_{ret}) - c(t-t_{ret}))$$
-->

<!--
<span style="color:red"> **todo** *Controllare formule e pulire presentazione.*
con $t_{ret}$ l'istante di tempo in cui è stato emesso il segnale dalla sorgente che raggiunge il punto $x$ nell'istante $t > t_{ret}$ (causalità)
</span>

$$\begin{aligned}
 | x - x_s(t_{ret}) | & = \quad  c (t - t_{ret}) \\
   x - x_s(t_{ret})   & = \pm c (t - t_{ret}) = \begin{cases} \quad c ( t-t_{ret} ) & , \quad x \ge x_s(t_{ret}) \\ - c ( t-t_{ret} ) & , \quad  x \le x_s(t_{ret}) \\ \end{cases}
\end{aligned}$$

<span style="color:red">
Nel caso di sorgente a velocità costante, $x_s(t) = x_{s,0} + v_s t$, e ricettore a velocità costante $x_r(t) = x_{r,0} + v_r t$.
</span>

$$\begin{aligned}
  x_r(t) -x_s(t_{ret}) & = \pm c ( t - t_{ret} ) \\
  x_{r,0} + v_r t - x_{s,0} - v_s t_{ret} & = \pm c ( t - t_{ret} ) \\
\end{aligned}$$


$$(v_s \mp c) t_{ret} = (v_r \mp c) t + x_{r,0} - x_{s,0}$$

$$t_{ret} = \dfrac{v_r \mp c}{v_s \mp c} t + \dfrac{x_{r,0} - x_{s,0}}{v_s \mp c}$$
-->

````{prf:example} Stima della velocità dell'ambulanza con effetto Doppler
:label: ex-doppler-ambulance-speed

Si conosce la temperatura ambiente, $T_a$, che permette di valutare la velocità di propagazione del suono, $c = \sqrt{\gamma R T}$. Mentre ci si trova per strada ad aspettare l'autobus, e stiamo giocando con il nostro smartphone con un'app che rende disponibili la misura della frequenza dei suoni ricevuti, sentiamo arrivare un'ambulanza.

Essendo a conoscenza dell'effetto Doppler, vogliamo stimare la velocità dell'ambulanza osservando la frequenza misurata del suono emesso dalla sirena dell'ambulanza mentre si sta avvicinando $f_1$ e mentre si sta allontanando da noi $f_2$. Si chiede quindi di:
1. stimare la velocità dell'ambulanza, $v$, rispetto alla strada
2. stimare la frequenza della sorgente, $f_0$
3. una volta nota la velocità dell'ambulanza e la frequenza del segnale emesso calcolati ai punti 1. e 2., stimare le frequenze misurate nei casi in cui:
    - non fossimo fermi rispetto alla strada, ma ci stessimo muovendo a un passo di $v_r = 1 \, m/s$ nella stessa direzione dell'ambulanza
    - fossimo fermi rispetto alla strada, ma ci fosse un vento uniforme con velocità $v_m = 3 \, m /s$ che soffia nella stessa direzione del moto dell'ambulanza

```{dropdown} Soluzione
:open:

(1-2) Supponiamo che l'ambulanza si muova da sinistra verso destra. 

**Ambulanza in avvicinamento.** 
Mentre l'ambulanza si avvicina a noi, veniamo raggiunti dalla parte disegnale che viaggia verso destra, $f(x - c t)$...Il segnale registrato ha una frequenza data dall'espressione {eq}`eq:doppler:right:freq`, con velocità dell'osservatore $v_r = 0 $

<!--
Il segnale misurato in $x_r$ al tempo $t$ è uguale al segnale emesso in $x_s$ al tempo $t_s = t - \frac{x_r - x_s(t)}{c}$, con $x_s(t) = x_{s,0} + v \, t$,
-->

$$f_1 = f^+_r = \frac{1}{1-\frac{v}{c}} \, f_s$$

**Ambulanza che si allontana.** Mentre l'ambulanza si allontana veniano raggiunti dalla parte di segnale che si muove verso sinistra, $f(x+ct)$...Il segnale registrato ha una frequenza data dall'espressione {eq}`eq:doppler:left:freq`, con velocità dell'osservatore $v_r = 0 $

$$f_2 = f^-_r = \frac{1}{1+\frac{v}{c}} \, f_s$$

Mettendo a sistema le due equazioni, si può calcolare la velocità dell'ambulanza e la frequenza della sirena

$$\begin{aligned}
 \left( 1 + \frac{v}{c} \right) f_2 = \left( 1 - \frac{v}{c} \right) f_1 \qquad & \rightarrow \qquad v = \dfrac{f_1 - f_2}{f_1 + f_2} \, c \\
  & \rightarrow \qquad f_s = \frac{2 f_1 f_2}{f_1 + f_2} \ .
\end{aligned}$$

(3) ...

```

````

````{prf:example} Effetto doppler in astronomia
:label: ex-doppler-astronomy

Si vuole determinare velocità della galassia **XXX** **todo** analizzando la radiazione elettromagnetica emessa dalla galassia che arriva sulla Terra. Nello spettro di emissione si riconosce la linea $H-\alpha$, legata alla presenza di idrogeno ionizzato, e a una transizione di un $e^-$ di un atomo di $H$ dal livello di energia $n=3$ al livello di energia $n=2$.

Queta riga spettrale è associata a una lunghezza d'onda $\lambda^0_{H\alpha} = 656.46 \, nm$ nel vuoto, e quindi $f^0_{H\alpha} = ...$, in un sistema in quiete relativa.

Nello spettro misurato si riconosce la linea $H\alpha$ con una lunghezza d'onda $\lambda = 659.5 \, nm$. (Virgo cluster)

Si chiede di:
1. calcolare la velocità radiale usando le formule per l'effetto Doppler non relativistico
2. valuatere l'errore commesso usando le formule dell'effetto Doppler non relativistico, rispetto all'uso delle formule che tengono conto degli effetti relativistici

  $$\lambda_{r} = \lambda_e \sqrt{\frac{1 + v/c}{1-v/c}}$$

Il rapporto,

$$z = \frac{\lambda_r - \lambda_e}{\lambda_e}$$ 

viene definito **red-shift**, o **spostamento verso il rosso**, come sarà più chiaro nella discussione dello [spettro elettromagnetico]()

```{dropdown} Soluzione

```

````


<!--
$$x - x_{s,0} - v_s t_{ret} = c \left( t - t_{ret} \right)$$

$$t_{ret} = \dfrac{c}{c - v_s} t - \dfrac{x - x_{s,0}}{c}$$
-->
