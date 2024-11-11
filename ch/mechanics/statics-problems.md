(physics-hs:mechanics:statics:problems)=
# Problemi

<!-- Esercizio ************************************************************* -->
````{only} latex

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 1.}
  Data la massa $m$ della massa puntiforme appeso tramite due fili inestensibili ideali di lunghezza $L_1$ e $L_2$ note, si calcolino le reazioni a terra.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-000-ese-000.png}
\end{minipage}
$$

**Soluzione.**
I fili inestensibili senza massa e senza rigidezza flessionale possono solo trasmettere un'azione assiale. Ci si aiuta qui con un sistema di coordinate cartesiane con asse $x$ orizzontale con coordinata crescente verso destra e asse $y$ verticale con coordinata crescente verso l'alto. Date le direzioni dei fili identificate dai vettori unitari $\hat{t}_1$, $\hat{t}_2$, l'equilibrio della massa $m$ è garantito dall'equilibrio delle forze,

$$\hat{0} = -m g \hat{y} + F_1 \hat{t}_1 + F_2 \hat{t}_2 \ .$$

Definiti gli angoli $\theta_1$, $\theta_2$, calcolabili dalla geometria del problema - qui considerati noti e calcolati in seguito - e tali che $\hat{t}_1 = \hat{x} \cos \theta_1 + \hat{y}  \sin \theta_1$, $\hat{t}_2 = \hat{x} \cos \theta_2 + \hat{y} \sin \theta_2$, le componenti cartesiane della condizione di equilibrio forniscono un sistema di due equazioni nelle due incognite $F_1$, $F_2$,

$$\begin{cases} 
  F_1 \cos \theta_1 + F_2 \cos \theta_2 = 0 \\
  F_1 \sin \theta_1 + F_2 \sin \theta_2 = m g \\
\end{cases}$$

che ha soluzione

$$
  \begin{bmatrix} F_1 \\ F_2 \end{bmatrix} 
    = \frac{1}{\cos \theta_1 \sin \theta_2 - \sin \theta_1 \cos \theta_2}
    \begin{bmatrix} \sin \theta_2 & - \cos \theta_2 \\ -\sin \theta_1 & \cos \theta_1 \end{bmatrix} \begin{bmatrix} 0 \\ m g \end{bmatrix} 
    = \frac{1}{\sin(\theta_2 - \theta_1)} \begin{bmatrix} - \cos \theta_2 \\ \cos \theta_1 \end{bmatrix} m g  \ .
$$

**todo** *Controllare conti. Aggiungere immagine.*

**Grandezze geometriche del problema.** **todo**

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 2.}
  Data la massa $m$ della massa puntiforme appeso tramite due fili inestensibili ideali di lunghezza $L_1$ nota e $L_2$ variabile, si calcolino le reazioni a terra in funzione della lunghezza del filo $2$.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-000-ese-001.png}
\end{minipage}
$$

**Soluzione.**


$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 3.}
  Data la massa $m$ della massa puntiforme appeso tramite un filo inestensibile ideale di lunghezza $L$ e una molla di costante elastica $k$ e lunghezza a riposo $x_0$ collegata a terra in un punto distante $H$ dal punto a terra dove è collegato il filo, si calcoli:
  \begin{enumerate}
    \item la posizione del punto 
    \item la lunghezza della molla
    \item le reazioni vincolari a terra 
  \end{enumerate}
  nella configurazione di equilibrio.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-000-ese-002.png}
\end{minipage}
$$

**Soluzione.**


$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 4.}
  Data $m$, $\mu^s$, trovare l'angolo massimo $\theta_{\max}$ per il quale esiste una condizione di equilibrio per il cubetto rosso.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-001-ese-000.png}
\end{minipage}
$$

**Soluzione.**
Per l'equilibrio del corpo è necessario l'equilibrio delle forze. Le forze agenti sul cubetto rosso sono la sua forza peso e la reazione di contatto $\vec{R}$ con la parete inclinata, che può essere scomposta nella direzione perpendicolare - reazione normale - e parallela alla parete - attrito.

La condizione di equilibrio,

$$\vec{0} = -m g \hat{y} + \vec{R}\ ,$$

