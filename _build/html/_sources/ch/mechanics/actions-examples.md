```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```

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

### Campo di gravità
Il campo di gravità generato da una massa $m_2$ posta in $P_2$ è **todo** una funzione dello spazio che associa a ogni punto $P$ un vettore,

$$\vec{g}(\vec{r}_1) = \dfrac{\vec{F}_{12}}{m_1} = G \dfrac{m_2}{r_{12}^2} \hat{r}_{12} \ ,$$

- **todo** abituarsi al concetto di campo, introdotto a partire dalla definizione operativa con *massa test*
- **todo** PSCE
- **todo** noto il campo di gravità $\vec{g}(P)$, la forza di gravità percepita da un sistema di massa $m$ in $P$ può essere scritta come

  $$\vec{F}_g = m \vec{g}(P)$$

**Energia potenziale gravitazionale.** E' possibile dimostrare che il campo gravitazionale è ... **todo**

$$V(P) = - G \, m \, m_1 \frac{1}{|P - P_1|}$$

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
## Azioni elastiche: molle lineari

Secondo la legge di Hooke, il comportamento di una molla elastica lineare ideale è descritto dall'equazione costitutiva

$$F = k (\ell - \ell_0) \ ,$$

essendo $F$ il valore assoluto della forza trasmessa dalla molla, $k$ la costante elastica della molla, $\ell_0$ la lunghezza a riposo della molla, e $\ell$ la lunghezza nella configurazione considerata.

**Energia potenziale.** 

$$\delta L =  F d \ell = k (\ell - \ell_0) d \ell$$

$$L = \int_{\ell_1}^{\ell_2} = \left[ \frac{1}{2} k \ell^2 - k \ell_0 \, \ell \right]\bigg|_{\ell_1}^{\ell_2}$$

$$V = \frac{1}{2} k (\ell - \ell_0)^2$$

## Azioni di contatto

### Reazioni vincolari di vincoli ideali
I vincoli ideali sono modelli di vincolo che **non compiono lavoro netto**, e per questo sono **elementi conservativi**. Come dovrebbe risultare evidente nei paragrafi successivi dalle espressioni delle velocità relative e dalle azioni scambiate, 

$$\begin{aligned}
P & = \mathbf{v}_1     \cdot \mathbf{F}_{21} + \mathbf{v}_2     \cdot \mathbf{F}_{12} 
    + \symbf{\omega}_1 \cdot \mathbf{M}_{21} + \symbf{\omega}_2 \cdot \mathbf{M}_{12} = \\ 
  & = ( \mathbf{v}_1 - \mathbf{v}_2 ) \cdot \mathbf{F}_{21}
    + ( \symbf{\omega}_1 - \symbf{\omega}_2 ) \cdot \mathbf{M}_{21} = \\ 
  & = \mathbf{v}^{rel}_{21} \cdot \mathbf{F}_{21}
    + \symbf{\omega}^{rel}_{21} \cdot \mathbf{M}_{21} \ ,
\end{aligned}$$

entrambi i termini sono nulli, o perché il moto relativo è nullo, o le azioni agiscono in direzione ortogonale ai moti relativi.

#### Incastro
Il vincolo di incastro impedisce sia il moto sia la rotazione relativa,

