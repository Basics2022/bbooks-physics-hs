(physics-hs:electromagnetism:electrostatics)=
# Elettrostatica

## Legge di Coulomb

Date due cariche elettriche puntiformi $q_1$, $q_2$, nella posizione $P_1$, $P_2$ nello spazio, la forza 

$$\vec{F}_{12} = k \frac{q_1 \, q_2}{|\vec{r}_{12}|^2} \, \hat{r}_{21} = \frac{1}{4 \pi \varepsilon}\frac{q_1 \, q_2}{|\vec{r}_{12}|^2} \, \hat{r}_{21}$$

essendo $\vec{r}_{21}$ il vettore che congiunge il punto $P_2$ con il punto $P_{1}$, $\vec{r}_{21} = \vec{r}_1 - \vec{r}_2$.


|![](../../media/electrostatics-coulomb-pp.png)|![](../../media/electrostatics-coulomb-pn.png)|![](../../media/electrostatics-coulomb-nn.png)|
|---|---|---|

<!--
```{figure} ../../media/electrostatics-coulomb-pp.png
---
width: 30%
---
```
```{figure} ../../media/electrostatics-coulomb-pn.png
---
width: 30%
---
```
```{figure} ../../media/electrostatics-coulomb-nn.png
---
width: 30%
---
```
-->
<!--
![](../../media/electrostatics-coulomb-pp.png)
![](../../media/electrostatics-coulomb-pn.png)
![](../../media/electrostatics-coulomb-nn.png)
-->

La scelta della definizione della costante di proporzionalità, $k = \frac{1}{4 \pi \varepsilon}$, viene fatta per ottenere un'espressione della [legge di Gauss per il campo elettrico](physics-hs:electromagnetism:electrostatics:maxwell:gauss) senza fattori numerici.

La costante $\varepsilon$ viene definita costante dielettrica del mezzo. Per cariche elettriche posizionate nello spazio "vuoto" (di materia ma non di proprietà fisiche), nell'espressione della legge di Coulomb compare la **costante dielettrica nel vuoto**,

$$\varepsilon_0 = 8.854 \cdot 10^{-12} \, C^2 \, N^{-1} \, m^{-2} \ .$$

Materiali isotropi lineari non dispersivi possono essere caratterizzati da una sola costante, la costante dielettrica del materiale. Questa caratteristica del materiale viene di solito definita come multiplo della costante dielettrica del vuoto, tramite la costante dielettrica relativa $\varepsilon_r$,

$$\varepsilon = \varepsilon_r \,\varepsilon_0 \ . $$

**todo**
- esperimento ed esercizio con elettroscopio e bilancia (similitudine con legge di gravitazione universale, ma doppia natura della carica elettrica + o -) **todo** riferimento alle prime esperienze sulle cariche elettriche
- **PSCE**

### Misura della carica elettrica
Un elettrometro è uno strumento di misura della carica elettrica. Una versione rudimentale di un elettrometro è la bilancia di torsione usata da Coulomb nei suoi esperimenti.

## Il campo elettrico
Data una distribuzione di cariche nello spazio, è possibile descriverla tramite l'effetto che avrebbe su una carica qualsiasi posta in un punto arbitrario dello spazio, introducendo la definizione di campo elettrico.

Viene data qui una **definizione operativa** del campo elettrico. Data una distribuzione di cariche, $q_i$, nei punti dello spazio $P_i$, si prende una carica test - di prova - di intensità nota $q^{test}$, che può essere posizionata in ogni punto $P$ dello spazio. E' inoltre possibile misurare la forza $\vec{F}(P; q^{test})$ agente sulla carica di prova dovuta all'interazione con la distribuzione di cariche in esame,

