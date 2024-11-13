(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule)=
# Energia interna e regola delle fasi di Gibbs

## Variabili di stato
```{prf:definition} Variabile di stato

**todo** *def di variabile di stato*
```

## Energia interna
```{prf:definition} Energia interna
**Gibbs** definisce l'energia interna del sistema come differenza tra la sua energia totale e l'energia cinetica "macroscopica", 

$$E = E^{tot} - K \ .$$
```

Il bilancio dell'energia interna viene ricavato come differenza dei bilanci dell'energia totale, descritto dal primo principio della termodinamica

$$d E^{tot} := \delta L^{ext} + \delta Q^{ext} \ ,$$

e il bilancio dell'energia cinetica, fornito dal teorema dell'energia cinetica ricavato in meccanica,

$$d K = \delta L^{ext} + \delta L^{int} \ .$$

Il bilancio dell'energia interna diventa quindi

$$d E = \delta Q^{ext} - \delta L^{int} \ .$$

## Regola delle fasi di Gibbs
```{prf:proposition} Regola delle fasi di Gibbs
Lo stato termodinamico di un sistema può essere descritto da un numero definito di variabili termodinamiche indipendenti, descritto dalla **regola delle fasi di Gibbs**,

$$F = C - P + 1 + W \ ,$$

cioè il numero di variabili indipendenti (o gradi di libertà), $F$, di un sistema è una funzione del numero di componenti $C$ di un sistema, il numero di fasi $P$ e il numero $W$ di modi del sistema di manifestare lavoro interno, come ad esempio:
- sforzi meccanici interni
- contributo della tensione superficiale
- energia dei legami delle molecole dei componenti
- contributo del campo elettromagnetico
```

```{prf:example} Sistema chiuso contentente un monocomponente (o non-reagente), monofase, elettricamente neutro (o non-soggetto a campo elettromagnetico)
:class: dropdown

In un sistema composto da un gas comprimibile, monocomponente e monofase (gassosa), elettricamente neutro, **todo** *altro?*, l'unica forma di lavoro interno è quello legato alla compressione, $\delta L^{int,rev} = P dV$, e quindi $W = 1$. Per questo sistema servono quindi, 

$$F = C - P + 1 + W = 1 - 1 + 1 + 1 = 2 \ ,$$

variabili di stato per definire lo stato del sistema.

```
```{prf:example} Sistema aperto contentente un monocomponente (o non-reagente), monofase, elettricamente neutro (o non-soggetto a campo elettromagnetico)
:class: dropdown

In un sistema aperto, la variazione di energia del sistema dipende anche dalla variazione della quantità di gas contenuto in esso. Quindi, in generale esistono $W = 2$ modi per far variare l'eneergia del sistema: tramite il lavoro di compressione, o tramite un flusso di materia all'interno del sistema. Servono quindi $F=3$ variabili di stato per definire lo stato del sistema.

```
``` {prf:example} Miscela reattiva di gas in un sistema chiuso
:class: dropdown

In una miscela reattiva di gas formata dai due composti $A$, $B$ in equilibrio secondo la reazione di equilibrio

$$n_a A + n_b B \leftrightarrow n A_a B_b$$

l'energia del sistema dipende dal lavoro meccanico di compressione della miscela dei gas, e dalla quantità dei 3 composti presenti nel gas. La variazione di questi composti non è però indipendente ma determinata dalla reazione di equilibrio. In particolare,

$$\begin{aligned}
  d n_{B} & = d n_{A} \frac{n_b}{n_a} \\
  d n_{A_a B_b} & = - d n_{A} \frac{n}{n_a} \\
\end{aligned}$$

La reazione è quindi determinata da 1 solo parametro. La variazione di energia del sistema è quindi determinata da $W=2$ processi: dal lavoro di compressione fatto sul sistema, e dallo stato della reazione. Per determinare lo stato del sistema servono quindi $F=3$ variabili di stato indipendenti, come ad esempio **todo** $T$, $P$, $n_A$? Non servono i potenziali chimici $\mu_A$, $\mu_B$, $\mu_{A_a B_b}$? Sono unicamente determinati?

```
```{prf:example} Sistema monocomponente durante una transizione di fase
:class: dropdown
**Transizione di fase del primo ordine.** Durante una transione di fase del primo ordine, sono simultaneamente presenti nel sistema $P = 2$ fasi. Secondo la regola delle fasi di Gibbs, lo stato del sistema è determinato da 

$$F = C - P + 1 + W = 1 - 2 + 1 + 1 = 1 \ ,$$

variabile di stato.

**Punto critico.** Il punto critico nel piano delle fasi di un sistema mono-componente definisce la condizione in cui sono simultaneamente presenti nel sistema $P = 3$ fasi. Secondo la regola delle fasi di Gibbs, lo stato del sistema è determinato da $F = 0$ variabili di stato: lo stato del sistema nel punto critico è univocamente definito, senza alcun grado di libertà.

```
```{prf:example} Solido
:class: dropdown

In assenza di altri fenomeni fisici, l'unica forma di lavoro in un solido è quella legata al lavoro di deformazione, $\delta L^{int,rev} = \sigma_{ij} \, d \varepsilon_{ij} dV$. Il tensore di deformazione è del secondo ordine e simmetrico, e ha quindi 6 componenti indipendenti nello spazio 3-dimensionale, e quindi $W=6$
```
```{prf:example} Miscele solide
:class: dropdown

- Fasi nelle miscele solide **todo**
```
```{prf:example} Influenza del campo elettromagnetico
:class: dropdown

- Campo elettrico e magnetizzazione **todo**
```

