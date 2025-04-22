<!--
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
-->

(physics-hs:mechanics:actions:examples)=
# Esempi di forze

(physics-hs:mechanics:actions:gravitation)=
## Gravità 

(physics-hs:mechanics:actions:gravitation:newton)=
### Legge di gravitazione universale
La forza $\vec{F}_{12}$ esercitata da un corpo di massa $m_2$ in $P_2$ su un corpo di massa $m_1$ in $P_1$ è descritta dalla **legge di gravitazione universale di Newton**,

$$\vec{F}_{12} = G \dfrac{m_1 m_2}{r_{12}^2} \hat{r}_{12} \ ,$$

avendo indicato con $\vec{r}_{12} = (P_2 - P_1)$ il vettore che punta dal punto $P_1$ al punto $P_2$, $r_{12} = |\vec{r}_{12}|$ il suo modulo, e $\hat{r}_{12} = \frac{\vec{r}_{12}}{|\vec{r}_{12}|}$ il vettore unitario lungo la stessa direzione, e con 

$$G = 6.67 \cdot 10^{-11} \frac{N \, m^2}{kg^2}$$ 

la **costante di gravitazione universale**, considerata una costante della natura. **todo**

```{admonition}
:class: tip

La legge di gravitazione universale è una legge di **interazione a distanza**, in cui la forza agente su un corpo in un punto $P_0(t)$ nello spazio dipende dalla posizione di un altro corpo nel punto $P_1(t)$ nello spazio nello stesso istante di tempo. L'espressione dell'interazione gravitazionale tramite la legge di gravitazione universale è quindi in contrasto con i postulati della fisica di Einstein, secondo la quale la velocità massima di trasmissione dell'informazione nello spazio è finita e uguale alla velocità della luce, $c \sim 3 \cdot 10^{8} \, m/s$.

```

(physics-hs:mechanics:actions:gravitation:field)=
### Campo di gravità
Il campo di gravità generato da una massa $m_2$ posta in $P_2$ è **todo** una funzione dello spazio che associa a ogni punto $P$ un vettore,

$$\vec{g}(\vec{r}_1) = \dfrac{\vec{F}_{12}}{m_1} = G \dfrac{m_2}{r_{12}^2} \hat{r}_{12} \ ,$$

- **todo** abituarsi al concetto di campo, introdotto a partire dalla definizione operativa con *massa test*
- **todo** PSCE
- **todo** noto il campo di gravità $\vec{g}(P)$, la forza di gravità percepita da un sistema di massa $m$ in $P$ può essere scritta come

  $$\vec{F}_g = m \vec{g}(P)$$

**Energia potenziale gravitazionale.** E' possibile dimostrare che il campo gravitazionale è ... **todo**

$$V(P) = - G \, m \, m_1 \frac{1}{|P - P_1|}$$

(physics-hs:mechanics:actions:gravitation:earth)=
### Campo di gravità nei pressi della superficie terrestre
All'interno di un dominio limitato nei pressi della superficie terrestre, è comune approssimare il campo di gravitazione terrestre come un campo uniforme, diretto lungo la verticale locale verso il centro della terra e di intensità $g = G \frac{M_E}{R_E^2}$.

E' possibile derivare questo modello, approssimando il vettore posizione rispetto al centro della terra $P - P_E \sim R_E \hat{r}$ e il versore che identifica la direzione da un punto del dominio al centro della Terra con la verticale locale $\hat{r}_{12} \sim - \hat{z}$

$$\vec{g}(\vec{r}) = - G \dfrac{M_E}{R_E^2} \hat{z} = - g \hat{z} \ .$$

La forza di gravità percepita da un corpo di massa $m$ nei pressi della superficie terrestre è quindi 

$$\vec{F}_g = - m g \hat{z} \ ,$$

quello che viene comunemente chiamato **peso**.

**Energia potenziale gravitazionale.** E' possibile dimostrare che il potenziale gravitazionale nei pressi della superficie terrestre diventa

$$V(P) = m \, g \, z_P \ .$$

```{dropdown} Dimostrazione.
:open:

Con l'espansione in serie, con $P - P_E = R_E \hat{r} + \vec{d}$, e $|\vec{d}| \ll R_E$

$$\begin{aligned}
  V(P) & = - G \, m \, M_E \frac{1}{|P - P_E|} = \\
       & \approx G M_E \, m \left[ - \frac{1}{R_E} + \frac{R_E \hat{r} \cdot \vec{d}}{R_E^3}  \right]   = \\
       & = \underbrace{- m \, \frac{ G M_E}{R_E}}_{\text{const}} + m \, \underbrace{\frac{G \, M_E}{R_E^2}}_{= g} \underbrace{\hat{r} \cdot \vec{d}}_{= z}
\end{aligned}$$


```

