(physics-hs:thermodynamics:foundation:principles)=
# Princìpi della termodinamica

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

