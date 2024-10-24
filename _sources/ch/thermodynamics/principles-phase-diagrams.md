(physics-hs:thermodynamics:foundation:principles:phase-diagrams)=
# Diagrammi termodinamici

## Diagramma di stato di un sistema mono-componente
Si consideri un sistema ad un componente, in grado di scambiare calore e con un unico modo di manifestare il lavoro reversibile interno al sistema, quello meccanico dovuto a un'espansione isotropa del volume, $\delta L^{int,rev} = P \, d V$.

<span style="color:red">Come applicarla? $P$, $T$ e concentrazioni? In una rappresentazione 3D del diagramma di stato, la superficie di stato è una superficie 2D, anche durante le transizioni di fase: queste sono descritte dalla composizione delle fasi, come frazioni molari. Queste non sono contate come gradi di libertà? I **gradi di libertà** sono cons le proprietà termodinamiche **intensive** indipendenti, come P,T</span>
Applicando la regola delle fasi di Gibbs,...

<span style="color:red">Diagramma 3D di sistema monocomponente</span>

- regione di una superficie 2D: ha 2 gradi di libertà
- curva sulla superficie di stato, es: trasformazione termodinamica: ha un grado di libertà
- punto: stato TD determinato, es. punto triplo, eutettico: zero gradi di libertà

## Piani termodinamici
<span style="color:red">Piani termodinamici: proiezioni 2D di un diagramma multi-dimensionale</span>
Esempi:
- piano P-V, Clapeyron
- piano T-S, entropico
- piano H-S, Mollier
- ...

### Piano di Clapeyron, P-V
**Lavoro.**
Nel caso di **sistemi chiusi** e **processi ideali**, il primo principio della termodinamica viene scritto

$$\begin{aligned}
  d E & = - \delta L^{int,rev} + \delta Q^{ext} = \\
      & = - P \, dV + T \, dS \ .
\end{aligned}$$

Nel caso in cui il contributo dell'**energia cinetica sia trascurabile**, il lavoro compiuto dal sistema sull'ambiente esterno coincide con

$$\delta L^{done} = - \delta L^{ext} = - d K + \delta L^{int} \approx \delta L^{int} \approx \delta L^{int,rev} =  P \, dV$$

Un sistema che compie una trasformazione termodinamica descritta dalla curva $\gamma$ nel piano $P-V$ di Clapeyron, compie un lavoro verso l'ambiente esterno che è uguale alla somma dei contributi elementari - e quindi l'integrale 

$$L^{done} = \int_{\gamma} \delta L^{done} \approx \int_{\gamma} P \, d V \ ,$$

che ha l'immediata rappresentazione grafica corrispondente all'area (con segno) tra il grafico della trasformazione e l'asse delle ascisse, $P=0$.

**Esempi di trasformazioni.**
...

### Piano entropico, T-S
Nel caso di trasformazioni ideali, il calore entrante nel sistema può essere identificato con il termines

$$\delta Q^{ext} = T \, d S - \underbrace{\delta^+ D}_{$=0$ ideal, rev.} \approx = T \, dS \ ..$$

Un sistema chiuso che compie una trasformazione termodinamica descritta dalla curva $\gamma$ nel piano $P-V$ di Clapeyron, assorbe calore dall'ambiente esterno che è uguale alla somma dei contributi elementari - e quindi l'integrale 

$$Q^{ext} = \int_{\gamma} \delta Q^{ext} \approx \int_{\gamma} T \, d S ,$$

che ha l'immediata rappresentazione grafica corrispondente all'area (con segno) tra il grafico della trasformazione e l'asse delle ascisse, $T=0$.
