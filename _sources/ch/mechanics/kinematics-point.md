<!--
````{only} html
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
````
-->

(physics-hs:mechanics:kinematics:point)=
# Cinematica del punto

<!--
## Prime definizioni
Quantità vettoriali...
- spostamento, composizione spostamenti
- velocità media, velocità puntuale
- accelerazione media, accelerazione puntuale
-->


## Configurazione e stato in un moto regolare (differenziabile)
La cinematica di un punto $P(t)$ è completamente definita dalla sua posizione nello spazio in funzione del tempo. La configurazione di un sistema puntiforme in un istante temporale è data dalla sua posizione rispetto a un punto $O$ preso come origine, come riferimento.

**Spostamento, velocità e accelerazione media in un intervallo di tempo $\ \Delta t_{12} = t_2 - t_1$.** Per un moto qualsiasi di un punto $P(t)$ riferito a un punto $O$ fisso, vegono definiti

$$\begin{aligned}
   \Delta \vec{r}_{P,12} & := P(t_2) - P(t_1) & \text{(spostamento di $P$ rispetto a $O$)} \\
   \langle \vec{v}_{P;12} \rangle & := \frac{\Delta \vec{r}_{P,12}}{\Delta t_{12}} & \text{(velocità media di $P$ rispetto a $O$)} \\
   \langle \vec{a}_{P,12} \rangle & := \frac{\Delta \vec{v}_{P,12}}{\Delta t_{12}} & \text{(accelerazione media di $P$ rispetto a $O$)} \\
\end{aligned}$$

**Velocità e accelerazioni istantanee.** Lo stato di un sistema puntiforme in un determinato istante temporale è definito dalla sua posizione e dalla sua velocità. Rispetto a un'origine considerata indipendente dal tempo, la posizione del punto $P$ è definita dal vettore euclideo $\vec{r}_P(t) = P(t) - O$ che congiunge l'origine $O$ con il punto $P$, la velocità e l'accelerazione sono rispettivamente la derivata prima e seconda della posizione rispetto al tempo,

$$\begin{aligned}
   \vec{r}_P(t) & := P(t) - O & \text{(posizione di $P$ rispetto a $O$)} \\
   \vec{v}_P(t) & := \frac{d \vec{r}_P}{dt}(t) & \text{(velocità di $P$ rispetto a $O$)} \\
   \vec{a}_P(t) & := \frac{d^2 \vec{r}_P}{dt^2}(t) = \frac{d \vec{v}_P}{dt}(t) & \text{(accelerazione di $P$ rispetto a $O$)} \\
\end{aligned}$$

```{prf:example} ...
:label: kinematics:avg

Un atleta si allena correndo attorno a un isolato con perimetro a forma di triangolo rettangolo, con due cateti di lunghezza $c_1 = 300 \, m$ e $c_2 = 400 \, m$. ...

Viene chiesto di calcolare:
- la velocità media dopo 5 giri completi;
- ...

```

(physics-hs:mechanics:kinematics:point:motion)=
## Moti particolari

(physics-hs:mechanics:kinematics:point:motion:a-0)=
### Moto non accelerato - o moto rettilineo uniforme.
Un moto non accelerato di un punto $P$ rispetto a un sistema di riferimento con origine in $O$ può essere definito dalla condizione di accelerazione nulla 

$$\vec{a}_P = \ddot{\vec{r}}_P(t) = \vec{0} \ ,$$

la cui integrazione due volte in tempo fornisce le leggi della velocità e dello spazio

$$\begin{cases}
  \vec{v}_P(t) & = \vec{c}_1 \\
  \vec{r}_P(t) & = \vec{c}_1 \, t + \vec{c}_2 \ .
\end{cases}$$

La condizione di accelerazione nulla implica accelerazione la condizione di **velocità costante**; la condizione di velocità costante implica che il moto del punto si svolge lungo una **traiettoria rettilinea**: l'equazione $\vec{r}_P(t) = \vec{c}_1 \, t + \vec{c}_2$ è infatti l'equazione parametrica di una retta nello spazio, con il tempo $t$ come parametro.

