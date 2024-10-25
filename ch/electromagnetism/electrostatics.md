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

$$L = \int_{\gamma} \vec{F}(P) \cdot d \vec{r} = - \Delta U = U(A) - U(B) \ ,$$

avendo definito $U(P)$ l'**energia potenziale**. Poiché la forza agente sulla carica può essere scritta come \vec{F}(P) = q \ , \vec{e}(P)$$, è possibile definire il lavoro e l'energia potenziale per unità di carica,

$$L = - \Delta U = - q \, {\Delta V} \ .$$

### Energia potenziale di una distribuzione di cariche
L'energia potenziale di un sistema di cariche è uguale al lavoro fatto per costruire tale distribuzione. Poiché in meccanica classica l'energia è definita a meno di una costante additiva arbitraria, si può considerare la condizione di riferimento con le cariche poste all'"infinito" o, meglio, infinitamente distanti una dalle altre.

In assenza di altri fenomeni, l'energia potenziale del sistema di cariche è uguale al lavoro fatto per costruire il sistema di cariche. Ad esempio, si può costruire il sistema di cariche
- posizionandole una alla volta ...

- posizionandole tutte insieme con una "scalatura" delle distanze ...


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








