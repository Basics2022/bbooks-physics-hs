(physics-hs:mechanics:dynamics:problems:extra)=
# Altri problemi

````{only} html

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 1. Sistema di carrucole
:columns: 8

Determinare le equazioni del moto, e determinare la direzione di rotazione delle due carrucole. Dopo aver trovato l'espressione letterale, determinare la direzione con $m_1 = 17 \, \text{kg}$, $m_2 = 100 \, \text{kg}$ $m_3 = 4 \, \text{kg}$.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/dynamics/pulley-1.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Equazioni del moto - con bilanci meccanici ("meccanica di Newton") - Approccio 1
:open:

Le equazioni pure del moto - cioé senza reazioni vincolari, o azioni interne - possono essere ricavate a partire dal:
* bilancio del momento della quantità di moto del sottosistema carrucola 1 + massa $m_1$ rispetto al centro della carrucola. Su questo sottosistema agiscono come forze esterne la forza peso, la reazione vincolare a terra e la tensione $T$ nel filo che sostiene la carrucola 2, e che viene "tagliato" per ottenere il sottosistema
* bilancio del momento della quantità di moto del sottosistema carrucola 2 + massa $m_2$ + massa $m_3$ rispetto al centro della carrucola. Su questo secondo sistema agiscono come forze esterne la forza peso, e la tensione $T$ nel filo che sostiene la carrucola 2
* bilancio della quantità di moto del sottosistema carrucola 2 + massa $m_2$ + massa $m_3$ rispetto al centro della carrucola

In queste 3 equazioni compaiono i due gradi di libertà $\theta_1$, $\theta_2$ e la azione interna $T$ del filo. Queste tre equazioni sono:

$$\begin{aligned}
  0 & = - I_1 \ddot{\theta}_1 + T R_1 - m_1 R_1^2 \ddot{\theta}_1 - m_1 R_1 g \\
  0 & = - I_2 \ddot{\theta}_2 + m_2 R_2 g - m_3 R_2 g - m_2 R_2 ( R_2 \ddot{\theta}_2 + R_1 \ddot{\theta}_1 ) - m_3 R_2 ( + R_2 \ddot{\theta}_2 - R_1 \ddot{\theta}_1 ) \\
  0 & = T - m_2 g - m_3 g + m_2 ( R_2 \ddot{\theta}_2 + R_1 \ddot{\theta}_1 ) + m_3 ( - R_2 \ddot{\theta}_2 + R_1 \ddot{\theta}_1 ) + M_2 R_1 \ddot{\theta}_1 - M_2 g \\
\end{aligned}$$

La seconda equazione è un'equazione pura del moto, non contenendo azioni interne o reazioni. Combinando la prima e la terza equazione, si può eliminare la dipendenza da $T$ (che poi può essere ricavata, una volta calcolata la dinamica del moto), per ottenere

$$\begin{aligned}
  0
  & = - I_1 \ddot{\theta}_1 + T R_1 - m_1 R_1^2 \ddot{\theta}_1 - m_1 R_1 g = \\
  & = - I_1 \ddot{\theta}_1 + \left( + m_2 g + m_3 g - m_2 ( R_2 \ddot{\theta}_2 + R_1 \ddot{\theta}_1 ) - m_3 ( - R_2 \ddot{\theta}_2 + R_1 \ddot{\theta}_1 ) - M_2 R_1 \ddot{\theta}_1 + M_2 g \right) R_1 - m_1 R_1^2 \ddot{\theta}_1 - m_1 R_1 g = \\
  & = - \ddot{\theta}_1 \left( I_1 + ( m_1 + m_2 + m_3 ) R_1^2 \right) - \ddot{\theta}_2 \left( ( m_2 - m_3 ) R_1 R_2 \right) + ( m_2 + m_3 - m_1 + M_2 ) R_1 g
\end{aligned}$$

Usando il formalismo matriciale, questa equazione e l'equazione di bilancio del momento della quantità di moto del secondo sottosistema sono una coppia di equazioni pure del moto

$$\begin{bmatrix} I_1 + (M_2+m_1+m_2+m_3) R_1^2 & (m_2 - m_3) R_1 R_2 \\ (m_2 - m_3) R_1 R_2 & I_2 + (m_2+m_3) R_2^2  \end{bmatrix}\begin{bmatrix} \ddot{\theta}_1 \\ \ddot{\theta}_2 \end{bmatrix} = \begin{bmatrix} ( M_2 - m_1 + m_2 + m_3 ) R_1 \\ ( m_2 - m_3 ) R_2  \end{bmatrix} g \ .$$

```

```{dropdown} Equazioni del moto - con bilanci meccanici ("meccanica di Newton") - Approccio 2

...scrivendo le equazioni di bilancio del momento della quantità di moto per:
* il sottosistema 2 (come prima)
* tutto il sistema (sottosistema 1 + sottosistema 2) rispetto al centro della carrucola 1

si ottiene direttamente una coppia di equazioni pure del moto. La seconda equazione consiste al procedimento fatto in precedenza di eliminazione della tensione $T$ nel filo mettendo insieme l'equazione 1 e 3.

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

Nel caso particolare in cui $m_1 = 17 \, \text{kg}$, $m_2 = 100 \, \text{kg}$ $m_3 = 4 \, \text{kg}$, l'accelerazione delle due carrucole è

$$\begin{aligned}
  \alpha_1 & = \frac{R_1 R_2^2 g}{\text{det}(\mathbf{M})} \left( - 17 \times ( 100 + 4 ) + 4 \times 100 \times 4 \right) \text{kg}^2 = ( - 168 \, \text{kg}^2 ) \frac{R_1 R_2^2 g}{\text{det}(\mathbf{M})} \\
  \alpha_2 & = \frac{2 R_1^2 R_2 g}{\text{det}(\mathbf{M})} \left( 17 \times ( 100 - 4 ) \right) \text{kg}^2 = 2 \times ( 1632 \, \text{kg}^2 ) \frac{R_1^2 R_2 g}{\text{det}(\mathbf{M})} \\
\end{aligned}$$

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
