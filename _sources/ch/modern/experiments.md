(modern:experiments)=
# Esperimenti

## Scoperta dell'elettrone - J.J.Thomson

```{dropdown} Moto di una carica in un campo elettromagnetico uniforme stazionario
Una volta scelto un sistema di riferimento (*così da poter identificare la posizione di un punto nello spazio con un vettore posizione $\vec{r} = R-O$ rispetto all'origine*), il campo elettromagnetico (rispetto al sistema di riferimento, **todo** *aggiungere sezione su relatività per elettromagnetismo, anche galileiana come approssimazione a bassa velocità*) in una regione dello spazio viene rappresentato dai campi vettoriali, 

$$\vec{e}(\vec{r},t) \, \quad \vec{b}(\vec{r},t) \ ,$$

che permettono di esprimere il campo elettrico e il campo magnetico come funzioni della variabile spazio $\vec{r}$ e tempo $t$.

La posizione di un punto $P$ nello spazio è identificata dal raggio vettore $\vec{r}_P(t)$, in generale funzione del tempo per punti in moto. La velocità e l'accelerazione del punto $P$ riferite al sistema di coordinate scelto sono rispettivamente la derivata prima e seconda del raggio vettore,

$$\vec{v}_P(t) = \frac{d \vec{r}_P}{d t} \ , \quad
  \vec{v}_P(t) = \frac{d \vec{r}_P}{d t} \ .$$

Una carica elettica di intensità $q_P$ in moto con una velocità $\vec{v}_P$ in un punto dello spazio $\vec{r}_P(t)$ in cui è presente un campo elettromagnetico $\vec{e}(\vec{r}_P,t)$, $\vec{b}(\vec{r}_P,t)$ è soggetta alla [forza di Lorentz](physics-hs:electromagnetism:lorentz),

$$\vec{F}_P(t) = q_P \left[ \vec{e}(\vec{r}_P(t),t) - \vec{b}(\vec{r}_P(t),t) \times \vec{v}_P(t) \right] \ .$$

e l'equazione del moto per la carica è

$$m_P \frac{ d^2 \vec{r}_P}{dt^2} = q_P \left[ \vec{e}(\vec{r}_P(t),t) - \vec{b}(\vec{r}_P(t),t) \times \frac{d \vec{r}_P}{dt} \right] \ .$$

Una volta inteso che le quantità che compaiono nell'equazione sono riferite al punto $P$, per alleggerire un po' la notazione si fanno cadere i pedici $_P$.

In generale, l'equazione del moto è un'equazione differenziale del secondo ordine non lineare, se il campo magnetico dipende dallo spazio o se il campo elettrico varia linearmente nello spazio. Se il campo elettromagnetico è costante (costante in tempo) e uniforme (costante in spazio), $\vec{e}(\vec{r},t) = \vec{E}$, $\vec{b}(\vec{r},t) = \vec{B}$, l'equazione del moto,

$$m \ddot{\vec{r}} = q \left[ \vec{E} - \vec{B} \times \dot{\vec{r}} \right] \ .$$

è una ODE lineare a coefficienti costanti, risolvibile in forma analitica.

**Esperimento di J.J.Thomson.** 
Condizioni iniziali $\vec{r} = \vec{0}$, $\vec{v}(0) = v_0 \hat{x}$

**Campo elettrico.** $\vec{E} = E \hat{y}$

$$\begin{cases}
  \ddot{x} = 0                \\
  \ddot{y} = \frac{q}{m} E    \\
  \ddot{z} = 0                \\
\end{cases}$$

$$
\begin{cases}
  x(t) = v_0 t \\
  y(t) = \frac{1}{2} \frac{q E}{m} t^2 \\
  z(t) =   0   \\
\end{cases}
\qquad , \qquad
\begin{cases}
  v_x(t) = v_0 \\
  v_y(t) = \frac{q E}{m} t \\
  v_z(t) =   0 \\
\end{cases}
$$


**Campo magnetico.** $\vec{B} = B \hat{y}$

$$
\vec{B} \times \vec{v} = \left|\begin{matrix} \hat{x} & \hat{y} & \hat{z} \\ 0 & B & 0 \\ v_x & v_y & v_z \end{matrix}\right| =  \hat{x} B v_z - \hat{z} B v_x 
$$

$$\begin{cases}
  \ddot{x} = - \frac{q B}{m} \dot{z} \\
  \ddot{y} = 0                       \\
  \ddot{z} =   \frac{q B}{m} \dot{x} \\
\end{cases}$$

$$\begin{cases}
  \ddot{v}_x + \left(\frac{q B}{m}\right)^2 v_x = 0 \\
  \ddot{v}_y = 0                                    \\
  \ddot{v}_z + \left(\frac{q B}{m}\right)^2 v_z = 0 \\
\end{cases}$$

$$\begin{cases}
v_x = A_x \cos \Omega t + B_x \sin \Omega t \\
v_y = A_y t + B_y                           \\
v_z = A_z \cos \Omega t + B_z \sin \Omega t \\
\end{cases}
\qquad \rightarrow \text{i.c.} \rightarrow \qquad
\begin{cases}
 A_x = v_0 \\
 B_y = 0 \\
 A_z = 0
\end{cases}
$$

Usando le equazioni del moto

$$\begin{cases}
  - v_0 \Omega \sin \Omega t + B_x \Omega \cos \Omega t = - \frac{q B}{m} B_z \sin \Omega t \\
  A_y = 0 \\
  B_z \Omega \cos \Omega t = \frac{q B}{m} \left( v_0 \cos \Omega t +  B_x \sin \Omega t \right) \\
\end{cases}
\qquad \rightarrow \qquad
\begin{cases}
  B_x = 0  \\
  A_y = 0 \\
  B_z = v_0 \\
\end{cases}$$

la velocità diventa

$$\begin{cases}
v_x(t) = v_0 \cos \Omega t  \\
v_y(t) = 0 \\
v_z(t) = v_0 \sin \Omega t \\
\end{cases}$$

mentre la posizione, integrando e applicando le condizioni iniziali, e ricorando che $\Omega = \frac{q B}{m}$

$$\begin{cases}
  x(t) = \frac{v_0}{B} \frac{m}{q} \sin \left( \frac{q}{m} B t \right)  \\
  y(t) = 0 \\
  z(t) = \frac{v_0}{B} \frac{m}{q} \left[ 1 - \cos \left( \frac{q}{m} B t \right) \right] \\
\end{cases}$$

**Soluzioni per piccole deviazioni** con campo elettromagnetico presente solo nella regione $x \in [0, L]$,
- **Campo elettrico**
  
   $$
   \begin{cases}
     v_x(t) = v_0 \\
     v_y(t) = \frac{q E}{m} t \\
     v_z(t) =   0 \\
   \end{cases}
   \qquad , \qquad
   \begin{cases}
     x(t) = v_0 t \\
     y(t) = \frac{1}{2} \frac{q E}{m} t^2 \\
     z(t) =   0   \\
   \end{cases}
   $$

   $$\begin{aligned} 
       x^* = L = v_0 t^* \quad & , \quad   y^* = \frac{1}{2} \frac{q}{m} E \left( \frac{L}{v_0} \right)^2 \\
     v_x^* = v_0         \quad & , \quad v_y^* =             \frac{q}{m} E \frac{L}{v_0} \\
   \end{aligned}$$

   Il rapporto $r_e = \frac{v_y^*}{v_x^*}$ può essere facilmente misurato e quindi considerarsi noto

   $$\frac{q}{m} = \frac{r_e v_0^2}{E L} $$

- **Campo magnetico**

  $$\begin{cases}
  v_x(t) \sim v_0  \\
  v_y(t) = 0 \\
  v_z(t) \sim v_0 \frac{q}{m} B t \\
  \end{cases}
  \qquad , \qquad
  \begin{cases}
    x(t) \sim v_0 t  \\
    y(t) = 0 \\
    z(t) \sim \frac{1}{2} \frac{q}{m} v_0 B t^2 \\
  \end{cases}$$

   $$\begin{aligned} 
       x^* = L = v_0 t^* \quad & , \quad   y^* = \frac{1}{2} \frac{q}{m} v_0 B \left( \frac{L}{v_0} \right)^2 \\
     v_x^* = v_0         \quad & , \quad v_y^* =             \frac{q}{m} v_0 B \frac{L}{v_0} \\
   \end{aligned}$$

   Il rapporto $r_b = \frac{v_y^*}{v_x^*}$ può essere facilmente misurato e quindi considerarsi noto

   $$\frac{q}{m} = \frac{r_b v_0}{B L} $$

   **Stima del rapport $\frac{q}{m}$** Esprimendo $v_0$ in funzione di $\frac{q}{m}$,

   $$ \qquad \rightarrow \qquad v_0 = \frac{q}{m} \frac{BL}{r_b}$$

   e sostituendo $v_0$ nell'espressione del rapporto che coinvolge il campo elettrico

   $$\frac{q}{m} = \frac{r_e}{EL} \left(\frac{q}{m}\right)^2 \left( \frac{B L}{r_b} \right)^2 \ ,$$

   si arriva alla stima 

   $$\frac{q}{m} = \frac{r_b^2}{r_e} \frac{E}{BL} \ .$$

```

