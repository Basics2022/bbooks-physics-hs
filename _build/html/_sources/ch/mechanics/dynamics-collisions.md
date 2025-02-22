(physics-hs:mechanics:dynamics:collisions)=
# Collisioni

Una descrizione dettagliata delle collisioni tra sistemi qualsiasi va ben al di là dello scopo di un primo approccio alla meccanica.

Qui, ci si limiterà allo studio di collisioni che:
- possono essere caratterizzate unicamente da un *coefficiente di ritorno*, $\varepsilon$ **todo**
- avvengono in intervalli di tempo ridotti, al limite nulli

Questi urti comportano delle variazioni finite delle quantità dinamiche in intervalli di tempo finiti, vengono definiti **urti impulsivi** (**todo** *verificare*) e  rappresentano un esempio di moto "non regolare", per il quale le equazioni cardinali della dinamica devono essere scritte in forma incrementale.

**todo** *approfondimento su forze impulsive e delta di Dirac?*

Tra due istanti temporali immediatamente precedente e immediatamente successivo all'urto tra due sistemi possono essere trascurate tutte le azioni agenti sul sistema complessivo tranne quelle **impulsive** dovute all'**urto**, e ad eventuali **reazioni vincolari** (vedi esercizi),

$$\begin{aligned}
  \vec{I}^{ext}   & = \Delta \vec{Q} \\
  \vec{J}_H^{ext} & = \Delta \vec{\Gamma}_H + \Delta \vec{x}_H \times \vec{Q} = \Delta \vec{\Gamma}_{H} \\
  L^{ext} + L^{int} & = \Delta K \ ,
\end{aligned}$$

con $\vec{I}^{ext}$ l'impulso delle forze esterne durante l'urto, $\vec{J}^{ext}$ l'impulso dei momenti esterni durante l'urto, $L^{ext}$, $L^{int}$ il lavoro delle forze esterne e interne durante l'urto.

E' bene osservare che in assenza di forze e momenti impulsivi esterni - anche dovuti a eventuali vincoli - ai due sistemi che collidono, la quantità di moto e il momento della quantità di moto del sistema complessivo si conservano in un urto.
Al contrario, in generale, l'**energia cinetica non si conserva** poiché dipende anche dal lavoro delle azioni interne che includono quelle impulsive scambiate durante l'urto.

Il **coefficiente di restituzione** $\varepsilon \in [0, 1]$ caratterizza il tipo di urto e ha una facile interpretazione se l'urto viene studiato usando un sistema di riferimento con orgine il centro di massa del sistema, $Q$. Le quantità riferite a questo sistema vengono indicate qui con l'apice.

Poiché si è scelto come riferimento il centro di massa, in assenza di forze implusive esterne,

$$\vec{0} = {\vec{p}^-}  = {\vec{p}^+} $$

$$\vec{0} = {\vec{p}^-}  = {\vec{p}_1^-}  + {\vec{p}_2^-} $$

$$\vec{0} = {\vec{p}^+}  = {\vec{p}_1^+}  + {\vec{p}_2^+} $$

<span style="color:red">**todo** *distinguere tra componente normale e tangenziale*</span>

Il coefficiente di restituzione viene definito come l'opposto del rapporto tra <span style="color:red">il valore assoluto (**todo** dovrebbe essere la componente normale, assumento che la componente tangenziale si conservi - oppure trovare anche un modello per la componente tangenziale, dovuta ad attrito)</span> della quantità di moto di uno dei due corpi dopo e prima dell'urto,

$$\varepsilon := - \frac{|{\vec{p}_1^{+ '}}   |}{|{\vec{p}_1^{- '}}  |} = - \frac{{|\vec{p}_2^{+ '}} |}{|{\vec{p}_2^{- '}} |}$$

In termini di energia cinetica, nel sistema di riferimento del centro di massa