(physics-hs:mechanics:actions:spring)=
## Azioni elastiche: molle lineari

Secondo la legge di Hooke, il comportamento di una molla elastica lineare ideale è descritto dall'equazione costitutiva

$$\vec{F} = - k (P - P_0) \ ,$$ (eq:spring)

essendo $\vec{F}$ la forza trasmessa dalla molla al corpo in $P$, $P_0$ l'altra estremità della molla, $k$ la costante elastica della molla.

```{admonition} R.Hooke, 1635-1703
:class: dropdown

Assistente di R.Boyle presso l'università di Oxford, e in seguito curatore degli esperimenti presso la Royal Society, fu protagonista come inventore e perfezionatore di strumenti scientifici negli anni della rivoluzione scientifica del XVII secolo. Tra le sue attività principali,
- la caratterizzazione di molle e materiali elastici, con la legge di Hooke come legge costitutiva di materiali elastici lineari
- l'utilizzo delle proprietà delle molle all'interno di strumenti meteorologici, per la misura della pressione atmosferica
- l'utilizzo di molle per l'alimentazione di orologi che fossero insensibili alle accelerazioni dello strumento
- la realizzazione di pompe pneumatiche che permisero a R.Boyle di svolgere i suoi esperimenti sui gas, e di formulare la [legge di Boyle](physics-hs:thermodynamics:matter:gases:ideal:experiments:boyle) per descrivere il comporamento a temperatura costante di gas rarefatti
- strumenti ottici per le osservazioni micsorsopiche e astronomiche

```

**todo** *Considerare il caso con lunghezza a riposo non nulla; discutere il caso 1-dimensionale; aggiungere esempi*

<!--
$$F = k (\ell - \ell_0) \ ,$$

essendo $F$ il valore assoluto della forza trasmessa dalla molla, $k$ la costante elastica della molla, $\ell_0$ la lunghezza a riposo della molla, e $\ell$ la lunghezza nella configurazione considerata.
-->

**Energia potenziale.** 

Il lavoro elementare della forza {eq}`eq:spring` di una molla elastica è

$$\begin{aligned}
 \delta L & = \vec{F} \cdot d \vec{r} = \\
 & = - k (P-P_0) \cdot d \vec{r} = \\
 & = - k (\vec{r} - \vec{r}_0) \cdot d \vec{r} = \\
 & = - k (\vec{r} - \vec{r}_0) \cdot d ( \vec{r} - \vec{r}_0 ) = \\
 & = - d \left( \dfrac{1}{2} k (\vec{r} - \vec{r}_0) \cdot (\vec{r} - \vec{r}_0) \right) = \\
 & = - d \left(  \dfrac{1}{2} k \left| \vec{r} - \vec{r}_0 \right|^2 \right) \ ,
\end{aligned}$$

avendo qui ipotizzato che la costante elastica $k$ sia costante e che il punto $P_0$ non si muova. Nel caso in cui si spostano entrambi gli estremi della molla, il lavoro rotale compiuto dalla molla è la somma del lavoro fatto a entrambi gli estremi

$$\begin{aligned}
  \delta L
  & = \vec{F}_1 \cdot d \vec{r}_1 + \vec{F}_2 \cdot d \vec{r}_2 = \\
  & = \vec{F}_1 \cdot d \vec{r}_1 - \vec{F}_1 \cdot d \vec{r}_2 = \\
  & = \vec{F}_1 \cdot \left( d \vec{r}_1 - \cdot d \vec{r}_2 \right) = \\
  & = - k ( \vec{r}_1 - \vec{r}_2 ) \cdot d \left( \vec{r}_1 - \vec{r}_2 \right) = \\
  & = - d \left( \dfrac{1}{2} k ( \vec{r}_1 - \vec{r}_2 ) \cdot \left( d \vec{r}_1 - \vec{r}_2 \right) \right) = \\
  & = - d \left( \dfrac{1}{2} k | \vec{r}_1 - \vec{r}_2 |^2 \right) \ , 
\end{aligned}$$

poiché la forza all'estremità $1$ è uguale e contraria alla forza all'estremità $2$, $\vec{F}_1 = - \vec{F}_2$. 

