(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule)=
# Gibbs: energia interna, regola delle fasi e funzioni multi-variabili

Seguendo il lavoro di Gibbs, in questa sezione vengono introdotti alcuni concetti come quello di [variabile di stato](physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:state-vars) ed [energia interna](physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:internal-energy), e la [regola delle fasi di Gibbs](physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:gibbs-phase-rule). Successivamente, il [primo principio della termodinamica viene riformulato](physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:first) utilizzando il formalismo introdotto da Gibbs che permette di identificare lo stato di un sistema con un numero limitato di variabili stato indipendenti e di esprimere le altre variabili (dipendenti) di stato come funzioni di più variabili.

(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:state-vars)=
## Variabili di stato
```{prf:definition} Variabile di stato

Una variabile di stato di un sistema è una proprietà fisica del sistema che dipende esclusivamente dallo stato corrente del sistema.

```

```{prf:example} Variabili di stato e non
Sono variabili di stato la temperatura, la pressione, l'energia interna, l'entropia,...
Non sono variabili di stato il lavoro o il calore scambiato dal sistema. **todo**

```

(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:internal-energy)=
## Energia interna
```{prf:definition} Energia interna
L'energia interna di un sistema viene definita come la differenza dell'energia totale e l'energia cinetica macroscopica del sistema,

$$E = E^{tot} - K \ .$$
```

E' possibile ricavare un bilancio per l'energia interna di un sistema chiuso sottraendo il bilancio dell'energia cinetica descritto dal teorema dell'energia cinetica al bilancio dell'energia totale fornito dal primo principio della termodinamica,

$$\begin{aligned}
  d E^{tot} & = \delta L^{ext} + \delta Q^{ext} \\
  d K       & = \delta L^{ext} + \delta L^{int} \ ,
\end{aligned}$$

Il bilancio dell'energia interna per un sistema chiuso diventa quindi

$$d E = \delta Q^{ext} - \delta L^{int} \ .$$

(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:gibbs-phase-rule)=
## Regola delle fasi di Gibbs
```{prf:definition} Fase
Una fase è definita come una porzione di un sistema chimico-fisico caratterizzata da proprietà chimico-fisiche (macroscopiche) uniformi. 
```
**todo**
- discussione delle proprietà
- esempi: miscela di gas miscibili costituisce una fase sola, nella quale non è possibile distinguere macroscopicamente i suoi componenti elementari; liquidi non miscibili rimangono macroscopicamente separati e quindi costituiscono più fasi, delle quali è possibile distinguere macroscopicamente composizioni chimiche differenti;...

```{prf:proposition} Regola delle fasi di Gibbs
Lo stato termodinamico (di equilibrio) di un sistema è identificato da un numero $F$ di variabili di stato **intensive** indipendenti, determinato dalla **regola delle fasi di Gibbs**,

$$F = C - P + 1 + W \ ,$$

cioè il numero di variabili intensive indipendenti (o gradi di libertà), $F$, di un sistema è una funzione del numero di componenti indipendenti $C$ di un sistema, il numero di fasi $P$ e il numero $W$ di modi del sistema di manifestare lavoro interno, come ad esempio:
- sforzi meccanici interni
- contributo della tensione superficiale
- energia dei legami delle molecole dei componenti
- contributo del campo elettromagnetico
```

```{dropdown} Discussione della regola delle fasi di Gibbs
Lo stato di equilibrio di un sistema è definito dal valore delle variabili di stato, che per un sistema gassoso non elettricamente carico sono: temperatura $T$, pressione $p$ e concentrazioni $C_{c,\phi}$ dei singoli componenti $c=1:C$ nelle singole fasi $\phi = 1:P$ all'interno del sistema.

Lo stato del sistema è quindi determinato dal valore delle $1+W$ variabili termodinamiche intensive, qui $W+1=2$ $T$, $p$, e dalle $C \, P$ frazioni $n_{c,\phi}$ (molari o di massa), per un totale di $N \, P + W + 1$ variabili.
In generele, queste variabili sono legate da alcune condizioni:

- $C \, (P-1)$ condizioni di equilibrio delle fasi di ogni singolo componente, descritte dall'uguaglianza dei potenziali chimici

  $$\mu_{c,\phi_1}(T,p) = \mu_{c,\phi_2}(T,p) = \dots = \mu_{c,\phi_P}(T,p)$$

- $P$ condizioni di unitarietà delle frazioni

  $$\sum_{c} n_{c,\phi} = 1$$

Quindi, con $C \, P + W + 1$ variabili e $P + C\, (P-1) = C \, P - C + P$ equazioni, si scopre che il problema può essere determinato da 

$$C \, P + W + 1 - C \, P + C - P  =  C - P + W + 1 = F \ ,$$

variabili indipendenti.

```