$$\begin{aligned}
{K^{+ '}} & = \frac{1}{2 m_1} {\vec{p}_1^{+ '}}  \cdot {\vec{p}_1^{+ '}}  + \frac{1}{2 m_2} {\vec{p}_2^{+ '}}  \cdot {\vec{p}_2^{+ '}}  = \\
       & = \varepsilon^2 \left[ \frac{1}{2 m_1} {\vec{p}_1^{- '}}  \cdot {\vec{p}_1^{- '}}  + \frac{1}{2 m_2} {\vec{p}_2^{- '}}  \cdot {\vec{p}_2^{- '}}  \right] = \varepsilon^2 {K^{- '}} 
\end{aligned}$$

## Problemi

**todo** Aggiungere pendolo di Newton

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione tra blocchi su piano orizzontale liscio
:columns: 8

Date le masse di due blocchi che scivolano su un piano orizzontale liscio, e le velocità iniziali dei due blocchi, e il coefficiente di restituzione dell'urto, viene chiesto di determinare le velocità dei due blocchi dopo l'urto.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-1d.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.

La posizione e la velocità del centro di massa del sistema sono

$$\begin{aligned}
  x_C & = \frac{x_1 m_1 + x_2 m_2}{m_1 + m_2} \\
  v_C & = \frac{m_1}{m_1+m_2} \dot{x}_1 + \frac{m_2}{m_1+m_2} \dot{x}_2  \\
\end{aligned}$$

In assenza di forze esterne parallele alla parete, la velocità del centro di massa del sistema è costante.
L'energia cinetica nel sistema di riferimento del centro di massa prima e dopo l'urto vale

$$\begin{aligned}
  K_- 
  & = \frac{1}{2} m_1 (\dot{x}_1 - v_C)^2 + \frac{1}{2} m_2 (\dot{x}_2 - v_C)^2 = \\
  & = \frac{1}{2} m_1 \left( \frac{m_2}{m_1+m_2} (\dot{x}_1 - \dot{x}_2) \right)^2 + \frac{1}{2} m_2 \left( \frac{m_1}{m_1+m_2} (\dot{x}_2 - \dot{x}_1) \right)^2 = \\
  & = \frac{1}{2} m_1 m_2 \frac{m_1 + m_2}{(m_1 + m_2)^2} (\dot{x}_1 - \dot{x}_2)^2 = \\
  & = \frac{1}{2} \frac{ m_1 m_2}{m_1 + m_2} (\dot{x}_1 - \dot{x}_2)^2 \ .
\end{aligned}$$

...

In termini di velocità relative

$$\begin{cases}
  0 = \mu_1 \dot{x}'_{1,-} + \mu_2 \dot{x}'_{2,-} = \mu_1 \dot{x}'_{1,+} + \mu_2 \dot{x}'_{2,+} \\
  \varepsilon^2 \left( \frac{1}{2} \mu_1 \dot{x}^{'2}_{1,-} + \frac{1}{2} \mu_2 \dot{x}^{'2}_{2,-} \right) = \frac{1}{2} \mu_1 \dot{x}^{'2}_{1,+} + \frac{1}{2} \mu_2 \dot{x}^{'2}_{2,+}
\end{cases}$$

Dalla prima

$$\dot{x}'_{2,+} = - \frac{\mu_1}{\mu_2} \dot{x}'_{1,+} $$

e quindi 

$$\frac{1}{2} \left( \mu_1 + \mu_2 \left( \frac{\mu_1}{\mu_2} \right)^2 \right) \dot{x}^{'2}_{1,+} = \varepsilon^2 K'_-$$

$$\begin{aligned}
  \dot{x}_{1,+} & = \mp \sqrt{ \frac{2 \varepsilon^2 K'_-}{ \mu_1 \left( 1 + \frac{\mu_1}{\mu_2} \right)} } \\
  \dot{x}_{2,+} & = \pm \sqrt{ \frac{2 \varepsilon^2 K'_-}{ \mu_2 \left( 1 + \frac{\mu_2}{\mu_1} \right)} } \\
\end{aligned}$$

poiché

$$
  \dot{x}_{2,+}
    = - \frac{\mu_1}{\mu_2} \dot{x}_{1,+} 
    = \pm \frac{\mu_1}{\mu_2} \sqrt{ \frac{2 \varepsilon^2 K'_-}{ \mu_1 \left( 1 + \frac{\mu_1}{\mu_2} \right)} }
    = \pm \sqrt{ \frac{2 \varepsilon^2 K'_-}{ \frac{\mu_2^2}{\mu_1} \left( 1 + \frac{\mu_1}{\mu_2} \right)} } 
    = \pm \sqrt{ \frac{2 \varepsilon^2 K'_-}{ \mu_2 \left( 1 + \frac{\mu_2}{\mu_1} \right)} } 
$$

```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione tra blocchi su piano orizzontale scabro
:columns: 8

Date le masse di due blocchi che scivolano su un piano orizzontale scabro, le velocità e la distanza iniziale tra i due blocchi, il coefficiente di restituzione dell'urto, il coefficiente di attrito dinamico $\mu^d$ tra i due blocchi e il piano orizzontale, viene chiesto di determinare:
- le condizioni affinché avvenga l'urto
- in caso di urto:
  - le velocità immediatamente dopo l'urto
  - la posizione finale delle due masse

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-1d-friction.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
**todo**
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Rimbalzo di una palla
:columns: 8

Dato il coefficiente di restituzione degli urti tra la palla di massa $m_1$ nota e il piano orizzontale, viene chiesto di determinare la distanza verticale percorsa dalla palla durante i rimbalzi.

**Oss.** Il numero di rimbalzi è infinito, ma il risultato si ottiene da una serie infinita convergente.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-bouncing-ball.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.

Il caso di urto contro una parete rigida fissa può essere rappresentato considerando il centro di massa dei corpi in urto coincidente con la parete fissa (come se calcolassimo l'urto tra palla e pianeta Terra. Non dovrebbe essere difficile immaginare - e calcolare - che l'urto di una palla di massa dell'ordine del chilogrammo non influenzi in maniera significativa lo stato della Terra).

Il moto è "conservativo a tratti" tra due urti consecutivi. Per ogni urto, vale la relazione

$$K_+ = \varepsilon^2 K_- \ ,$$

per l'energia cinetica prima e dopo ogni urto, $K_-$ e $K_+$ rispettivamente.

Partendo in quiete da una quota $h$, l'energia meccanica del sistema prima del primo urto vale

$$E_0 = m g h_0 \ .$$

L'energia meccanica dopo l'$n$-esimo urto vale

$$E_n = E_0 \varepsilon^{2n} \ .$$

La quota massima raggiunta dopo l'$n$-esimo urto vale

$$h_n = \frac{E_n}{mg} = \frac{E_0}{mg} \varepsilon^{2n} = h_0 \varepsilon^{2n} \ .$$

La distanza verticale coperta dalla palla fino all'$N$-esimo urto è

$$S_N = h_0 + \sum_{n=1}^{N} 2 \, h_n = h_0 \left( 1 + \sum_{n=1}^N \varepsilon^{2n} \right) \ .$$

La somma vale

$$S_N = h_0 \left( 1 + 2 \, \frac{1 - \varepsilon^{2(N+1)}}{1-\varepsilon^{2}} \right) \ .$$

Per il numero di rimbalzi che tende all'infinito, se $\varepsilon < 1$ la serie è una **serie geometrica convergente** e la palla compie la distanza finita

$$S = h_0 \left( 1 + \frac{2}{1-\varepsilon^{2}} \right) \ .$$


```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione di un sistema massa-molla con una parete
:columns: 8

Data la configurazione iniziale del sistema massa-molla, con lunghezza a riposo nulla $\ell_0$ e allungamento iniziale $x_0$, viene chiesto di descrivere l'evoluzione del sistema in funzione del coefficiente di restituzione $\varepsilon$ degli urti tra la massa e la parete rigida verticale. In particolare, si chiede di distinguere il caso di urto elastico dai casi di urto parzialmente elastico.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-bouncing-block-spring.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
**todo**
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisioni tra due blocchi e una parete rigida
:columns: 8

Nel caso di urti perfettamente elastici tra i due blocchi e con la parete, viene chiesto di determinare il numero di urti tra i due blocchi.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-bouncing-blocks.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
**todo**
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Proiettile su pendolo con massa concentrata
:columns: 8

Un proiettile colpisce un pendolo. In funzione del coefficiente di restituzione $\varepsilon$, viene chiesto di determinare:
- le condizioni immediatamente successive all'urto
- l'energia meccanica dissipata nell'urto
- l'angolo massimo raggiunto dal pendolo

Si calcolino poi le reazioni vincolari a terra, prima, durante e dopo l'urto.

Si analizzi inizialmente il caso di urto anelastico.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-pendulum-0.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.

**Urto anelastico.** Nel caso di urto anelastico, il proiettile di massa $m$ rimane incastrato nella massa $M$. Usando il bilancio del momento della quantità di moto rispetto alla cerniera per confrontare le due condizioni prima e dopo l'urto, in assenza di reazioni impulsive che hanno momento non nullo rispetto alla rotazione attorno alla cerniera, si ha:

$$\Delta L_H = 0 \quad \rightarrow \quad m v^- L = (m+M) v^+ L \ ,$$

e quindi 

$$\begin{aligned}
   v^+            & = \frac{1}{1+ \frac{M}{m}} v^-  \\
   \dot{\theta}^+ & = \frac{1}{1+ \frac{M}{m}} \frac{v^-}{L}  
\end{aligned}$$

L'energia meccanica dissipata nell'urto è uguale alla differenza di energia cinetica, poiché non ci sono variazioni finite impulsive di energia potenziale,

$$\begin{aligned}
  \Delta E = \Delta K 
  & = \frac{1}{2} m v_-^2 - \frac{1}{2} (m + M) v_+^2 = \\
  & = \frac{1}{2} m v_-^2 - \frac{1}{2} (m + M) \frac{m^2}{(m+M)^2} v_-^2 = \\
  & = \frac{1}{2} m v_-^2 \left[ 1 - \frac{m}{m+M} \right] = \\
  & = \frac{1}{2} m v_-^2 \frac{1}{1+\frac{m}{M}} \ .
\end{aligned}$$

Dall'istante successivo all'urto, il sistema è conservativo. E' possibile quindi calcolare la quota massima raggiunta dal pendolo dalla conservazione dell'energia meccanica,

$$E = \frac{1}{2} (m+M) |\vec{v}|^2 + (m+M) g h \ .$$

Scegliendo la quota di riferimento per l'energia potenziale nel punto più basso della traiettoria, e riconoscendo che nel punto più alto la velocità del sistema è nulla, si possono confrontare le due condizioni 1) subito dopo l'urto e 2) nel punto di altezza massima

$$\frac{1}{2} (m+M) L^2 \dot{\theta}_1^2 = (m + M) g h_2 \ ,$$

per trovare

$$h_2 = \frac{1}{2} \frac{L^2 \dot{\theta}_1^2}{g} \ .$$





```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Proiettile su pendolo con massa distribuita
:columns: 8

Un proiettile colpisce un pendolo. In funzione del coefficiente di restituzione $\varepsilon$, viene chiesto di determinare:
- le condizioni immediatamente successive all'urto
- l'angolo massimo raggiunto dal pendolo.

Si calcolino poi le reazioni vincolari a terra, prima, durante e dopo l'urto.

Si analizzi inizialmente il caso di urto anelastico.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-pendulum-1.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.

**Urto anelastico.** Nel caso di urto anelastico, il proiettile di massa $m$ rimane incastrato nella massa $M$. Usando il bilancio del momento della quantità di moto rispetto alla cerniera per confrontare le due condizioni prima e dopo l'urto, in assenza di reazioni impulsive che hanno momento non nullo rispetto alla rotazione attorno alla cerniera, si ha:

$$\Delta L_H = 0 \quad \rightarrow \quad m v^- L = m v^+ L + \frac{1}{3} M L^2 \dot{\theta} = \left( m + \frac{1}{3} M \right) L v_+ \ ,$$

e quindi 

$$\begin{aligned}
   v^+            & = \frac{1}{1+ \frac{1}{3} \frac{M}{m}} v^-  \\
   \dot{\theta}^+ & = \frac{1}{1+ \frac{1}{3} \frac{M}{m}} \frac{v^-}{L}  
\end{aligned}$$

L'energia meccanica dissipata nell'urto è uguale alla differenza di energia cinetica, poiché non ci sono variazioni finite impulsive di energia potenziale,

$$\begin{aligned}
  \Delta E = \Delta K 
  & = \frac{1}{2} m v_-^2 - \left[ \frac{1}{2} m v_+^2 + \frac{1}{2} \frac{1}{3} M L^2 \dot{\theta}_+^2 \right]= \\
  & = \frac{1}{2} m v_-^2 - \frac{1}{2} \left( m + \frac{1}{3}M \right) \frac{1}{\left( 1 + \frac{1}{3}\frac{M}{m} \right)^2} v_-^2 = \\
  & = \frac{1}{2} m v_-^2 \left[ 1 - \frac{m}{m+ \frac{1}{3} M} \right] = \\
  & = \frac{1}{2} m v_-^2 \frac{1}{1 + 3\frac{m}{M}} \ .
\end{aligned}$$

Dall'istante successivo all'urto, il sistema è conservativo. E' possibile quindi calcolare la quota massima raggiunta dal pendolo dalla conservazione dell'energia meccanica,

$$\begin{aligned}
  E & = \frac{1}{2} m |\vec{v}|^2 + \frac{1}{2} \frac{1}{3} M L^2 \dot{\theta}^2 + \left(m + \frac{M}{2} \right) g h \\
    & = \left( \frac{1}{2} m + \frac{1}{6} M \right) L^2 \dot{\theta}^2 + \left( m + \frac{M}{2} \right) g h \\
\end{aligned}.$$

**todo** Aggiungere qualche parola sull'espressione dell'energia potenziale, che potrebbe essere scritta come 

$$m g h + M g \left(-\frac{R}{2} + \frac{h}{2} \right)$$

Scegliendo la quota di riferimento per l'energia potenziale nel punto più basso della traiettoria, e riconoscendo che nel punto più alto la velocità del sistema è nulla, si possono confrontare le due condizioni 1) subito dopo l'urto e 2) nel punto di altezza massima

$$\left( m + \frac{M}{2} \right) g h_2 = \left( \frac{1}{2} m + \frac{1}{6} M \right) L^2 \dot{\theta}_1^2 \ ,$$

per trovare

$$h_2 = \frac{\left(\frac{1}{2} m + \frac{1}{6} M \right) L^2 \dot{\theta}_1^2 }{\left( m + \frac{M}{2} \right) g} \ .$$

```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Proiettile su bersaglio di poligono di tiro
:columns: 8

Un proiettile colpisce il bersaglio di un poligono, inizialmente appoggiato alla parete verticale. In funzione del coefficiente di restituzione $\varepsilon$, viene chiesto di determinare:
- le condizioni immediatamente successive all'urto
- la velocità minima del proiettile prima dell'urto che garantisce di abbattere il bersaglio.

Si calcolino poi le reazioni vincolari a terra, prima, durante e dopo l'urto.

Si analizzi inizialmente il caso di urto anelastico.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-pendulum-2.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.

**Urto anelastico.** Usando il bilancio della quantità di moto in direzione orizzontale e il bilancio del momento della quantità di moto rispetto alla cerniera,

$$\begin{cases}
  - m v_-   + ( M + m ) L   \dot{\theta}_+ = I_{A,x} + I_{B,x} \\
  - m L v_- + ( M + m ) L^2 \dot{\theta}_+ = I_{B,x} \ell \qquad \text{if $I_{B,x} > 0$, else $I_{B,x} = 0$}  \\
\end{cases}$$

**todo**

```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione su sistema libero rigido di masse concentrate
:columns: 8

Un proiettile colpisce un sistema rigido di due masse concentrate, libero e inizialmente in quiete. Si chiede di determinare il moto dei sistemi dopo l'urto, in funzione del coefficiente di restituzione.

Si analizzi inizialmente il caso di urto anelastico.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-rod-1.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
**Urto anelastico.** Usando il bilancio della quantità di moto in direzione orizzontale e il bilancio del momento della quantità di moto, con il vincolo cinematico imposto dalla condizione di urto anelastico, si ricavano le condizioni

$$\begin{cases}
 m v_- = M ( \dot{x} + \frac{L}{2} \dot{\theta}) + M ( \dot{x} - \frac{L}{2} \dot{\theta}) +  m ( \dot{x} + \frac{L}{2} \dot{\theta}) \\
   0   = M L ( \dot{x} - \frac{L}{2} \dot{\theta}) \ .
\end{cases}$$

e quindi

$$\dot{x} = \frac{1}{2} L \dot{\theta}$$
$$m v_- = (M + m)  L \dot{\theta}$$

e **se** $m \ne 0$,

$$\begin{cases}
  \dot{\theta} = \frac{1}{1 + \frac{M}{m}} \frac{v_-}{L} \\
  \dot{x}      = \frac{1}{2} \frac{1}{1 + \frac{M}{m}} v_-
\end{cases}$$



```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione su sistema libero rigido a massa distribuita
:columns: 8

Un proiettile colpisce un sistema rigido di due masse concentrate, libero e inizialmente in quiete. Si chiede di determinare il moto dei sistemi dopo l'urto, in funzione del coefficiente di restituzione.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-rod-2.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
**todo**
```
