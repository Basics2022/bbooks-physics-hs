(physics-hs:mechanics:dynamics:problems:extra)=
# Altri problemi

````{only} html

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 1. Sistema di carrucole
:columns: 8

Determinare le equazioni del moto, e determinare la direzione di rotazione delle due carrucole.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/dynamics/pulley-1.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Equazioni del moto - con bilanci meccanici ("meccanica di Newton")

```
```{dropdown} Equazioni del moto - con equazioni di Lagrange
:open:

Questo approccio richiede la conoscenza della meccanica lagrangiana, che non rientra nel programma di scuola superiore. Per riferimenti, [Physics-Mechanics:Lagrangian Mechanics](https://basics2022.github.io/bbooks-physics-mechanics/ch/lagrange.html).

Il sistema ha due gradi di libertà. Qui si scelgono gli angoli di rotazione delle carrucole $\theta_1$, $\theta_2$ come gradi di libertà indipendenti. Le equazioni di Lagrange (del secondo tipo)

$$\dfrac{d}{dt} \left( \frac{\partial \mathscr{L}}{\partial \dot{q}^k}  \right) - \frac{\partial \mathscr{L}}{\partial q^k} = Q_k \ ,$$

forniscono le equazioni pure del moto, dove $\mathscr{L}$ indica la lagrangiana del sistema, $\mathscr{L} = K + U$, somma dell'energia cinetica e del potenziale (opposto dell'energia potenziale, anche se questa definizione viene contestata da qualcuno. Se siete tra questi, scrivete $\mathscr{L} = K - V$ che passa la paura e la polemica, e passate oltre). L'energia cinetica e il potenziale del problema sono rispettivamente

$$\begin{aligned}
  K & = \frac{1}{2} \left( I_2 + ( m_2 + m_3 ) R_2^2 \right) \dot{\theta}_2^2 + \frac{1}{2} \left( I_1 + (M_2 + m_1 + m_2 + m_3) R_1^2 \right) \dot{\theta}_1^2  + ( m_2 - m_3 ) R_1 R_2 \dot{\theta}_1 \dot{\theta}_2 \\
  U & = ( m_2 - m_3 ) g R_2 \theta_2 + ( M_2 - m_1 + m_2 + m_3 ) g R_1 \theta_1 \ .
\end{aligned}$$

Inserendo le espressioni di energia cinetica e potenziale nelle equazioni di Lagrange, si trovano le equazioni pure del moto del sistema

$$\begin{bmatrix} I_1 + (M_2+m_1+m_2+m_3) R_1^2 & (m_2 - m_3) R_1 R_2 \\ (m_2 - m_3) R_1 R_2 & I_2 + (m_2+m_3) R_2^2  \end{bmatrix}\begin{bmatrix} \ddot{\theta}_1 \\ \ddot{\theta}_2 \end{bmatrix} = \begin{bmatrix} ( M_2 - m_1 + m_2 + m_3 ) R_1 \\ ( m_2 - m_3 ) R_2  \end{bmatrix} g \ .$$

```

```{dropdown} Accelerazione
:open:

Invertendo la matrice dei coefficienti costanti che moltiplica il vettore delle accelerazioni $\ddot{\theta}_k$, si ottiene l'espressione esplicita delle accelerazioni in funzione delle caratteristiche del sistema e della accelerazione di gravità $g$,

$$\begin{bmatrix} \ddot{\theta}_1 \\ \ddot{\theta}_2 \end{bmatrix} = \frac{1}{\text{det}(\mathbf{M})} \begin{bmatrix} I_2 + (m_2+m_3) R_2^2 & -(m_2 - m_3) R_1 R_2 \\ -(m_2 - m_3) R_1 R_2 & I_1 + (M_2+m_1+m_2+m_3) R_1^2   \end{bmatrix}\begin{bmatrix} ( M_2 - m_1 + m_2 + m_3 ) R_1 \\ ( m_2 - m_3 ) R_2  \end{bmatrix} g \ .$$

e quindi

$$\begin{aligned}
  \begin{bmatrix} \ddot{\theta}_1 \\ \ddot{\theta}_2 \end{bmatrix} 
  & = \frac{1}{\text{det}(\mathbf{M})} \begin{bmatrix} \left( I_2 + (m_2+m_3) R_2^2 \right) \left( M_2 - m_1 + m_2 + m_3 \right) R_1 -(m_2 - m_3) (m_2-m_3) R_1 R_2^2 \\ -(m_2 - m_3) (M_2 - m_1 + m_2 +m_3 ) R_1^2 R_2 + \left( I_1 + (M_2+m_1+m_2+m_3) \right)(m_2 - m_3) R_1^2 R_2 \end{bmatrix} g = \\