**todo** 
- Fare esempi che chiariscano la definizione di fase (es: solidi o liquidi puri rappresentano fasi a sé stanti), e di componente indipendente (es: reazioni chimiche, senza componenti in eccesso, determinano dei vincoli che riducono il numero di sostanze indipendenti, grazie ai rapporti stechiometrici tra le sostanze)
- discutere il ruolo delle frazioni di fase di un singolo componente e il fatto che non sono variabili di stato; esempio passaggio di fase liquido-vapore: l'equilibrio è determinato dal valore di $P$ (o di $T$), la frazione di vapore è una conseguenza di altre variabili estensive del sistema.

```{prf:example} Sistema chiuso contentente un monocomponente (o non-reagente), monofase, elettricamente neutro (o non-soggetto a campo elettromagnetico)
:class: dropdown

In un sistema composto da un gas comprimibile, monocomponente e monofase (gassosa), elettricamente neutro, **todo** *altro?*, l'unica forma di lavoro interno è quello legato alla compressione, $\delta L^{int,rev} = P dV$, e quindi $W = 1$. Per questo sistema servono quindi, 

$$F = C - P + 1 + W = 1 - 1 + 1 + 1 = 2 \ ,$$

variabili di stato per definire lo stato del sistema.

```
```{prf:example} Sistema aperto contentente un monocomponente (o non-reagente), monofase, elettricamente neutro (o non-soggetto a campo elettromagnetico)
:class: dropdown

In un sistema aperto, la variazione di energia del sistema dipende anche dalla variazione della quantità di gas contenuto in esso. Quindi, in generale esistono $W = 2$ modi per far variare l'eneergia del sistema: tramite il lavoro di compressione, o tramite un flusso di materia all'interno del sistema. Servono quindi $F=3$ variabili di stato per definire lo stato del sistema.

```
``` {prf:example} Miscela reattiva di gas in un sistema chiuso
:class: dropdown

In una miscela reattiva di gas formata dai due composti $A$, $B$ in equilibrio secondo la reazione di equilibrio

$$n_a A + n_b B \leftrightarrow n A_a B_b$$

l'energia del sistema dipende dal lavoro meccanico di compressione della miscela dei gas, e dalla quantità dei 3 composti presenti nel gas. La variazione di questi composti non è però indipendente ma determinata dalla reazione di equilibrio. In particolare,

$$\begin{aligned}
  d n_{B} & = d n_{A} \frac{n_b}{n_a} \\
  d n_{A_a B_b} & = - d n_{A} \frac{n}{n_a} \\
\end{aligned}$$

La reazione è quindi determinata da 1 solo parametro. La variazione di energia del sistema è quindi determinata da $W=2$ processi: dal lavoro di compressione fatto sul sistema, e dallo stato della reazione. Per determinare lo stato del sistema servono quindi $F=3$ variabili di stato indipendenti, come ad esempio **todo** $T$, $P$, $n_A$? Non servono i potenziali chimici $\mu_A$, $\mu_B$, $\mu_{A_a B_b}$? Sono unicamente determinati?

```
```{prf:example} Sistema monocomponente durante una transizione di fase
:class: dropdown
**Transizione di fase del primo ordine.** Durante una transione di fase del primo ordine, sono simultaneamente presenti nel sistema $P = 2$ fasi. Secondo la regola delle fasi di Gibbs, lo stato del sistema è determinato da 

$$F = C - P + 1 + W = 1 - 2 + 1 + 1 = 1 \ ,$$

variabile di stato.

**Punto critico.** Il punto critico nel piano delle fasi di un sistema mono-componente definisce la condizione in cui sono simultaneamente presenti nel sistema $P = 3$ fasi. Secondo la regola delle fasi di Gibbs, lo stato del sistema è determinato da $F = 0$ variabili di stato: lo stato del sistema nel punto critico è univocamente definito, senza alcun grado di libertà.

```
```{prf:example} Solido
:class: dropdown

In assenza di altri fenomeni fisici, l'unica forma di lavoro in un solido è quella legata al lavoro di deformazione, $\delta L^{int,rev} = \sigma_{ij} \, d \varepsilon_{ij} dV$. Il tensore di deformazione è del secondo ordine e simmetrico, e ha quindi 6 componenti indipendenti nello spazio 3-dimensionale, e quindi $W=6$
```
```{prf:example} Miscele solide
:class: dropdown

- Fasi nelle miscele solide **todo**
```
```{prf:example} Influenza del campo elettromagnetico
:class: dropdown

- Campo elettrico e magnetizzazione **todo**
```

