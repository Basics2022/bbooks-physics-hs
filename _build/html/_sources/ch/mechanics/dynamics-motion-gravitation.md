```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```

(physics-hs:mechanics:dynamics:motion:gravitation)=
# Gravitazione

<!--
- legge di gravitazione universale
- problema dei due corpi
  - trattazione
  - applicazioni:
    - velocità cosmiche (1a e 3a con grafico energia meccanica; 2a: velocità di fuga)
    - lanciatori, multi-stadio:
      - Tsiolkovski (formula della spinta; esercizio per sistemi aperti), Goddard, Oberth
      - W.von Braun: dalla Germania nazista, al programma spaziale NASA
    - progettazione orbitale: satelliti geostazionari; trasferimento di Hohmann; fionda gravitazionale
- problema dei 3 corpi:
  - punti lagrangiani. Esempio: telescopio Webb
-->

## Legge di gravitazione universale
$$\vec{F}_{10} = G \, m_0 \, m_1 \frac{\vec{r}_{01}}{\left|\vec{r}_{01}\right|^3}$$

## Problema dei due corpi

In meccanica classica, il problema dei due corpi si riferisce alla dinamica di un sistema formato da due corpi puntiformi soggetti unicamente alla mutua interazione gravitazionale, descritta dalla legge di gravitazione universale di Newton.

Il sistema formato dai due punti è un sistema chiuso e isolato, sul quale non agiscono azioni esterne. La quantità di moto rispetto a un sistema di riferimento inerziale rimane quindi costante. Rimane quindi costante la velocità del centro di massa $G$,

$$G = \frac{m_0 \, P_0 + m_1 \, P_1}{m_0 + m_1} \ ,$$

ed è possibile definire un sistema di riferimento inerziale con origine nel centro di massa del sistema. Il raggio vettore tra i due corpi può quindi essere riscritto,

$$P_1 - G = P_1 - \frac{m_0 \, P_0 + m_1 \, P_1}{m_0 + m_1} = \frac{ - m_0 \, P_0 + m_0 \, P_1}{m_0 + m_1} = \frac{m_0}{m_0 + m_1}(P_1 - P_0) \ .$$

L'equazione del moto per il corpo $1$ nel sistema di riferimento inerziale con origine in $G$ segue il secondo principio della dinamica. L'equazione del moto può essere scritto in termini del raggio vettore tra corpo $1$ e centro di massa,

$$\begin{aligned}
  m_1 \dfrac{d^2}{dt^2}(P_1-G) & = - G m_0 m_1 \frac{P_1 - P_0}{|P_1 - P_0|^3} = \\
                               & = - G \dfrac{(m_0 + m_1)^2}{m_0} m_1 \frac{P_1 - G}{|P_1 - G|^3} 
\end{aligned}$$

o in termini del raggio vettore tra i due corpi $P_1 - P_0$

$$
  \frac{m_0 m_1}{m_0 + m_1} \dfrac{d^2}{dt^2}(P_1-P_0) = - G m_0 m_1 \frac{P_1 - P_0}{|P_1 - P_0|^3} 
$$
$$
  m_1 \dfrac{d^2}{dt^2}(P_1-P_0) = - G ( m_0 + m_1 ) m_1 \frac{P_1 - P_0}{|P_1 - P_0|^3} 
$$

Le equazioni del moto in questi due sistemi di riferimento possono essere scritte nella forma

$$m_1 \, \ddot{\vec{r}} = - G M m_1 \frac{\vec{r}}{r^3} \ .$$

### Traiettorie, coniche, ed energia

E' possibile dimostrare che il moto di ognuno dei due corpi è un moto piano, e che la traiettoria avviene descrive una conica.

- **todo** Dimostrare che il moto è piano
- **todo** Dimostrare che la traiettoria è una conica

Il tipo di curva conica dipende da una grandezza scalare che può essere ricondotta a un'energia. Il prodotto scalare della velocità $\dot{\vec{r}}$ con l'equazione del moto, permette di ricavare un principio di conservazione dell'energia,

$$\begin{aligned}
  0 & = \dot{\vec{r}} \cdot \left( m \ddot{\vec{r}} + G M m \frac{\vec{r}}{r^3} \right) = \\
    & = \dfrac{d}{dt} \left( \frac{1}{2} m \left|\dot{\vec{r}}\right|^2 - G M m \frac{1}{r}\right) = \dfrac{d E^{mec}}{dt}
\end{aligned}$$

Usando il sistema di coordinate polari, e la costanza della velocità angolare $\Omega = \frac{1}{2}{r^2}{\dot{\theta}}$, si può scrivere

$$\begin{aligned}
  \frac{E^{mec}}{m} & = \frac{1}{2} \dot{r}^2 + \frac{1}{2} r^2 \dot{\theta}^2 - \frac{G M}{r} = \\
                    & = \frac{1}{2} \dot{r}^2 + 2 \frac{\Omega^2}{r^2} - \frac{G M}{r} = \\
                    & = \frac{1}{2} \dot{r}^2 + v_r(r) \ .
\end{aligned}$$

