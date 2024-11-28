(physics-hs:thermodynamics:principles)=
# Princìpi della termodinamica

In questo capitolo vengono presentati i princìpi della termodinamica classica, i concetti e il formalismo matematico utili per formularli.
I princìpi della termodinamica vengono introdotti per **sistemi chiusi**, e successivamente estesi ai sistemi aperti. 

<!--
Ricordando che la termodinamica classica fornisce una descrizione macroscopica mediata della dinamica microscopica di sistemi composti da molti componenti elementari, il livello di dettaglio microscopico può essere usato per fornire un significato alle variabili termodinamiche usate nella descrizione macroscopica.
-->
- Il [**principio di conservazione della massa - di Lavoisier**](physics-hs:thermodynamics:foundation:principles:lavoisier) valido in meccanica classica, riassumibile con la formula *"nulla si crea, nulla si distrugge, ma tutto si trasforma"*, asserisce che in un sistema chiuso la massa è costante,

  $$d M = 0 \ .$$

- Il [**primo principio della termodinamica**](physics-hs:thermodynamics:foundation:principles:first) fornisce la forma generale del bilancio dell'energia *totale* di un sistema chiuso, riconoscendo il lavoro delle forze esterne $\delta L^{ext}$ e il calore $\delta Q^{ext}$ scambiato dal sistema con l'ambiente esterno come le cause della variazione dell'energia totale del sistema.

  $$d E^{tot} = \delta L^{ext} + \delta Q^{ext} \ .$$

- L'opera di **Gibbs** fornisce [**i concetti necessari e una formalizzazione matematica**](physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule) rigorosa della termodinamica classica. Vengono introdotti i concetti di energia interna, variabile di stato, la regola delle fasi di Gibbs; vengono poi presentati alcuni [diagrammi di fase](physics-hs:thermodynamics:foundation:principles:phase-diagrams) per la rappresentazione dello stato di un sistema e le trasformazioni termodinamiche e che verranno utilizzati nei capitoli successivi.

- Il [**secondo principio della termodinamica**](physics-hs:thermodynamics:foundation:principles:second) traduce le tendenze naturali: la dissipazione dell'energia meccanica macroscopica e la trasmissione del calore da un corpo caldo a un corpo freddo, in un principio formulabile in termini di **entropia**,

$$d S \le \frac{\delta Q}{T} \ .$$

- Infine, i bilanci delle quantità fisiche per [**sistemi aperti**](physics-hs:thermodynamics:foundation:principles:open) vengono ricavati modificando i bilanci per sistemi chiusi, introducendo i termini di **flusso delle grandezze fisiche dovuti al trasporto di materia** attraverso la frontiera del sistema.

<!--
<span style="color:red">Sistemare come presentazione! I contenuti vengono divisi nelle sezioni successive.</span>

In questa sezione vengono presentati i princìpi fondamentali della termodinamica classica. **todo**

**Principio di conservazione della massa.**
Nell'ambito della fisica classica, la massa di un sistema chiuso è costante.

**Primo principio della termodinamica - bilancio dell'energia totale.**
Il primo principio della termodinamica rappresenta il bilancio di energia totale per un sistema chiuso (**todo** *riferimenti a sistemi aperti e chiusi*),

  $$d E^{tot} = \delta L^{ext} + \delta Q^{ext} \ . $$
  
  Usando il teorema dell'energia cinetica (**todo** riferimento alla meccanica), $dK = \delta L^{ext} + \delta L^{int}$, e la definizione di energia interna come differenza tra energia totale ed energia cinetica macroscopica, $E := E^{tot} - K$,
  
  $$d E = - \delta L^{int} + \delta Q^{ext} \ .$$

**Regola delle fasi di Gibbs.**
L'energia interna può essere scritta come funzione di stato, $E(S, X_k)$, **todo** con variabili indipendenti ...

$$\begin{aligned}
dE & = \left(\dfrac{\partial E}{\partial S}\right)_{\mathbf{X}} d S 
     + \left(\dfrac{\partial E}{\partial X_k}\right)_{S} d X_k  = \\
   & = T \, d S + \sum_k F_k \, d X_k
\end{aligned}$$

La variazione di energia interna rispetto alla variabile $S$ corrisponde alla temperatura,

$$T = \left(\dfrac{\partial E}{\partial S}\right)_{\mathbf{X}} \ge 0 \ .$$


**Secondo principio della termodinamica - irreversibilità.**

- Secondo principio per sistemi semplici **todo** *temperatura uniforme*

  $$\begin{aligned}
    dE & = \delta Q^{ext} - \delta L^{int} = \\
       & = \underbrace{\delta Q^{ext} + \delta^+ D}_{\delta U} - \delta L^{int, rev} = \\
  \end{aligned}$$
  
  $$\begin{cases}
  -\delta L^{int,rev} & = \displaystyle\sum_k F_k \, d X_k \\
  \delta U            & = T \, dS
  \end{cases}$$
-->