può essere proiettata lungo la direzione normale alla parete $\hat{n}$ e la direzione tangente $\hat{t}$ (verto l'alto, così che $\hat{y} = - \cos \theta \, \hat{n} - \sin \theta \, \hat{t}$

$$\begin{cases}
0 = N - m g \cos \theta \\
0 = F - m g \sin \theta \ ,
\end{cases}$$

così che $F = N \, \tan \theta$. Bisogna infine verificare che questa forza di attrito statico possa essere trasmessa, con la condizione

$$|F| \le F^{s,max} = \mu^s \, N \ ,$$

insieme alla condizione di contatto $N \ge 0$, e quindi

$$|\tan \theta| \le \mu^s \ .$$

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 5.}
  Data $m$, $M$, $\mu^s$ tra i due solidi, si chiede di calcolare:
  \begin{enumerate}
    \item la risultante delle azioni scambiate tra i due corpi
    \item la risultante delle reazioni vincolari a terra agenti sul solido blu,
  \end{enumerate}
  nella condizione di equilibrio del sistema, nell'ipotesi che l'attrito tra solido blu e terra sia trascurabile. Verificare le condizioni limite tra $\theta$ e $\mu^s$ affinché l'equilibrio sia possibile
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-001-ese-001.png}
\end{minipage}
$$

**Soluzione.**
Il piano orizzontale liscio non può trasmettere nessuna forza orizzontale al prisma triangolare. L'equilibrio delle forze del prisma triangolare, necessaria alla condizione di equilibrio, implica quindi che la risultante delle forze di contatto con il blocchetto rosso ha direzione verticale anch'essa.

Dalla condizione di equilibrio per il blocchetto rosso,

$$\vec{0} = - m g \hat{y} + \vec{R}_{quad, tri} \qquad \rightarrow \qquad \vec{R}_{quad, tri} = m g \hat{y} \ .$$

La risultante delle forze scambiate tra i corpi è quindi uguale e contraria al peso del cubetto (**1**). L'equilibrio del corpo triangolare

$$
  \vec{0} = - M g \hat{y} + \vec{R}_{tri, quad} + \vec{R}_{tri, plane} \ ,
$$

implica che la reazione $\vec{R}_{tri,plane}$ agente sul solido triangolare dovuta alla superficie orizzontale è uguale e contraria alla somma del peso dei due solidi (**2**),

$$
  \vec{R}_{tri,plane}   = M g \hat{y} - \vec{R}_{tri, quad}     
                        = M g \hat{y} + \vec{R}_{quad, tri}     
                        = M g \hat{y} + m g \hat{y} \ .
$$

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 6.}
  Data la massa $m$ del blocco rosso, la costante elastica $k$ della molla lineare ideale, con lunghezza a riposo $\ell_0$, viene chiesto di:
  \begin{enumerate}
    \item determinare la lunghezza della molla nella condizione di equilibrio, nell'ipotesi che l'attrito tra blocco rosso e piano inclinato sia trascurabile
    \item determinare le possibili condizioni di equilibrio, nell'ipotesi che l'attrito statico tra blocco rosso e piano inclinato sia $\mu^s$
  \end{enumerate}
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-001-ese-002.png}
\end{minipage}
$$

**Soluzione.**
I fili inestensibili trasmettono solo azione assiale nela direzione del filo, costante in ogni sua sezione. Le condizioni di equilibrio alla rotazione di una carrucola assicurano che sia costante l'azione assiale ai due capi di un filo parzialmente avvolto attorno alla carrucola, nel caso di attriti nulli (carrucola ideale).

Il problema può essere risolto scrivendo le condiizoni di equilibrio della molla,

  $$F = k (\ell - \ell_0)$$

e del blocchetto rosso, proiettate in direzione perpendicolare e tangente alla superficie inclinata

  $$
  \vec{0} = \vec{F} + m \vec{g} + \vec{R}
  \qquad , \qquad
  \begin{cases}
    t: \ 0 = - F + m g \sin \theta + F_t \\
    n: \ 0 = \ \ - m g \cos \theta + F_n \\
  \end{cases}
  $$

**In assenza di attrito, $F_t = 0$.** In assenza di attrito, la reazione tangenziale è nulla $F_t = 0$ e quindi

$$\begin{aligned}
  F_n          & = m g \cos \theta \\
  F            & = m g \sin \theta \\
  \Delta \ell  & = \frac{m g}{k} \sin \theta \\
\end{aligned}$$

**Con attrito statico.** In presenza di attrito statico, la soluzione non è unicamente determinata ma bisogna discutere le condizioni che garantiscono l'equilibrio, verificando la condizione $|F_t| \le \mu^s F_n$. Le espressione delle componenti normali e tangenziali della reazione vincolare agente sul blocchetto,

$$\begin{aligned}
  F_n & = m g \cos \theta \\
  F_t & = k \Delta \ell - m g \sin \theta
\end{aligned}$$

permettono di scrivere la condizione che garantisce l'equilibrio come

$$
 | k \Delta \ell - m g \sin \theta | \le \mu_s m g \cos \theta 
$$

e quindi

