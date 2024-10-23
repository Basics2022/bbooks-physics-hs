(physics-hs:thermodynamics:heat-engine:joule-brayton)=
# Ciclo Joule-Brayton

**Storia e applicazioni.**
Il ciclo Joule-Brayton rappresenta il ciclo termodinamico ideale per il funzionamento a ciclo continuo delle macchine a gas.

Nelle moderne applicazioni, le turbine a gas possono operare 
- a ciclo aperto: motori a getto, ad esempio per propulsione aeronautica
- ciclo chiuso: turbine con rigenerazione
- cicli combinati

Entrambe le configurazioni sono realizzate con macchine termiche continue, che sono **sistemi aperti** **todo** *scrivere la sezione per i sistemi aperti e aggiungere riferimento*

## Ciclo Joule-Brayton aperto

## Ciclo Joule-Brayton chiuso

Un modello ideale del ciclo Joule-Brayton è formato da:
- $1 \rightarrow 2$ compressione adiabatica in compressore, tipicamente dinamico assiale - sistema aperto
- $2 \rightarrow 3$ combustione a pressione costante: la combustione avviene in camera di combustione aperta e viene modellata come una trasformazione termodinamica a pressione costante; in prima approssimazione, si può trascurare il flusso di massa del combustibile e la variazione delle proprietà chimico-fisiche del fluido di lavoro; la reazione di combustione produce il calore in ingresso al sistema
- $3 \rightarrow 4$ espansione adiabatica in turbina - sistema aperto
- $4 \rightarrow 1$, raffreddamento a pressione costante

## Rendimento del ciclo Joule-Brayton

$$\eta = 1 + \dfrac{\dot{Q}_{41}}{\dot{Q}_{23}}
       = 1 + \dfrac{\dot{m} \, c_P \, (T_1 - T_4)}{\dot{m} \, c_P \, (T_3 - T_2)}
       = 1 + \dfrac{T_1 - T_4}{T_3 - T_2}
$$

Usando le condizioni, **todo** *usare direttamente le espressioni delle adiabatiche ideali ricavate nella sezione delle trasformazioni termodinamiche con gas ideali*

$$P_2 = P_3 \qquad , \qquad P_1 = P_4$$
$$P_1 \, V_1^{\gamma} = P_2 \, V_2^{\gamma}$$
$$P_3 \, V_3^{\gamma} = P_4 \, V_4^{\gamma}$$

e la legge dei gas ideali, $P V = m R T$, assumendo che sia un'equazione di stato adatta a descrivere il fluido di lavoro, per riscrivere l'equazione delle trasformazioni adiabatiche

$$\begin{aligned}
  P_1^{1-\gamma} \, T_1^{\gamma} & = P_2^{1-\gamma} \, T_2^{\gamma} \\
  P_3^{1-\gamma} \, T_3^{\gamma} & = P_4^{1-\gamma} \, T_4^{\gamma}
\end{aligned}
\begin{aligned}
  & \qquad \rightarrow \qquad  (T_4 - T_1) \, P_1^{\frac{1-\gamma}{\gamma}} = (T_3 - T_2) \, P_2^{\frac{1-\gamma}{\gamma}} \\
  & \qquad \rightarrow \qquad  \dfrac{T_4 - T_1}{T_3 - T_2} = \left( \dfrac{P_1}{P_2} \right)^{\frac{\gamma-1}{\gamma}} = \dfrac{1}{\beta^{\frac{\gamma - 1}{\gamma}}} \\
\end{aligned}
$$

è possibile riscrivere l'espressione del rendimento del ciclo Otto in funzione unicamente del rapporto di compressione $\beta := \dfrac{P_2}{P_1}$,

$$\eta = 1 - \dfrac{1}{\beta^{\frac{\gamma-1}{\gamma}}} \ .$$


## Esempio
**todo**


