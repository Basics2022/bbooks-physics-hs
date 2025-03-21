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


$$M_j \partial_{tt} u(x_j,t) - \Delta x^2 K \partial_{xx} u(x_j,t) = F_j(t) $$


(physics-hs:waves:equation:examples:mechanics:torsion)=
### Torsione - catena di molle rotazionali

$$I \partial_{tt} \theta(x_j,t) - \Delta x^2 K_t \partial_{xx} \theta(x_j,t) = M_j(t)$$


(physics-hs:waves:equation:examples:mechanics:string)=
### Filo teso

$$M_j \partial_{tt} u(x_j,t) - \Delta x^2 N_0 \partial_{xx} u(x_j,t) = F_j(t)$$

Esempio: corde di strumenti musicali.

(physics-hs:waves:equation:examples:fluids)=
## Fluidi

(physics-hs:waves:equation:examples:fluids:sound)=
### Suono

La percezione umana dell'udito è legata alla trasduzione di perturbazioni di pressione di ampiezza limitata da parte del nostro sistema di misura che va dall'orecchio al nostro cervello, capace di percepire perturbazioni di frequenza compresa qualitativamente tra $20 \, \text{Hz}$ e $20.000 \, \text{Hz}$.

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

(physics-hs:waves:equation:examples:fluids:surface)=
### Onde su superficie libera


(physics-hs:waves:equation:examples:em)=
## Campo elettromagnetico