$$- \mu_s m g \cos \theta + mg \sin \theta \le k \Delta \ell \le  \mu_s m g \cos \theta + mg \sin \theta \ .$$

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 7.}
  Data la massa $m$ del blocco rosso, il raggio $R_1$, $R_2$ delle due carrucole, si chiede di determinare la forza $\vec{F}$ da applicare nella condizione di equilibrio, nell'ipotesi di fili inestensibili e carrucole ideali e senza massa.
  % 
  Si chiede poi di ripetere il calcolo nell'ipotesi in cui la massa delle carrucole non sia trascurabile, ma siano $M_1$ per la carrucola vincolata a terra, e $M_2$ per la carrucola non vincolata a terra.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-000.png}
\end{minipage}
$$

**Soluzione.**

$$\begin{aligned}
0 & = - m g + T_1 \\
0 & = F + T_1 - M g \\
0 & - M g R_2 + F \, (2 R_2)
\end{aligned}$$

$$\begin{aligned} 
  F & = \frac{1}{2} M g \\
  T_1
\end{aligned}

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 8.}
  Nel meccanismo di un orologio i 3 componenti che devono guidare il moto delle lancette dei secondi, dei minuti e delle ore, connessi "in cascata" tramite ingranaggi (con rapporto dei raggi $1:60$ **todo** scriverlo esplicitamente?). Conoscendo la costante elastica $k$ e la compressione $\Delta \theta$ della molla che guida il componente che guida la lancetta delle ore, si chiede di:
  \begin{enumerate}
    \item determinare la forza necessaria da applicare alla lancetta dei secondi nel punto indicato nell'imagine, necessaria a garantire la posizione di equilibrio
    \item le reazioni vincolari in corrispondenza delle cerniere che collegano a terra i 3 componenti, nell'ipotesi che non si scambino forze in direzione radiale
  \end{enumerate}
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-001.png}
\end{minipage}
$$

**Soluzione.**

$$
F      R_1 & = F_{12} R_2 \\
F_{12} R_2 & = F_{23} R_3 \\
F_{23} R_3 & = k \Delta \theta \ .
$$

$$
  F = \frac{R_2}{R_1} \frac{R_3}{R_2} \frac{1}{R_3} k \Delta \theta \ .
$$

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 9.}
  Data la lunghezza $L$ e la massa $m$ dell'asta rigida con distribuzione di massa uniforme e il coefficiente di attrito stativo $\mu^s$ tra asta e superficie orizzontale, si chiede di:
  \begin{enumerate}
    \item determinare la condizione limite dell'equilibrio
    \item determinare le reazioni a terra
  \end{enumerate}
  nell'ipotesi che l'attrito sulla superficie verticale sia trascurabile.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-002.png}
\end{minipage}
$$

**Soluzione.**

$$\begin{aligned}
x & : 0 =  N_{1} + F^{s}_2 \\
y & : 0 = - m g + N_{2} \\
\text{rot, 2} & : 0 = m g \frac{\ell}{2} \cos \theta - N_{1} \ell \sin \theta
\end{aligned}$$

$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 10.}
  Data la lunghezza $L$ e la massa $m$ dell'asta rigida incernierata a terra, e la costante elastica $k$ della molla rotazionale, si chiede di:
  \begin{enumerate}
    \item calcolare la condizione di equilibrio
    \item le reazioni vincolari sull'asta
  \end{enumerate}
  discutendo i due casi determinati dalla condizione di appoggio dell'estremo superiore dell'asta sulla parete verticale.
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-003.png}
\end{minipage}
$$

**Soluzione.**
Nel caso generale,

$$\begin{aligned}
  x & : 0 =  N_{1} + F_{2,x} \\
  y & : 0 =  - m g + F_{2,y} \\
  \text{rot, 2} & : 0 = m g \frac{\ell}{2} \cos \theta - N_{1} \ell \sin \theta + k \Delta \theta
\end{aligned}$$

Il contatto avviene quando la rigidezza della molla garantisce una condizione di equilibrio con $\Delta \theta < \overline{\Delta \theta}$.
Se non c'è contatto, $N_1 = 0$; se c'è contatto, in generale $N_1 > 0$.


$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 11.}
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-004.png}
\end{minipage}
$$

**Soluzione.**


$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 12.}
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-005.png}
\end{minipage}
$$

**Soluzione.**


$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 13.}
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-006.png}
\end{minipage}
$$

**Soluzione.**


$$
\begin{minipage}[t]{.55\textwidth}
  \vspace{0pt}
  \textbf{Problema 14.}
\end{minipage}
\hspace{.05\textwidth}
\begin{minipage}[t]{.40\textwidth}
  \vspace{0pt}
  \includegraphics[width=.95\textwidth]{../../media/pb-statics-002-ese-007.png}
\end{minipage}
$$

**Soluzione.**


````


````{only} html
<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 1.
:columns: 8