(physics-hs:thermodynamics:foundation:principles:gibbs-phase-rule:first)=
## Primo principio in termini delle variabili di stato
L'energia interna è una variabile estensiva di un sistema termodinamico. In generale, può essere scritta come una funzione di $...$ variabili estensive che rappresentano i modi del sistema di manifestare la sua energia interna (**todo** *sia dovuta al lavoro svolto su di esso, sia al calore apportato al sistema, sia alla sua composizione chimica e quindi all'energia contenuta nei legami*)


$$E(S, X_k) \ ,$$

avendo indicato con $X_k$ tutte le variabili di stato la cui variazione è associata a un lavoro interno reversibile, ed $S$ la variabile di stato la cui variazione è associata al calore scambiato con l'ambiente esterno e alle azioni interne dissipative.  **todo** *facendo riferimento al capitolo sulle funzioni e sul calcolo multivariabile*

Assumendo che la funzione $E$ sia continua e differenziabile, almeno a tratti, si può scrivere il differenziale - esatto - dell'energia interna in funzione degli incrementi delle variabili indipendenti,

$$\begin{aligned}
dE & = \left. \dfrac{\partial E}{\partial S} \right|_{\mathbf{X}} d S 
     + \left. \dfrac{\partial E}{\partial X_k} \right|_{S} d X_k  = \\
   & = T \, d S + \sum_k F_k \, d X_k \ ,
\end{aligned}$$

avendo definito $F_k$ le forze generalizzate associate agli spostamenti generalizzati $dX_k$ e introdotto la definizione delle variabili $T$ ed $S$, che corrispondono alle grandezze fisiche temperatura ed entropia, come descritto in seguito **todo**.

**todo**
- <span style="color:red">con questo formalismo è immediato formulare il **secondo** e il **terzo principio della termodinamica** come $dS \ge \frac{\delta Q^{ext}}{T}$, e $T \ge 0$</span>

L'espressione del differenziale dell'energia interna può essere confrontata con il bilancio dell'energia interna scritto in termini del calore apportato al sistema e del lavoro interno,

$$\begin{aligned}
  d E & = \delta Q^{ext} - \delta L^{int} = \\
      & = \delta Q^{ext} + \delta^+ D - \delta L^{int,rev} \ .
\end{aligned}$$

avendo riconosciuto il lavoro interno $\delta L^{int}$ come somma di un contributo reversibile e un contributo di dissipazione, mai negativo, $\delta L^{int} = \delta L^{int,rev} - \delta^+ D$.

Poiché $d E$ è un differenziale esatto e $\delta L^{int,rev}$ è un contributo reversibile, segue che la somma dei due contributi in generale non reversibili, $\delta U := \delta Q^{ext} + \delta^+ D$, è un contributo reversibile. Confrontando le due espressioni del differenziale dell'energia interna, si può associare il lavoro interno reversibile alla somma dei lavori formati come prodotto delle forze generalizzate $F_k$ e le variazioni delle variabili di stato $X_k$, e il termine $\delta U$ al prodotto $T \, dS$,

