(physics-hs:mechanics:dynamics:eom:open)=
# Equazioni cardinali della dinamica per sistemi aperti

Nelle sezioni precedenti, i [principi della dinamica](physics-hs:mechanics:dynamics:eom), le [equazioni cardinali](physics-hs:mechanics:dynamics:eom) e le [leggi di conservazione](physics-hs:mechanics:dynamics:conservation) sono state presentate per i **sistemi chiusi**, che non scambiano massa con l'ambiente esterno.

In questa sezione si presentano i bilanci di massa, quantità di moto e energia cinetica per sistemi aperti; pur non potendo dare una dimostrazione rigorosa, si mostra il procedimento generale per ricavare un bilancio per un sistema aperto dal corrisponte bilancio per un sistema chiuso.

Questi risultati verranno applicati successivamente per:
- il calcolo reazioni in sistemi termo-meccanici
- la derivazione dell'[equazione delle onde per l'acustica](physics-hs:waves:equation:examples:fluids:sound)
- ...

(physics-hs:mechanics:dynamics:eom:open:mass)=
## Bilancio della massa

(physics-hs:mechanics:dynamics:eom:open:momentum)=
## Bilancio della quantità di moto

(physics-hs:mechanics:dynamics:eom:open:angular-momentum)=
## Bilancio del momento della quantità di moto


## Esempi
````{prf:example} Sistemi discreti - Moto di una barca per reazione
:class: dropdown
:label: mechanics:dynamics:open:ex:boat

Una barca di massa $M$ è stata caricata con $N$ palle di cannone, ciascuna di massa $m$, così che la massa totale è $M = M_0 + N m$. La barca si muove lungo una traiettoria rettilinea, inizialmente con velocità $\vec{v}_0 = v_0 \hat{x}$. Sulla barca è presente un cannone in grado di sparare i proiettili esattamente nella stessa direzione della traiettoria, con un a velocità relativa di $\vec{v}_p - \vec{v}^- = \vec{v}_p^{rel,-} = - v^{rel} \hat{x}$, con $v^{rel} > 0$, rispetto alla velocità della barca **prima dello sparo**, $\vec{v}^-$.

Viene chiesto di determinare la velocità della barca dopo $n \le N$ spari. **todo** *e di determinare dopo quanti spari, i proiettili vengono sparati nella stessa direzione "assoluta" in cui si muove la barca*

**Soluzione.**
```{dropdown} Approccio 1. Conservazione della quantità di moto di un sistema chiuso costituito dalla barca e dalla palla di cannone sparata.
<!-- :open: -->

Non agendo altre forze nette sul sistema, la quantità di moto del sistema chiuso è conservata tra un istante di tempo precedente e successivo allo sparo $n$-esimo.

$$\begin{aligned}
  M_{n} v_{n} 
  & = M_{n+1} v_{n+1} + m v_{p,n+1} \\
  & = ( M_{n} - m ) v_{n+1} + m ( v_{n} + v_p^{rel} ) \\
\end{aligned}$$

$$\begin{aligned}
  v_{n+1} - v_n & = \frac{m}{M_n - m} v_p^{rel} = \\
  & = \frac{m}{M_0 + (N-n)m - m} v_p^{rel} = \\
  & = \frac{m}{M - (1+n) m} v_p^{rel}
\end{aligned}$$

La velocità $v_{n+1}$ può quindi essere riportata alla velocità $v_0$ sommando gli $n$ contributi $v_{n+1} - v_{n}$, $v_{n} - v_{n-1}$,...

$$\begin{aligned}
  v_{n+1} - v_0 & = v_{n+1} - v_n + v_n - v_{n-1} + \dots + v_1 - v_0 = \\
  & = \frac{m}{M - (1+n) m} v_p^{rel} +  \frac{m}{M - n m} v_p^{rel} + \dots + \frac{m}{M-m} v^{rel}_p = \\
  & = \frac{m}{M} v_p^{rel} \sum_{k = 0}^{n} \frac{1}{1 - (1+k) \frac{m}{M}} \ .
\end{aligned}$$


**oss.** L'equazione ... può essere riscritta mettendo in evidenza le variazioni delle grandezze fisiche velocità e massa

$\Delta v_{n+1} = v_{n+1} - v_n$, $\Delta M_{n+1} = M_{n+1} - M_{n}$

$$\Delta v_{n+1} = - \frac{\Delta M_{n+1}}{M_{n+1}} v_p^{rel} \ .$$

```

