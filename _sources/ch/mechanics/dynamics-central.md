(physics-hs:mechanics:dynamics:motion:central)=
# Moti centrali

In meccanica, un moto centrale è definito come il moto di un corpo soggetto a un campo di forze con simmetria sferica rispetto a un punto $C$. Scegliendo questo punto come oridine di un sistema di riferimento, ogni punto dello spazio risulta determinato dal raggio vettore $\vec{r}$ tra il centro e il punto. Un campo di forze centrale può essere scritto come

$$\vec{F}(\vec{r}) = F_r(|\vec{r}|) \hat{r} \ ,$$

cioè la forza ha direzione radiale e la sua intensità dipende solo dalla distanza dal centro.

**Esempi.** Alcuni esempi che possono essere rappresentati come moti centrali sono:
- il moto di una massa vincolata a terra con una molla, $\vec{F} = - k \vec{r} = - k r \hat{r} \propto r$
- il moto di due corpi con massa soggetti alla mutua interazione gravitazionale, $\vec{F} = - G m_1 m_2\frac{\vec{r}}{|\vec{r}|^3} = - G m_1 m_2\frac{1}{|\vec{r}|^2} \hat{r} \propto \frac{1}{r^2}$
- il moto di due corpi con carica elettrica soggetti alla mutua interazione elettrica, $\vec{F} = \frac{q_1 q_2}{4\pi\varepsilon} \frac{\vec{r}}{|\vec{r}|^3} = \frac{q_1 q_2}{4\pi\varepsilon} \frac{1}{|\vec{r}|^2} \hat{r} \propto \frac{1}{r^2}$

Nel primo caso, l'intensità della forza ha una dipendenza lineare con la distanza dal centro; negli altri due casi, l'intensità della forza è inversamente proporzionale al quadrato della distanza dal centro. Si noti la (quasi) uguaglianza formale tra l'interazione gravitazionale soggetta alla legge di gravitazione universale di Newton e l'interazione elettrica soggetta alla forza di Coulomb. I due casi hanno però una differenza fondamentale: nel caso di interazione gravitazionale due corpi si attraggono sempre, nel caso di interazione elettrica, due corpi con carica di segno opposto si attraggono mentre due corpi con carica di segno uguale si respingono.

Nelle sezioni successive vengono discussi i casi di [forza proporzionale alla distanza]() e [forza proporzionale al quadrato della distanza]().

(physics-hs:mechanics:dynamics:motion:central:r)=
## Forza proporzionale alla distanza

L'equazione del moto di un corpo soggetto a un campo di forze centrali con intensità proporzionale alla distanza dal centro è

$$m \ddot{\vec{r}} = -k \vec{r}$$

**todo**


(physics-hs:mechanics:dynamics:motion:central:r-2)=
## Forza inversamente proporzionale al quadrato della distanza

L'equazione del moto di un corpo soggetto a un campo di forze centrali con intensità inversamente proporzionale al quadrato della distanza dal centro è

$$m \ddot{\vec{r}} = c \frac{\vec{r}}{\vec{|\vec{r}|^3}} \ ,$$ (eq:central:r-2:eom)

...**todo** *bla bla*


(physics-hs:mechanics:dynamics:motion:central:plane)=
```{dropdown} Moto piano
Il moto avviene in un piano identificato dalla posizione e dalla velocità (iniziale). Nel caso in cui la velocità risulta allineata con la direzione radiale si verifica solo nel caso degenere in cui il moto è rettilineo: se la velocità è allineata alla direzione radiale in un istante temporale, lo è sempre; viene da sé, che in ogni altro caso di moto centrale, la velocità non ha mai direzione radiale.

Poiché il vettore $\vec{r} \times \vec{v}$ è costante,

$$\frac{d}{dt} \left( \vec{r} \times \dot{\vec{r}} \right) = \underbrace{\dot{\vec{r}} \times \dot{\vec{r}}}_{= \vec{0}} + \vec{r} \times \ddot{\vec{r}} = \underbrace{\vec{r} \times c \frac{\vec{r}}{|\vec{r}|^3}}_{=\vec{0}} = \vec{0} \ ,$$

si può concludere che il moto avviene nel piano identificato dai vettori posizione $\vec{r}$ e velocità $\vec{v}$. Indichiamo la direzione normale al piano con il versore $\hat{k}$.
Poiché il moto è piano, può essere studiato con un sistema di coordinate 2-dimensionale. Si sceglie qui un sistema di [coordiante polari](physics-hs:mechanics:dynamics:motion:central:polar).

```

(physics-hs:mechanics:dynamics:motion:central:ang-mom)=
```{dropdown} Costanza del momento angolare e della velocità areolare
Il **momento angolare** $\vec{l}$ del corpo attorno al centro del campo, è il prodotto della massa $m$ per il vettore $\vec{r} \times \vec{v}$ costante,

$$\vec{l} = m \vec{r} \times \vec{v} \ ,$$

ed è quindi **costante** a sua volta. La **velocità areolare**, definita come l'area descritta $\hat{k} dA = \frac{1}{2} \vec{r} \times d \vec{r}$ (area del triangolino elementare che ha come base lo spostamento elementare $d \vec{r}$) per unità di tempo $dt$, risulta essere uguale alla metà del vettore $\vec{r} \times \vec{v}$

$$\vec{\Omega} = \frac{1}{2} \vec{r} \times \vec{v} = \frac{\vec{l}}{2 m} \ ,$$

ed è quindi **costante** a sua volta.

```

