(physics-hs:thermodynamics:heat-engine:td-cycles)=
# Trasformazioni termodinamiche

...

## Fluidi

Per un sistema **chiuso** composto da un volume di fluido monofase, che manifesta lavoro interno solo nella forma $\delta L^{i,rev} = -P dV$

$$d E & = \delta Q^e - \delta L^i = \delta Q^e + \delta^+ D - \delta L^{i, rev} $$
$$d E = T d S - P d V$$

**Trasformazione isocora, $V $ cost.** Per una trasformazione isocora il volume del sistema non varia, $d V = 0$. Quindi il lavoro interno reversibile è nullo, $\delta L^{i,rev} = - P dV = 0$. Durante questa trasformazione segue quindi che la variazione di energia interna del sistema è uguale alla somma del contributo del calore immesso nel sistema e alla dissipazione,

$$d E = \delta Q^e + \delta^+ D = T dS \ .$$

Nel caso di trasformazione ideale, per la quale si può trascurare la dissipazione, $\delta^+ D = 0$,

$$d E = \delta Q^e = T dS \ .$$

**Trasformazione isoterma, $T $ cost.** Per una trasformazione isoterna nessuno dei tre contributi di variazione di energia, calore e lavoro è nullo in generale. Il termine di calore+dissipazione lungo una trasformazione a temperatura costante $T = \overline{T}$ assume però un'espressione molto semplice

$$\int_{\gamma} T dS = \overline{T} \int_{\gamma_{1,2}} d S = \overline{T} (S_2 - S_1) = \overline{T} \Delta S_{1,2} \ .$$

Nel caso di trasformazinoe ideale, per la quale si può trascurare la dissipazione, $\delta^+ D = 0$, questo termine corrispende al calore immesso nel sistema, $T d S = \delta Q$, e quindi

$$Q_{12} = \overline{T} (S_2 - S_1) \ .$$

**Trasformazione isobara, $P $ cost.** Per una trasformazione isobara nessuno dei tre contributi di variazione di energia, calore e lavoro è nullo in generale. Il termine di lavoro interno ideale lungo una trasformazione a temperatura costante $T = \overline{T}$ assume però un'espressione molto semplice

$$\int_{\gamma} P dV = \overline{P} \int_{\gamma_{1,2}} d V = \overline{P} (V_2 - V_1) = \overline{P} \Delta V_{1,2} \ .$$

Nel caso di trasformazinoe ideale, per la quale si può trascurare la dissipazione, $\delta^+ D = 0$, e di trasformazione sufficientemente lenta da poter trascurare le variazioni di energia cinetica del sistema rispetto alle variazioni di energia interna, questo termine corrispende al lavoro fatto dal sistema, 

$$d K = \delta L^e + \delta L^i = \delta L^e + \delta L^{i,rev} - \delta^+ D \qquad \rightarrow \qquad \delta L := - \delta L^e \sim \delta L^{int,rev} \ .$$

o per una trasformazione finita

$$\Delta L_{12} = \overline{P} (V_2 - V_1) \ ,$$

avendo definito il lavoro fatto dal sistema sull'ambiente esterno $L$ come l'opposto del lavoro fatto dall'ambiente esterno sul sistema $L^e$, $L = - L^e$.

**Trasformazione adiabatica, $\delta Q = 0$.** In una trasformazione adiabatica, senza apporto di calore, la variazione dell'energia interna è uguale all'opposto del lavoro interno del sistema o, nelle stesse ipotesi di contributo cinetico trascurabile discusse per le trasformazioni isobare, uguale al lavoro fatto dall'ambiente sul sistema

$$d E = - \delta L^i = \delta L^{e} = - \delta L \ .$$

Nel caso di trasformazione ideale, $\delta^+ D = 0$, $\delta L^i = \delta L^{i,rev} = P dV$, si ottiene una trasformazione isentropica (Se $\delta Q = 0$ e $\delta^+ D = 0$ segue $dS = 0$, vedi sotto) e l'espressione della variazione di energia

$$d E = - P dV \ .$$

**Trasformazione isentropica, $S $ cost.** Una trasformazione isentropica è una trasformazione **adiabatica ideale**, senza dissipazione. Infatti, per una trasformazione adiabatica $\delta Q = 0$, per una trasformazione senza dissipazione $\delta^+ D = 0$ e segue immediatamente

$$T d S = \delta Q + \delta^+ D = 0 \ .$$

### Gas ideali
Per un [gas ideale](physics-hs:thermodynamics:matter:gases:ideal) si può utilizzare la sua equazione di stato

$$P = \rho R_g T \ ,$$

e l'espressione dell'energia interna in funzione solo della temperatura **todo** *riferimento*

$$E = m c_v T \ ,$$

e ottenere dei risultati un po' più espliciti. In questa sezione vengono considerate trasformazioni ideali e con termini cinetici trascurabili.

**Trasformazione isocora, $V $ cost.** La condizione di volume costante e sistema chiuso - massa costante - in condizioni di grandezze fisiche uniformi nello spazio corrisponde alla condizione di densità costante,

$$\rho = \frac{m}{V} = \frac{\overline{m}}{\overline{V}} = \overline{\rho} \ .$$

La legge dei gas quindi impone un legame lineare tra pressione e temperatura del sistema durante la trasformazione, $P = \overline{\rho} R_g T$.