```{dropdown} Approccio 2. Conservazione della quantità di moto di un sistema aperto costituito dalla barca.

$$\Delta \vec{Q} + \Delta t \, \Phi(\rho \vec{v}) = \vec{0} \ ,$$

$$\begin{aligned}
  \vec{0} & = M_{n+1} \vec{v}_{n+1} - M_{n} \vec{v}_n + m \vec{v}_p =  \\
          & = M_{n+1} \vec{v}_{n+1} - M_{n} \vec{v}_n + m ( \vec{v}_p^{rel} + \vec{v}_n )  \\
\end{aligned}$$

$$\vec{v}_{n+1} - \vec{v}_n = \frac{m}{M_{n+1}} \vec{v}_p^{rel} \ .$$

```

````
````{prf:example} Sistemi discreti - Moto di una giostra per reazione
:class: dropdown
:label: mechanics:dynamics:open:ex:carousel

Una giostra è libera di ruotare attorno al suo centro, grazie a una cerniera cilindrica. Sulla giostra, sono state caricate delle palline di massa $m$, posizionate al bordo della giostra, che vengono lanciate in direzione tangenziale alla giostra da un marchingegno che riesce a fornire alle palline una velocità relativa rispetto alla velocità prima del lancio uguale a $v_p^{rel}$. La giostra ha raggio $R$ e massa $M$.

<!--
*Suggerimento.* Il momento della quantità di moto è una grandezza fisica additiva. Il momento della quantità di moto di una massa puntiforme rispetto a un punto è $$\vec{L}_i = m_i \vec{r}_i \times \vec{v}_i$$
-->

Viene chiesto di determinare la velocità angolare della giostra dopo $n \le N$ lanci. **todo** *e di determinare dopo quanti lanci, le palline vengono sparate nella stessa direzione "assoluta" in cui gira la giostra*

**todo** *Ripetere l'esercizio con le palline inizialmente posizionate sull'asse, poi trasportate sul bordo della giostra prima di essere lanciate.* *Primo trasferimento usando la conservazione del momento della quantità di moto, come una ballerina che cambia $I$, poi lancio...*

```{dropdown} Approccio 1. Conservazione della quantità di moto di un sistema chiuso costituito dalla giostra e dalla palla.
```

```{dropdown} Approccio 2. Conservazione della quantità di moto di un sistema aperto costituito dalla giostra.
:open:

Il bilancio del momento della quantità di moto rispetto al centro della giostra attorno all'asse di rotazione è

$$\Delta L_{0,z} + \Delta t \, \Phi(\rho \vec{r} \times \vec{v}) = \vec{0}$$

Poichè il momento di inerzia tra un lancio e un altro diminuisce di una quantità costante dovuta al lancio di una pallina,  $I_{z,n+1} = I_{z,n} - m R^2$, si può riscrivere l'equazione di bilancio

$$\begin{aligned}
  0 & = I_{z,n+1} \Omega_{n+1} - I_{z,n} \Omega_n + m R v_p =  \\
    & = I_{z,n+1} \Omega_{n+1} - I_{z,n} \Omega_n + m R ( R \Omega_n + v_p^{rel} ) \\
    & = I_{z,n+1} \Omega_{n+1} - I_{z,n+1} \Omega_n + m R v_p^{rel}
\end{aligned}$$

per ricavare una relazione che lega la variazione di velocità angolare alla variazione di inerzia e al numero di palle lanciate,

$$\begin{aligned}
  \Omega_{n+1} - \Omega_n & =  \frac{m R}{I_{z,n+1}} v_p^{rel} = \\
                          & = - \frac{\Delta I_{z}}{I_{z,n+1}} \frac{v_p^{rel}}{R} = \\
                          & =  \frac{m R}{I - (n+1) mR^2} v_p^{rel} = \ ,
\end{aligned}$$

essendo $I = I_0 + N m R^2$ l'inerzia iniziale dell'intero sistema.



```

````