(physics-hs:mechanics:dynamics:motion:central:polar)=
```{dropdown} Equazioni in coordinate polari
Poiché il [moto è piano](physics-hs:mechanics:dynamics:motion:central:plane), è possibile introdurre un sistema di coordinate polari. La posizione di un punto è identificato dal vettore  $\vec{r} = r \hat{r}$, la velocità e l'accelerazione si ricavano derivando nel tempo,

$$\begin{aligned}
 \vec{r} & = r \hat{r} \\
 \vec{v} & =  \dot{\vec{r}} = \dot{r} \hat{r} + r \dot{\theta} \hat{\theta} \\
 \vec{a} & = \ddot{\vec{r}} = \left( \ddot{r} - r \dot{\theta}^2 \right) \hat{r} + \left( 2 \dot{r} \dot{\theta} + r \ddot{\theta} \right) \hat{\theta} \\
\end{aligned}$$

e l'equazione del moto {eq}`eq:central:r-2:eom` può essere scritta nelle sue componenti radiale e tangenziale

$$\begin{cases}
 r      \ & : \quad m \left( \ddot{r} - r \dot{\theta}^2 \right) = c \frac{1}{r^2} \\
 \theta \ & : \quad m \left( 2 \dot{r} \dot{\theta} + r \ddot{\theta} \right) = 0 \ .
\end{cases}$$ (eq:central:r-2:eom:coords)

```

```{dropdown} Costanza dell'energia
Moltiplicando scalarmente l'equazione del moto {eq}`eq:central:r-2:eom` per il vettore velocità $\dot{\vec{r}}$ si ottiene il bilancio dell'energia meccanica

$$0
 = \dot{\vec{r}} \cdot \left[ m \ddot{\vec{r}} - c \frac{\vec{r}}{|\vec{r}|^3} \right] 
 = \dfrac{d}{dt} \left[ \frac{1}{2} m |\dot{r}|^2 + \frac{c}{r} \right] \ ,
$$

che si traduce nella legge di conservazione dell'energia meccanica,

$$E = \frac{1}{2} m |\dot{\vec{r}}|^2 + \frac{c}{r} = \text{const.}$$

L'energia meccanica può essere riscritta usando le coordiante polari $r$, $\theta$ e la costanza del momento angolare $\vec{l}$,

$$\begin{aligned}
 E & = \frac{1}{2} m |\dot{\vec{r}}|^2 + \frac{c}{r} = \\
   & = \frac{1}{2} m \left( \dot{r}^2 + r^2 \dot{\theta}^2 \right) + \frac{c}{r} = \\
   & = \frac{1}{2} m \dot{r}^2 + \frac{1}{2} \frac{l^2}{m r^2} + \frac{c}{r} \\
\end{aligned}$$

dopo aver espresso il momento angolare in coordinate polari 

$$\vec{l} = l \hat{k} = m \vec{r} \times \vec{v} = m r^2 \dot{\theta} \hat{k} \ ,$$

per poter esprimere la derivata nel tempo dell'angolo $\theta$ in fuzione del momento angolare $l$, e del raggio $r$

$$\dot{\theta} = \frac{l}{m r^2} \ .$$ (eq:theta-ang-mom)

```

```{dropdown} Traiettorie e coniche
:open:

Si cerca la traiettoria $r(\theta)$ descritta nel moto del corpo. L'equazione del moto assume una forma semplice da risolvere dopo aver introdotto la funzione $z = \frac{1}{r}$. Si calcolano le derivate sfruttando l'espressione della funzione $z$, e l'espressione {eq}`eq:theta-ang-mom` della derivata della coordinata angolare

$$\begin{aligned}
   \dot{r} & = -\frac{1}{z^2} z'(\theta) \dot{\theta} = -\frac{1}{z^2} \frac{l}{m r^2} z'(\theta) = - \frac{l}{m} z'(\theta) \\
  \ddot{r} & = - \frac{l}{m} \dot{\theta} z''(\theta) = - z^2 \frac{l^2}{m^2} z''(\theta) \\
\end{aligned}$$

Esprimendo la componente radiale dell'equazione del moto {eq}`eq:central:r-2:eom:coords` si ottiene un'equazione differenziale ordinaria lineare a coefficienti costanti del secondo ordine,

$$\begin{aligned}
  & - m z^2 \frac{l^2}{m^2} z'' - m \frac{1}{z} \frac{l^2 z^4}{m^2} = c z^2 \\
\end{aligned}$$

$$ \quad \rightarrow \quad z'' + z = - \frac{m c }{l^2} \ ,$$

la cui soluzione è $z(\theta) = A \cos \theta + B \sin \theta - \frac{m c}{l^2}$ o, in termini del raggio $r$,

$$r(\theta) = \frac{1}{- \frac{m c}{l^2} + A \cos \theta + B \sin \theta} \ .$$


```


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
