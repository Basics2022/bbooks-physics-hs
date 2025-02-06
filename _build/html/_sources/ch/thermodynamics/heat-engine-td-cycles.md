(physics-hs:thermodynamics:heat-engine:td-cycles)=
# Cicli termodinamici

Un ciclo termodinamico è una sequenza di trasformazioni termodinamiche che riportano il sistema al suo stato di partenza.
In un piano termodinamico, un ciclo termodinamico è rappresentato da una curva chiusa.

- **todo.** Sistemi aperti/sistemi chiusi

Per un **sistema chiuso**, il primo principio della termodinamica rappresenta il bilancio di energia totale, 

$$d E^{tot} = \delta Q^e + \delta L^e \ ,$$

L'energia è una variabile di stato del sistema (**todo** *riferimenti*), e quindi il suo valore alla fine di un ciclo termodinamico coincide con il suo valore all'inizio del ciclo. Nell'ipotesi di **regime periodico** dello stato del sistema descritto da un **ciclo** termodinamico, dopo un ciclo la differenza di energia del sistema è nulla, $\Delta E^{tot} = 0$, 

$$0 = \underbrace{ \oint_\gamma d E^{tot} }_{\Delta E^{tot}} = \underbrace{\oint_\gamma \delta Q^e}_{Q^{e,1}} + \underbrace{\oint_\gamma \delta L^e}_{= L^{e,1}} \ ,$$

e quindi il lavoro **fatto dal sistema** - definito come l'opposto del lavoro fatto sul sistema, $L^e$ - in un ciclo, $L^1 := -L^{e,1}$, è uguale al calore netto immesso nel sistema in un ciclo, $Q^{e,1}$,

$$L^{1} = Q^{e,1} \ .$$

Come sarà chiaro più tardi con l'[enunuciato di Kelvin del secondo principio della termodinamica](physics-hs:thermodynamics:heat-engine:second-principle:kelvin), una macchina termica in funzionamento diretto - con l'obiettivo di produrre un lavoro meccanico positivo - scambia calore con l'ambiente esterno sia assorbendo sia rilasciando calore: tipicamente assorbe calore $Q^{e}_{in} > 0$ come meccanismo necessario al funzionamento della macchina (es. combustione, scambi di calore con sorgenti calde/riscaldate,...) e rilascia calore nell'ambiente $Q^{e}_{out} < 0$. Separando il ciclo nelle fasi in cui viene rilasciato introdotto calore nel sistema e nelle fasi in cui il sistema rilascia calore nell'ambiente e - proprio volendo metterle in evidenza - nelle fasi adiabatiche in cui non c'è scambio di calore con l'ambiente

$$\begin{aligned}
  \gamma & = \gamma_{Q,in} \cup \gamma_{Q,out} \cup \gamma_{ad} \\
  \emptyset & = \gamma_{Q,in} \cap \gamma_{Q,out} \cap \gamma_{ad} \ ,
\end{aligned}$$

$$\begin{aligned}
  Q^{e,1} = \oint_{\gamma} \delta Q^{e} 
  = \int_{\gamma_{Q,in}} \delta Q^e + \int_{\gamma_{Q,out}} \delta Q^e + \int_{\gamma_{ad}} \delta Q^e 
  = \underbrace{Q^{e,1}_{in}}_{> 0} + \underbrace{Q^{e,1}_{out}}_{< 0} + 0
\end{aligned}$$


(physics-hs:thermodynamics:heat-engine:td-cycles:efficiency)=
## Rendimento termico

Ricordando l'osservazione fatta nell'introduzione riguardo le macchine in funzionamento periodico o in ciclo continuo, si definisce qui il rendimento delle macchine termiche in funzionamento periodico in termini di lavoro e calore per ogni ciclo; dovrebbe essere immediata l'estensione di questa definizione al caso di macchine termiche in funzionamento continuo in termini di potenza meccanica e flusso di calore per unità di tempo.

```{prf:definition} Rendimento termodinamico
Il rendimento termodinamico di una macchina termica è definita come il rapporto tra l'effetto utile della macchina e l'apporto esterno.
```

La definizione di rendimento termodinamico dipende quindi dallo scopo e dal funzionamento della macchina termica.


```{prf:definition} Rendimento termodinamico - macchina termica diretta
Una macchina termica in funzionamento diretto ha come obiettivo quello di convertire un apporto di calore $Q^{e}_{in} > 0$ in lavoro meccanico utile $L = -L^e > 0$. Il rendimento di una macchina termica in funzionamento diretto è quindi

$$\eta = \frac{L}{Q^{e}_{in}} \ .$$

```

Utilizzando la relazione tra calore e lavoro in un ciclo **todo** *ref*e riconoscendo i contributi netti entranti e uscenti di calore dal sistema, si può scrivere

$$\eta = \frac{L}{Q_{in}} = \frac{Q_{in} + Q_{out}}{Q_{in}} = 1 + \frac{Q_{out}}{Q_{in}} = 1 - \frac{|Q_{out}|}{Q_{in}} \ .$$

**todo** In un sistema in cui sia trascurabile l'energia cinetica del sistema sia trascurabile rispetto alla variazione di energia interna, si può approssimare $E^{tot} = K + E \approx E$.

**todo** Per sistemi aperti, in regime stazionario...