Data la massa $m$ della massa puntiforme appeso tramite due fili inestensibili ideali di lunghezza $L_1$ e $L_2$ note, si calcolino le reazioni a terra.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-000-ese-000.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 2.
:columns: 8

Data la massa $m$ della massa puntiforme appeso tramite due fili inestensibili ideali di lunghezza $L_1$ nota e $L_2$ variabile, si calcolino le reazioni a terra in funzione della lunghezza del filo $2$.
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-000-ese-001.png)
:::

::::

```{dropdown} Soluzione.
```


<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 3.
:columns: 8

Data la massa $m$ della massa puntiforme appeso tramite un filo inestensibile ideale di lunghezza $L$ e una molla di costante elastica $k$ e lunghezza a riposo $x_0$ collegata a terra in un punto distante $H$ dal punto a terra dove è collegato il filo, si calcoli:
1. la posizione del punto 
2. la lunghezza della molla
3. le reazioni vincolari a terra 
nella configurazione di equilibrio.
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-000-ese-002.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 4.
:columns: 8

Data $m$, $\mu^s$, trovare l'angolo massimo $\theta_{\max}$ per il quale esiste una condizione di equilibrio.
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-001-ese-000.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 5.
:columns: 8

Data $m$, $M$, $\mu^s$ tra i due solidi, si chiede di calcolare:
- la risultante delle azioni scambiate tra i due corpi
- la risultante delle reazioni vincolari a terra agenti sul solido blu,

nella condizione di equilibrio del sistema, nell'ipotesi che l'attrito tra solido blu e terra sia trascurabile. Verificare le condizioni limite tra $\theta$ e $\mu^s$ affinché l'equilibrio sia possibile
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-001-ese-001.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 6.
:columns: 8

Data la massa $m$ del blocco rosso, la costante elastica $k$ della molla lineare ideale, con lunghezza a riposo $\ell_0$, viene chiesto di:
- determinare la lunghezza della molla nella condizione di equilibrio, nell'ipotesi che l'attrito tra blocco rosso e piano inclinato sia trascurabile
- determinare le possibili condizioni di equilibrio, nell'ipotesi che l'attrito statico tra blocco rosso e piano inclinato sia $\mu^s$
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-001-ese-002.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 7.
:columns: 8

Data la massa $m$ del blocco rosso, il raggio $R_1$, $R_2$ delle due carrucole, si chiede di determinare la forza $\vec{F}$ da applicare nella condizione di equilibrio, nell'ipotesi di fili inestensibili e carrucole ideali e senza massa.

Si chiede poi di ripetere il calcolo nell'ipotesi in cui la massa delle carrucole non sia trascurabile, ma siano $M_1$ per la carrucola vincolata a terra, e $M_2$ per la carrucola non vincolata a terra.
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-000.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 8.
:columns: 8

Nel meccanismo di un orologio i 3 componenti che devono guidare il moto delle lancette dei secondi, dei minuti e delle ore, connessi "in cascata" tramite ingranaggi (con rapporto dei raggi $1:60$ **todo** scriverlo esplicitamente?). Conoscendo la costante elastica $k$ e la compressione $\Delta \theta$ della molla che guida il componente che guida la lancetta delle ore, si chiede di:
- determinare la forza necessaria da applicare alla lancetta dei secondi nel punto indicato nell'imagine, necessaria a garantire la posizione di equilibrio
- le reazioni vincolari in corrispondenza delle cerniere che collegano a terra i 3 componenti, nell'ipotesi che non si scambino forze in direzione radiale.
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-001.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 9.
:columns: 8

Data la lunghezza $L$ e la massa $m$ dell'asta rigida con distribuzione di massa uniforme e il coefficiente di attrito stativo $\mu^s$ tra asta e superficie orizzontale, si chiede di:
- determinare la condizione limite dell'equilibrio
- determinare le reazioni a terra
nell'ipotesi che l'attrito sulla superficie verticale sia trascurabile
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-002.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 10.
:columns: 8

Data la lunghezza $L$ e la massa $m$ dell'asta rigida incernierata a terra, e la costante elastica $k$ della molla rotazionale, si chiede di:
- calcolare la condizione di equilibrio
- le reazioni vincolari sull'asta
discutendo i due casi determinati dalla condizione di appoggio dell'estremo superiore dell'asta sulla parete verticale.
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-003.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 11.
:columns: 8

Testo del problema...
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-004.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 12.
:columns: 8

Testo del problema...
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-005.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 13.
:columns: 8

Testo del problema...
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-006.png)
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 14.
:columns: 8

Testo del problema...
:::

:::{grid-item-card} 
:columns: 4

![](../../media/pb-statics-002-ese-007.png)
:::

::::

```{dropdown} Soluzione.
```

````
