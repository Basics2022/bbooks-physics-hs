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

Nelle sezioni successive vengono discussi i casi di [forza proporzionale alla distanza](physics-hs:mechanics:dynamics:motion:central:r) e [forza proporzionale al quadrato della distanza](physics-hs:mechanics:dynamics:motion:central:r-2).

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

(physics-hs:mechanics:dynamics:motion:central:energy)=
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
\end{aligned}$$ (eq:dynamics:central:r-2:energy)

dopo aver espresso il momento angolare in coordinate polari 

$$\vec{l} = l \hat{k} = m \vec{r} \times \vec{v} = m r^2 \dot{\theta} \hat{k} \ ,$$

per poter esprimere la derivata nel tempo dell'angolo $\theta$ in fuzione del momento angolare $l$, e del raggio $r$

$$\dot{\theta} = \frac{l}{m r^2} \ .$$ (eq:theta-ang-mom)

```

(physics-hs:mechanics:dynamics:motion:central:trajectory)=
```{dropdown} Traiettorie e coniche

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

Questa equazione rappresenta la più generale equazione delle [coniche in coordinate polari](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/analytic_geometry/analytic_geometry_2d/conics.html). L'arbitrarietà nella scelta della direzione dalla quale misurare gli angoli può essere utilizzata per riscrivere il denominatore,

$$A \cos \theta + B \sin \theta 
 & = \sqrt{A^2+B^2} \left[ \underbrace{\frac{A}{\sqrt{A^2+B^2}}}_{\cos \phi} \cos \theta + \underbrace{\frac{B}{\sqrt{A^2+B^2}}}_{\sin \phi} \sin \theta \right] = \\
 & = \sqrt{A^2+B^2} \left[ \cos \phi \cos \theta + \sin \phi \sin \theta \right] = \\
 & = \sqrt{A^2+B^2} \cos( \theta - \phi ) \ .
$$

per riscrivere l'equazione

$$\begin{aligned}
 r(\theta)
  & = \frac{1}{-\frac{m c}{l^2} + \sqrt{A^2 + B^2} \cos(\theta-\phi) } = \\
  & = \frac{ \frac{l^2}{m|c|} }{ - \text{sign}(c) + \frac{l^2}{m |c|} \sqrt{A^2 + B^2} \cos(\theta-\phi)} = \\
  & = \frac{ed}{-\text{sign}(c) + e \cos(\theta-\phi)} \ .
\end{aligned}$$ (eq:dynamics:central:r-2:trajectory:conics)

```

(physics-hs:mechanics:dynamics:motion:central:trajectory-el)=
```{dropdown} Equazione della traiettoria in funzione dell'energia e del momento angolare

Manipolando i risultati ottenuti, si vuole esprimere l'equazione della traiettoria {eq}`eq:dynamics:central:r-2:trajectory:conics` in termini delle costanti del moto, l'energia $E$ e il momento angolare $l$. Si valuta la derivata nel tempo dell'equazione {eq}`eq:dynamics:central:r-2:trajectory:conics`

$$
\dot{r} = \frac{ - e^2 d \sin(\theta-\phi) }{\left( -\text{sign}(c) + e \cos(\theta-\phi) \right)^2} \dot{\theta}
= - \frac{r^2}{d}  \frac{l}{m r^2} \sin(\theta-\phi) = - \frac{l}{m d} \sin(\theta-\phi)
$$

con $d = \frac{1}{\sqrt{A^2 + B^2}}$, $ed = \frac{l^2}{m |c|}$, e si inserisce nell'espressione dell'energia {eq}`eq:dynamics:central:r-2:energy`

$$\begin{aligned}
  E & = \frac{1}{2} m \dot{r}^2 + \frac{1}{2} \frac{l^2}{m r^2} + \frac{c}{r} = \\
    & = \frac{1}{2} m \frac{l^2}{m^2 d^2} \sin^2(\theta-\phi) + \frac{1}{2} \frac{l^2}{m \left(\frac{l^2}{m |c|}\right)^2} \left( -\text{sign}(c) + e \cos(\theta-\phi)  \right)^2 + c \frac{-\text{sign}(c) + e \cos(\theta-\phi)}{ \frac{l^2}{m |c|} } = \\
    & = \frac{l^2}{2md^2} \sin^2(\theta-\phi) + \frac{m c^2}{2 l^2} \left( 1 - 2\text{sign}(c) e \cos(\theta-\phi) + e^2 \cos^2(\theta-\phi) \right) + \frac{m c^2}{l^2} \left( - 1 + \text{sign}(c) e \cos(\theta-\phi) \right) = \\
    & = \frac{l^2}{2md^2} \sin^2(\theta-\phi) + \frac{1}{d^2} \frac{l^4}{m^2 c^2} \frac{m c^2}{2 l^2} \cos^2(\theta-\phi) 
     - \frac{m c^2}{2 l^2} = \\ 
    & = \frac{l^2}{2md^2} - \frac{m c^2}{2 l^2} \ ,
\end{aligned}$$

per ricavare i coefficienti dell'equazione generale delle coniche in funzione dei parametri fisici del problema,

$$\begin{aligned}
  \frac{1}{d^2} & = \frac{2m}{l^2} \left( E + \frac{m c^2}{2 l^2} \right) \\ 
  e & = \frac{l^2}{m |c|} \frac{1}{d} = \frac{l^2}{m |c|}\frac{m|c|}{l^2} \sqrt{1 + \frac{2 E l^2}{m |c|^2}} =  \sqrt{1 + \frac{2 E l^2}{m |c|^2}}
\end{aligned}$$

L'equazione delle coniche può quindi essere riscritta come

$$r(\theta) = \frac{\frac{l^2}{m|c|}}{-\text{sign}(c) + \sqrt{1 + 2 \frac{E l^2}{m|c|^2}} \cos(\theta-\phi)} \ .$$ (eq:dynamics:central:r-2:trajectory:el)

L'espressione dell'eccentricità permette di stabilire il legame tra i valori delle costanti del moto $E$, $l$ e il tipo di conica che descrive la traiettoria

$$\begin{array}{lcc}
\textbf{Conica} & \textbf{e} & \textbf{E} \\ \hline
\text{circonferenza} & 0           & -\frac{m|c|^2}{2l^2} \\ 
\text{ellisse}       & \in [0,1)   & \in \left[-\frac{m|c|^2}{2l^2}, 0 \right) \\ 
\text{parabola}      & 1           & 0                    \\ 
\text{iperbole}      & > 1         & > 0                  \\ 
\end{array}$$

**Osservazione.** Giunti verso la fine di un libro sulla meccanica, dovrebbe fare storcere il naso parlare in termini di valore assoluto di energia (almeno per quanto riguarda la meccanica classica). Questo è possibile, poiché la costante additiva arbitraria è stata fissata (implitamente, **todo** *essere più espliciti nella sezione*) nella sezione sulla [costanza dell'energia](physics-hs:mechanics:dynamics:motion:central:energy), ponendo uguale a zero la condizione di quiete a distanza infinita dal centro.

```

