(physics-hs:thermodynamics:foundation:principles:phase-diagrams)=
# Diagrammi termodinamici

I diagrammi di fase forniscono degli strumenti per una rappresentazione grafica-geometrica dello stato e delle trasformazioni di un sistema termodinamico. A seconda del sistema considerato e delle condizioni alle quali è sottoposto, è utile usare un insieme specifico di variabili di stato indipendenti per rappresentare lo stato del sistema. Così, ad esempio:
- per sistemi impiegati nell'ambito delle macchine termiche a fluido, in generale determinati da $F=2$ variabili di stato indipendenti, risulta utile rappresentare lo stato del sistema usando come coppia di variabili indipendenti $P$, $T$ (piano di Clapeyron) o $T$, $S$ (piano entropico), nei quali risultano evidenti per sistemi chiusi rispettivamente il lavoro o il calore scambiato con l'ambiente esterno;
- per l'aria umida e lo studio di sistemi di condizionamento o metereologia, determinati da $F=3$ variabili di stato indipendenti, ma con $P$ circa costante in un gran numero di applicazioni, risulta conveniente usare la coppia di variabili $H$, $x$  (diagramma di Mollier) per valori di pressione $P_0$ dati;
- <span style="color:red"> ...**todo** piano per reazioni chimiche...</span>
- <span style="color:red"> ...**todo** piano delle fasi in metallurgia, con fasi solide...</span>

Questa sezione si concentra su sistemi gassosi non reagenti monofase e sulla rappresentazione dello stato di tali sistemi nei piani di Clapeyron $P-V$ e nel piano entropico $T-S$. L'uso del diagramma di Mollier viene rimandato alla sezione sull'[aria umida](physics-hs:thermodynamics:matter:humid-air), <span style="color:red"> dopo aver introdotto i potenziali termodinamici per i gas, e le miscele?</span>

## Diagramma di stato di un sistema mono-componente gassoso
Si consideri un sistema ad un componente, in grado di scambiare calore e con un unico modo di manifestare il lavoro reversibile interno al sistema, quello meccanico dovuto a un'espansione isotropa del volume, $\delta L^{int,rev} = P \, d V$.

Un sistema chiuso monofase formato da un gas non reagente, ha un unico modo $W=1$ di manifestare lavoro interno reversibile, il lavoro meccanico di compressione, $\delta L^{int,rev} = P dV$, in assenza di carica elettrica o altri meccanismi per compiere lavoro. Come conseguenza della [regola delle fasi di Gibbs](physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:gibbs-phase-rule),

$$F = C - P + W - 1 = 1 - 1 + 1 + 1 = 2 \ ,$$

il sistema ha due gradi di libertà, $F=2$, cioè il suo stato è determinato da due variabili intensive indipendenti. Lo stato del sistema può quindi essere completamente rappresentato in uno spazio dimensionale, cioè in un piano di stato.
Le due scelte discusse qui sono il piano di Clapeyron e il piano entropico.

<!--
<span style="color:red">Come applicarla? $P$, $T$ e concentrazioni? In una rappresentazione 3D del diagramma di stato, la superficie di stato è una superficie 2D, anche durante le transizioni di fase: queste sono descritte dalla composizione delle fasi, come frazioni molari. Queste non sono contate come gradi di libertà? I **gradi di libertà** sono cons le proprietà termodinamiche **intensive** indipendenti, come P,T</span>
Applicando la regola delle fasi di Gibbs,...

<span style="color:red">Diagramma 3D di sistema monocomponente</span>

- regione di una superficie 2D: ha 2 gradi di libertà
- curva sulla superficie di stato, es: trasformazione termodinamica: ha un grado di libertà
- punto: stato TD determinato, es. punto triplo, eutettico: zero gradi di libertà
-->

<!--
## Piani termodinamici
<span style="color:red">Piani termodinamici: proiezioni 2D di un diagramma multi-dimensionale</span>
Esempi:
- piano P-V, Clapeyron
- piano T-S, entropico
- piano H-S, Mollier
- ...
-->

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

$$\delta Q^{ext} = T \, d S - \underbrace{\delta^+ D}_{=0 \text{ ideal, rev.}} = T \, dS \ ..$$

Un sistema chiuso che compie una trasformazione termodinamica descritta dalla curva $\gamma$ nel piano $P-V$ di Clapeyron, assorbe calore dall'ambiente esterno che è uguale alla somma dei contributi elementari - e quindi l'integrale 

$$Q^{ext} = \int_{\gamma} \delta Q^{ext} \approx \int_{\gamma} T \, d S ,$$

che ha l'immediata rappresentazione grafica corrispondente all'area (con segno) tra il grafico della trasformazione e l'asse delle ascisse, $T=0$.