**Scelta conveniente sistemi di riferimento.** Una volta identificata la retta sulla quale si svolge la traiettoria, può risultare conveniente introdurre un sistema di coordinate 1-dimensionale per parametrizzare la retta.

**Costanti di integrazione.** Poiché si parte da una condizione sull'accelerazione e si integra due volte nel tempo per ottenere la posizione in funzione del tempo, compaiono 2 costanti di integrazione (vettoriali) $\vec{c}_1$, $\vec{c}_2$. Per determinare univocamente un moto non accelerato servono due condizioni (vettoriali) indipendenti e compatibili[^ic] tra di loro, come mostrato negli esempi {prf:ref}`kinematics:point:uniform:cauchy` e {prf:ref}`kinematics:point:uniform:points`.

[^ic]: Indipendenti: devono fornire tutte le informazioni necessarie (non devono ripetere la stessa informazione); compatibili: devono fornire informazioni che non sono tra di loro mutuamente esclusive.

<!--
Come dimostrato in appendice, il [moto non accelerato è un moto lungo una traiettoria rettilinea a velocità costante](physics-hs:mechanics:kinematics:notes:point:a-0), 
-->

```{prf:example} Stato iniziale
:label: kinematics:point:uniform:cauchy
:class: dropdown

Note le condizioni iniziali sullo stato (posizione e velocità),

$$\begin{cases}
  \vec{r}(t_0) = \vec{r}_0 \\
  \vec{v}(t_0) = \vec{v}_0 \ ,
\end{cases}$$
 
le leggi del moto diventano

$$\begin{cases}
  \vec{v}_P    & = \vec{v}_0  \\
  \vec{r}_P(t) & = \vec{v}_0 \, ( t - t_0 ) + \vec{r}_0 \ ,
\end{cases}$$

```


```{prf:example} Posizione nota in due istanti noti
:label: kinematics:point:uniform:points
:class: dropdown

Nota la posizione in due istanti di tempo noti,

$$\begin{cases}
  \vec{r}(t_0) = \vec{r}_0 \\
  \vec{r}(t_1) = \vec{r}_1 \ ,
\end{cases}$$

le leggi del moto diventano 

$$\begin{cases}
  \vec{v}_P    & = \frac{\vec{r}_1 - \vec{r}_0}{t_1 - t_0} \\
  \vec{r}_P(t) & = \vec{v}_P \, ( t - t_0 ) + \vec{r}_0 \ ,
\end{cases}$$

```

<span style="color:red">
**todo** moto rettilineo; uso dei sistemi di riferimento
</span>

(physics-hs:mechanics:kinematics:point:motion:a)=
### Moto uniformemente accelerato
Un moto uniformemente accelerato di un punto $P$ rispetto a un sistema di riferimento con origine in $O$ può essere definito dalla condizione di accelerazione costante

$$\vec{a}_P = \ddot{\vec{r}}_P(t) = \vec{a} \ ,$$

la cui integrazione due volte in tempo fornisce le leggi della velocità e dello spazio

$$\begin{cases}
  \vec{v}_P(t) & = \vec{a} t               + \vec{c}_1 \\
  \vec{r}_P(t) & = \dfrac{1}{2}\vec{a} t^2 + \vec{c}_1 \, t + \vec{c}_2 \ .
\end{cases}$$

Tra i moti uniformemente accelerati si possono distinguere due situazioni: 
1. il **moto rettilineo uniformemente accelerato**, se la velocità iniziale è nulla o allineata con l'accelerazione costante
2. il **moto parabolico**, se la velocità iniziale e l'accelerazione non sono allineate; in questo caso, il [moto uniformemente accelerato è un moto piano](physics-hs:mechanics:kinematics:notes:point:motion:a:planar), che avviene nel piano passante per un punto della traiettoria e nel quale giacciono i vettori velocità e accelerazione. 

**Scelta conveniente sistemi di riferimento.** Per un moto rettilineo uniformemente accelerato, una volta identificata la retta sulla quale si svolge la traiettoria, può risultare conveniente introdurre un sistema di coordinate 1-dimensionale per parametrizzare la retta. Per un moto parabolico, una volta identificato il piano nel quale si svolge il moto, può risultare conveniente introdurre un sistema di coordinate (cartesiano? perché no) 2-dimensionale per parametrizzare il piano del moto.

