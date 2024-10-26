(physics-hs:electromagnetism:electrostatics)=
# Elettrostatica

## Legge di Coulmb

Date due cariche elettriche puntiformi $q_1$, $q_2$, nella posizione $P_1$, $P_2$ nello spazio, la forza 

$$\vec{F}_{12} = k \frac{q_1 \, q_2}{|\vec{r}_{12}|^2} \, \hat{r}_{21} = \frac{1}{4 \pi \varepsilon}\frac{q_1 \, q_2}{|\vec{r}_{12}|^2} \, \hat{r}_{21}$$

essendo $\vec{r}_{21}$ il vettore che congiunge il punto $P_2$ con il punto $P_1$, $\vec{r}_{21} = \vec{r}_1 - \vec{r}_2$.

**todo**
- definizione della costante di proporzionalità $k = 4 \pi \varepsilon$ guidata dalla legge di Gauss
- costante dielettrica, nel vuoto e del materiale...; 
- esperimento ed esercizio con elettroscopio e bilancia (similitudine con legge di gravitazione universale, ma doppia natura della carica elettrica + o -)
- **PSCE**

## Il campo elettrico
Viene data una distribuzione di cariche, $q_i$, nei punti dello spazio $P_i$. Si prende una carica test, una carica di prova, di intensità nota $q^{test}$, che può esseere mossa a discrezione in ogni punto $P$ dello spazio e per la quale è possibile misurare la forza $\vec{F}(P)$ agente su di essa a causa della distribuzione di cariche,

$$\begin{aligned}
  \vec{F}_{test}(P)
  & = \sum_i \vec{F}_{test,i}(P) = \\
  & = \sum_i \frac{1}{4 \pi \varepsilon}\frac{q_i \, q_{test}}{|\vec{r}_{i,test,i}|^2} \, \hat{r}_{i,test} = \\
  & = q_{test} \sum_i \frac{1}{4 \pi \varepsilon}\frac{q_i}{|\vec{r}_{i,test,i}|^2} \, \hat{r}_{i,test} = \\
  & = q_{test} \, \vec{e}(P; \, q_i, \, P_i) \ .
\end{aligned}$$

Poichè la forza sulla carica di prova è proporzionale alla sua carica elettrica, è possibile descrivere l'effetto della distribuzione nota di cariche nello spazio con la funzione $\vec{e}(P; \, q_i, \, P_i)$. Questa funzione viene definita **campo elettrico** della distribuzione delle cariche.

Noto il campo elettrico di una dsitribuzione di cariche, la forza agente su una carica elettrica $q$ posta nel punto $P$ dello spazio è

$$\vec{F} = q \, \vec{e}(P)$$

- **todo** Poichè il PSCE vale per la forza, il **PSCE** vale per il campo elettrico

### Campo conservativo
Come mostrato (**todo** <span style="color:red"> ah sì? fare riferimenti qui?</span>) per il campo gravitazionale, anche il campo elettrostatico è un campo conservativo.

Il lavoro fatto dal campo su una carica che descrive una traiettoria $\gamma$, con estremi $A$, $B$ è uguale a

$$\begin{aligned}
  L & = \int_{\gamma} \vec{F}(P) \cdot d \vec{r} = - \int_{\gamma} \nabla U(P) \cdot d \vec{r} = - \Delta U = U(A) - U(B) \\
    & = q \, \int_{\gamma} \vec{e}(P) \cdot d \vec{r} = - q \int_{\gamma} \nabla V(P) \cdot d \vec{r} = - q \, \Delta V = q \, \left( V(A) - V(B) \right) \\
\end{aligned}$$

avendo definito l'**energia potenziale** $U(P)$ del sistema di cariche che produce il campo elettrico $\vec{e}(P)$ e il **potenziale elettrico** $V(P)$ come l'energia potenziale per unità di carica $q$.

Il potenziale generato da una carica $q_i$ posizionata punto "potenziante" $P_i$ nel punto "potenziato" $P$

$$V_i(P) = - \frac{1}{4 \pi \varepsilon} \frac{q_i}{|\vec{r}_i|} \ ,$$

con $\vec{r}_i = P_i - P$. Poichè il PSCE vale per la forza e il campo elettrico, il **PSCE** vale per il potenziale, e quindi il potenziale elettrico generato da un sistema di cariche è la somma del potenziale elettrico generato dalle singole cariche,

$$V_i(P) = - \frac{1}{4 \pi \varepsilon} \sum_i \frac{q_{i}}{\left|\vec{r}_{i}\right|} $$

### Energia potenziale di una distribuzione di cariche

L'energia potenziale di un sistema di cariche è uguale al lavoro (<span style="color:red">delle forze esterne = - lavoro forza elettrica</span>) fatto per costruire tale distribuzione. Poiché in meccanica classica l'energia è definita a meno di una costante additiva arbitraria, si può considerare la condizione di riferimento con le cariche poste all'"infinito" o, meglio, infinitamente distanti una dalle altre.

Per un sistema di cariche puntiformi, l'energia potenziale del sistema è uguale alla somma dell'energia potenziale tra le singole coppie di cariche

$$E^{pot} = - \sum_{\{i,j\}, i \ne j} V_{ij} = \sum_{\{i,j\}, i \ne j} \frac{1}{4 \pi \varepsilon} \frac{{q}_{i} \, q_{j}}{r_{ij}} \ ,$$

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


## Verso le equazioni di Maxwell

### Legge di Gauss per il flusso del campo elettrico

**todo** come dimostrarla senza usare troppa matematica? Esempio in caso semplice, ma come generalizzarlo?

  $$\Phi_{\partial V}(\vec{d}) = Q_V$$

**todo** come introdurre $\vec{d}$? Definire risposta dei materiali prima?

### Legge di Faraday, in elettrostatica
- La legge di Faraday in elettrostatica è una diretta conseguenza della conservatività del campo elettrico

  $$\Gamma_{\ell}(\vec{e}) = \oint_{\ell} \vec{e} \cdot \hat{t} = 0 \ .$$

- Questa equazione è valida **solo** in un regime elettrostatico: la forma generale dell'equazione di Faraday prevede un termine dipendente dal tempo, che è identicamente nullo nel regime elettrostatico.

## Moto di una carica in un campo elettrico
Il moto di una corpo puntiforme di massa $m$ e carica elettrica $q$ in una regione dello spazio nel quale c'è un campo elettrico $\vec{e}(\vec{r})$ è soggetto a una forza esterna $\vec{F}^{el} = q \, \vec{e}(P)$. L'equazione del moto diventa quindi

  $$m \ddot{ \vec{r} } = \vec{R}^{ext} = q \, \vec{e}(P) + \vec{F}^{\text{non }\vec{e}}$$

- **todo** esempi


## **todo** ...
**todo**
<span style="color:red"> Dove trattare i condensatori? </span>

- distribuzione di carica su conduttori sulla superficie
  - esempi: gabbia di Faraday,
    - condensatore
      - campi elettrici nei materiali: polarizzazione
      - energia accumulata
      - sistemi di condensatori