$$\begin{cases}
  -\delta L^{int,rev} & = \displaystyle\sum_k F_k \, d X_k \\
  \delta U            & = T \, dS
\end{cases}$$

```{dropdown} Temperatura, $\ T, \ $ ed entropia, $\ S$
:open:

In assenza di lavoro esterno compiuto sul sitema, e in assenza di dissipazione $\delta^+ D = 0$, segue che 

$$\begin{aligned}
 & d E^{tot} = d E = \delta Q^{ext} \\
 & d S = \frac{\delta Q^{ext}}{T} \\
\end{aligned}$$

Si considera un sistema chiuso e isolato formato da due sistemi in equilibrio al loro interno, che possono scambiare tra di loro calore ma non lavoro.

L'energia totale del sistema è costante, $E = E_1 + E_2$. Se i due sottosistemi non sono a temperatura iniziale uguale, si osserva un flusso di energia nella forma di calore dal sistema più caldo a quello più freddo, che soddisfa la disuguaglianza

$$
 \frac{\delta Q_{12}}{T_1} + \frac{\delta Q_{21}}{T_2} \ge 0 \quad \rightarrow \quad
 d S_1 + d S_2 \ge 0
$$

La quantità $S = S_1 + S_2$ è non decrescente.

Nel caso generale di un sistema semplice usando la definizione $dS = \frac{\delta U}{T} = \frac{\delta Q^{ext} + \delta^+ D}{T}$ e ricordando che la dissipazione è non negativa, $\delta^+ D \ge 0$, segue che

$$d S \ge \frac{\delta Q^{ext}}{T} \ .$$

<!--
$$E_1(T_1) + E_2(T_2) = E = \text{const}$$

$$\frac{d E_1}{d T_1} = -\frac{d E_2}{d T_2} \frac{d T_2}{d T_1}$$
-->

```


Da L.E. Reichl, A Modern Course in Statistical Physics, con qualche incoerenza **todo** *controllare!*

$$\delta W = - P dV + J dL + \sigma d A + V \left( \vec{e} \cdot d \vec{p} + \vec{h} \cdot d \vec{m}\right) + \phi d q $$

- con $J$, $\sigma$ tensioni per unità di lunghezza e di area, $d L $, $d A$ variazione di lunghezza o di area,
- con $\vec{e}$, $\vec{h}$ campi elettrico e magnetico, $\vec{p}$, $\vec{m}$ polarizzazione e magnetizzazione
- $\phi$ potenziale elettrico, $q$ carica elettrica (per sistemi aperti, altrimenti o $dq \equiv 0$ o si starebbe creando carica elettrica netta!)

```{prf:example} Sistema gassoso chiuso monocomponente
:class: dropdown

L'energia del sistema, $E(S,V)$

$$dE = T \, dS - P \, dV$$

```
```{prf:example} Sistema gassoso aperto monocomponente
:class: dropdown

L'energia del sistema, $E(S,V,N)$

$$dE = T \, dS - P \, dV + \mu \, dN$$

```
```{prf:example} Miscela reattiva di gas in un sistema chiuso
:class: dropdown

L'energia del sistema

$$\begin{aligned}
  dE & = T \, dS - P \, dV + \mu_k \, dN_k = \\
     & = T \, dS - P \, dV + \left( \mu_k n_k \right) dN
\end{aligned}$$

avendo indicato con $n_k$ i coefficienti stechiomentrici (con segno) della reazione, e con $N$ una quantità che identifica l'equilibrio della reazione, in maniera tale da poter scrivere la variazione di ogni componente come $d N_k = n_k \, d N$.

```
```{prf:example} Miscela monocomponente durante una transizione di fase
:class: dropdown

**todo** come trattare la frazione delle fasi?

```
```{prf:example} Solido
:class: dropdown

Sistema solido di volume iniziale $V$ con stato di sforzo e deformazione uniforme, e piccole deformazioni

$$dE = T \, dS - V \, \sigma_{ij} \, d \varepsilon_{ij} $$

```
```{prf:example} Miscele solide
:class: dropdown

**todo**
```
```{prf:example} Influenza del campo magnetico
:class: dropdown

$$dE = T \, dS - P \, d V + H \, dM$$

**todo**
```