**Costanti di integrazione.** Poiché si parte da una condizione sull'accelerazione e si integra due volte nel tempo per ottenere la posizione in funzione del tempo, compaiono 2 costanti di integrazione (vettoriali) $\vec{c}_1$, $\vec{c}_2$. Per determinare univocamente un moto non accelerato servono due condizioni (vettoriali) indipendenti e compatibili[^ic] tra di loro, come mostrato negli esempi {prf:ref}`kinematics:point:accel:cauchy` e {prf:ref}`kinematics:point:accel:points`.

```{prf:example} Stato iniziale
:label: kinematics:point:accel:cauchy
:class: dropdown

Note le condizioni iniziali sullo stato (posizione e velocità),

$$\begin{cases}
  \vec{r}(t_0) = \vec{r}_0 \\
  \vec{v}(t_0) = \vec{v}_0 \ ,
\end{cases}$$
 
le leggi del moto diventano

$$\begin{cases}
  \vec{v}_P(t) & = \vec{a} t                     + \vec{v}_0  \\
  \vec{r}_P(t) & = \dfrac{1}{2}\vec{a} (t-t_0)^2 + \vec{v}_0 \, ( t - t_0 ) + \vec{r}_0 \ ,
\end{cases}$$

```

```{prf:example} Posizione nota in due istanti noti
:label: kinematics:point:accel:points
:class: dropdown

$$\begin{cases}
  \vec{r}_0 & = \dfrac{1}{2}\vec{a} t_0^2 + \vec{c}_1 \, t_0 + \vec{c}_2 \\ 
  \vec{r}_1 & = \dfrac{1}{2}\vec{a} t_1^2 + \vec{c}_1 \, t_1 + \vec{c}_2 \ ,
\end{cases}$$

$$\begin{aligned}
  \vec{c}_1 & = \left[ \vec{r}_1 - \vec{r}_0 - \dfrac{1}{2} \vec{a} \left( t_1^2 - t_0^2 \right) \right] \dfrac{1}{t_1 - t_0} = \\
   & = \frac{\vec{r}_1 - \vec{r}_0 }{t_1-t_0} - \dfrac{1}{2} \vec{a} \left( t_0 + t_1 \right) \\
  \vec{c}_2 & = \vec{r}_0 - \dfrac{1}{2} \vec{a} t_0^2 - t_0 \left[ \frac{\vec{r}_1 - \vec{r}_0 }{t_1-t_0} - \dfrac{1}{2} \vec{a} \left( t_0 + t_1 \right) \right] = \\
   & = \dfrac{1}{2} \vec{a} t_0 t_1 + \frac{\vec{r}_0 \, t_1 - \vec{r}_1 \, t_0}{t_1-t_0}
\end{aligned}$$

```

<span style="color:red">
**todo** moto piano (rettilineo se $\vec{a}$, $\vec{v}_0$ sono allineati); uso dei sistemi di riferimento
</span>

(physics-hs:mechanics:kinematics:point:motion:circular)=
### Moto circolare
Il moto di un punto su una traiettoria circolare può essere rappresentato comodamente usando un sistema di **coordinate polari** con origine coincidente con il centro $C$ della circonferenza

$$
r = R  \qquad , \qquad  \theta = \theta_P(t)
$$

con la distanza del punto $P$ dal centro della circonferenza $C$ costante e l'angolo $\theta_P(t)$ come coordinata libera che descrive il moto; oppure usando un sistema di **coordinate cartesiane** che descrivono il piano del moto

$$\begin{aligned}
  P(t) - C 
  & = R \cos \theta_P(t) \, \hat{x} + R \sin \theta_P(t) \, \hat{y} = \\
  & = R \hat{r}(P(t)) \\
\end{aligned}$$ (eq:kinematics:point:circuilar:p)

avendo usato il versore in direzione radiale della base locale indotta dal sistema di coordinate polari,

