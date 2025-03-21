(physics-hs:waves:equation:examples)=
# Equazione delle onde in diversi sistemi
In questa sezione viene discusso il ruolo dell'equazione delle onde in diversi ambiti della fisica. La dinamica di perturbazioni di ampiezza "sufficientemente piccola" è descritta da un problema lineare, governato dall'equazione delle onde...**todo**

(physics-hs:waves:equation:examples:mechanics)=
## Sistemi meccanici

(physics-hs:waves:equation:examples:mechanics:axial)=
### Azione assiale - catena di molle lineari

$$M_j \ddot{U}_j(t) = F_{j,j-1} + F_{j,j+1} + F_j^{ext}(t) = K_{j,j-1} \left( U_{j-1}(t) - U_j(t) \right) + K_{j,j+1} \left( U_{j+1}(t) - U_{j}(t) \right) + f_j^{ext}$$

...

Se le molle hanno tutte la stessa rigidezza, $K$,

$$M_j \ddot{U}_j(t) - K \left( U_{j-1}(t) - 2 U_j(t) + U_{j+1}(t) \right) =  F^e_j(t) \ .$$ (eq:axial:discrete:index)

**Condizioni iniziali e condizioni al contorno.**

**Forma matriciale.** Il problema può essere riscritto usando il formalismo matriciale come

$$\begin{aligned}
  \mathbf{M} \ddot{\mathbf{U}} + \mathbf{K} \mathbf{U} = \mathbf{F}^e \ ,
\end{aligned}$$

con le matrici

$$\mathbf{K} = K \begin{bmatrix}
   2    & -1    &  0    &  0    & 0     & \dots & 0     \\
  -1    &  2    & -1    &  0    & 0     & \dots & 0     \\ 
   0    & -1    &  2    & -1    & 0     & \dots & 0     \\
  \dots & \dots & \dots & \dots & \dots & \dots & \dots \\
   0    & 0     & \dots & 0     &    2  & -1    &  0    \\  
   0    & 0     & \dots & 0     &   -1  &  2    & -1    \\  
\end{bmatrix}$$

$$\mathbf{M} = \begin{bmatrix}
   M_1  &  0    &  0    &  \dots   & 0     \\
   0    &  M_2  &  0    &  \dots   & 0     \\ 
   0    &  0    &  M_3  &  \dots   & 0     \\
  \dots & \dots & \dots &  \dots   & \dots \\
   0    & 0     & \dots &  M_{n-1} & 0     \\  
   0    & 0     & \dots &  0       & M_n   \\  
\end{bmatrix}$$

$$\mathbf{U}(t) = \begin{bmatrix} U_0(t) & U_1(t) & \dots & U_n(t) \end{bmatrix}^T$$
$$\mathbf{F}(t) = \begin{bmatrix} F_0(t) & F_1(t) & \dots & F_n(t) \end{bmatrix}^T$$

**Approssimazione di un problema continuo.** Gli elementi del vettore $\mathbf{U}$ possono essere interpretati come i valori di una funzione del tempo e dello spazio, $u(x,t)$, per determinati valori della variabile indipendente $x$,

$$U_j(t) = u(x_j, t) \ .$$

Se i punti di coordinata $x_j$ hanno intervalli regolari,

$$x_j = x_{j-1} + \Delta x \qquad , \qquad x_j = j \, \Delta x \qquad j = 0:n \ ,$$

con $\Delta x$ "sufficientemente piccolo", allora l'approssimazione in serie di Taylor

$$\begin{aligned}
  & u(x_i,t) \\
  & u(x_i+\Delta x, t) = u(x_i,t) + \Delta x \partial_x u(x_i,t) + \dfrac{1}{2} \Delta x^2 \partial_{xx} u(x_i,t) + o(\Delta x^2) \\
  & u(x_i-\Delta x, t) = u(x_i,t) - \Delta x \partial_x u(x_i,t) + \dfrac{1}{2} \Delta x^2 \partial_{xx} u(x_i,t) + o(\Delta x^2) \\
\end{aligned}$$

permette di riconoscere l'approssimazione centrata della derivata seconda $\partial_{xx} u(x_i, t)$ valutata in $x = x_i$,

$$\partial_{xx} u(x_i,t) = \dfrac{u(x_i-\Delta x,t) - 2 u(x_i,t) + u(x_i+\Delta x,t)}{\Delta x^2}$$


$$M_j \partial_{tt} u(x_j,t) - K \partial_{xx} u(x_j,t) = F_j(t) $$


(physics-hs:waves:equation:examples:mechanics:torsion)=
### Torsione - catena di molle rotazionali

$$I \partial_{tt} \theta(x_j,t) - K_t \partial_{xx} \theta(x_j,t) = M_j(t)$$


(physics-hs:waves:equation:examples:mechanics:string)=
### Filo teso

$$M_j \partial_{tt} u(x_j,t) - N_0 \partial_{xx} u(x_j,t) = F_j(t)$$

Esempio: corde di strumenti musicali.

(physics-hs:waves:equation:examples:fluids)=
## Fluidi

(physics-hs:waves:equation:examples:fluids:sound)=
### Suono

La percezione umana dell'udito è legata alla trasduzione di perturbazioni di pressione di ampiezza limitata da parte del nostro sistema di misura che va dall'orecchio al nostro cervello, capace di percepire perturbazioni di frequenza compresa qualitativamente tra $20 \, \text{Hz}$ e $20.000 \, \text{Hz}$.

E' possibile ricavare l'equazione delle onde per il campo di pressione usando le equazioni di [bilancio per sistemi aperti](physics-hs:mechanics:dynamics:eom:open) di massa e di quantità di moto, applicati a dei volumi elementari del dominio di interesse.

