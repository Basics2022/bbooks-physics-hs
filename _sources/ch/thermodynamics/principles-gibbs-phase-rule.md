(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule)=
# Energia interna e regola delle fasi di Gibbs

## Energia interna
Gibbs definisce l'energia interna del sistema come differenza tra la sua energia totale e l'energia cinetica "macroscopica", 

$$E = E^{tot} - K \ .$$

Il bilancio dell'energia interna viene ricavato come differenza dei bilanci dell'energia totale, descritto dal primo principio della termodinamica

$$d E^{tot} = \delta L^{ext} + \delta Q^{ext} \ ,$$

e il bilancio dell'energia cinetica, fornito dal teorema dell'energia cinetica ricavato in meccanica,

$$d K = \delta L^{ext} + \delta L^{int} \ .$$

Il bilancio dell'energia interna diventa quindi

$$d E = \delta Q^{ext} - \delta L^{int} \ .$$

## Variabili di stato e regola delle fasi
**todo** *def di variabile di stato*
Lo stato termodinamico di un sistema può essere descritto da un numero definito di variabili termodinamiche indipendenti, descritto dalla **regola delle fasi di Gibbs**,

$$F = C - P + 1 + W \ ,$$

cioè il numero di variabili indipendenti (o gradi di libertà), $F$, di un sistema è una funzione del numero di componenti $C$ di un sistema, il numero di fasi $P$ e il numero $W$ di modi del sistema di manifestare lavoro interno, come ad esempio:
- sforzi meccanici interni
- contributo della tensione superficiale
- energia dei legami delle molecole dei componenti
- contributo del campo elettromagnetico

**Esempi.**
- In un sistema composto da un gas comprimibile, monocomponente e monofase (gassosa), elettricamente neutro, **todo** *altro?*, l'unica forma di lavoro interno è quello legato alla compressione, $\delta L^{int,rev} = P dV$, e quindi $W = 1$. Per questo sistema servono quindi, 

  $$F = C - P + 1 + W = 1 - 1 + 1 + 1 = 2 \ ,$$

  variabili di stato per definire lo stato del sistema.

- Solido elastico, ... **todo**
- Miscela reattiva di gas
- Sistema monocomponente durante una transizione di fase
  - transizione di fase del primo ordine
  - punto critico
- Fasi nelle miscele solide
- Campo elettrico e magnetizzazione


## Primo principio in termini delle variabili di stato
L'energia interna è una variabile di stato che, secondo la regola delle fasi, può essere scritta come

$$E(S, X_k) \ ,$$

avendo indicato con $X_k$ tutte le variabili (**todo** *di stato?*) la cui variazione è associata a un lavoro interno reversibile, ed $S$ la variabile di stato la cui variazione è associata al calore scambiato con l'ambiente esterno e alle azioni interne dissipative. Il differenziale - **esatto** - dell'energia interna

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