\end{aligned}$$

Assumendo trascurabile l'inerzia delle carrucole rispetto a quella dei pesi, $M_k = 0$, $I_k = 0$,

$$\begin{aligned}
  \begin{bmatrix} \ddot{\theta}_1 \\ \ddot{\theta}_2 \end{bmatrix} 
  & = \frac{1}{\text{det}(\mathbf{M})} \begin{bmatrix} \left( (m_2+m_3) R_2^2 \right) \left( - m_1 + m_2 + m_3 \right) R_1 -(m_2 - m_3) (m_2-m_3) R_1 R_2^2 \\ -(m_2 - m_3) (- m_1 + m_2 +m_3 ) R_1^2 R_2 + \left( (m_1+m_2+m_3) \right)(m_2 - m_3) R_1^2 R_2 \end{bmatrix} g = \\
  & = \frac{1}{\text{det}(\mathbf{M})} \begin{bmatrix} R_1 R_2^2 ( -m_1(m_2+m_3) + (m_2+m_3)^2 - (m_2-m_3)^2 ) \\ R_1^2 R_2 ( m_1 (m_2 - m_3) - (m_2^2 - m_3^2) + m_1 (m_2-m_3) + (m_2^2-m_3^2) ) \end{bmatrix} g = \\
\end{aligned}$$

e quindi

$$\begin{aligned}
  \begin{bmatrix} \ddot{\theta}_1 \\ \ddot{\theta}_2 \end{bmatrix} 
  & = \frac{1}{\text{det}(\mathbf{M})} \begin{bmatrix}( -m_1(m_2+m_3) + 4 m_2 m_3 ) R_1 R_2^2  \\ 2 m_1 (m_2-m_3) R_1^2 R_2 \end{bmatrix} g \ .
\end{aligned}$$

Poiché il determinante della matrice $\mathbf{M}$ è positivo - matrice di massa, in equazioni pure del moto senza vincoli algebrici..., vedi [qui](https://basics2022.github.io/bbooks-physics-mechanics/ch/lagrange-properties.html#lagrange-equations-of-the-ii-kind) - il segno delle accelerazioni è determinato unicamente dal segno degli elementi del vettore. Quindi:
* l'accelerazione della carrucola $2$ è positiva (in senso anti-orario, per le convenzioni scelte) se $m_2 > m_3$
* l'accelerazione della carrucola $1$ è positiva (sempre in senso anti-orario, per le convenzioni scelte) se $4 m_2 m_3 > m_1 (m_2 + m_3)$

```

```{dropdown} Moto del sistema

L'integrazione delle equazioni di moto è banale, poiché le accelerazioni sono costanti. Indicando le accelerazioni costanti con $\alpha_1$ e $\alpha_2$, la legge del moto degli angoli delle carrucole è

$$\theta_k(t) = \frac{1}{2} \alpha_k t^2 + \Omega_{k,0} t + \theta_{k,0} \ ,$$

con $\Omega_{k,0}$ e $\theta_{k,0}$ rispettivamente la velocità e la posizione all'istante iniziale, da determinare con due condizioni (qui non fornite): se si ipotizza che il sistema si trovi inizialmente in quite e l'angolo iniziale sia il riferimento nullo, allora 

$$\theta_k(t) = \frac{1}{2} \alpha_k t^2  \ .$$
```

````

<!--
````{only} latex

% Esercizio *****************************************************************
$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 1.}
Una palla di massa $m$ si trova inizialmente in quiete rispetto a un'osservatore inerziale, a una quota $h$ sopra la superficie terrestre.
La palla viene lasciata cadere dalla condizione di quiete. Viene chiesto di determinare:
1. la velocità di impatto con il terreno
2. il tempo impiegato per raggiungere il terreno.

Viene chiesto di svolgere i conti trascurando la resistenza dell'aria. Si chiede poi di:
3. confrontare i risultati ottenuti con i risultati per un corpo di massa $M > m$ 
4. confrontare i risultati ottenuti con i risultati che si otterrebbero nei pressi della superficie lunare.

Raggio Terra: $R_E = 6380 \, km$ ; massa Terra: $M_E = 5.98 \cdot 10^{24} \, kg$;
Raggio Luna:  $R_M = 1740 \, km$ ; massa Luna:  $M_M = 7.34 \cdot 10^{22} \, kg$;
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/dynamics/free-fall.png}
\end{minipage}
$$

**Soluzione.**

**Accelerazione nei pressi della superficie di un pianeta.** L'accelerazione di gravità nei pressi della superficie di un pianeta è data dalla formula **todo** *ref*


````
-->
