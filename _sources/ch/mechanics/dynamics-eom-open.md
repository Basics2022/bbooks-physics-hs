(physics-hs:mechanics:dynamics:eom:open)=
# Equazioni cardinali della dinamica per sistemi aperti

Nelle sezioni precedenti, i [principi della dinamica](physics-hs:mechanics:dynamics:eom), le [equazioni cardinali](physics-hs:mechanics:dynamics:eom) e le [leggi di conservazione](physics-hs:mechanics:dynamics:conservation) sono state presentate per i **sistemi chiusi**, che non scambiano massa con l'ambiente esterno.

In questa sezione si presentano i bilanci di massa, quantità di moto e energia cinetica per sistemi aperti; pur non potendo dare una dimostrazione rigorosa, si mostra il procedimento generale per ricavare un bilancio per un sistema aperto dal corrisponte bilancio per un sistema chiuso.





## Esempi
```{prf:example} Sistemi discreti - Moto di una barca per reazione

```
```{prf:example} Sistemi discreti - Moto di una giostra per reazione

```
```{prf:example} Sistemi continui - Equazione della spinta per i razzi - Tsiolkovski
L'equazione della spinta per i razzi - di Tsiolkovski **todo** *un po' di storia? riferimento all'astronomia? riferimenti alla dinamica gravitazionale?* - è una prima approssimazione del moto di un razzo a reazione, cioè che usa lo scarico di gas ad alta velocità come mezzo di spinta. Il sistema formato dalla struttura del razzo e il contenuto di combustibile e gas all'interno della struttura del razzo è un sistema aperto, che può scambiare materia attraverso la sezione dell'ugello. L'equazione permette di ricavare la velocità del razzo in funzione dell'espulsione della massa e della velocità effettiva, relativa, di espulsione dei gas dal razzo. L'equazione può essere ricavata usando i bilanci di massa e di quantità di moto per sistemi aperti, 

$$\begin{aligned}
  \dfrac{d M_{v(t)}}{dt} & + \Phi_{\partial v(t)}(\rho) = 0 \\
  \dfrac{d \vec{Q}_{v(t)}}{dt} & + \vec{\Phi}_{\partial v(t)}(\rho \vec{v}) = \vec{R}_{v(t)}^{ext}
\end{aligned}$$

applicando alcune semplificazioni ragionevoli per un modello di prima approssimazione. Assumendo che le proprietà (densità, velocità) siano uniformi sulla superficie dell'ugello, i flussi uscenti di massa e quantità di moto possono essere scritti come

$$\begin{aligned}
  \Phi_{\partial v(t)}(\rho) = \dot{m}_e \qquad m \qquad \Phi_{\partial v(t)}(\rho \vec{v}) = \dot{m}_e \vec{v} \ ,
\end{aligned}$$

La quantità di moto del sistema al tempo $t$ può essere scritta come prodotto della massa $M(t)$ e la velocità del baricentro $\vec{v}_G(t)$ del sistema contenuto nel volume $v(t)$. La risultante delle forze è la somma delle forze di volume, tipicamente il peso, e le forze agenti sulla superficie del volume $v(t)$, tipicamente le forze aerodinamiche. Il flusso di quantità di moto attraverso la frontiera del sistema $\partial v(t)$, assumendo


```
