<!--
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
-->

(physics-hs:mechanics:dynamics)=
# Dinamica

<!--
```{dropdown} todo
- Sistemare l'introuzione e il capitolo
- Aggiungere i concetti di **equilibrio** e **stabilità**. Fare riferimento alla capitolo sulla [statica](physics-hs:mechanics:statics), se necessario
- ...
```
-->

La dinamica si occupa del moto dei sistemi e delle cause del moto, mettendo insieme la descrizione [cinematica](physics-hs:mechanics:kinematics), l'[inerzia](physics-hs:mechanics:inertia) dei sistemi a perseverare nel moto, e le [azioni](physics-hs:mechanics:actions) come causa di una variazione del moto. La [statica](physics-hs:mechanics:statics) rappresenta un caso particolare di dinamica, in cui il sistema di interesse rimane nella configurazione di riferimento.

[**Princìpi della dinamica**](physics-hs:mechanics:dynamics:principles). Insieme al principio della conservazione della massa, vengono formulati i tre principi della dinamica di Newton per sistemi chiusi rispetto a sistemi di riferimento inerziali (1. principio di inerzia, 2. bilancio della quantità di moto e 3. principio di azione e reazione); successivamente viene discusso il significato della relatività galileiana e il ruolo dei sistemi di riferimento inerizali.

<!--  -->

[**Equazioni cardinali della dinamica**](physics-hs:mechanics:dynamics:eom). Vengono presentate le tre equazioni cardinali della dinamica per sistemi chiusi, che mettono in relazione la variazione delle grandezze dinamiche alle azioni, e che nel caso di moti regolari possono essere scritte in forma differenziale

$$\begin{aligned}
 \dot{\vec{Q}} & = \vec{R}^{ext} & \text{(bilancio quantità di moto)} \\
 \dot{\vec{L}}_H + \dot{\vec{x}}_H \times \vec{Q} & = \vec{M}_H^{ext} & \text{(bilancio momento della quantità di moto)} \\
 \dot{K} & = P^{tot} & \text{(bilancio energia cinetica)} 
\end{aligned}$$ (dynamics:eom)

```{admonition} Espressione delle equazioni di bilancio
:class: tip

Come dimostrato in [appendice](physics-hs:mechanics:dynamics:notes), le equazioni di bilancio hanno la stessa forma {eq}`dynamics:eom` per ogni sistema chiuso se scritti in termini di variazione di quantità di moto, momento della quantità di moto ed energia cinetica, senza esplicitare la forma particolare di queste grandezze dinamiche per i sistemi particolari presi in considerazione. Vengono forniti alcuni esempi ed esercizi svolti.

```

[**Leggi di conservazione**](physics-hs:mechanics:dynamics:conservation). Sotto opportune ipotesi immediatamente riconoscibili dalle equazioni cardinali {eq}`dynamics:eom`, vengono ricavate le leggi di conservazione validi per i sistemi meccanici,

$$\begin{aligned}
  \vec{R}^{ext} & = \vec{0} \qquad  & \rightarrow \qquad \ \ \vec{Q} = \text{const.} \\
  \vec{M}_H^{ext} & = \vec{0}, \dot{\vec{x}}_H \times \vec{Q} = \vec{0} \qquad  & \rightarrow \qquad \vec{L}_H = \text{const.} \\
  P^{tot} & = \vec{0} \qquad  & \rightarrow \qquad \ \  K = \text{const.} \\
\end{aligned}$$ (dynamics:eom:conservation)

Nel caso in cui le azioni agenti sul sistema non abbiano potenza nulla, ma che siano forze conservative, si riconosce la [legge di conservazione dell'energia meccanica $E^{mec}$](physics-hs:mechanics:dynamics:conservation:mechanical-energy), definita come somma dell'energia cinetica, $K$, e dell'energia potenziale, $V$,

$$P^{tot} = -\dot{V} \ , \quad E^{mec} = K + V \qquad \rightarrow \qquad E^{mec} = \text{const.}$$

[**Equilibrio e stabilità**](physics-hs:mechanics:equilibrium-stability). <span style="color:red">**todo**</span>

[**Esempi**](physics-hs:mechanics:dynamics:examples). Vengono analizzati alcuni sistemi particolari, di interesse pratico, storico, e/o didattico, per iniziare a fare pratica con i princìpi, le equazioni e i criteri mostrati in precedenza.

[**Sistemi aperti**](physics-hs:mechanics:dynamics:eom:open). Vengono discussi i bilanci delle quantità fisiche di massa, quantità di moto e momento della quantità di moto per sistemi aperti che possono scambiare massa con l'estero, e che quindi non hanno massa costante.

[**Urti**](physics-hs:mechanics:dynamics:collisions).
Vengono studiati alcuni sistemi in cui il moto non è regolare e derivabile, almeno in corrispondenza degli eventi di urto.
Viene presentato un modello di urto tra sistemi fondato unicamente sul coefficiente di restituzione, $\varepsilon$, per rappresentare la frazione di energia meccanica persa dal sistema durante l'urto. Vengono presentati dei problemi risolti grazie ai princìpi di conservazione e alle equazioni cardinali in forma incrementale. 

[**Moti centrali e gravitazione**](physics-hs:mechanics:dynamics:motion:central).
Viene studiata la dinamica di alcuni sistemi soggetti a una forza centrale, usando come esempi la forza generata da una molla elastica o la forza gravitazionale. L'interazione gravitazionale tra **due corpi** viene studiata in dettaglio, a causa della sua rilevanza storica: la corretta descrizione delle orbite dei pianeti attorno al Sole è stato uno dei primi successi della meccanica e la legge di gravitazione universale di Newton. Nell'ambito del problema dei due corpi, viene dimostrato che i corpi si muovono lungo traiettorie rappresentabili come [sezioni coniche](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/analytic_geometry/analytic_geometry_2d/conics.html), nelle quali il Sole occupa un fuoco; vengono quindi enunciate e dimostrate le [leggi di Keplero](physics-hs:mechanics:dynamics:motion:gravitation:kepler) per le orbite chiuse.

<!--
## Princìpi della dinamica
1.
2.
3.

## Equazioni del moto
- Bilancio della quantità di moto
- Bilancio del momento della quantità di moto
- Bilancio dell'energia cinetica

## Princìpi di conservazione

## Moti particolari
- moti piani: moto rettilineo uniforme, moto uniformemente accelerato; moto su una circonferenza; moti armonici
- moti centrali **todo** scegliere se trattare qui $F \propto r^2 ,r^{-2}$
- moti non regolari: urti
- gravità e moto dei corpi celesti (leggi di Keplero)
-->