```{prf:example} Sistemi continui - Equazione della spinta per i razzi - Tsiolkovski
:class: dropdown
:label: mechanics:dynamics:open:ex:rockets

L'equazione della spinta per i razzi - di Tsiolkovski **todo** *un po' di storia? riferimento all'astronomia? riferimenti alla dinamica gravitazionale?* - è una prima approssimazione del moto di un razzo a reazione, cioè che usa lo scarico di gas ad alta velocità come mezzo di spinta. Il sistema formato dalla struttura del razzo e il contenuto di combustibile e gas all'interno della struttura del razzo è un sistema aperto, che può scambiare materia attraverso la sezione dell'ugello. L'equazione permette di ricavare la velocità del razzo in funzione dell'espulsione della massa e della velocità effettiva, relativa, di espulsione dei gas dal razzo. L'equazione può essere ricavata usando i bilanci di massa e di quantità di moto per sistemi aperti, 

$$\begin{aligned}
  \dfrac{d M_{v(t)}}{dt} & + \Phi_{\partial v(t)}(\rho) = 0 \\
  \dfrac{d \vec{Q}_{v(t)}}{dt} & + \vec{\Phi}_{\partial v(t)}(\rho \vec{v}) = \vec{R}_{v(t)}^{ext}
\end{aligned}$$

applicando alcune semplificazioni ragionevoli per un modello di prima approssimazione. Assumendo che le proprietà (densità, velocità) siano uniformi sulla superficie dell'ugello, i flussi uscenti di massa e quantità di moto possono essere scritti nei termini del flusso di massa $\dot{m}_e$ attraverso l'ugello,

$$\begin{aligned}
  \Phi_{\partial v(t)}(\rho) = \dot{m}_e \qquad , \qquad \Phi_{\partial v(t)}(\rho \vec{v}) = \dot{m}_e \vec{v} \ ,
\end{aligned}$$

Usando l'equazione della massa, segue immediatamente $\dot{M}_{v(t)} = - \dot{m}_e$.
La quantità di moto del sistema al tempo $t$ può essere scritta come prodotto della massa $M_{v(t)}(t)$ e la velocità del baricentro $\vec{v}_G(t)$ del sistema contenuto nel volume $v(t)$. La risultante delle forze è la somma delle forze di volume, tipicamente il peso, e le forze agenti sulla superficie del volume $v(t)$, tipicamente le forze aerodinamiche. L'equazione della quantità di moto può quindi essere riscritta come

$$\dot{M} \vec{v} + M \dot{\vec{v}} + \dot{m}_e \vec{v}_e = M(t) \vec{g} + \vec{F}^{aero} \ .$$

Scrivendo la velocità di efflusso come somma della velocità del baricentro e della velocità relativa al baricentro, $\vec{v}_e = \vec{v} + \vec{v}_e^{rel}$, usando l'equazione della massa $\dot{m}_e = - \dot{M}$, si può riscrivere l'equazione

$$M \dot{\vec{v}} = \dot{M} \vec{v}_e^{rel} + M(t) \vec{g} + \vec{F}^{aero} \ ,$$

e riconoscere il termine $\dot{M} \vec{v}_e^{rel}$ come la spinta generata sul razzo dall'efflusso dei gas.

Nel caso in cui si possano trascurare le forze esterne agenti sul sistema rispetto alla spinta, l'equazione di moto fornisce una relazione differenziale tra la massa $M(t)$ e la velocità $\vec{v}$ del sistema,

$$M \dot{\vec{v}} = \dot{M} \vec{v}_e^{rel} \ .$$

Spostando tutto da una parte dell'uguale, e dividendo per la massa $M$, e ricordando che $\frac{d}{dt} \ln x(t) = \frac{\dot{x}(t)}{x(t)}$, assumendo che la velocità relativa di efflusso sia costante, si può riscrivere l'equazione in termini di una derivata in tempo nulla,

$$\begin{aligned}
  0 = \dot{\vec{v}} - \frac{\dot{M}}{M} \vec{v}_e^{rel} = \dfrac{d}{dt} \left( \vec{v} - \vec{v}^{rel}_e \ln \frac{M}{M_0} \right) \ ,
\end{aligned}$$

che implica la costanza della funzione derivata,

$$\vec{v}_2 - \ln \frac{M_2}{M_0} \vec{v}^{rel}_e = \vec{v}_1 - \ln \frac{M_1}{M_0} \vec{v}^{rel}_e \ ,$$

che può essere riscritta come

$$\vec{v}_2 - \vec{v}_1 =  \vec{v}^{rel}_e \, \ln \frac{M_2}{M_1}\ .$$



```