$$\begin{aligned}
  \vec{F}_{test}(P, q^{test})
  & = \sum_i \vec{F}_{test,i}(P) = \\
  & = \sum_i \frac{1}{4 \pi \varepsilon}\frac{q_i \, q_{test}}{|\vec{r}_{i,test,i}|^2} \, \hat{r}_{i,test} = \\
  & = q_{test} \sum_i \frac{1}{4 \pi \varepsilon}\frac{q_i}{|\vec{r}_{i,test,i}|^2} \, \hat{r}_{i,test} = \\
  & = q_{test} \, \vec{e}(P; \, q_i, \, P_i) \ .
\end{aligned}$$

Poichè la forza sulla carica di prova è proporzionale alla sua carica elettrica, è possibile descrivere l'effetto della distribuzione nota di cariche nello spazio con la funzione $\vec{e}(P; \, q_i, \, P_i)$. Questa funzione viene definita **campo elettrico** della distribuzione delle cariche.

Viceversa, noto il campo elettrico di una distribuzione di cariche, la forza agente su una carica elettrica $q$ posta nel punto $P$ dello spazio è

$$\vec{F} = q \, \vec{e}(P) \ .$$

- **todo** Poichè il PSCE vale per la forza, il **PSCE** vale per il campo elettrico

### Campo conservativo
Come mostrato (**todo** <span style="color:red"> ah sì? fare riferimenti qui?</span>) per il campo gravitazionale, anche il campo elettrostatico è un campo conservativo.

Il lavoro fatto dal campo su una carica che descrive una traiettoria $\gamma$, con estremi $A$, $B$ è uguale a

$$\begin{aligned}
  L & = \int_{\gamma} \vec{F}(P) \cdot d \vec{r} = - \int_{\gamma} \nabla U(P) \cdot d \vec{r} = - \Delta U = U(A) - U(B) \\
    & = q \, \int_{\gamma} \vec{e}(P) \cdot d \vec{r} = - q \int_{\gamma} \nabla V(P) \cdot d \vec{r} = - q \, \Delta V = q \, \left( V(A) - V(B) \right) \\
\end{aligned}$$

avendo definito l'**energia potenziale** $U(P)$ del sistema di cariche che produce il campo elettrico $\vec{e}(P)$ e il **potenziale elettrico** $V(P)$ come l'energia potenziale per unità di carica $q$. Sia l'energia potenziale sia il potenziale sono definiti a meno di una costante additiva.

Il potenziale generato da una carica $q_i$ posizionata punto "potenziante" $P_i$ nel punto "potenziato" $P$

$$V_i(P) = \frac{1}{4 \pi \varepsilon} \frac{q_i}{|\vec{r}_i|} \ ,$$

con $\vec{r}_i = P - P_i$. Poichè il PSCE vale per la forza e il campo elettrico, il **PSCE** vale per il potenziale, e quindi il potenziale elettrico generato da un sistema di cariche è la somma del potenziale elettrico generato dalle singole cariche,

$$V_i(P) = \frac{1}{4 \pi \varepsilon} \sum_i \frac{q_{i}}{\left|\vec{r}_{i}\right|} $$

### Energia potenziale di una distribuzione di cariche

L'energia potenziale di un sistema di cariche è uguale al lavoro (<span style="color:red">delle forze esterne = - lavoro forza elettrica</span>) fatto per costruire tale distribuzione. Poiché in meccanica classica l'energia è definita a meno di una costante additiva arbitraria, si può considerare la condizione di riferimento con le cariche poste all'"infinito" o, meglio, infinitamente distanti una dalle altre.

Per un sistema di cariche puntiformi, l'energia potenziale del sistema è uguale alla somma dell'energia potenziale tra le singole coppie di cariche

$$E^{pot} = \sum_{\{i,j\}, i \ne j} V_{ij} = \sum_{\{i,j\}, i \ne j} \frac{1}{4 \pi \varepsilon} \frac{{q}_{i} \, q_{j}}{r_{ij}} \ ,$$

senza ripetere la sommatoria sulle coppie con gli elementi invertiti.

Seguono due dimostrazioni di questa formula, ottenute costruendo il sistema di cariche dall'infinito in due maneire diverse.