Il lavoro è identicamente nullo, $d L^ì = 0$ e quindi la variazione di energia corrisponde alla variazione di calore immesso nel sistema

$$T dS = \delta Q^e = d E = m c_v dT \ ,$$

da cui si può ricavare la variazione di entropia in funzione della variazione della temperatura,

$$d S = m c_v \dfrac{d T}{T} \qquad \rightarrow \qquad \Delta S_{12} = m c_v \ln \dfrac{T_2}{T_1} \ .$$

La trasformazione può essere rappresentata nei piani termodinamici $P-V$ e $T-S$ come delle curve parametrizzabili con un parametro libero,

$$P = \overline{\rho} R T$$
$$e_2 - e_1 = c_v (T_2 - T_1) = \frac{c_v}{\overline{\rho} R} (P_2 - P_1)$$
$$d s = c_v \dfrac{dT}{T} \quad \rightarrow \quad s_2 - s_1 = c_v \ln \frac{T_2}{T_1} $$
$$d s = c_v \dfrac{dP}{P} \quad \rightarrow \quad s_2 - s_1 = c_v \ln \frac{P_2}{P_1} $$

```{list-table}
:header-rows: 0

* - ![](../../media/td-transformations-v.png)

```

**Trasformazione isoterma, $T $ cost.** Per una tasformazione isoterma $P = \rho R_g \overline{T} = \frac{\overline{m}}{V} R_g \overline{T}$. La variazione di energia interna è nulla, poiché $dT = 0$ implica $d E = m c_v dT = 0$. Seque quindi che il lavoro fatto dal sistema è uguale al calore immesso in esso. Nel caso ideale

$$\overline{T} dS = \delta Q^{e} = \delta L = P dV \ ,$$

da cui si può ricavare la variazione di entropia come

$$d S = \overline{m} R_g \dfrac{d V}{V} \qquad \rightarrow \qquad \frac{Q_{12}}{\overline{T}} = \Delta S_{12} = \overline{m} R_g \ln \frac{V_2}{V_1} \ .$$

La trasformazione può essere rappresentata nei piani termodinamici $P-V$ e $T-S$ come delle curve parametrizzabili con un parametro libero,

$$P = \rho R \overline{T}$$
$$e_2 = e_1 = c_v \overline{T}$$
$$d s = R \dfrac{d\rho}{\rho} \quad \rightarrow \quad s_2 - s_1 = R \ln \frac{\rho_2}{\rho_1} = - R \ln \frac{V_2}{V_1} $$
$$d s = R \dfrac{d P  }{P   } \quad \rightarrow \quad s_2 - s_1 = R \ln \frac{P_2}{P_1} $$

```{list-table}
:header-rows: 0

* - ![](../../media/td-transformations-t.png)
```

**Trasformazione isobara, $P $ cost.**

...

La trasformazione può essere rappresentata nei piani termodinamici $P-V$ e $T-S$ come delle curve parametrizzabili con un parametro libero,

$$\overline{P} = \rho R T$$
$$e_2 - e_1 = c_v (T_2 - T_1) = \frac{c_v}{R} \overline{P} (V_2 - V_1)$$
$$d s = c_P \dfrac{d\rho}{\rho} \quad \rightarrow \quad s_2 - s_1 = c_P \ln \frac{\rho_2}{\rho_1} = - c_P \ln \frac{V_2}{V_1} $$
$$d s = c_P \dfrac{d T  }{T   } \quad \rightarrow \quad s_2 - s_1 = c_P \ln \frac{T_2}{T_1} $$

```{list-table}
:header-rows: 0

* - ![](../../media/td-transformations-p.png)
```

**Trasformazione isentropica, $S $ cost.** Una trasformazione isentropica - adiabatica ideale con $\delta Q = 0$, $\delta^+ D = 0$, $\delta S = 0$ - la variazione di energia interna del sistema è uguale al lavoro fatto sul sistema

$$- P dV = \delta L^e = d E = \overline{m} c_v d T \ ,$$

da cui

$$0 = ds = - R \frac{d P}{P} + c_P \frac{d T}{T} =  c_v \frac{d P}{P} - c_P \frac{d \rho}{\rho} = - R \frac{d \rho}{\rho} + c_v \frac{d T}{T} $$

$$\begin{aligned}
  \left(\frac{P_2}{P_1}      \right) & = \left(\frac{\rho_2}{\rho_1} \right)^{\gamma}  \\  
  \left(\frac{P_2}{P_1}      \right) & = \left(\frac{T_2}{T_1}       \right)^{\frac{\gamma}{\gamma-1}}  \\
  \left(\frac{\rho_2}{\rho_1}\right) & = \left(\frac{T_2}{T_1}       \right)^{\frac{1}{\gamma-1}}  \\
\end{aligned}$$

avendo usato le relazioni

$$c_P - c_v = R$$
$$\gamma = \frac{c_P}{c_v}$$

per calcolare i rapporti

$$\begin{aligned}
 \frac{c_P}{c_v} & = \gamma \\
 \frac{c_P}{R}   & = \frac{\gamma}{\gamma - 1} \\
 \frac{c_v}{R}   & = \frac{1}{\gamma - 1} \\
\end{aligned}$$

...

```{list-table}
:header-rows: 0

* - ![](../../media/td-transformations-s.png)
```
