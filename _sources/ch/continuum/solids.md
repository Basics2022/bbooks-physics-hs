
(continuum:solids)=
# Solidi

Piccoli spostamenti e piccole vibrazioni: regime in cui si studia la statica delle strutture la dinamica di spostamenti di ampiezza limitata rispetto a una condizione di riferimento - tipicamente vibrazioni o oscillazioni. **todo** *collegamento a onde?*

I solidi **elastici** - *ma cosa sono i solidi elastici?* - possono essere modellati come sistemi di molle e masse. **todo** *aggiungere collegamento*

## Elementi allungati - le travi

### Approccio agli spostamenti

Nel caso di travi allungate è possibile riportare gli spostamenti di tutti i punti di una sezione della trave agli spostamenti di un suo punto e alla rotazione della sezione.

### Sforzi

### Azioni interne

La distribuzione di sforzi agenti su ogni sezione interna di una trave in generale ha come risultante una forza e un momento, rispetto a un punto.
Tra le componenti della forza si possono riconoscere:
- l'azione assiale, definita come la componente della risultante degli sforzi interni lungo l'asse della trave
- le due componenti del taglio, definite come le componenti della risultante degli sforzi interni perpendicolari all'asse della trave

Tra le componentni del momento, si possono riconsocere:
- il momento torcente, definito come la componente del momento lungo l'asse della trave
- le due componenti del momento flettente

### Legge costitutiva - per le travi
Nel caso particolare di travi a sezione costante simmetrica, è possibile definire una legge costitutiva tra le azioni interne e i gradi di libertà della trave particolarmente semplice, in cui le azioni interne e i gradi di libertà risultano disaccoppiati, se il punto di riferimento è il centro (di simmetria geometrica e di proprietà fisiche) della sezione

$$\begin{aligned}
  N  (z) & = EA   u'_z(z)                               && \quad M_z = GJ_t \theta'_z(z) \\
  T_x(z) & = GA_x \left( u'_x(z) - \theta_y(z) \right)  && \quad M_x = EJ_x \theta'_x(z) \\
  T_y(z) & = GA_y \left( u'_y(z) + \theta_x(z) \right)  && \quad M_y = EJ_y \theta'_y(z) \\
\end{aligned}$$

### Statica

### Equazioni indefinite di equilibrio
$$\begin{aligned}
  N'  (z) & = f_z(z) && \quad M'_z(z) = m_z(z) \\
  T'_x(z) & = f_x(z) && \quad M'_x(z) = m_x(z) + T_y(z) \\
  T'_y(z) & = f_y(z) && \quad M'_y(z) = m_y(z) - T_x(z) \\
\end{aligned}$$

**Travi snelle.** Per travi snelle, si può dimostrare che il contributo del taglio risulta trascurabile rispetto alle altre azioni. Questa condizione ha una conseguenza anche sulla cinematica dei punti della trave,

$$\begin{aligned}
  T_x = 0 \quad & \rightarrow \quad u'_x(z) = \theta_y(z) \\
  T_y = 0 \quad & \rightarrow \quad u'_y(z) =-\theta_x(z) \\
\end{aligned}$$

e sulle equazioni di equilibrio del corpo che, in assenza di momenti flettenti distribuiti, $m_x(z) = m_y(z) = 0$, diventano

$$\begin{aligned}
  N'    & = f_z \\
  M'_z  & = m_z \\
  M''_x & = f_x \\ 
  M''_y & =-f_y \\ 
\end{aligned}$$

o, in termini di spostamento,

$$\begin{aligned}
  EA u''_z    & = f_z \\
  GJ_t \theta''_z  & = m_z \\
 -EJ_x u''''_x & = f_x \\ 
 -EJ_y u''''_y & = f_y \\ 
\end{aligned}$$

.


(continuum:solids:non-elastic)=
## Meccanismi non elastici

(continuum:solids:plastic)=
### Snervamento e rottura

(continuum:solids:fatigue)=
### Fatica nei solidi

(continuum:solids:creep)=
### Creep - scorrimento viscoso

### todo
- Cenni di propagazione perturbazioni come onde, es:
  - fluidi:
    - pressione e acustica, piccole perturbazioni e urti
    - onde con superficie libera (mare, rubinetto,...)
  - perturbazioni nei solidi:
    - corda di una chitarra; altri esempi con elementi 1d
    - esempi con membrane (es, nostro orecchio)
    - esempi di propagazione in mezzi (più o meno) continui
    - onde sismiche








