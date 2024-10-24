(physics-hs:thermodynamics:matter:gases:ideal:formulas)=
# Caratteristiche dei gas perfetti

## Legge di stato

$$\begin{aligned}
  P V & =    N \, k_B \, T & \\
                           & & \qquad \text{$\left( N = N_A \, n \ , \  N_A \, k_B = R \right)$} \\ \\
  P V & =    n \, R   \, T & \\
                           & & \qquad \text{$\left( m = M_m \, n \ , \  R_g = \frac{R}{M_m} \right)$} \\ \\
  P V & =    m \, R_g \, T & \\
                           & & \qquad \text{$\left( m = \rho \, V \right)$} \\ \\
  P   & = \rho \, R_g \, T & \qquad \\
\end{aligned}$$

## Primo principio della termodinamica

Per un gas comprimibile monocomponente, il lavoro interno meccanico reversibile è

$$\delta L^{int,rev, mech} = P \, d V$$

In assenza di altre interazioni di lavoro, il bilancio di energia interna per un gas comprimible diventa

$$\begin{aligned}
  d E & = \delta Q^{ext} + \delta^+ D - \delta L^{int,rev} = \\
      & = T \, dS - P \, dV \ .
\end{aligned}$$

## Energia interna, entalpia e calori specifici
**Energia interna.** Seguendo le conclusioni del modello di gas ideale fornito dalla [teoria cinetica dei gas](physics-hs:thermodynamics:matter:gases:ideal:kinetic-theory), l'espressione dell'energia interna di un gas perfetto può essere scritta come,

$$E = \frac{f}{2} \, N \, k_B \, T = \frac{f}{2} \, n \, R \, T = m \frac{f}{2} \, R_g \, T \ .$$

**Entalpia.** Usando la definizione di entalpia $H = E + F_i \, X_i = E + P \, V$, l'equazione di stato e l'espressione dell'energia interna dei gas perfetti, l'entalpia di un gas perfetto può essere scritta come

$$H = \left(\frac{f}{2} + 1 \right) \, N \, k_B \, T = \left( \frac{f}{2} + 1 \right) \, n \, R \, T = m \left( \frac{f}{2} + 1 \right) \, R_g \, T \ .$$

**Calore specifico a volume costante.** Se il volume del sistema è costante, il lavoro interno è nullo (**todo** complessivo, reversibile, <span style="color:red">aggiungere ipotesi di stato di equilibrio una volta per tutte?</span>), $\delta L = 0$, $dE = \delta Q^{ext} = T \, dS$

$$m \, c_v \, d T := \delta Q^{ext}\big|_v = dE\big|_v = m \frac{f}{2} \, R_g \, d T 
\qquad \rightarrow \qquad
c_v = \frac{f}{2} \, R_g \ .$$


**Calore specifico a pressione costante.** Il differenziale dell'entropia a pressione costante,

$$dH\big|_P = d ( E + P \, V )\big|_P  = d E\big|_P  + \underbrace{d P}_{=0} \, V + P \, dV\big|_P \ ,$$

può essere utilizzato per riscrivere il bilancio di energia intenra a pressione costante,

$$dH\big|_P = dE\big|_P + P \delta V\big|_P = \delta Q^{ext}\big|_P + \delta^+ D\big|_P \ .$$

Nell'ipotesi che la dissipazione sia nulla, (**todo** <span style="color:red">aggiungere ipotesi di stato di equilibrio una volta per tutte?</span>)), si può quindi legare la variazione di entalpia del sistema all'apporto di calore al sistema, e al calore specifico a pressione costante,

$$m \, c_P \, dT := \delta Q^{ext}\big|_P = d H \big|_P = m \left( \frac{f}{2} + 1 \right) \, R_g \, d T 
\qquad \rightarrow \qquad
c_P = \left( \frac{f}{2} + 1 \right) \, R_g \ .$$

