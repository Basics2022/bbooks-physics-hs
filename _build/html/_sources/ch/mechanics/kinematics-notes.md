(physics-hs:mechanics:kinematics:notes)=
# Note e dimostrazioni

(physics-hs:mechanics:kinematics:notes:point)=
## Cinematica del punto

(physics-hs:mechanics:kinematics:notes:point:a-0)=
### Moto uniforme, $\ \ddot{\vec{r}}_P(t) = \vec{0}$
Il moto uniforme è un moto rettilineo.

```{dropdown} Dimostrazione
:name: kinematics-notes-uniform

Poiché $\ddot{\vec{r}}_P(t) = \vec{0}$, allora

$$\begin{aligned}
  \dot{\vec{r}}_P(t) & = \vec{v} \\
  \vec{r}_P(t) & = \vec{r}_0 + \vec{v} \, t \\
\end{aligned}$$

L'espressione della posizione in funzione del tempo è l'espressione parametrica della retta passante per $\vec{r}_0$ con la stessa direzione del vettore velocità $\vec{v}$, vedi [Matematica:Geometrica analitica nello spazio:Rette nello spazio](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/analytic_geometry/analytic_geometry_3d/lines.html#definizione-ed-equazione).

```

(physics-hs:mechanics:kinematics:notes:point:motion:a)=
### Moto uniformemente accelerato, $\ \ddot{\vec{r}}_P(t) = \vec{a}$

<!--
(physics-hs:mechanics:kinematics:notes:point:motion:a:linear)=
#### Moto rettilineo uniformemente accelerato - moto rettilineo

(physics-hs:mechanics:kinematics:notes:point:motion:a:planar)=
#### Moto parabolico - moto piano
-->

Il moto uniformemente accelerato è un moto piano. Se la velocità iniziale $\vec{v}_0$ (o in qualsiasi istante temporale) ha la stessa direzione dell'accelerazione costante, $\vec{a}$, allora il moto è rettilineo e si svolge sulla retta passante per il punto iniziale $P_0$ con la direzione di $\vec{a}$.
Nel caso in cui $\vec{v}_0$ e $\vec{a}$ non sono allineati, il moto è parabolico e si svolge nel piano passante per $P_0$ con direzione normale sia a $\vec{v}_0$ sia a $\vec{a}$.

<!--posizione del punto $P$ in un istante, e la sua velocità $\dot{\vec{r}}_P(t) = \vec{v}_P(t)$, il moto si svolge nel piano passante per $P$, nel quale giacciono i vettori velocità $\vec{v}_P(t)$ e accelerazione $\vec{a}$.-->

```{dropdown} Dimostrazione
:name: kinematics-notes-const-a-planar

Data l'accelerazione costante $$\ddot{\vec{r}}_P(t) = \vec{a}$$, velocità e posizione sono

$$\begin{aligned}
  \vec{v}_P(t) & = \vec{v}_0 + \vec{a} \, t \\
          P(t) & =       P_0 + \vec{v}_0 \, t + \dfrac{1}{2} \vec{a} \ t^2 \\
\end{aligned}$$

**Moto rettilineo uniformemente accelerato.** Se $\vec{v}_0 = v_0 \hat{t}$, $\vec{a} = a \hat{t}$, allora

$$\begin{aligned}
  \vec{v}_P(t) & = ( v_0 + a \, t ) \hat{t} \\
          P(t) - P_0 & = \left( v_0 \, t + \dfrac{1}{2} a \, t^2 \right) \hat{t}  \\
\end{aligned}$$

**Moto parabolico.** Si scelgono due direzioni ortogonali $\hat{x}$, $\hat{y}$ definite dalle direzioni di $\vec{a}$ e $\vec{v}_0$

$$\begin{aligned}
  \vec{a}   & = a \hat{x} \\
  \vec{v}_0 & = v_{0,x} \hat{x} + v_{0,y} \hat{y} \\
\end{aligned}$$

con $v_{0,y} \ne 0$ (altrimenti si è nel caso di moto rettilineo uniformemente accelerato con $\vec{v}_0 \parallel \vec{a}$) così che la posizione in funzione del tempo è

$$\begin{aligned}
  P(t) - P_0 = \Delta x_P(t) \hat{x} + \Delta y_P(t) \hat{y} =
  \hat{x} \left( \dfrac{1}{2} a t^2 + v_{0,x} t \right) +
  \hat{y} \left( v_{0,y} t \right)
\end{aligned}$$

ed è possibile scrivere la coordinata $x$ in funzione della coordinata $y$ come

$$\Delta x_P = \frac{1}{2} \, a \, \dfrac{ \Delta y_P^2}{v_{0,y}^2} + \frac{v_{0,x}}{v_{0,y}} \Delta y_P$$

```
