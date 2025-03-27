<!--
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
-->

(physics-hs:mechanics:dynamics:conservation)=
# Leggi di conservazione

Partendo dalle equazioni di bilancio,

$$\begin{aligned}
 \dot{\vec{Q}} & = \vec{R}^{ext} & \text{(bilancio quantità di moto)} \\
 \dot{\vec{L}}_H + \dot{\vec{x}}_H \times \vec{Q} & = \vec{M}_H^{ext} & \text{(bilancio momento della quantità di moto)} \\
 \dot{K} & = P^{tot} & \text{(bilancio energia cinetica)}
\end{aligned}$$

sotto opportune ipotesi, si ottengono alcune leggi di conservazione di quantità meccaniche.

(physics-hs:mechanics:dynamics:conservation:momentum)=
## Conservazione della quantità di moto
L'equazione di bilancio della quantità di moto di un sistema chiuso garantisce che la quantità di moto di un sistema chiuso è costante se la risultante delle forze esterne sul sistema è nulla,

$$
  \vec{R}^{ext} = \vec{0} \qquad  \rightarrow \qquad \ \ \vec{Q} = \text{const.} 
$$

(physics-hs:mechanics:dynamics:conservation:angular-momentum)=
## Conservazione del momento della quantità di moto
L'equazione di bilancio del momento della quantità di moto di un sistema chiuso garantisce che il momento della quantità di moto di un sistema chiuso è costante se la risultante dei momenti esterni sul sistema è nulla, ed è nullo il termine di trasporto,

$$
  \vec{M}_H^{ext} = \vec{0} \ , \quad \dot{\vec{x}}_H \times \vec{Q} = \vec{0} \qquad  \rightarrow \qquad \vec{L}_H = \text{const.}
$$

(physics-hs:mechanics:dynamics:conservation:kinetic-energy)=
## Conservazione del momento dell'energia cinetica
L'equazione di bilancio dell'energia cinetica di un sistema chiuso garantisce che il momento della quantità di moto di un sistema chiuso è costante se la risultante della potenza di tutte le azioni agenti sul sistema è nulla, 

$$
  P^{tot} = \vec{0} \qquad  \rightarrow \qquad \ \  K = \text{const.}
$$

(physics-hs:mechanics:dynamics:conservation:mechanical-energy)=
## Conservazione dell'energia meccanica
Se in un sistema agiscono solo [azioni conservative](physics-hs:mechanics:actions:conservative) - sia azioni interne sia azioni esterne -, è valida la conservazione dell'energia meccanica.
La potenza delle azioni conservative può essere scritta come derivata nel tempo di una funnzione energia potenziale, $P^{tot} = - \dot{V}$. 
Definendo l'**energia meccanica** come la somma dell'energia cinetica del sistema e dell'energia potenziale, 

$$E^{mec} := K + V \ ,$$

 segue immediatamente che, in assenza di azioni non-conservative l'energia meccanica di un sistema è costante,

$$\dot{K} = P^{tot} = - \dot{V} \quad \rightarrow \quad \dfrac{d}{dt} \left( K + V \right) = 0 \quad \rightarrow \quad E^{mec} = \text{const.}$$


```{prf:example} Rotazione di una ballerina
:label: mechanics:dynamics:dancer

```