$$
\begin{cases}
  \mathbf{0} = \mathbf{v}^{rel}_{21}     = \mathbf{v}_{2}     - \mathbf{v}_{1} \\
  \mathbf{0} = \symbf{\omega}^{rel}_{21} = \symbf{\omega}_{2} - \symbf{\omega}_{1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \qquad \mathbf{F}_{12} = - \mathbf{F}_{21} \\
  \qquad \mathbf{M}_{12} = - \mathbf{M}_{21} \\
\end{cases}
$$

#### Pattino
Il vincolo di pattino impedisce il moto relativo in una direzione e la rotazione relativa.

$$
\begin{cases}
  \quad \forall \ \mathbf{v}^{rel}_{\hat{\mathbf{t}},21}     = \mathbf{v}_{\hat{\mathbf{t}},2}     - \mathbf{v}_{\hat{\mathbf{t}},1} \\
          0  = v^{rel}_{\hat{\mathbf{n}},21}     = v_{\hat{\mathbf{n}},2}     - v_{\hat{\mathbf{n}},1} \\
  \mathbf{0} = \symbf{\omega}^{rel}_{21} = \symbf{\omega}_{2} - \symbf{\omega}_{1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \mathbf{0} = \mathbf{F}_{\hat{\mathbf{t}},12} = \mathbf{F}_{\hat{\mathbf{t}},21} \\
  \qquad F_{\hat{\mathbf{n}},12} = - F_{\hat{\mathbf{n}},21} \\
  \qquad \mathbf{M}_{12} = - \mathbf{M}_{21} \\
\end{cases}
$$

#### Cerniera (cilindrica)
Il vincolo di pattino impedisce il moto relativo e consente solo la rotazione attorno a un asse.

$$
\begin{cases}
  \mathbf{0} = \mathbf{v}^{rel}_{21}     = \mathbf{v}_{2}     - \mathbf{v}_{1} \\
  \quad \forall \ \omega^{rel}_{\hat{\mathbf{t}},21} = \omega_{\hat{\mathbf{t}},2} - \omega_{\hat{\mathbf{t}},1} \\
  \mathbf{0} = \symbf{\omega}^{rel}_{\hat{\mathbf{n}},21} = \symbf{\omega}_{\hat{\mathbf{n}},2} - \symbf{\omega}_{\hat{\mathbf{n}},1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \qquad \mathbf{F}_{12} = - \mathbf{F}_{21} \\
  0 =  M_{\hat{\mathbf{t}},12} = M_{\hat{\mathbf{t}},21} \\
  \qquad \mathbf{M}_{\hat{\mathbf{n}},12} = - \mathbf{M}_{\hat{\mathbf{n}},21} \\
\end{cases}
$$

#### Cerniera (sferica)
Il vincolo di pattino impedisce il moto relativo, consentendo una rotazione generica.

$$
\begin{cases}
  \mathbf{0} = \mathbf{v}^{rel}_{21}     = \mathbf{v}_{2}     - \mathbf{v}_{1} \\
  \quad \forall \symbf{\omega}^{rel}_{21} = \symbf{\omega}_{2} - \symbf{\omega}_{1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \qquad \mathbf{F}_{12} = - \mathbf{F}_{21} \\
  \mathbf{0} =  \mathbf{M}_{12} = \mathbf{M}_{21} \\
\end{cases}
$$

#### Carrello
Il vincolo di carello può essere pensato come la combinazione di un pattino e di una cerniera

$$
\begin{cases}
  \quad \forall \ \mathbf{v}^{rel}_{\hat{\mathbf{t}},21}     = \mathbf{v}_{\hat{\mathbf{t}},2}     - \mathbf{v}_{\hat{\mathbf{t}},1} \\
          0  = v^{rel}_{\hat{\mathbf{n}},21}     = v_{\hat{\mathbf{n}},2}     - v_{\hat{\mathbf{n}},1} \\
  \quad \forall \ \omega^{rel}_{\hat{\mathbf{t}},21} = \omega_{\hat{\mathbf{t}},2} - \omega_{\hat{\mathbf{t}},1} \\
  \mathbf{0} = \symbf{\omega}^{rel}_{\hat{\mathbf{n}},21} = \symbf{\omega}_{\hat{\mathbf{n}},2} - \symbf{\omega}_{\hat{\mathbf{n}},1} \\
\end{cases}
\qquad , \qquad
\begin{cases}
  \mathbf{0} = \mathbf{F}_{\hat{\mathbf{t}},12} = \mathbf{F}_{\hat{\mathbf{t}},21} \\
  \qquad F_{\hat{\mathbf{n}},12} = - F_{\hat{\mathbf{n}},21} \\
  0 =  M_{\hat{\mathbf{t}},12} = M_{\hat{\mathbf{t}},21} \\
  \qquad \mathbf{M}_{\hat{\mathbf{n}},12} = - \mathbf{M}_{\hat{\mathbf{n}},21} \\
\end{cases}
$$

#### Appoggio
Il vincolo di appoggio è un vincolo monolatero **todo** *aggiungere descrizione*

### Attrito
#### Attrito statico

L'attrito statico è la forma di attrito che si manifesta tra due corpi quando non c'è moto relativo tra di essi, come una forza tangenziale alla superficie di contatto. Il più semplice modello di attrito statico prevede che il modulo massimo della forza di attrito $F^s_{max}$ che si può esercitare tra due corpi è proporzionale alla reazione normale tra di essi, $N$,

$$F^s_{max} = \mu^s \, N \ .$$

Il coefficiente di proporzionalità $\mu^s$ viene definito **coefficiente di attrito statico**. In generale, le forze di attrito statico sono determinate dalle condizioni di equilibrio del corpo, se queste condizioni sono ottenibili ed  è soddisfatta la relazione

$$|F^s| \ge F^s_{max} \ .$$


#### Attrito dinamico

L'attrito dinamico è la forma di attrito che si manifesta tra due corpi a contatto e in moto relativo, come una forza tangenziale alla superficie di contatto. Il più semplice modello di attrito statico prevede che la forza di attrito dinamico sia proporzionale alla reazione normale tra i due corpi e diretta in verso opposto alla velocità relativa,

$$\vec{F}_{12} = - \mu^d N \frac{\vec{v}_{12}}{|\vec{v}_{12}|} \ ,$$

avendo definito $\vec{F}_{12}$ come la forza agente sul corpo $1$ a causa del corpo $2$, e $\vec{v}_{12} = \vec{v}_1 - \vec{v}_2$ la velocità del corpo $1$ relativa al corpo $2$.
 
#### Puro rotolamento