<!--
In assenza di altri fenomeni, l'energia potenziale del sistema di cariche è uguale al lavoro fatto per costruire il sistema di cariche. Ad esempio, si può costruire il sistema di cariche
-->

<span style="color:red"> **todo** </span>

```{dropdown} Posizionando una carica alla volta
$$\begin{aligned}
  L^{ext}_1 & = 0 \\
  L^{ext}_2 & = \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_2}{r_{12}}  \\
  L^{ext}_3 & = \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_3}{r_{13}} + \frac{1}{4 \pi \varepsilon} \frac{q_2 \, q_3}{r_{23}}  \\
            & ... \\
  L^{ext}_n & = \sum_{j=1}^{n-1} \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_n}{r_{1n}} \\
\end{aligned}$$

$$E^{pot} = L^{ext} = \sum_i L^{ext}_i = \sum_{\{i, j\}, i \ne j} \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_j}{r_{ij}} \ .$$
```

```{dropdown} Posizionando le cariche contemporanamente
Posizionando tutte le cariche contamporaneamente con una "scalatura" delle distanze, $\vec{r}_i(\alpha) = \frac{\vec{r}_i}{\alpha}$, $\alpha \in (0, 1]$, il lavoro delle forze elettriche è

$$\begin{aligned}
  dL_i(\alpha) & = \sum_{j \ne i} \vec{F}_{ij}(\alpha) \cdot d \vec{r}_i(\alpha) = \\
  & = \sum_{j \ne i} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{\left| \frac{\vec{r}_i}{\alpha} - \frac{\vec{r}_j}{\alpha}\right|^2} \hat{r}_{ji} \cdot \left(-\frac{\vec{r}_i}{\alpha^2}\right) \, d \alpha = \\
  & = - \sum_{j \ne i} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{\hat{r}_{ji} \cdot\vec{r}_i}{\left| \vec{r}_i - \vec{r}_j\right|^2}  \, d \alpha
\end{aligned}$$

$$\begin{aligned}
 dL(\alpha) & = \sum_i d L_i = \\
  & = - \sum_{i} \sum_{j \ne i} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{\hat{r}_{ji} \cdot\vec{r}_i}{\left| \vec{r}_i - \vec{r}_j\right|^2}  \, d \alpha = \\
  & = - \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{\hat{r}_{ji} \cdot \left( \vec{r}_i - \vec{r}_j \right)}{\left| \vec{r}_i - \vec{r}_j\right|^2}  \, d \alpha = \\
  & = - \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{r_{ij}}  \, d \alpha  \ ,
\end{aligned}$$

e il lavoro diventa

$$
 L = \int_{\alpha = 0}^{1} dL (\alpha) =  - \int_{\alpha=0}^{1} \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{r_{ij}}  \, d \alpha = - \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{r_{ij}} \ .
$$
```

## Campo elettrico nei materiali

- polarizzazione...

Per materiali lineari isotropi,

$$\vec{d} := \varepsilon \vec{e} = \varepsilon_0 \vec{e} + \vec{p}$$

**todo** polarizzazione, cariche libere e cariche "vincolate"

(physics-hs:electromagnetism:electrostatics:maxwell)=
## Verso le equazioni di Maxwell

(physics-hs:electromagnetism:electrostatics:maxwell:gauss)=
### Legge di Gauss per il flusso del campo elettrico

  $$\Phi_{\partial V}(\vec{d}) = Q_V$$

