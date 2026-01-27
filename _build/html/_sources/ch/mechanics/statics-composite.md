(physics-hs:statics:composite)=
# Statica di sistemi composti

Un sistema composto - o complesso - è un sistema formato da diversi sotto-sistemi - o elementi - che interagiscono in generale interagiscono tra di loro.

Le condizioni necessarie all'equilibrio di un sistema composto o di un sistema continuo deformabile[^deformable-sys] - o di un sistema composto di sottosistemi di tipo diverso: puntiformi, estesi rigidi, estesi deformabili - sono:

[^deformable-sys]: Un sistema continuo deformabile può essere pensato come un sistema formato da un numero infinito di sottosistemi di dimensione infinitesima, che si scambiano tra di loro azioni meccaniche. Nel modello di un sistema continuo *non polare* di Cauchy, porzioni adiacenti del sistema si scambiano solo forze e non momenti. La condizione di equilibrio per alcuni sistemi deformabili viene discussa nella [sezione sulla meccanica del continuo](physics-hs:continuum:intro). Per quanto riguarda la [statica dei fluidi](fluids:statics), la condizione di equilibrio globale del sistema - che impone l'equilibrio di tutte le sue parti - dà origine alla [legge di Stevino](fluids:statics:stevino), come una forma differenziale - locale, di tutte le sue parti - della condizione di equilibrio.

- l'equilibrio di tutti i suoi sotto-sistemi alle forze esterni al sotto-sistema
- l'equilibrio di tutti i suoi sotto-sistemi ai momenti esterni al sotto-sistema

cioé per il sottosistema $s$, la somma di tutte le forze esterne al sottosistema e la somma di tutti i momenti esterni al sottositema rispetto a un polo devono essere uguali a zero,

$$\begin{cases}
  \sum_k \vec{F}^{ext,s}_k = \vec{0} \\
  \sum_k \vec{M}^{ext,s}_{k,H} = \vec{0} \ .  
\end{cases}$$

```{prf:example} Equilibrio di un sistema composto

Esempio: due corpi di massa $m$ collegati da una molla lineare ideale, di massa trascurabile, e di costante elastica $k$ e posti su un piano orizzontale senza attrito, senza forze esterne oltre al loro peso e le reazioni normali del piano, e con allungamento iniziale della molla non nullo e uguale a $\Delta x_0$.

Sul sistema composto dai due corpi e dalla molla agiscono forze esterne con risultante nulla, ma non su tutti i suoi sotto-sistemi:
- sulla molla senza massa agiscono due forze ai suoi estremi uguali e contrarie $\vec{F}_1 = - k \Delta \vec{x}$, $\vec{F}_2 = k \Delta \vec{x}$; quindi la risultante delle forze agenti sulla molla è nulla;
- sul corpo $1$ agiscono forza peso e reazione del piano (che si equilibrano) e la reazione della molla $-\vec{F}_1 = k \Delta \vec{x}$; quindi la risultante delle forze esterne al corpo $1$ agenti sul corpo $1$ è in generale diversa da zero e uguale a  $\vec{R}^{1,ext} = -\vec{F}_1 = k \Delta \vec{x}$
- sul corpo $2$ agiscono forza peso e reazione del piano (che si equilibrano) e la reazione della molla $-\vec{F}_2 =-k \Delta \vec{x}$; quindi la risultante delle forze esterne al corpo $2$ agenti sul corpo $2$ è in generale diversa da zero e uguale a  $\vec{R}^{2,ext} = -\vec{F}_2 =-k \Delta \vec{x}$

Se l'allungamento iniziale non è nullo, i due corpi non rimangono fermi - in condizioni statiche, di equilibrio - ma i due corpi del sistema oscillano, anche se la risultante delle forze esterne al sistema è nulla.

```
