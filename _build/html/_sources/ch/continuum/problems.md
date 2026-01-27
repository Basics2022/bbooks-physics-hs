(physics-hs:continuum:problems)=
# Problemi

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

````

````{only} html
::::{grid}
:gutter: 2

:::{grid-item-card} Problema 1.
:columns: 8

Due corpi sferici di pari volume e densità $\rho_1$ e $\rho_2$ sono immersi in pari volume di acqua di pari densità $\rho_{H_2 O}$. La geometria del sistema è simmetrica rispetto al piano verticale passante per il polo sulla quale la trave orizzontale è appoggiata. Il corpo $1$ è connesso a terra da un filo. Il sistema è in un piano verticale e soggetto a un campo gravitazionale uniforme.

Si chiede di calcolare se il sistema può trovarsi in equilibrio.

:::

:::{grid-item-card} 
:columns: 4

![](../../media/continuum/water-lever.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
:open:

Un sistema è in equilibrio alla rotazione rispetto a un polo $H$, se la somma dei momenti esterni agenti sul sistema rispetto al polo è identicamente nulla,

$$\sum_i \vec{M}_{H,i} = \vec{0} \ ,$$

vedi [condizioni necessarie all'equilibrio per sistemi rigidi](physics-hs:mechanics:statics:rigid)[^rigid-equil].

[^rigid-equil]: Il sistema in quiete, nelle condizioni di equilibrio - da verificare -, si può trattare come sistema rigido, poiché non c'è nessun moto relativo tra i suoi componenti, benché esso sia costituito da più sotto-sistemi, alcuni nemmeno nello stato solido. In generale, per verificare l'**equilibrio di un sistema composto** va verificato l'**equilibrio di tutti i suoi sotto-sistemi**. Per motivi di sintesi, ci si limita ad affermare che questo è verificato per il problema in esame, nel caso in cui il sia in equilibrio rispetto alla rotazione attorno al polo $H$, e si lascia un'eventuale dimostrazione al lettore.

In questo caso siamo interessati solo ai momenti rispetto alla direzione $z$ uscente dal piano. Nella soluzione del problema, si considera il sistema formato dalla trave, dai due contenitori, dall'acuqa contenuta in essi, e dalle due sfere. Seguendo questa scelta, le azioni esterne agenti sul sistema sono:
- le reazioni in corrispondenza dei vincoli con l'esterno: la forza $\vec{R}_H$ in corrispondenza della cerniera in $H$ e la tensione del filo $\vec{T}$; la risultante agente sul sistema dovuta alla pressione dell'aria può essere trascurata, e nel caso non sia trascurata la risultante del suo momento rispetto al polo $H$ è nulla per la simmetria del sistema;
- la forza peso degli elementi del sistema, sia dei corpi solidi, sia dell'acqua contenuta nel sistema.

**Osservazione.** La [forza di Archimede](fluids:statics:archimedes) è una forza interna scambiata tra i corpi solidi e l'acqua nella quale sono immersi; per [il terzo principio della dinamica di Newton - azione e reazione](physics-hs:mechanics:dynamics:principles), la loro risultante è nulla: il solido $1$ riceve una spinta dal fluido verso l'alto, mentre il fluido riceve dal solido $1$ una spinta verso il basso di intensità $\rho_{H_2 O} V_1 g$, con $V_1$ il volume del corpo $1$.

![](../../media/continuum/water-lever-forces.png)

Ora, prendendo con segno positivo le forze che promuovono una rotazione antioraria del sistema, la componente $z$ della risultante dei momenti rispetto ad $H$ vale

$$\begin{aligned}
  \sum_i M_{H,z,i} 
  & = P_{H_2 O} h + P_1 h + P^{\text{contenitore 1}} h - T h - P_{H_2 O} h - P_2 h - P^{\text{contenitore 1}} h = \\
  & = \left( P_1 - T - P_2 \right) h \ .
\end{aligned}$$

Ora, per trovare il risultato è necessario calcolare la tensione $T$ nel filo. Nell'ipotesi di equilibrio, la tensione del filo viene calcolata dall'equilibrio verticale della sfera $1$,

$$0 = T - P_1 + F^{\text{Arch}} = T - P_1 + \rho_{H_2 O} g V_1 \quad \rightarrow \quad P_1 - T = \rho_{H_2 O} V_1 g \ .$$

![](../../media/continuum/water-lever-archimedes.png)

Sostituendo l'espressione di $P_1 - T$ nella risultante dei momenti si ottiene quindi

$$\sum_i M_{H,z,i} = \rho_{H_2 O} V_1 g - \rho_2 V_2 g \ .$$

Se i volumi dei due corpi sono uguali $V_1 = V_2 = V$, si ottiene quindi

$$\sum_i M_{H,z,i} = \left( \rho_{H_2 O} - \rho_2 \right) V g \ .$$

Il sistema è in equilibrio solo se il corpo $2$ ha densità pari a quella dell'acqua, $\rho_2 = \rho_{H_2 O}$. Nel caso in cui il corpo $2$ ha densità minore dell'acqua, $\rho_2 < \rho_{H_2 O}$, la risultante dei momenti è positiva e - per la convenzione scelta - promuove una rotazione in verso antiorario.


```


````
