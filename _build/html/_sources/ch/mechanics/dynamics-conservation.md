```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```

(physics-hs:mechanics:dynamics:conservation)=
# Leggi di conservazione

Partendo dalle equazioni di bilancio,

$$\begin{aligned}
 \dot{\vec{Q}} & = \vec{R}^{ext} & \text{(bilancio quantità di moto)} \\
 \dot{\vec{L}}_H + \dot{\vec{x}}_H \times \vec{Q} & = \vec{M}_H^{ext} & \text{(bilancio momento della quantità di moto)} \\
 \dot{K} & = P^{tot} & \text{(bilancio energia cinetica)}
\end{aligned}$$

sotto opportune ipotesi, si ottengono alcune leggi di conservazione di quantità meccaniche.

**Conservazione della quantità di moto.**
L'equazione di bilancio della quantità di moto di un sistema chiuso garantisce che la quantità di moto di un sistema chiuso è costante se la risultante delle forze esterne sul sistema è nulla,

$$
  \vec{R}^{ext} = \vec{0} \qquad  \rightarrow \qquad \ \ \vec{Q} = \text{const.} 
$$

**Conservazione del momento della quantità di moto.**
L'equazione di bilancio del momento della quantità di moto di un sistema chiuso garantisce che il momento della quantità di moto di un sistema chiuso è costante se la risultante dei momenti esterni sul sistema è nulla, ed è nullo il termine di trasporto,

$$
  \vec{M}_H^{ext} = \vec{0} \ , \quad \dot{\vec{x}}_H \times \vec{Q} = \vec{0} \qquad  \rightarrow \qquad \vec{L}_H = \text{const.}
$$

```{prf:example} Rotazione di una ballerina
:label: mechanics:dynamics:dancer

```

**Conservazione del momento dell'energia cinetica.**
L'equazione di bilancio dell'energia cinetica di un sistema chiuso garantisce che il momento della quantità di moto di un sistema chiuso è costante se la risultante della potenza di tutte le azioni agenti sul sistema è nulla, 

$$
  P^{tot} = \vec{0} \qquad  \rightarrow \qquad \ \  K = \text{const.}
$$

**Conservazione del momento dell'energia meccanica.** Se le azioni agenti su un sistema sono conservative, la loro potenza può essere scritta come derivata nel tempo di un'energia potenziale, $P^{tot} = - \dot{V}$. Se si definisce **energia meccanica** la somma dell'energia cinetica del sistema e dell'energia potenziale delle azioni agenti sul sistema, $E^{mec} := K + V$, segue immediatamente che, in assenza di azioni non-conservative l'energia meccanica di un sistema è costante,

$$P^{tot} = - \dot{V} \qquad \rightarrow \qquad E^{mec} = \text{const.}$$

