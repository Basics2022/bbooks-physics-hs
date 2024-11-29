(physics-hs:thermodynamics:foundation:principles:second)=
# Secondo principio della termodinamica

## Enunciato di Clausius
L'enunciato di Clausis del secondo principio della termodinamica può essere formulato in maniera abbastanza naturale con il formalismo introdotto.

### Sistemi semplici
 La variazione elementare di entropia $d S$ di un sistema semplice chiuso a temperatura uniforme $T$ è maggiore o uguale al rapporto tra il flusso di calore elementare introdotto nel sistema e la temperatura del sistema stesso,
  
  $$dS = \underbrace{\dfrac{\delta^+ D}{T}}_{\ge 0} + \dfrac{\delta Q^{ext}}{T} \ge \dfrac{\delta Q^{ext}}{T} \ .$$

Questo è l'enunciato di Clausius del secondo principio della termodinamica per sistemi semplici con temperatura omogenea.

### Sistemi composti
**todo** definizione di sistema composto. Avviene conduzione tra i sotto-sistemi.

L'entropia in termodinamica classica è una grandezza fisica estensiva: l'entropia di un sistema composto da $N$ sotto-sistemi semplici è la somma dell'entropia dei sotto-sistemi,

$$S = \sum_{n=1:N} S_n \ .$$

Il bilancio dell'entropia del singolo sotto-sistema che scambia calore con gli altri sotto-sistemi e l'ambiente esterno viene scritto come

  $$\begin{aligned}
    dS_i & = \dfrac{\delta Q^{ext,i}_i}{T_i} + \dfrac{\delta^+ D_i}{T_i} = \\
         & = \dfrac{\delta Q^{ext}_i}{T_i} + \dfrac{\sum_{k \ne i} \delta Q_{ik}}{T_i} + \dfrac{\delta^+ D_i}{T_i} \ge \\
         & \ge \dfrac{\delta Q^{ext}_i}{T_i} + \dfrac{\sum_{k \ne i} \delta Q_{ik}}{T_i} \ . 
  \end{aligned}$$

Il bilancio dell'entropia dell'intero sistema viene ricavato sommando i bilanci dell'entropia dei singoli sotto-sistemi,

  $$\begin{aligned}
    dS & = \sum_i d S_i \ge \\
       & \ge \sum_i \left\{ \dfrac{\delta Q^{ext}_i}{T_i} + \dfrac{\sum_{k \ne i} \delta Q_{ik}}{T_i} \right\} = \\
       & = \sum_i \dfrac{\delta Q^{ext}_i}{T_i} + \underbrace{\sum_{\left\{i,k\right\}} \delta Q_{ik} \left( \dfrac{1}{T_i} - \dfrac{1}{T_k} \right)}_{\ge 0} \ge \\
       & \ge \sum_i \dfrac{\delta Q^{ext}_i}{T_i} \ . 
  \end{aligned}$$

avendo usato la relazione che rappresenta la tendenza naturale della trasmissione del calore "da un sistema a temperatura maggiore a un sistema a temperatura minore",

$$\delta Q_{ik} \left( \dfrac{1}{T_i} - \dfrac{1}{T_k} \right) \ge 0 \ .$$

**todo** *aggiungere riferimento alla tendenza naturale nella trasmissione del calore*

## Aumento dell'entropia nell'universo
Se consideriamo l'universo come il sistema chiuso e isolato (ma sarà vero? E chi lo sa? Forse è sensato che lo sia, ma tante cose che sembrano sensate oggi saranno fregnacce tra qualche anno) formato da un sistema di interesse $sys$ e dall'ambiente esterno $env$.

La variazione dell'entropia dell'universo è la somma della variazione nel sistema e nell'ambiente esterno. Si indica con $\delta Q_{sys,env}$ il flusso di calore che, se positivo, fa aumentare l'energia del sistema e diminuire quella dell'ambiente esterno. Assumendo che i due sotto-sistemi siano internamente omogenei,

$$\begin{aligned}
d S^{univ} & = d S^{sys} + d S^{env} = \\
           & = \dfrac{\delta Q_{sys,env}}{T^{sys}} + \dfrac{\delta Q_{env,sys}}{T^{env}} = \\
           & = \dfrac{\delta Q_{sys,env}}{T^{sys}} - \dfrac{\delta Q_{sys,env}}{T^{env}} = \\
           & = \delta Q_{sys,env} \left( \dfrac{1}{T^{sys}} - \dfrac{1}{T^{env}} \right) \ge 0 \ ,
\end{aligned}$$

si ottiene la relazione

$$dS^{univ} \ge 0 \ ,$$

che prevede la "non-diminuzione" dell'entropia dell'universo.