## Primo principio in termini delle variabili di stato
Lo stato di un sistema termodinamico può essere identificato da un insieme di variabili di stato termodinamiche. **todo** *celta della variabili associate a variazione di energia...*

L'energia interna è quindi una variabile di stato dipendente dalle variabili indipendenti scelte,

$$E(S, X_k) \ ,$$

avendo indicato con $X_k$ tutte le variabili (**todo** *di stato?*) la cui variazione è associata a un lavoro interno reversibile, ed $S$ la variabile di stato la cui variazione è associata al calore scambiato con l'ambiente esterno e alle azioni interne dissipative. **todo** *facendo riferimento al capitolo sulle funzioni e sul calcolo multivariabile*

Il differenziale - **esatto** - dell'energia interna

$$\begin{aligned}
dE & = \left(\dfrac{\partial E}{\partial S}\right)_{\mathbf{X}} d S 
     + \left(\dfrac{\partial E}{\partial X_k}\right)_{S} d X_k  = \\
   & = T \, d S + \sum_k F_k \, d X_k
\end{aligned}$$

può essere confrontato con il bilancio dell'energia interna,

$$\begin{aligned}
  d E & = \delta Q^{ext} + \delta L^{int} = \\
      & = \delta Q^{ext} + \delta^+ D - \delta L^{int,rev} \ .
\end{aligned}$$

Poiché $d E$ è un differenziale esatto e $\delta L^{int,rev}$ è un contributo reversibile, segue che la somma dei due contributi in generale non reversibili, $\delta U := \delta Q^{ext} + \delta^+ D$, è un contributo reversibile. Confrontando le due espressioni del differenziale dell'energia interna, si può associare questo contributo al termine $T \, dS$, il lavoro interno reversibile alla somma dei contributi formati come prodotto delle forze generalizzate $F_k$ e le variazioni delle variabili di stato $X_k$,

$$\begin{cases}
  -\delta L^{int,rev} & = \displaystyle\sum_k F_k \, d X_k \\
  \delta U            & = T \, dS
\end{cases}$$

Da L.E. Reichl, A Modern Course in Statistical Physics, con qualche incoerenza **todo** *controllare!*

$$\delta W = - P dV + J dL + \sigma d A + V \left( \vec{e} \cdot d \vec{p} + \vec{h} \cdot d \vec{m}\right) + \phi d q $$

- con $J$, $\sigma$ tensioni per unità di lunghezza e di area, $d L $, $d A$ variazione di lunghezza o di area,
- con $\vec{e}$, $\vec{h}$ campi elettrico e magnetico, $\vec{p}$, $\vec{m}$ polarizzazione e magnetizzazione
- $\phi$ potenziale elettrico, $q$ carica elettrica (per sistemi aperti, altrimenti o $dq \equiv 0$ o si starebbe creando carica elettrica netta!)

```{prf:example} Sistema gassoso chiuso monocomponente
:class: dropdown

L'energia del sistema, $E(S,V)$

$$dE = T \, dS - P \, dV$$

```
```{prf:example} Sistema gassoso aperto monocomponente
:class: dropdown

L'energia del sistema, $E(S,V,N)$

$$dE = T \, dS - P \, dV + \mu \, dN$$

```
```{prf:example} Miscela reattiva di gas in un sistema chiuso
:class: dropdown

L'energia del sistema

$$\begin{aligned}
  dE & = T \, dS - P \, dV + \mu_k \, dN_k = \\
     & = T \, dS - P \, dV + \left( \mu_k n_k \right) dN
\end{aligned}$$

avendo indicato con $n_k$ i coefficienti stechiomentrici (con segno) della reazione, e con $N$ una quantità che identifica l'equilibrio della reazione, in maniera tale da poter scrivere la variazione di ogni componente come $d N_k = n_k \, d N$.

```
```{prf:example} Miscela monocomponente durante una transizione di fase
:class: dropdown

**todo** come trattare la frazione delle fasi?

```
```{prf:example} Solido
:class: dropdown

Sistema solido di volume iniziale $V$ con stato di sforzo e deformazione uniforme, e piccole deformazioni

$$dE = T \, dS - V \, \sigma_{ij} \, d \varepsilon_{ij} $$

```
```{prf:example} Miscele solide
:class: dropdown

**todo**
```
```{prf:example} Influenza del campo magnetico
:class: dropdown

$$dE = T \, dS - P \, d V + H \, dM$$

**todo**
```