## La radioattività - Esperimento dei coniugi Curie

```{dropdown}
- Elettroscopio [piezoelettrico](physics-hs:modern:intro:experiences:piezoel)
- ...


```


## Misura della carica dell'elettrone - Millikan

```{dropdown} Misura della carica dell'elettrone
L'esperimento permette di stimare la carica dell'elettrone grazie alle misure sul moto in un fluido di gocce d'olio cariche elettricamente. Vengono confrontate almeno due condizioni differenti, identificate dall'intensità nota del campo elettrico $\vec{E}$ applicato al sistema, che si manifesta come forza  $\vec{F}^{el} = q \vec{E}$ sul moto di una corpo con carica elettrica $q$.

Il confronto tra le velocità limite $v_{\infty,E}$ e $v_{\infty,0}$ nelle due condizioni permette di ottenere un misura della carica $q$ del corpo in esame.

Nell'esperimento di Millikan è impossibile controllare la carica esatta di ogni goccia d'olio. Ripetendo l'esperimento più volte su un gran numero di gocce si osserva che la misura della carica di queste gocce restituisce valori multipli di una carica "elementare", che viene considerata la carica dell'elettrone.

L'esperimento sfrutta la [legge di Stokes](fluids:dynamics:stokes), che prevede una resistenza aerodinamica lineare tra la forza agente su un corpo di piccole dimensioni e la sua velocità relativa al fluido nel quale si muove,

$$\vec{F}^{aero} = - 6 \pi \mu R \vec{v}_{rel} = - c \vec{v} \ ,$$

avendo indicato con $c$ la costante di proporzionalità (per ogni goccia, bisogna stimare $R$, qua lo supponiamo misurato e quindi noto), e considerato il fluido a riposo.

Se il campo elettrico $\vec{E} = E \hat{z}$ è allineato con la gravità locale, $\vec{g} = g \hat{z}$, la componente lungo questa direzione dell'equazione di moto della goccia è

$$m \ddot{z} = F^{peso}_z + F^{aero}_z + F^{el}_z = m g - c \dot{z} + q E$$

che può essere riscritta in termini della componente $z$ della velocità,

$$m \dot{v}_z + c v_z = m q + q E \ .$$

Integrando in tempo con la condizione iniziale $v_z(0) = v_0$, si può esprimere la velocità in funzione del tempo,

$$v_z(t; E) = v_0 + \left[ \frac{m g + q E}{c} - v_0 \right] (1 - e^{-\frac{c}{m}t}) \ .$$

Facendo tendere $t \rightarrow +\infty$, si ottiene la velocità limite

$$v_{z, \infty}(E) = \frac{m g + q E}{c} = \frac{m g}{c} + \frac{E}{c} q \ ,$$

considerata nota dalle misure. Confrontando la velocità limite misurata per due valori del campo elettrico, si può eliminare la dipendenza dalla massa e ottenere 

$$v_{z, \infty}(E_2) - v_{z, \infty}(E_1) = \frac{E_2 - E_1}{c} q \qquad \rightarrow \qquad q = \frac{c \left(v_{z,\infty}(E_2)- v_{z,\infty}(E_1) \right)}{E_2 - E_1}$$

```


