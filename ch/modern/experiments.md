(modern:experiments)=
# Esperimenti

(modern:experiments:thomson:electron)=
## Scoperta dell'elettrone - J.J.Thomson

**todo** 
- link a [conduzione di corrente elettrica nei gas](physics-hs:electromagnetism:electric-current:gas)
- cenni all'esperimento di Goldstein (1886), che si era concentrato solo sul raggio "sbagliato"
- cenni all'esperimento di Hertz (1887), fallito a causa di un apparato sperimentale inadeguato. **todo** *collegamento a logica, conoscenza ed epistemologia e [criterio di Fisher](https://basics2022.github.io/bbooks-programming-hs/ch/statistics/hp-test.html#statistics-hs-inference-hp-test)*

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

**Esperimento e modello atomico di Rutherford.** Gli esperimenti condotti da Geiger[^geiger] e Mardsen sotto la supervisione di Rutherford a Manchester consistono in esperimenti di scattering, in cui un fascio di particelle-$\alpha$[^alpha-particle] viene direzionato contro una sottile lamina di oro. Le particelle-$\alpha$ interagiscono con la lamina e vengono deviate. In questo esperimento si osserva che un grandissimo di numero di particelle subisce una deviazione minima, come se non interagissero con la struttura dell'oro; al crescere dell'angolo di deviazione diminuisce il numero misurato di particelle che hanno subito quella deviazione; alcune particelle subiscono anche una deviazione maggiore di $90°$, inclusa una deviazione di $180°$ corrispondente a un "rimbalzo normale" sulla lamina: la frequenza di questi eventi è sempre più piccola ma non nulla.

[^geiger]: Lo stesso Geiger dal quale prende il nome il contatore Geiger, quello strumento di misura della radiazioni gracchiante che magari si è incontrato in qualche documentario su radioattività, nucleare, o in qualche film apocalittico di società post-nucleari...

[^alpha-particle]: Le particelle-$\alpha$ sono isotopi $\text{He}^{2+}$, atomi di elio che hanno 2 elettroni in meno. Per quanto ci interessa qui, le particelle-$\alpha$ sono particelle cariche positivamente.

La spiegazione dell'esperimento da parte di Rutherford è alla base del suo modello atomico: la distribuzione delle particelle-$\alpha$ misurata è compatibile un'interazione elettrica tra cariche positive puntiformi. Rutherford quindi ipotizza che la materia sia formata da atomi quasi del tutto "vuoti": le cariche positive sono concentrate in un **nucleo** di dimensioni estremamente compatte (**todo** *stima delle dimensioni da parte di Rutherford e misura di oggi*), attorno al quale sono disposte le cariche negative. **todo** *poca attenzione alle cariche negative fino al modello di **Bohr**. Atomo con nucleo positivo e cariche negative che possono trovarsi in orbite ben definite, discrete, caratterizzate da numeri atomici interi.*

**Scattering come problema di due corpi.** Qui si costruisce un problema di scattering tra due corpi puntiformi dotati di carica con lo stesso segno. Si assume che il corpo "bersaglio" rimane in quiete (*ad esempio, particella "proiettile" leggera e lenta; se questa ipotesi non è valida, bisogna considerare il "rinculo" della particella "bersaglio"*). Questo è un caso particolare di [moto centrale](physics-hs:mechanics:dynamics:motion:central:r-2), con forza inversamente proporzionale al quadrato della distanza. Infatti, scegliendo come origine il centro della carica bersaglio, la forza agente sulla carica proiettile è

$$\vec{F} = \frac{q_1 q_2}{4\pi\varepsilon} \frac{\vec{r}}{|\vec{r}|^3} \ ,$$

e l'equazione del moto è

$$m \ddot{\vec{r}} = \frac{q_1 q_2}{4\pi\varepsilon} \frac{\vec{r}}{|\vec{r}|^3} = c \frac{\vec{r}}{|\vec{r}|^3} \ .$$

Poiché la forza è repulsiva, la traiettoria della particella proiettile è un'iperbole per qualsiasi valore dei parametri del problema. L'equazione della traiettoria è data dall'espressione {eq}`eq:dynamics:central:r-2:trajectory:el`,

$$r(\theta) = \frac{\frac{l^2}{m|c|}}{-1 + \sqrt{1 + 2 \frac{E l^2}{m|c|^2}} \cos(\theta-\phi)} \ ,$$

avendo usato $\text{sign}(c) = 1$, poiché la costante $c = \frac{q_1 q_2}{4\pi\varepsilon}$ è positiva per due cariche di segno uguale.

