<!--
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
-->

(physics-hs:mechanics:actions:def)=
# Forza, momento di una forza, azioni distribuite

(physics-hs:mechanics:actions:def:force)=
## Forza concentrata

Una forza (concentrata) è una quantità **vettoriale** di dimensioni fisiche,

$$[\text{forza}] = \frac{\text{[massa]}\text{[lunghezza]}}{\text{[tempo]}^2}$$

che può essere misurata con un sensore di forza a 3 assi (o un dinamometro).
Oltre alle informazioni tipiche di una quantità vettoriale - intensità, direzione e verso - contenute nel vettore forza $\vec{F}$, è spesso necessario conoscere il **punto** - o meglio la **retta di applicazione** -  della forza.

(physics-hs:mechanics:actions:def:moment)=
## Momento di una forza concentrata
Il momento di una forza $\vec{F}$ applicata nel punto $P$, o con retta di applicazione passante per $P$, rispetto al punto $H$ viene definito come il prodotto vettoriale,

$$\vec{M}_H = (P - H) \times \vec{F}$$

(physics-hs:mechanics:actions:def:equivalent)=
## Sistema di forze, risultante delle azioni e carichi equivalenti
Dato un sistema di $N$ forze $\left\{ \vec{F}_n \right\}_{n=1:N}$, applicate nei punti $P_n$, si definiscono:
- **risultante** del sistema di forze: la somma delle forze,

  $$\vec{R} = \sum_{n=1}^{N} \vec{F}_n \ ,$$

- risultante dei momenti rispetto a un punto $H$: la somma dei momenti

  $$\vec{M}_H = \sum_{n=1}^{N} (P_n - H) \times \vec{F}_n \ ,$$

- un **carico equivalente**: un sistema di forze che ha la stessa risultante di forze e momenti; per un sistema di forze, è possibile definire un carico equivalente formato da una sola forza, la risultante delle forze $\vec{R}$ applicata nel punto $Q$ ricavato dall'equivalenza ai momenti

  $$\begin{aligned}
    \vec{R} & = \sum_{n=1}^{N} \vec{F}_n \\
    (Q - H) \times \vec{R} & = \sum_{n=1}^{N} (P_n - H) \times \vec{F}_n \\
  \end{aligned}$$

(physics-hs:mechanics:actions:def:torque)=
## Coppia di forze
Una coppia di forze è un carico equivalente a due forze di uguale intensità e verso opposto, $\vec{F}_2 = - \vec{F}_1$, applicate in due punti $P_1$, $P_2$ non allineati lungo la retta di applicazione delle forze per avere effetti non nulli.

<!--
**todo** *immagine*
-->

La risultante delle forze è nulla,

$$\vec{R} = \vec{F}_1 + \vec{F}_2 = \vec{F}_1 - \vec{F}_1 = \vec{0} \ ,$$

mentre la risultante dei momenti non dipende dal polo dei momenti,

$$\begin{aligned}
  \vec{M}_H & = (P_1 - H) \times \vec{F}_1 + (P_2 - H) \times \vec{F}_2 = \\
  & = (P_1 - H) \times \vec{F}_1 - (P_2 - H) \times \vec{F}_1 = \\
  & = (P_1 - P_2) \times \vec{F}_1 =: \vec{C} \ .
\end{aligned}$$

(physics-hs:mechanics:actions:def:field)=
## Campo di forze
Un campo di forze è una funzione a valori vettoriali dello spazio, che ha come variabile indipendente il punto $P$ nello spazio e valore - o variabile dipendente - il vettore forza $\vec{F}(P)$ percepito da un sistema se posizionato in quel punto,

$$\vec{F}(P) \ .$$

A volte il campo di forze viene definito per unità di una grandezza fisica dei sistemi fisici sui quali la forza può agire. Ad esempio
- il campo di [forza gravitazionale](physics-hs:mechanics:actions:gravitation:newton), può essere definito tramite il [campo gravitazionale](physics-hs:mechanics:actions:gravitation:newton), $\vec{g}(P)$ che ha le dimensioni fisica di forza su massa, o accelerazione; noto il campo gravitazionale in $P$ e la massa $m$ di un sistema che si trova in $P$, la forza di gravità agente sul sistema è

   $$\vec{F}(P) = m \vec{g}(P)$$

- campo di [forza elettrica](physics-hs:electromagnetism:electrostatics:coulomb) può essere definito tramite il [campo elettrico](physics-hs:electromagnetism:electrostatics:e-field), $\vec{e}(P)$ che ha le dimensioni fisica di forza su carica elettrica; noto il campo elettrico in $P$ e la carica elettrica $q$ di un sistema che si trova in $P$, la forza di elettrica agente sul sistema è

   $$\vec{F}(P) = q \vec{e}(P)$$

Altre volte il campo di forze può rappresentare l'effetto di un elemento meccanico su altri sistemi ai quali è connesso. Ad esempio, gli effetti di una [molla elastica di massa trascurabile](physics-hs:mechanics:actions:gravitation:spring) con un'estremità connessa a terra in $P_0$ su un corpo posto in $P$ possono essere rappresentati da un campo di forze elastico


(physics-hs:mechanics:actions:def:density)=
## Azioni distribuite
**todo**
