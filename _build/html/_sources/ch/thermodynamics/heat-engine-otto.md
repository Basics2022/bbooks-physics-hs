(physics-hs:thermodynamics:heat-engine:otto)=
# Ciclo Otto

**Storia e applicazioni.**

## Ciclo Otto reale
...

## Ciclo Otto ideale
Un modello ideale del ciclo Otto è formato da:
- $0 \rightarrow 1$ aspirazione a pressione costante, $P_1$. Durante l'aspirazione, il sistema è aperto: le valvole di aspirazione sono aperte per far entrare l'aria in camera di combustione. Alla fine dell'aspirazione, le valvole vengono chiuse e il sistema di interesse è un sistema chiuso
- $1 \rightarrow 2$ compressione adiabatica in sistema chiuso
- $2 \rightarrow 3$ combustione a volume costante: la combustione avviene in maniera sufficientemente veloce da poter essere modellata come una trasformazione termodinamica a volume costante, in corrispondenza del punto morto superiore; in prima approssimazione, si può trascurare il flusso di massa del combustibile e la variazione delle proprietà chimico-fisiche del fluido di lavoro; la reazione di combustione produce il calore in ingresso al sistema
- $3 \rightarrow 4$ espansione adiabatica
- $4 \rightarrow 1$, $1 \rightarrow 0$ scarico libero e scarico forzato. **todo** in prima approssimazione, la parte di scarico al punto morto inferiore non produce lavoro poiché $\Delta V_{14} = 0$ e la fase di scarico forzata è equilibrata dalla fase di aspirazione. 

## Rendimento del ciclo Otto


$$\eta = 1 + \dfrac{\Delta Q_{41}}{\Delta Q_{23}}
       = 1 + \dfrac{m \, c_V \, (T_1 - T_4)}{m \, c_V \, (T_3 - T_2)}
       = 1 + \dfrac{T_1 - T_4}{T_3 - T_2}
$$

Usando le condizioni, **todo** *usare direttamente le espressioni delle adiabatiche ideali ricavate nella sezione delle trasformazioni termodinamiche con gas ideali*

$$V_2 = V_3 \qquad , \qquad V_1 = V_4$$
$$P_1 \, V_1^{\gamma} = P_2 \, V_2^{\gamma}$$
$$P_3 \, V_3^{\gamma} = P_4 \, V_4^{\gamma}$$

e la legge dei gas ideali, $P V = m R T$, assumendo che sia un'equazione di stato adatta a descrivere il fluido di lavoro, per riscrivere l'equazione delle trasformazioni adiabatiche

$$\begin{aligned}
  T_1 \, V_1^{\gamma-1} & = T_2 \, V_2^{\gamma-1} \\
  T_3 \, V_3^{\gamma-1} & = T_4 \, V_4^{\gamma-1}
\end{aligned}
\begin{aligned}
  & \qquad \rightarrow \qquad  (T_4 - T_1) \, V_1^{\gamma-1} = (T_3 - T_2) \, V_2^{\gamma - 1} \\
  & \qquad \rightarrow \qquad  \dfrac{T_4 - T_1}{T_3 - T_2} = \left( \dfrac{V_2}{V_1} \right)^{\gamma-1} = \dfrac{1}{\beta^{\gamma - 1}} \\
\end{aligned}
$$

è possibile riscrivere l'espressione del rendimento del ciclo Otto in funzione unicamente del rapporto di compressione volumetrico $\beta := \dfrac{V_1}{V_2}$,

$$\eta = 1 - \dfrac{1}{\beta^{\gamma-1}} \ .$$

## Funzionamento di un motore interno

## Esempio