Poiché $\frac{1}{2}\dot{r}^2 \ge 0$, il moto è possibile per tutti i valori di $r$ tali che $\frac{E}{m} \ge v_r(r)$. Il valore di $E$ identifica le traiettorie. **todo** *aggiungere grafici*
- esiste un valore minimo di $E$: questo valore è associato a un'orbita circolare
- per $E_{min} \le E \le 0$ esistono due soluzioni dell'equazione $\frac{E}{m} - v_r(r) = 0$: orbite chiuse, ellittiche o circolari (per $E = E_{min}$)
- $E = 0$ è un caso limite che separa le orbite chiuse e le orbite aperte: a $E = 0$ è associata un'orbita parabolica
- per $E > 0$ le orbite aperte sono iperboliche


### Traiettorie chiuse e leggi di Keplero

**Prima legge.** Un pianeta descrive un'orbita ellittica attorno al Sole, che si trova in uno dei due fuochi.

**Seconda legge legge.** Considerando l'area descritta dal moto del pianeta attorno al Sole, la velocità angolare è costante lungo la traiettoria.

**Terza legge.** In un sistema di pianeti, il quadrato del periodo delle orbite descritte dai pianeti è proporzionale al cubo del semiasse maggiore della traiettoria, $T^2 \propto a^3$.


<span style="color:red">**todo** rispetto a quale sistema di riferimento? Serve l'approssimazione che la massa del Sole sia $>>$ delle masse dei pianeti, se si considera inerziale un sistema di coordinate con origine nel Sole? O bisogna/si può usare un sistema inerziale con origine nel centro di massa del sistema (considerato isolato)</span>

**Moto piano.** Siano $\vec{r}$, $\vec{v}$ la posizione e la velocità del pianeta rispetto al Sole. La forza di gravità agente sul pianeta è

$$\vec{F} = - G M m \frac{\vec{r}}{r^3} \ .$$

E' facile dimostrare che il moto è piano, cioè che la posizione e la velocità del pianeta sono sempre ortogonali a una direzione costante.

$$\frac{d}{dt} \left( \vec{r} \times \vec{v} \right) = \underbrace{\vec{v} \times \vec{v}}_{=\vec{0}} + \vec{r} \times \vec{a}  = - G M m \underbrace{\vec{r} \times \frac{\vec{r}}{r^3}}_{=\vec{0}} = \vec{0} \ .$$

Poiché il vettore $\vec{r} \times \vec{v} =: \frac{L}{m} \hat{k}$ è costante, è costante sia il suo valore assoluto sia la sua direzione: affinché $\vec{r} \times \vec{v}$ sia allineato con $\hat{k}$, i vettori $\vec{r}$, $\vec{v}$ devono essere ortogonali a $\hat{k}$.

**Coordinate polari.** Per descrivere il moto piano di un punto, si può usare un sistema di coordinate 2-dimensionale. Si sceglie un sistema di coordinate polari con origine coincidente con il Sole. La posizione del pianeta è identificata dal raggio vettore

$$\vec{r} = r \, \hat{r} \ ,$$

e la derivate dei versori radiale e azimuthale valgono

$$\begin{aligned}
\dot{\hat{r}}      & =   \dot{\theta} \hat{\theta} \\
\dot{\hat{\theta}} & = - \dot{\theta} \hat{r} \\
\end{aligned}$$

La posizione, la velocità e l'accelerazione del pianeta possono essere scritte come

$$\begin{aligned}
\vec{r} & = r \, \hat{r} \\
\vec{v} & = \dot{r} \, \hat{r} + r \dot{\theta} \, \hat{\theta} \\
\vec{a} & = \left[ \ddot{r} - r \dot{\theta}^2 \right] \, \hat{r} +  \left[ 2 \dot{r} \dot{\theta} + r \ddot{\theta} \right] \, \hat{\theta}  \\
\end{aligned}$$

La **velocità areolare**, $\vec{\Omega} = \frac{1}{2} \vec{r} \times \vec{v} $ è costante e uguale a 

$$\vec{\Omega} = \frac{1}{2} \frac{L}{m} \hat{k} = \frac{1}{2} r^2 \dot{\theta} \, \hat{k} \ .$$

<!--
Il **periodo** $T$

$$T = \frac{A}{\Omega} = \frac{\pi \, a \, b}{\Omega} \ .$$
-->

Dall'espressione della velocità angolare costante, si può ricavare il legame tra $\dot{\theta}$ ed $r$,

$$\dot{\theta} = \frac{\Omega}{r^2} \ .$$

Usando le coordinate polari, l'equazione del moto $m \ddot{\vec{r}} = -G M m \frac{\vec{r}}{r^3}$ viene scritta in componenti,

$$\begin{aligned}
r      & : \ m (\ddot{r} - r\dot{\theta}^2) = - G M m \frac{1}{r^2} \\
\theta & : \ m ( 2 \dot{r} \dot{\theta} + r \ddot{\theta}^2 ) = 0
\end{aligned}$$