```{dropdown} Dimostrazione della legge di Gauss
**Dimostrazione per una carica puntiforme e una superficie sferica.**
Il calcolo diretto del flusso del campo elettrico generato da una carica puntiforme attraverso una superficie sferica di raggio $r$ centrata nella carica

$$\Phi_{S^{sphere}}(\vec{d}) = \oint_{S^{sphere}} \vec{d} \cdot \hat{n} = \oint_{S^{sphere}} \frac{1}{4 \pi }\frac{q}{r^2} \underbrace{\hat{r} \cdot \hat{r}}_{=1} \ .  $$

L'integranda è costante, essendo $r$ costante sulla superficie sferica, e quindi si riduce al prodotto della funzione integranda per l'estensione del dominio di integrazione, qui la superficie estenra della sfera. Ricordando che la superficie di una superficie sferica di raggio $r$ è $S = 4 \pi r^2$, si ottiene l'espressione della legge di Gauss per il campo elettrico di una carica puntiforme attraverso una superficie sferica,

$$\Phi_{S^{sphere}}(\vec{d}) = 4 \, \pi \, r^2 \frac{1}{4 \, \pi \, r^2} q = q \ .$$

**todo** obs: andamento del campo come $r^{-2}$ implica andamento del flusso costante attraverso superfici che sottengono lo stesso **angolo solido**

**todo** ... altra osservazione che ora non ricordo...

**Dimostrazione per una carica puntiforme e per una superficie arbitraria.**
Usando l'osservazione sull'andamento del campo, e la definizione di angolo solido

$$\oint_S \frac{q}{4 \pi} \frac{1}{r^2} \hat{r} \cdot \hat{n} \, dS =
\oint_{\Omega} \frac{q}{4 \pi}  \, d \Omega = q $$


**Dimostrazione per una distribuzione di carica qualsiasi e superficie arbitraria.**
Avendo dimostrato la legge di Gauss per una carica puntiforme attraverso una superficie arbitraria, la legge di Gauss per il campo $\vec{d}$ generato da una distribuzione di carica qualsiasi segue immediatamente, ricordando che vale il PSCE

$$\Phi_{\partial V}(\vec{d}_i) = q_i$$

$$\sum_i \Phi_{\partial V}(\vec{d}_i) = \Phi_{\partial V} \left(\sum_i \vec{d}_i \right) = \sum_i q_i$$

$$\Phi_{\partial V}(\vec{d}) = Q_V$$

```

### Legge di Faraday, in elettrostatica
- La legge di Faraday in elettrostatica è una diretta conseguenza della conservatività del campo elettrico

  $$\Gamma_{\ell}(\vec{e}) = \oint_{\ell} \vec{e} \cdot \hat{t} = 0 \ .$$

- Questa equazione è valida **solo** in un regime elettrostatico: la forma generale dell'equazione di Faraday prevede un termine dipendente dal tempo, che è identicamente nullo nel regime elettrostatico.

```{dropdown} Dimostrazione della legge di Faraday
**Dimostrazione per una carica puntiforme e un percorso circolare.**
Il calcolo diretto della circuitazione del campo elettrico generato da una carica puntiforme lungo un percorso circolare di raggio $r$ centrato nella carica

$$\Gamma_{\ell^{circle}}(\vec{e}) = \oint_{\ell^{circle}} \vec{e} \cdot \hat{t} = \oint_{S^{sphere}} \frac{1}{4 \pi \varepsilon}\frac{q}{r^2} \underbrace{\hat{r} \cdot \hat{t}}_{=0} = 0 \ ,  $$

poiché il versore tangente al percorso circolare è ortogonale al campo elettrico, diretto in direzione radiale.

**Dimostrazione per una carica puntiforme e un percorso arbitrario.**

**Dimostrazione per una distribuzione di carica qualsiasi e percorso arbitrario.**
Avendo dimostrato la legge di Faraday nel caso stazionario per una carica puntiforme lungo un percorso arbitrario, la legge di Faraday in regime stazionario per il $\vec{e}$ generato da una distribuzione di carica qualsiasi segue immediatamente, ricordando che vale il PSCE

$$\Gamma_{\partial S}(\vec{e}_i) = 0$$

$$\sum_i \Gamma_{\partial S}(\vec{e}_i) = \Gamma_{\partial S} \left(\sum_i \vec{e}_i \right) = 0$$

$$\Gamma_{\partial S}(\vec{e}) = 0$$

```

