(continuum:solids)=
# Solidi

In questa sezione viene inizialmente introdotto il comportamento di un solido, caratterizzato con una [**prova mono-assiale a trazione**](contiuum:solids:mono-axial); successivamente viene presentato il modello più semplice di solido deformabile, la [**trave elastica**](continuum:solids:beam): per questi elementi strutturali, vengono analizzate le azioni interne e le condizioni di equilibrio, prima di fornire alcuni esempi.


Piccoli spostamenti e piccole vibrazioni: regime in cui si studia la statica delle strutture la dinamica di spostamenti di ampiezza limitata rispetto a una condizione di riferimento - tipicamente vibrazioni o oscillazioni. **todo** *collegamento a onde?*

I solidi **elastici** - *ma cosa sono i solidi elastici?* - possono essere modellati come sistemi di molle e masse. **todo** *aggiungere collegamento*

(contiuum:solids:mono-axial)=
## Prova mono-assiale

(contiuum:solids:beam)=
## Elementi allungati - le travi

(contiuum:solids:beam:displacement)=
### Approccio agli spostamenti

Nel caso di travi allungate è possibile riportare gli spostamenti di tutti i punti di una sezione della trave agli spostamenti di un suo punto e alla rotazione della sezione.

(contiuum:solids:beam:stress)=
### Sforzi

(contiuum:solids:beam:internal-actions)=
### Azioni interne

La distribuzione di sforzi agenti su ogni sezione interna di una trave in generale ha come risultante una forza e un momento, rispetto a un punto.
Tra le componenti della forza si possono riconoscere:
- l'azione assiale, definita come la componente della risultante degli sforzi interni lungo l'asse della trave
- le due componenti del taglio, definite come le componenti della risultante degli sforzi interni perpendicolari all'asse della trave

Tra le componentni del momento, si possono riconsocere:
- il momento torcente, definito come la componente del momento lungo l'asse della trave
- le due componenti del momento flettente

(contiuum:solids:beam:constitutive-law)=
### Legge costitutiva - per le travi
Nel caso particolare di travi a sezione costante simmetrica, è possibile definire una legge costitutiva tra le azioni interne e i gradi di libertà della trave particolarmente semplice, in cui le azioni interne e i gradi di libertà risultano disaccoppiati, se il punto di riferimento è il centro (di simmetria geometrica e di proprietà fisiche) della sezione

$$\begin{aligned}
  N  (z) & = EA   u'_z(z)                               && \quad M_z = GJ_t \theta'_z(z) \\
  T_x(z) & = GA_x \left( u'_x(z) - \theta_y(z) \right)  && \quad M_x = EJ_x \theta'_x(z) \\
  T_y(z) & = GA_y \left( u'_y(z) + \theta_x(z) \right)  && \quad M_y = EJ_y \theta'_y(z) \\
\end{aligned}$$

(contiuum:solids:beam:statics)=
### Statica

(contiuum:solids:beam:statics:equil)=
#### Equazioni indefinite di equilibrio
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
  N'    & = f_z  \qquad && \qquad \ \quad EA u''_z        = f_z \\
  M'_z  & = m_z  \qquad && \qquad \ \quad GJ_t \theta''_z = m_z \\
  M''_x & = f_x  \qquad && \qquad -EJ_x u''''_x           = f_x \\     
  M''_y & =-f_y  \qquad && \qquad -EJ_y u''''_y           = f_y \\     
\end{aligned}$$

(contiuum:solids:beam:statics:bc)=
#### Condizioni al contorno
...condizioni essenziali (sugli spostamenti, dai vincoli) e naturali (dai carichi)...

### Modelli discreti(zzati)
...

```{prf:example} Distribuzione di sforzi assiali, o come rompere una matita/un righello
:label: solids-pencil
:class: dropdown

**Trave con carico assiale agli estremi.** Dalle condizioni di equilibrio, l'azione interna è costante lungo tutta la trave,

$$N(z) = N \ ,$$

e lo sforzo uniforme sulla sezione è

$$\sigma(z) = \frac{N(z)}{A}$$

Con una trave rettangolare di base $a$ e altezza $b$, $\sigma = \frac{N}{a b}$

**Trave con momento flettente agli estremi.**

$$M(z) = M \ ,$$

e la distribuzione lineare "a farfalla" degli sforzi assiali sulla sezione è

$$\sigma(z,x) = \frac{M_y(z)}{J_y} x $$

$$\sigma_{max}(z,x) = \frac{M}{ \frac{1}{12} a^3 b } \frac{a}{2}$$

---

$$M_y = \int_A \sigma(x) x \, dA = \int_A c x^2 \ dA = c J_y$$

$$c = \frac{M_y}{J_y} \ ,$$

$$\sigma(z,x) = \frac{M_y(z)}{J_y} \, x \ .$$

Per una sezione rettangolare di base $a$ e di altezza $b$,

$$J_y = \int_A x^2 \, dA = \int_{x=-\frac{a}{2}}^{\frac{a}{2}} \int_{y=-\frac{b}{2}}^{\frac{b}{2}} x^2 \, dx \, dy = \frac{1}{12} a^3 b $$

**Trave appoggiata agli estremi e caricata in centro.** 

```
```{prf:example} Strutture reticolari
:label: solids-frame

```

(continuum:solids:non-elastic)=
## Meccanismi non elastici

(continuum:solids:plastic)=
### Snervamento e rottura

(continuum:solids:instability)=
### Instabilità
- Esempi di instabilità di punta: spaghetto
- Modello strutturale discreto

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


## Esercizi
- strutture **isostatiche**:
  - aggiungere una definizione di strutture isostatiche
  - reazioni vincolari e azioni interne con condizioni di equilibrio