**todo** *Considerare il caso con lunghezza a riposo non nulla*

$$\delta L =  F d \ell = k (\ell - \ell_0) d \ell$$

$$L = \int_{\ell_1}^{\ell_2} = \left[ \frac{1}{2} k \ell^2 - k \ell_0 \, \ell \right]\bigg|_{\ell_1}^{\ell_2}$$

$$V = \frac{1}{2} k (\ell - \ell_0)^2$$

(physics-hs:mechanics:actions:contact)=
## Azioni di contatto

(physics-hs:mechanics:actions:contact:ideal-constraints)=
### Reazioni vincolari di vincoli ideali
I vincoli ideali sono modelli di vincolo che **non compiono lavoro netto**, e per questo sono **elementi conservativi**. Come dovrebbe risultare evidente nei paragrafi successivi dalle espressioni delle velocità relative e dalle azioni scambiate, 

$$\begin{aligned}
P & = \vec{v}_1     \cdot \vec{F}_{21} + \vec{v}_2     \cdot \vec{F}_{12} 
    + \vec{\omega}_1 \cdot \vec{M}_{21} + \vec{\omega}_2 \cdot \vec{M}_{12} = \\ 
  & = ( \vec{v}_1 - \vec{v}_2 ) \cdot \vec{F}_{21}
    + ( \vec{\omega}_1 - \vec{\omega}_2 ) \cdot \vec{M}_{21} = \\ 
  & = \vec{v}^{rel}_{21} \cdot \vec{F}_{21}
    + \vec{\omega}^{rel}_{21} \cdot \vec{M}_{21} \ ,
\end{aligned}$$

entrambi i termini sono nulli, o perché il moto relativo è nullo, o le azioni agiscono in direzione ortogonale ai moti relativi.

(physics-hs:mechanics:actions:contact:ideal-constraints:fix)=
#### Incastro
Il vincolo di incastro impedisce sia il moto sia la rotazione relativa,