**Esempi: calcolo del calore specifico di gas**
```{dropdown} Idrogeno molecolare, $\text{ H}_2$
Assumendo che l'idrogeno, $\text{H}_2$, con massa molare $M_m = 2.0 \frac{\text{kg}}{\text{kmol}}$, si comporti come un gas perfetto nella condizione di interesse, la costante specifica dell'idrogeno molecolare vale

$$R_g = \frac{R}{M_m} = \frac{8314 \frac{\text{J}}{\text{kmol} \text{ K}}}{2 \frac{\text{kg}}{\text{kmol}}} = 4157 \frac{\text{J}}{\text{kg} \text{ K}} .$$

e i calori specifici

$$c_v = \frac{5}{2} \, R_g = \frac{5}{2} \, 4157 \, \frac{\text{J}}{\text{kg} \text{ K}} = 10392.5 \, \frac{\text{J}}{\text{kg} \text{ K}} $$
$$c_P = \frac{7}{2} \, R_g = \frac{7}{2} \, 4157 \, \frac{\text{J}}{\text{kg} \text{ K}} = 14549.5 \, \frac{\text{J}}{\text{kg} \text{ K}} $$
```
```{dropdown} Elio, $\text{ He}$
Assumendo che l'elio, $\text{He}$, con massa molare $M_m = 4 \frac{\text{kg}}{\text{kmol}}$, si comporti come un gas perfetto nella condizione di interesse, la costante specifica dell'idrogeno molecolare vale

$$R_g = \frac{R}{M_m} = \frac{8314 \frac{\text{J}}{\text{kmol} \text{ K}}}{4 \frac{\text{kg}}{\text{kmol}}} = 2078.5 \frac{\text{J}}{\text{kg} \text{ K}} .$$

e i calori specifici

$$c_v = \frac{3}{2} \, R_g = \frac{3}{2} \, 2078.5 \, \frac{\text{J}}{\text{kg} \text{ K}} = 3117.8 \, \frac{\text{J}}{\text{kg} \text{ K}} $$
$$c_P = \frac{5}{2} \, R_g = \frac{5}{2} \, 2078.5 \, \frac{\text{J}}{\text{kg} \text{ K}} = 5196.2 \, \frac{\text{J}}{\text{kg} \text{ K}} $$
```
<!--**Esempio: aria.**-->
```{dropdown} Aria, miscela di gas
L'aria è una miscela di gas (**todo** *riferimento a miscele?*) composta da $\text{N}_2$, $\text{O}_2$,... la cui massa molare è la media pesata delle masse molari dei suoi componenti, $M_m = 28.97 \frac{\text{kg}}{\text{kmol}}$.
La costante specifica dell'aria è quindi

$$R_g = \frac{R}{M_m} = \frac{8314 \frac{\text{J}}{\text{kmol} \text{ K}}}{28.97 \frac{\text{kg}}{\text{kmol}}} = 287 \frac{\text{J}}{\text{kg} \text{ K}} .$$

Essendo composta da molecole di gas biatomiche, i gradi di libertà della singola molecola sono $f = 5$ (3 legati alla traslazione, 2 alla rotazione; manca la rotazione attorno all'asse della molecola, assumendo trascurabile l'inerzia attorno a quell'asse). I calori specifici valgono quindi

$$c_v = \frac{5}{2} \, R_g = \frac{5}{2} \, 287 \, \frac{\text{J}}{\text{kg} \text{ K}} =  717.5 \, \frac{\text{J}}{\text{kg} \text{ K}} $$
$$c_P = \frac{7}{2} \, R_g = \frac{7}{2} \, 287 \, \frac{\text{J}}{\text{kg} \text{ K}} = 1004.5 \, \frac{\text{J}}{\text{kg} \text{ K}} $$
```

## Variazioni di entropia
La variazione dell'entropia di un gas perfetto può essere scritta in diverse forme partendo dal primo principio della termodinamica e usando l'espressione dell'energia interna e la legge di stato dei gas perfetti per cambiare le variabili indipendenti,

$$\begin{aligned}
  ds & = \frac{1}{T} \left( d e + \frac{P}{\rho^2} d \rho \right) = \\
     & = c_v \frac{dT}{T} + R_g \frac{d \rho}{\rho} = \\
     & = c_P \frac{dT}{T} + R_g \frac{d P}{P} = \\
     & = c_P \frac{d \rho}{\rho} + c_v \frac{d P}{P}  \ .
\end{aligned}$$