## Modello atomico di Rutherford - Geiger-Mardsen
```{dropdown} Scattering
:open:

Gli esperimenti condotti da Geiger[^geiger] e Mardsen sotto la supervisione di Rutherford a Manchester consistono in esperimenti di scattering, in cui un fascio di particelle-$\alpha$[^alpha-particle] viene direzionato contro una sottile lamina di oro. Le particelle-$\alpha$ interagiscono con la lamina e vengono deviate. In questo esperimento si osserva che un grandissimo di numero di particelle subisce una deviazione minima, come se non interagissero con la struttura dell'oro; al crescere dell'angolo di deviazione diminuisce il numero misurato di particelle che hanno subito quella deviazione; alcune particelle subiscono anche una deviazione maggiore di $90°$, inclusa una deviazione di $180°$ corrispondente a un "rimbalzo normale" sulla lamina: la frequenza di questi eventi è sempre più piccola ma non nulla.

La spiegazione dell'esperimento da parte di Rutherford è alla base del suo modello atomico: la distribuzione delle particelle-$\alpha$ misurata è compatibile un'interazione elettrica tra cariche positive puntiformi. Rutherford quindi ipotizza che la materia sia formata da atomi quasi del tutto "vuoti": le cariche positive sono concentrate in un **nucleo** di dimensioni estremamente compatte (**todo** *stima delle dimensioni da parte di Rutherford e misura di oggi*), attorno al quale sono disposte le cariche negative. **todo** *poca attenzione alle cariche negative fino al modello di **Bohr**. Atomo con nucleo positivo e cariche negative che possono trovarsi in orbite ben definite, discrete, caratterizzate da numeri atomici interi.*

Si vuole studiare il moto di una corpo puntiforme di massa $m$ e carica elettrica $q$, rispetto a un corpo di carica elettrica $Q$ (concorde per scattering) e soggetto al campo elettrico generato dalla carica $Q$ e quindi a una forza

[^geiger]: Geiger quello del contatore di radiazioni, quello che gracchia
[^alpha-particle]: particelle $\alpha$ sono isotopi di $\text{He}^{2+}$, cioè atomi di elio ai quali mancano due elettroni, quindi carichi positivamente. Questo è quello che interessa a noi qui. **todo** aggiungere riferimento a radioattività

$$\vec{F} = \frac{q Q}{4 \pi \varepsilon} \frac{\vec{r}}{r^3} = c \, \frac{\vec{r}}{r^3} \ .$$

Si osservi che per la (quasi) analogia formale tra la [forza di Coulomb](physics-hs:electromagnetism:electrostatics:coulomb) e la [legge di gravitazione universale di Newton](physics-hs:mechanics:dynamics:motion:gravitation:newton), questo problema ha delle similitudini con il [problema dei due corpi](physics-hs:mechanics:dynamics:motion:gravitation:two-bodies) soggetti alla mutua interazione gravitazionale.

L'equazione dinamica del corpo è quindi

$$m \ddot{\vec{r}} = c \, \frac{\vec{r}}{r^3} \ .$$

**Moto piano.**  E' immediato dimostrare che il moto è piano, cioè che la posizione e la velocità del pianeta sono sempre ortogonali a una direzione costante.

$$\frac{d}{dt} \left( \vec{r} \times \vec{v} \right) = \underbrace{\vec{v} \times \vec{v}}_{=\vec{0}} + \vec{r} \times \vec{a}  = \frac{c}{m} \, \underbrace{\vec{r} \times \frac{\vec{r}}{r^3}}_{=\vec{0}} = \vec{0} \ .$$

Poiché il vettore $\vec{r} \times \vec{v} =: \frac{L}{m} \hat{k}$ è costante, è costante sia il suo valore assoluto sia la sua direzione: affinché $\vec{r} \times \vec{v}$ sia allineato con $\hat{k}$, i vettori $\vec{r}$, $\vec{v}$ devono essere ortogonali a $\hat{k}$.

**Coordinate polari.** Per descrivere il moto piano di un punto, si può usare un sistema di coordinate 2-dimensionale. Si sceglie un sistema di coordinate polari con origine coincidente con il corpo di carica $Q$. La posizione del pianeta è identificata dal raggio vettore

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

Usando le coordinate polari, l'equazione del moto $m \ddot{\vec{r}} = c \, \frac{\vec{r}}{r^3}$ viene scritta in componenti,

$$\begin{aligned}
r      & : \ m (\ddot{r} - r\dot{\theta}^2) = c \, \frac{1}{r^2} \\
\theta & : \ m ( 2 \dot{r} \dot{\theta} + r \ddot{\theta}^2 ) = 0
\end{aligned}$$

**Traiettoria, $r(\theta)$.**
Inserendo l'espressione $\dot{\theta} = \frac{\Omega}{r^2}$ nella componente radiale, e definendo la funzione $z = \frac{1}{r}$, le derivate nel tempo della coordinata radiale possono essere riscritte come

$$\dot{r} = -\frac{1}{z^2}\frac{d z}{d \theta} \dot{\theta} = -\Omega \frac{dz}{d\theta} $$

$$\ddot{r} = \dot{\theta} \frac{d}{d \theta} \left( - \Omega \frac{dz}{d \theta} \right) = - z^2 \Omega^2 z''(\theta)$$

e la componente radiale dell'equazione di moto,

$$-z^2 \Omega^2 z'' - z^3 \Omega^2 = c \, z^2$$
$$ z'' + z  = -\frac{c}{\Omega^2}$$

$$z(\theta) = - \frac{c}{\Omega^2} + A \cos(\theta) + B \sin(\theta) \ .$$

e quindi

$$r(\theta) = \frac{\Omega^2}{c} \frac{1}{A \dfrac{\, \Omega^2}{c} \cos \theta + B \dfrac{\, \Omega^2}{c} \sin \theta - 1}$$

**todo** *Perché si possono considerare $A > 0$ e tale da ottenere un'iperbole quando $B = 0$?*

*Scelta della direzione di riferimento:*
- *direzione del perielio: $r(\theta=0) = \min r$, $B = 0$,?*

**todo** *Finire esercizio (nel file sorgente ci sono linee commentate che possono essere utili); aggiungere immagini; calcolare sezione d'urto e distribuzione urti e confronto con risultati di Rutherford*

<!--
Scelte diverse si ottengono da una trasformazione di coordinate con una rotazione dell'asse di riferimento: $\theta_1 = \theta - \theta_0$, e quindi

$$r(\theta) = \frac{\Omega^2}{GM}\frac{1}{1 + \frac{A\Omega^2}{GM} \cos \theta} = \frac{\Omega^2}{GM}\frac{1}{1 + \frac{A\Omega^2}{GM} \cos (\theta_1 + \theta_0 )} = \frac{\Omega^2}{GM}\frac{1}{1 + \underbrace{\frac{A\Omega^2}{GM} \cos \theta_0}_{= A_1} \cos \theta_1 \underbrace{- \frac{A \Omega^2}{GM} \sin \theta_0}_{= B_1} \sin \theta_1 }$$

Il confronto con l'equazione delle coniche in coordinate polari, permette di riconoscere l'eccentricità, $e$ e il prodotto $e \, D$ dell'eccentricità per la distanza $D$ tra fuoco e direttrice,

$$e = \frac{A \Omega^2}{GM} \qquad , \qquad e \, D = \frac{\Omega^2}{GM}$$

$$r(\theta) = \frac{\Omega^2}{GM}\frac{1}{1 + \frac{A\Omega^2}{GM} \cos \theta}$$
$$r(\theta) = \frac{e \, D}{1 + e \, \cos \theta}$$

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

-->

```

## Lo spin - Stern-Gerlach
```{dropdown} Moto di un dipolo magnetico in un campo magnetico non uniforme
:open:

```


