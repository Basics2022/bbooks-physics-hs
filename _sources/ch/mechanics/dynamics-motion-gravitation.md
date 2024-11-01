(physics-hs:mechanics:dynamics:motion:gravitation)=
# Gravitazione

## Legge di gravitazione universale
$$\vec{F}_{10} = G \, m_0 \, m_1 \frac{\vec{r}_{01}}{\left|\vec{r}_{01}\right|^3}$$

## Problema dei due corpi

### Coniche

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

La definizione di $r(z)$ e una scelta opportuna di $\theta$ (**todo** a cosa corrisponde?), permettono di scrivere 

$$r(\theta) = \frac{\Omega^2}{G M}\frac{1}{1 + \frac{A \, \Omega^2}{GM} \cos \theta}$$

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