**Caratteristiche geometriche della traiettoria - angolo di deflessione.** Le caratteristiche geometriche di questa traiettoria possono essere ricavate confrontanto l'espressione della traiettoria con l'espressione generale delle [coniche in coordinate polari](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/analytic_geometry/analytic_geometry_2d/conics.html). In particolare,
- l'eccentricità è

  $$e = \sqrt{1+2\frac{E l^2}{m c^2}}$$

<!--
- il coefficiente $d = $
-->

- il coefficienti $a$, $b$ dell'iperbole possono essere espressi in funzione dell'eccentricità e della semi-distanza tra i fuochi $c$

  $$a = \frac{c}{e} \qquad , \qquad b = \frac{\sqrt{e^2-1}}{e} c$$

Usando questi parametri geometrici è possibile determinare l'angolo di deflessione,

$$\delta = \pi - 2 \theta^* \ ,$$

con 

$$\tan \theta^* = \frac{b}{a} = \sqrt{e^2-1} = \sqrt{1 + 2 \frac{E l^2}{m c^2} - 1} = \sqrt{2 \frac{E l^2}{m c^2}} \ . $$

$$\theta^* = \frac{\pi - \delta}{2}$$

$$\tan \theta^* = \tan\left( \frac{\pi}{2} - \frac{\delta}{2} \right) = \frac{1}{\tan \frac{\delta}{2} } $$

$$\delta = 2 \text{atan} \sqrt{ \frac{m c^2}{2 E l^2} }$$

Il momento e l'energia vengono valutati all'infinito, $E = \frac{1}{2} m v_{\infty}^2$, $l = m h v_{\infty}$, avendo definito $v_{\infty}$ il modulo della velocità all'infinito e $h$ il coefficiente di impatto della traiettoria, cioè la distanza tra la tangente all'infinito e il punto bersaglio,

$$\delta = 2 \, \text{atan} \sqrt{ \frac{m c^2}{2 \frac{1}{2} m v_{\infty}^2 m^2 h^2 v_{\infty}^2} } = 2 \, \text{atan} \left( \frac{c}{m h v_{\infty}^2} \right) $$

**Sezione d'urto.**

$$2 \pi h dh = - 2 \pi R \, R \, \sin \delta \, d \delta \, r $$

con $r$ la densità relativa tra sezione di uscita e sezione di ingresso

$$\sigma = r \, R^2 = - \frac{h}{\sin \delta} \frac{dh}{d \delta}$$

$$h = \frac{c}{m v_{\infty}^2} \frac{1}{\tan \frac{\delta}{2}}$$

$$\frac{dh}{d \delta} = - \frac{c}{m v_{\infty}^2} \frac{1}{\tan^2 \frac{\delta}{2}} \frac{1}{2} \frac{1}{\cos^2 \frac{\delta}{2}} = - \frac{c}{2 m v_{\infty}^2} \frac{1}{\sin^2 \frac{\delta}{2}} $$

Riscrivendo $\sin \delta = 2 \sin \frac{\delta}{2} \cos \frac{\delta}{2}$, la sezione d'urto diventa

$$\begin{aligned}
  \sigma(\delta) & = - \frac{h}{\sin \delta} \frac{dh}{d\delta} = \frac{c}{m v_{\infty}^2} \frac{\cos \frac{\delta}{2}}{\sin \frac{\delta}{2}} \frac{1}{2 \sin \frac{\delta}{2} \cos \frac{\delta}{2}} \frac{c}{2 m v_{\infty}^2} \frac{1}{\sin^2 \frac{\delta}{2}} \\
\end{aligned}$$

$$
\qquad \rightarrow \qquad \sigma(\delta) = \left(\frac{c}{2 m v_{\infty}^2}\right)^2 \frac{1}{\sin^4 \frac{\delta}{2}} \ .
$$

Questa espressione della sezione d'urto ha un buon accordo con i dati sperimentali registrati da Geiger e Mardsen, e portano quindi Rutherford a postulare l'interazione come interazione tra due particelle con carica uguale, la particelle-$\alpha$ proiettile e il nucleo degli atomi, sufficientemente compatti e lontani gli uni dagli altri da poter trascurare le interazioni di una particella-$\alpha$ con più nuclei della sottile lamina d'oro.

**todo**
- *discussione degli effetti di rinculo, e dei risultati con proeittili ad alta energia...*


```

(modern:experiments:stern-gerlach)=
## Lo spin - Stern-Gerlach
```{dropdown} Moto di un dipolo magnetico in un campo magnetico non uniforme
:open:

```


