(physics-hs:thermodynamics:heat-engine:carnot)=
# Carnot e le "Riflessioni sulla forza motrice del fuoco"

Una **macchina ideale** è una macchina in cui:
- non si verificano fenomeni di dissipazione dell'energia meccanica $\delta^+ D = 0$, in cui i processi sono quasi-stazionari; i termini cinetici possono essere trascurati, 

  $$\begin{aligned}
    K & \sim 0 \\
    E^{tot} & = K + E \sim E \\
    d K & = \delta P^{tot} = \delta L^{e} + \delta L^{i} & & \quad \rightarrow \quad \delta L^{e} \sim - \delta L^i \\
    d E^{tot} & = \delta Q^{e} + \delta L^e              & & \quad \rightarrow \quad \delta E \sim \delta Q^{e} - \delta L^i
  \end{aligned}$$

- la trasmissione del calore tra la macchina e le sorgenti di calore esterne avvengono con differenza di temperatura nulla

<!--
$$d E^{tot} = \delta Q^{ext} + \delta L^{ext} \ ,$$

$$dS = \dfrac{\delta Q^{ext}}{T} + \dfrac{\delta^+D}{T} \ge  \dfrac{\delta Q^{ext}}{T} \ .$$

$$0 = \oint_{\gamma} d E^{tot} = \oint_{\gamma} \delta Q^{ext} + \oint_{\gamma} \delta L^{ext}$$

Il lavoro fatto in un ciclo è

$$\Delta L^{1-cycle} = - \Delta L^{ext} = \Delta Q^{ext} \ .$$
-->

(physics-hs:thermodynamics:heat-engine:carnot:td-cycle)=
## Ciclo di Carnot
Il ciclo di Carnot è formato da due adiabatiche ideali e due isoterme ideali.

Per una trasformazione ideale rappresentata nel piano $T-S$ dalla curva $\gamma$, il calore entrante nel sistema è uguale all'integrale **todo** *ref*

$$\Delta Q = \int_{\gamma} T d S \ .$$

La massimizzazione del rendimento di una macchina termica in funzionamento periodico diretto consiste nella massimizzazione di $Q^{e,1}_{in}$ e la minimizzazione di $|Q^{e,1}_{out}|$.

Il rendimento massimo di una macchina termica che scambia calore con due sistemi a temperatura costante $T_1 > T_2$ si ottiene con due trasformazioni isoterme con il sistema alla temperatura delle fonti di calore (e quindi estremamente lente, poiché avvengono con differenza di temperatura nulla o trascurabile **todo** *riferimento alla sezione sui meccanismi di trasmissione del calore*), e due trasformazioni adiabatiche ideali in cui il sistema non scambia calore con l'esterno.

$$\begin{aligned}
  Q^{1}_{in}  & = \int_{S = S_1}^{S_2} T \, dS = \int_{S = S_1}^{S_2} T_1 \, dS =   T_1 \Delta S \\
  Q^{1}_{out} & = \int_{S = S_2}^{S_1} T \, dS = \int_{S = S_2}^{S_1} T_2 \, dS = - T_2 \Delta S \\
\end{aligned}$$

$$\eta_{C} = 1 + \frac{Q^{e,1}_{out}}{Q^{e,1}_{in}} = 1 + \frac{T_2 \, \Delta S}{T_1 \, \Delta S} = 1 - \dfrac{T_2}{T_1} \ .$$


**todo**
- rappresentare il ciclo nel [piano entropico $T-S$](physics-hs:thermodynamics:foundation:principles:phase-diagrams:gas-1:ts), ricordando il significato geometrico delle aree in questo piano, e (di)mostrando le conclusioni del [teorema di Carnot](physics-hs:thermodynamics:heat-engine:carnot:td-cycle:theorem)
- rappresentare un ciclo in cui le trasformazioni isoterme avvengono con una differenza finita di temperatura tra la macchina e i sistemi con cui la macchina scambia calore, mostrando:
  - il rendimento confrontato al rendimento della macchina ideale
  - la variazione di entropia nell'universo

(physics-hs:thermodynamics:heat-engine:carnot:td-cycle:theorem)=
## Teorema di Carnot
Il rendimento massimo di una macchina termica che scambia calore con due sorgenti di calore a temperatura costante $T_1$, $T_2 < T_1$ è quello del [ciclo di Carnot](physics-hs:thermodynamics:heat-engine:carnot:td-cycle). Quindi ogni macchina termica che scambia calore con due sorgenti di calore a temperatura costante $\eta$ ha un'efficienza minore di quella di una macchina di Carnot che opera tra sorgenti di calore con le stesse temperature,

$$\eta \le \eta_C = 1 - \dfrac{T_2}{T_1} \ .$$