$$\begin{aligned}
  \hat{r}     \left( P(t) \right) & = \hat{x} \, \cos \theta_P(t) + \hat{y} \, \sin \theta_P(t) \\
  \hat{\theta}\left( P(t) \right) & =-\hat{x} \, \sin \theta_P(t) + \hat{y} \, \cos \theta_P(t) \\
\end{aligned}$$

```{note}
I versori indotti dalle coordinate polari dipendono dalla posizione del punto $P$ nello spazio e quindi, quando questa dipendente dal tempo, funzione del tempo $t$. E' necessario ricordarsi di questa dipendenza quando si usa l'espressione $P(t) - C = R \hat{r}(P(t))$ per calcolare la velocità e l'accelerazione del punto $P(t)$, come mostrato di seguito. In particolare, si dimostra che

$$\begin{aligned}
\dfrac{d \hat{r}}{dt} & = \dot{\theta}_P(t) \, \hat{\theta}(P(t)) \\
\dfrac{d \hat{\theta}}{dt} & = - \dot{\theta}_P(t) \, \hat{r}(P(t))
\end{aligned}$$
```

Data l'espressione {eq}`eq:kinematics:point:circuilar:p` della posizione del punto $P(t)$ espressa in funzione del tempo, è possibile calcolare la velocità e l'accelerazione del punto, valutando le derivate prima e seconda della posizione rispetto al tempo,

$$\begin{cases}
  \vec{v}_P(t) & = R \dot{\theta}_P(t) \left( -\sin \theta_P(t) \hat{x} + \cos \theta_P(t) \hat{y} \right) = \\
               & = R \dot{\theta}_P(t) \hat{\theta}(P(t)) \\
  \vec{a}_P(t) & = \hat{x} R \left[ - \ddot{\theta}_P(t) \, \sin \theta_P(t) - \dot{\theta}_P^2 \cos \theta_P(t) \right]
                 + \hat{y} R \left[   \ddot{\theta}_P(t) \, \cos \theta_P(t) - \dot{\theta}_P^2 \sin \theta_P(t) \right] = \\
               & = R \ddot{\theta}_P(t) \left( -\sin \theta_P(t) \hat{x} + \cos \theta_P(t) \hat{y} \right)
                 + R \ddot{\theta}_P^2(t) \left( -\cos \theta_P(t) \hat{x} - \sin \theta_P(t) \hat{y} \right) = \\
               & = R \ddot{\theta}_P(t) \hat{\theta}(P(t)) - R \dot{\theta}_P^2(t) \hat{r}(P(t)) \ .
\end{cases}$$

La **velocità** ha direzione $\hat{\theta}(P(t))$ ed è quindi **tangente alla traiettoria** circolare. L'accelerazione può avere una direzione generica nel piano, e può avere:
 - componente tangente alla traiettoria, l'accelerazione tangenziale, $R \ddot{\theta}^2_P(t) \hat{\theta}(P(t))$
 - componente normale alla traiettoria verso il centro della traiettoria, l'accelerazione normale o **centripeta**, $-R \dot{\theta}^2_P(t) \hat{r}(P(t))$



(physics-hs:mechanics:kinematics:point:motion:circular-uniform)=
#### Moto circolare uniforme
Il moto circolare uniforme ha modulo della velocità costante, 

$$|\vec{v}_P(t)| = |R \dot \theta_P(t)| \ .$$

e quindi la derivata nel tempo della coordinata $\theta_P$ è costante,

$$\dot\theta_P(t) = \Omega \ .$$

Quindi, l'accelerazione tangenziale un punto $P$ che compie un moto circolare uniforme è nulla. L'accelerazione ha solo componente componente centripeta.

$$\begin{aligned}
  \vec{v}_P & = R \Omega \hat{\theta}_P \\
  \vec{a}_P & =- R \Omega^2 \hat{r}_P \\
\end{aligned}$$

<!-- - **todo** pulsazione, periodo, frequenza,... -->

(physics-hs:mechanics:kinematics:point:motion:harmonic)=
### Moto armonico lungo un segmento
Un moto armonico lungo un segmento può essere definito come la proiezione di un punto che compie un moto circolare uniforme su una circonferenza che ha il segmento come diametro **todo**