## Moto di una carica in un campo elettrico
Il moto di una corpo puntiforme di massa $m$ e carica elettrica $q$ in una regione dello spazio nel quale c'è un campo elettrico $\vec{e}(\vec{r})$ è soggetto a una forza esterna $\vec{F}^{el} = q \, \vec{e}(P)$. L'equazione del moto diventa quindi

  $$m \ddot{ \vec{r} } = \vec{R}^{ext} = q \, \vec{e}(P) + \vec{F}^{\text{non }\vec{e}}$$

- **todo** esempi

## Condensatore

### Condensatore infinito piano
$$e = \frac{\sigma}{\varepsilon}$$

$$Q = \sigma \, A$$

$$\Delta V = \int_{\ell} \vec{e} \cdot d \vec{r} = \ell \, e$$

$$ Q = \sigma \, A = \varepsilon \, e \, A = \frac{\varepsilon \, \ell}{A} \, \Delta V = C \, \Delta V \ ,$$

$C$ capacità, $C = \frac{\varepsilon \, A}{\ell}$ capacità per un condensatore piano.

```{dropdown} Condensatore cilindrico
**todo**
```

```{dropdown} Condensatore sferico
Tra le sfere del condensatore, il campo elettrico è ha direzione radiale e valore assoluto $\propto r^{-2}$,

$$\vec{e}(r) = \frac{1}{4 \pi \varepsilon} \frac{Q}{r^2} \hat{r} \ .$$

dove la carica totale della superficie sferica con distribuzione di carica uniforme è data dal prodotto della densità superficiale di carica e la superficie, $Q = \sigma \, S_1 = \sigma \, 4 \pi \, R_1^2$.
La differenza di potenziale tra le due armature è quindi

$$\Delta V = - \int_{\ell} \vec{e}(r) \cdot \hat{r} = \int_{r=R_1}^{R_2} \frac{Q}{4 \pi r^2} dr = \frac{1}{4 \pi \varepsilon} \frac{1}{r} \bigg|_{R_1}^{R_2} = - \frac{1}{4 \pi \varepsilon} \left(\frac{1}{R_1} - \frac{1}{R_2} \right) \ , Q \ .$$

La formula precedente e la definizione di capacità, $$Q = C , \Delta V$$, consente di determinare la capacità di un condensatore sferico ideale,

$$C = 4 \pi \, \varepsilon \,  \frac{R_1 \, R_2}{R_2 - R_1} \ .$$
```

<!-- **todo** non qui! Spostare nella pagina riassuntiva delle equazioni di Maxwell?

### Equazioni di Maxwell e carica di un condensatore
**todo** significato del termine $\dot{\Phi}_{S}(\vec{d})$

L'equazione di Ampére-Maxwell,

$$\Gamma_{\partial S}(\vec{h}) - \dot{\Phi}_{S}(\vec{d}) = i_S $$

viene applicata a un condensatore piano, usando due superfici $S_1$, $S_2$ che hanno lo stesso contorno, $\ell$

- $S_1$ è tagliata dal conduttore 

  $$\Gamma_{\ell}(\vec{h}) = i_{S_1}$$

- $S_2$ passa tra le armature del condensatore

  $$\Gamma_{\ell}(\vec{h}) = \dot{\Phi}_{S_2}(\vec{d})$$

Segue che $i_{S_1} = \dot{\Phi}_{S_2}(\vec{d})$ e quindi si ritrova la legge di conservazione della carica elettrica,

$$i = \dfrac{d}{dt} \left( A \, d \right) = \dfrac{d}{dt} \left( A \, \varepsilon \, e \right) = \dfrac{d Q}{dt} \ .$$


## **todo** ...
**todo**
<span style="color:red"> Dove trattare i condensatori? </span>

- distribuzione di carica su conduttori sulla superficie
  - esempi: gabbia di Faraday,
    - condensatore
      - campi elettrici nei materiali: polarizzazione
      - energia accumulata
      - sistemi di condensatori
-->