**Traiettoria, $r(\theta)$.**
Inserendo l'espressione $\dot{\theta} = \frac{\Omega}{r^2}$ nella componente radiale, e definendo la funzione $z = \frac{1}{r}$, le derivate nel tempo della coordinata radiale possono essere riscritte come

$$\dot{r} = -\frac{1}{z^2}\frac{d z}{d \theta} \dot{\theta} = -\Omega \frac{dz}{d\theta} $$

$$\ddot{r} = \dot{\theta} \frac{d}{d \theta} \left( - \Omega \frac{dz}{d \theta} \right) = - z^2 \Omega^2 z''(\theta)$$

e la componente radiale dell'equazione di moto,

$$-z^2 \Omega^2 z'' - z^3 \Omega^2 = - G M z^2$$
$$ z'' + z  = \frac{G M}{\Omega^2}$$

$$z(\theta) = \frac{G M}{\Omega^2} + A \cos(\theta) + B \sin(\theta) \ .$$

e quindi

$$r(\theta) = \frac{\Omega^2}{G M}\frac{1}{1 + A \dfrac{\, \Omega^2}{GM} \cos \theta + B \dfrac{\, \Omega^2}{GM} \sin \theta}$$

Scelta della direzione di riferimento: direzione del perielio: $r(\theta=0) = \min r$, $B = 0$,

Scelte diverse si ottengono da una trasformazione di coordinate con una rotazione dell'asse di riferimento: $\theta_1 = \theta - \theta_0$, e quindi

$$r(\theta) = \frac{\Omega^2}{GM}\frac{1}{1 + \frac{A\Omega^2}{GM} \cos \theta} = \frac{\Omega^2}{GM}\frac{1}{1 + \frac{A\Omega^2}{GM} \cos (\theta_1 + \theta_0 )} = \frac{\Omega^2}{GM}\frac{1}{1 + \underbrace{\frac{A\Omega^2}{GM} \cos \theta_0}_{= A_1} \cos \theta_1 \underbrace{- \frac{A \Omega^2}{GM} \sin \theta_0}_{= B_1} \sin \theta_1 }$$

Il confronto con l'equazione delle coniche in coordinate polari, permette di riconoscere l'eccentricità, $e$ e il prodotto $e \, D$ dell'eccentricità per la distanza $D$ tra fuoco e direttrice,

$$e = \frac{A \Omega^2}{GM} \qquad , \qquad e \, D = \frac{\Omega^2}{GM}$$

$$r(\theta) = \frac{\Omega^2}{GM}\frac{1}{1 + \frac{A\Omega^2}{GM} \cos \theta}$$
$$r(\theta) = \frac{e \, D}{1 + e \, \cos \theta}$$



<!--
$$e = - \frac{A \Omega^2}{GM}$$
$$e D = \frac{\Omega^2}{GM}$$
$$D= -\frac{1}{A}$$

$$c = \frac{e^2}{1-e^2} D$$
$$a = \frac{c}{e} = \frac{e}{1-e^2} D$$
$$b = \sqrt{a^2 - c^2} = \sqrt{\frac{1 - e^2}{e^2}} c = \sqrt{\frac{1 - e^2}{e^2}}  \frac{e^2}{1-e^2} D = \frac{e D}{\sqrt{1-e^2}} = a \, \sqrt{1-e^2} $$
-->

Poiché la velocità areolare è costante, il periodo dell'orbita è uguale al raggporto tra l'area dell'ellisse e la velocità areaolare,

$$T = \frac{\pi a b}{\Omega} = \pi \frac{a^2 \sqrt{1-e^2}}{\Omega} = $$

$$1-e^2 = 1 - \left(\frac{A \Omega^2}{GM} \right)^2 = \frac{\Omega^2}{GM \, a} $$

$$\rightarrow \qquad \frac{\sqrt{1-e^2}}{\Omega} = \frac{1}{\sqrt{GM} \sqrt{a}}$$

$$\rightarrow \qquad T = \pi \frac{a^{\frac{3}{2}}}{\sqrt{GM}}$$


$$
 2a = \frac{\Omega^2}{GM+A \Omega^2} + \frac{\Omega^2}{GM-A \Omega^2} 
    = \Omega^2 \frac{2 GM }{(GM)^2 - A^2 \Omega^4}
$$

$$A^2 \Omega^4 = (GM)^2 - \frac{GM \, \Omega^2}{a}$$

$$\frac{\Omega^2}{GM}\frac{1}{a} = 1 - \left(\frac{A \Omega^2}{GM}\right)^2$$

$$\frac{1}{a} = \left( 1 - \left(\frac{A \Omega^2}{GM}\right)^2 \right) \frac{GM}{\Omega^2}$$

<!--
Il semiasse maggiore è dato da

$$\begin{aligned}
a & = \frac{1}{2} \left( r(0)+r(\pi) \right) = \\
  & = \frac{\Omega^2}{GM} \left[ \frac{1}{1+\frac{A \Omega^2}{GM}} + \frac{1}{1-\frac{A \Omega^2}{GM}} \right] = \\
  & = \dfrac{2}{ \left(\frac{GM}{\Omega^2} \right)^2 - A^2}
\end{aligned}$$
-->
