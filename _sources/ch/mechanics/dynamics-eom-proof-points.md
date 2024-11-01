```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```

(physics-hs:mechanics:dynamics:eom:points)=
# Equazioni cardinali della dinamica per sistemi di punti

Partendo dalle equazioni dinamiche per un punto, si ricavano le equazioni dinamiche per un sistema di punti,

$$\begin{aligned}
 \dot{\vec{Q}} & = \vec{R}^{ext} & \text{(bilancio quantità di moto)} \\
 \dot{\vec{L}}_H + \dot{\vec{x}}_H \times \vec{Q} & = \vec{M}_H^{ext} & \text{(bilancio momento della quantità di moto)} \\
 \dot{K} & = P^{tot} & \text{(bilancio energia cinetica)} \ .
\end{aligned}$$

sfruttando il terzo principio della dinamica di azione/reazione. Lo sviluppo delle equazioni permette di comprendere l'origine della natura additiva delle grandezze dinamiche di sistemi composti da più componenti,

$$\begin{aligned}
\vec{Q}     & = \sum_i \vec{Q}_i     & \text{(quantità di moto)}\\
\vec{L}_{H} & = \sum_i \vec{L}_{H,i} & \text{(momento della quantità di moto)}\\
 K          & = \sum_i K_i           & \text{(energia cinetica)} \ .
\end{aligned}$$


(quantità di moto, momento della quantità di moto, energia cinetica), 

```{dropdown} Bilancio della quantità di moto.
:open:

E' possibile scrivere il bilancio della quantità di moto per ogni punto $i$ del sistema, scrivendo la risultante delle forze esterne agente sul punto come la somma delle forze esterne all'intero sistema agenti sul punto e le forze interne scambiate con gli altri punti del sistema,

$$\vec{R}_i^{ext,i} = \vec{F}_i^{ext} + \sum_{j \ne i} \vec{F}_{ij} \ .$$

L'equazione di bilancio per la $i$-esima massa diventa quindi

$$\dot{\vec{Q}}_i = \vec{R}_i^{ext,i} = \vec{F}_i^{ext} + \sum_{j \ne i} \vec{F}_{ij} \ .$$

Sommando le equazioni di bilancio di tutte le masse, si ottiene

$$\begin{aligned}
\sum_{i} \dot{\vec{Q}}_i & = \sum_i \vec{F}_{i}^{ext} + \sum_i \sum_{j \ne i} \vec{F}_{ij} = \\
                            & = \sum_i \vec{F}_{i}^{ext} + \sum_{\{i,j\}} \underbrace{\left( \vec{F}_{ij} + \vec{F}_{ji} \right)}_{=\vec{0}} 
\end{aligned}$$

e definendo la quantità di moto di un sistema come la somma delle quantità di moto delle sue parti e la risultante delle forze esterne come somma delle forze esterne agenti sulle parti del sistema, 

  $$\vec{Q} := \sum_i \vec{Q}$$
  $$\vec{R}^{ext} := \sum_i \vec{F}_i^{ext}$$

si ritrova la forma generale del bilancio della quantità di moto,

$$\dot{\vec{Q}} = \vec{R}^{ext} \ .$$
```

```{dropdown} Bilancio del momento della quantità di moto
:open:

E' possibile scrivere il bilancio del momento della quantità di moto per ogni punto $i$ del sistema, scrivendo la risultante dei momenti esterni agente sul punto come la somma dei momenti esterni all'intero sistema agenti sul punto e i momenti interni scambiati con gli altri punti del sistema,

$$\vec{M}_{H,i}^{ext,i} = \vec{M}_{H,i}^{ext} + \sum_{j \ne i} \vec{M}_{H,ij} \ .$$

Nel caso le parti del sistema interagiscano tramite forze, il momento rispetto al polo $H$ generato dalla massa $j$ sulla massa $i$ vale

$$\vec{M}_{H,ij} = (\vec{r}_i - \vec{r}_H) \times \vec{F}_{ij} \ .$$

L'equazione di bilancio per la $i$-esima massa diventa quindi

$$\dot{\vec{L}}_{H,i} + \dot{\vec{r}}_H \times \vec{Q}_i = \vec{M}_{H,i}^{ext,i} = \vec{M}_{H,i}^{ext} + \sum_{j \ne i} \vec{M}_{H,ij} \ .$$

Sommando le equazioni di bilancio di tutte le masse, si ottiene

$$\begin{aligned}
\sum_{i} \left( \dot{\vec{L}}_i + \dot{\vec{r}}_H \times \vec{Q}_i \right) & = \sum_i \vec{M}_{H,i}^{ext} + \sum_i \sum_{j \ne i} \vec{M}_{H,ij} = \\
                            & = \sum_i \vec{M}_{H,i}^{ext} + \sum_{\{i,j\}} \underbrace{\left( \vec{M}_{H,ij} + \vec{M}_{H,ji} \right)}_{=\vec{0}} 
\end{aligned}$$

e riconoscendo la quantità di moto del sistema e definendo il momento della quantità di moto di un sistema come la somma del momento della quantità di moto delle sue parti e la risultante dei momenti esterni come somma dei momenti esterni agenti sulle parti del sistema, 

  $$\vec{L}_H := \sum_i \vec{L}_{H,i}$$
  $$\vec{M}_H^e := \sum_i \vec{M}_{H,i}^{ext}$$

si ritrova la forma generale del bilancio del momento della quantità di moto,

$$\dot{\vec{L}}_{H} + \dot{\vec{r}}_H \times \vec{Q} = \vec{M}_H^{ext} \ .$$
```

```{dropdown} Bilancio dell'energia cinetica.
:open:

E' possibile ricavare il bilancio dell'energia cinetica del sistema, moltiplicando scalarmente il bilancio della quantità di moto di ogni punto,

$$\vec{v}_i \cdot m_i \dot{\vec{v}}_i = \vec{v}_i \cdot \left( \vec{F}_i^{e} + \sum_{j \ne i} \vec{F}_{ij} \right) \ ,$$

riconoscendo nel primo termine la derivata nel tempo dell'energia cinetica dell'$i$-esimo punto,

$$\dot{K}_i = \dfrac{d}{dt} \left( \frac{1}{2} m_i \vec{v}_i \cdot \vec{v}_i \right) = m_i \vec{v}_i \cdot \dot{\vec{v}}_i \ ,$$

e sommando queste equazioni di bilancio per ottenere

$$\begin{aligned}
  \sum_i \dot{K}_i = \sum_i \vec{v}_i \cdot  \vec{F}_i^{e} + \sum_i \vec{v}_i \cdot \sum_{j \ne i} \vec{F}_{ij} \ . 
\end{aligned}$$

Definendo l'energia cinetica di un sistema come la somma dell'energia cinetica delle sue parti, e definendo la potenza delle forze esterne/interne agenti sul sistema come la somma della potenza di tutte le forze esterne/interni al sistema,

$$K :=  \sum_i K_i$$
$$P^e := \sum_i P^{ext}_i = \sum_i \vec{v}_i \cdot  \vec{F}_i^{ext} $$
$$P^i := \sum_i P^{int}_i = \sum_i \vec{v}_i \cdot \sum_{j \ne i} \vec{F}_{ij}$$

si ritrova la forma generale del bilancio dell'energia cinetica,

$$\dot{K} = P^{ext} + P^{int} = P^{tot} \ .$$
```