$$
\begin{cases}
  \vec{0} = \vec{v}^{rel}_{21}     = \vec{v}_{2}     - \vec{v}_{1} \\
  \vec{0} = \vec{\omega}^{rel}_{21} = \vec{\omega}_{2} - \vec{\omega}_{1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \qquad \vec{F}_{12} = - \vec{F}_{21} \\
  \qquad \vec{M}_{12} = - \vec{M}_{21} \\
\end{cases}
$$

(physics-hs:mechanics:actions:contact:ideal-constraints:skate)=
#### Pattino
Il vincolo di pattino impedisce il moto relativo in una direzione e la rotazione relativa.

$$
\begin{cases}
  \quad \forall \ \vec{v}^{rel}_{\hat{t},21}     = \vec{v}_{\hat{t},2}     - \vec{v}_{\hat{t},1} \\
          0  = v^{rel}_{\hat{n},21}     = v_{\hat{n},2}     - v_{\hat{n},1} \\
  \vec{0} = \vec{\omega}^{rel}_{21} = \vec{\omega}_{2} - \vec{\omega}_{1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \vec{0} = \vec{F}_{\hat{t},12} = \vec{F}_{\hat{t},21} \\
  \qquad F_{\hat{n},12} = - F_{\hat{n},21} \\
  \qquad \vec{M}_{12} = - \vec{M}_{21} \\
\end{cases}
$$

(physics-hs:mechanics:actions:contact:ideal-constraints:hinge-cylindrical)=
#### Cerniera (cilindrica)
Il vincolo di pattino impedisce il moto relativo e consente solo la rotazione attorno a un asse.

$$
\begin{cases}
  \vec{0} = \vec{v}^{rel}_{21}     = \vec{v}_{2}     - \vec{v}_{1} \\
  \quad \forall \ \omega^{rel}_{\hat{t},21} = \omega_{\hat{t},2} - \omega_{\hat{t},1} \\
  \vec{0} = \vec{\omega}^{rel}_{\hat{n},21} = \vec{\omega}_{\hat{n},2} - \vec{\omega}_{\hat{n},1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \qquad \vec{F}_{12} = - \vec{F}_{21} \\
  0 =  M_{\hat{t},12} = M_{\hat{t},21} \\
  \qquad \vec{M}_{\hat{n},12} = - \vec{M}_{\hat{n},21} \\
\end{cases}
$$

(physics-hs:mechanics:actions:contact:ideal-constraints:hinge-spherical)=
#### Cerniera (sferica)
Il vincolo di pattino impedisce il moto relativo, consentendo una rotazione generica.

$$
\begin{cases}
  \vec{0} = \vec{v}^{rel}_{21}     = \vec{v}_{2}     - \vec{v}_{1} \\
  \quad \forall \vec{\omega}^{rel}_{21} = \vec{\omega}_{2} - \vec{\omega}_{1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \qquad \vec{F}_{12} = - \vec{F}_{21} \\
  \vec{0} =  \vec{M}_{12} = \vec{M}_{21} \\
\end{cases}
$$

(physics-hs:mechanics:actions:contact:ideal-constraints:cart)=
#### Carrello
Il vincolo di carello può essere pensato come la combinazione di un pattino e di una cerniera

$$
\begin{cases}
  \quad \forall \ \vec{v}^{rel}_{\hat{t},21}     = \vec{v}_{\hat{t},2}     - \vec{v}_{\hat{t},1} \\
          0  = v^{rel}_{\hat{n},21}     = v_{\hat{n},2}     - v_{\hat{n},1} \\
  \quad \forall \ \omega^{rel}_{\hat{t},21} = \omega_{\hat{t},2} - \omega_{\hat{t},1} \\
  \vec{0} = \vec{\omega}^{rel}_{\hat{n},21} = \vec{\omega}_{\hat{n},2} - \vec{\omega}_{\hat{n},1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \vec{0} = \vec{F}_{\hat{t},12} = \vec{F}_{\hat{t},21} \\
  \qquad F_{\hat{n},12} = - F_{\hat{n},21} \\
  0 =  M_{\hat{t},12} = M_{\hat{t},21} \\
  \qquad \vec{M}_{\hat{n},12} = - \vec{M}_{\hat{n},21} \\
\end{cases}
$$

(physics-hs:mechanics:actions:contact:ideal-constraints:monolateral)=
#### Appoggio
Il vincolo di appoggio è un vincolo monolatero **todo** *aggiungere descrizione*

(physics-hs:mechanics:actions:contact:friction)=
### Attrito
(physics-hs:mechanics:actions:contact:friction:static)=
#### Attrito statico

L'attrito statico è la forma di attrito che si manifesta tra due corpi quando non c'è moto relativo tra di essi, come una forza tangenziale alla superficie di contatto. Il più semplice modello di attrito statico prevede che il modulo massimo della forza di attrito $F^s_{max}$ che si può esercitare tra due corpi è proporzionale alla reazione normale tra di essi, $N$,

$$F^s_{max} = \mu^s \, N \ .$$

Il coefficiente di proporzionalità $\mu^s$ viene definito **coefficiente di attrito statico**. In generale, le forze di attrito statico sono determinate dalle condizioni di equilibrio del corpo, se queste condizioni sono ottenibili ed  è soddisfatta la relazione

$$|F^s| \ge F^s_{max} \ .$$


(physics-hs:mechanics:actions:contact:friction:dynamic)=
#### Attrito dinamico

L'attrito dinamico è la forma di attrito che si manifesta tra due corpi a contatto e in moto relativo, come una forza tangenziale alla superficie di contatto. Il più semplice modello di attrito statico prevede che la forza di attrito dinamico sia proporzionale alla reazione normale tra i due corpi e diretta in verso opposto alla velocità relativa,

$$\vec{F}_{12} = - \mu^d N \frac{\vec{v}_{12}}{|\vec{v}_{12}|} \ ,$$

avendo definito $\vec{F}_{12}$ come la forza agente sul corpo $1$ a causa del corpo $2$, e $\vec{v}_{12} = \vec{v}_1 - \vec{v}_2$ la velocità del corpo $1$ relativa al corpo $2$.
 
(physics-hs:mechanics:actions:contact:pure-rolling)=
### Puro rotolamento
In generale, è necessario garantire l'attrito per garantire la condizione di puro rotolamento.
Nella condizione di puro rotolamento, i punti materiali delle due superfici in corrispondenza del punto di contatto hanno la stessa velocità.

Nonostante la presenza di attrito per garantire il puro rotolamento, questo vincolo è un vincolo ideale con potenza nulla: la forze scambiate tra le due superfici sono uguali e opposte per il terzo [principio della dinamica - azione e reazione](physics-hs:mechanics:dynamics:principles), mentre la velocità dei punti nei quali le forze sono applicate è uguale per la condizione di puro rotolamento.

**todo**
- ragionare sul punto di contatto...(i punti materiali a contatto cambiano da un istante all'altro, in generale)
- fare bilancio di potenze