Si assume qui che il fluido nel quale si propaga la perturbazione acustica sia in quiete. Il calcolo viene inizialmente svolto in un ambito di spazio e variaili discrete, e solo alla fine vengono riconosciute le espressioni approssimate alle differenze delle derivate per tornare a un modello continuo. Si assume una dimensione uniforme dei domini elementari.

(physics-hs:waves:equation:examples:fluids:sound:1d)=
#### Dominio 1-dimensionale

Si considerano serie di elementi...e si scrive il bilancio di massa per gli elementi con indice intero, e il bilancio di quantità di moto per i volumi di indice frazionario "adiacenti"

$$\begin{aligned}
  \Delta x \, \dot{\rho}_i & = \overline{\rho} u_{i-\frac{1}{2}} - \overline{\rho} u_{i+\frac{1}{2}} \\
  \Delta x \, \overline{\rho} \dot{u}_{i-\frac{1}{2}} & = P_{i-1} - P_{i} \\
  \Delta x \, \overline{\rho} \dot{u}_{i+\frac{1}{2}} & = P_{i  } - P_{i+1}  
\end{aligned}$$

Derivando in tempo il bilancio della massa dell'elemento $i$ e sostituendo in esso le due espressioni del bilancio della quantità di moto degli elementi $i-\frac{1}{2}$ e $i+\frac{1}{2}$ si ottiene

$$\Delta x \ddot{\rho}_i = \frac{1}{\Delta x} \left[ P_{i-1} - 2 P_i + P_{i+1} \right] \ ,$$

e ricordando la definizione di velocità del suono $a$ **todo** (data dove? Forse è proprio questo il posto dove darla, assumendo una relazione lineare - tanto tutto o quasi è lineare nel piccolo - tra la perturbazione di pressione e la pertubazione di densità $P_i = a^2 \rho_i$), si può scrivere

$$\frac{1}{a^2} \ddot{P}_i - \dfrac{P_{i-1} - 2 P_i + P_{i+1}}{\Delta x^2} = 0 \ .$$

Avendo indicato il valore della pressione in $x_k$ come $P_k = P(x_k)$, si può riconoscere l'approssimazione della derivata seconda della pressione, e tornando al continuo e ricordando il significato di derivata parziale, ricavare l'equazione delle onde per la perturbazione di pressione in un mezzo in quiete[^medium-at-res]

$$\frac{1}{a^2} \partial_{tt} P - \partial_{xx} P = 0 \ .$$

[^medium-at-rest]: Il concetto di quiete è sempre riferito a un osservatore.

**Osservazione.** Il metodo descritto qui rappresenta un'applicazione elementare del metodo dei volumi finiti, metodo utilizzato per la soluzione numerica di equazioni differentiali.

(physics-hs:waves:equation:examples:fluids:sound:nd)=
#### Dominio n-dimensionale

Si può ripetere il procedimento per un [dominio 1-dimensionale](physics-hs:waves:equation:examples:fluids:sound:1d) in un dominio $n$-dimensionale, usando due suddivisioni "sfalsate" del dominio, una per calcolare il bilancio di massa, l'altra per calcolare il bilancio di quantità di moto. Ripendo il procedimento, si arriva a un'equazione che contiene l'approssimazione dell'operatore laplaciano della pressione,

$$\begin{aligned}
 \text{2-d:} & \quad \dfrac{P_{i-1,j-1}+P_{i-1,j+1}+P_{i+1,j+1}+P_{i+1,j-1}-4 P_{i,j}}{\Delta x^2} \sim \partial_{xx} P_i + \partial_{yy} P_i \\
 \text{3-d:} & \quad \dfrac{P_{i-1,j-1,k-1}+\dots + P_{i+1,j+1,k+1}-8 P_{ijk}}{\Delta x^2} \sim \partial_{xx} P_i + \partial_{yy} P_i + \partial_{zz} P_i \\
\end{aligned}$$

Per motivi di sintesi e per motivi di comprensione, l'approssimazione del laplaciano della pressione può essere scritta come sommatoria delle differenze della pressione nei domini $\mathbf{j}$ vicini al dominio $\mathbf{i}$, cioè appartenenti a quella che viene definita bolla di $\mathbf{i}$, $\mathbf{j} \in B(\mathbf{i})$,

$$\nabla^2 P_i \sim \dfrac{\sum_{\mathbf{j} \in B(\mathbf{i})}\left( P_{\mathbf{j}} - P_{\mathbf{i}} \right)}{\Delta x^2} \ .$$

```{prf:example} Dominio $2$-dimensionale

```

```{prf:example} Dominio $3$-dimensionale

```

<!--
**Suono in un tubo.** 

Poi da cancellare o riscrivere meglio per il livello

$$P(\rho,s)$$ 

$$d P = \left( \dfrac{\partial P}{\partial \rho} \right)_s \, d \rho + \left( \dfrac{\partial P}{\partial s} \right)_{\rho} \, ds $$

$$
\begin{cases}
  \dfrac{1}{c^2} \partial_t P + \rho_0 \partial_x u = 0 \\
  \rho_0 \partial_t u + \partial_x P = 0 \\
\end{cases}
$$

$$\dfrac{1}{c^2} \partial_{tt} P - \partial_{xx} P = 0$$

**Suono nello spazio.**

$$\dfrac{1}{c^2} \partial_{tt} P - \nabla^2 P = 0$$
-->

(physics-hs:waves:equation:examples:fluids:surface)=
### Onde su superficie libera


(physics-hs:waves:equation:examples:em)=
## Campo elettromagnetico

