(physics-hs:mechanics:dynamics:principles)=
# Princìpi della dinamica di Newton

La meccanica classica di Newton viene costruita assumendo valido il **principio di conservazione della massa** e i **tre principi della dinamica**.

**Principio di conservazione della massa.** In meccanica classica, il principio di Lavoisier di conservazione della massa può essere riassunto con la formula "niente si crea, niente si distrugge". Per essere più precisi, il principio di conservazione della massa postula che la massa di un sistema chiuso è costante.

**Primo principio - principio di inerzia.** Un sistema (o meglio, il baricentro di un sistema) sul quale agisce una forza esterna netta nulla, persevera nel suo stato di quiete o di moto rettilineo uniforme rispetto a un [sistema di riferimento inerziale](physics-hs:mechanics:dynamics:principles:inertial-ref-frame).

**Secondo principio - bilancio della quantità di moto per sistemi chiusi.** Rispetto a un sistema di riferimento inerziale, la variazione della quantità di moto $\vec{Q}$ di un sistema chiuso è uguale all'impulso delle forze esterne $\vec{I}^{ext}$ agenti su di esso,

$$\Delta \vec{Q} = \vec{I}^{ext} \ .$$

Nel caso di moto regolare, in cui la quantità di moto del sistema è una grandezza continua e differenziabile rispetto al tempo, il secondo principio può essere scritto in forma differenziale, facendo tendere a zero l'intervallo di tempo considerato

$$\dot{\vec{Q}} = \vec{R}^{ext} \ ,$$

avendo indicato con $\vec{R}^{ext}$ la risultante delle forze esterne agenti sul sistema.

**Terzo principio - principio di azione-reazione.** Se un sistema $i$ esercita una forza $\vec{F}_{ji}$ sul sistema $j$, allora il sistema $j$ esercita sul sistema $i$ una forza $\vec{F}_{ij}$ "uguale e contraria" - stesso valore assoluto e verso opposto,

$$\vec{F}_{ij} = - \vec{F}_{ji} \ .$$


**todo** **Osservazioni**
- sistema di riferimento inerziale e invarianza galileiana
- sistemi aperti e sistemi chiusi: sottolineare la validità di $\Delta \vec{Q} = \vec{I}^{ext}$ solo per sistemi chiusi, mentre per sistemi aperti è necessario un termine di flusso della quantità meccanica. Riferimento alla meccanica dei fluidi


(physics-hs:mechanics:dynamics:principles:inertial-ref-frame)=
## Sistemi di riferimento inerziali e invarianza galileiana.
La formulazione dei princìpi della dinamica si basa sul concetto di sistema di riferimento inerziale, di cui non è stato ancora detto nulla.
E' possibile dare una definizione operativa di osservatore inerziale (o sistema di riferimento inerziale? **todo**), supponendo che:
- l'osservatore sia dotato di uno strumento in grado di misurare le forze e i momenti ai quali è soggetto (**todo** ad esempio una bilancia o una combinazione di dinamometri)
- sia possibile conoscere le azioni "vere" (**todo** fare riferimento alle forze "vere" note: gravitazione - che in meccanica classica è una forza -, elettromagnetica, nucleare forte e debole; o le loro manifestazioni macroscopiche come ad esempio forze di contatto) agenti sul sistema.

**Definizione.**
Un osservatore è inerziale se la lettura degli strumenti di misura in suo possesso corrisponde alle azioni "vere" agenti sul sistema. In particolare, in assenza di azioni nette gli strumenti restituiscono una misura nulla.

```{prf:example} Sistemi inerziali, azioni vere e relatività generale

Esperimento mentale di A.Einstein dell'ascensore senza finestre come esperimento mentale introduttivo alla [relatività generale](physics-hs:modern:einstein:general).

```

**Definizione quantità cinematiche.**
Sia $O$ l'origine di un sistema di riferimento coincidente con un'osservatore inerziale, la velocità di un punto $P$ rispetto a $O$ è a derivata del vettore posizione $P - O$ rispetto al tempo (assoluto in meccanica classica di Newton)

$$\vec{v}_P = \dfrac{d}{dt} (P - O) \ .$$

La quantità di moto di un sistema rispetto al sistema di riferimento inerziale con origine in $O$ è data dal prodotto della massa del sistema per la velocità del centro di massa $G$,

$$\vec{Q} = m \, \vec{v}_G \ .$$

**Equivalenza di sistemi inerziali e invarianza galileiana.**
Dato un sistema inerziale, ogni altro sistema in moto relativo con un moto di traslazione a velocità costante è un sistema inerziale.

**todo** *Prova.*

**Invarianza galileiana.**
- Posizione
  
  $$P - O_0 = P - O_1 + O_1 - O_0$$

- Velocità e quantità di moto
  
  $$\vec{v}_{P/0} = \vec{v}_{P/1} + \vec{v}_{O_1/0}$$

  $$\begin{aligned}
    m \vec{v}_{G/0} & = m \vec{v}_{G/1} + m \vec{v}_{O_1/0} \\
       \vec{Q}_{/0} & = \vec{Q}_{/1} + m \vec{v}_{O_1/0}
  \end{aligned}$$

  con $\frac{d}{dt} \vec{v}_{O_1/0} = \vec{a}_{O_1/0} = \vec{0}$.

- Accelerazione e secondo principio della dinamica

  $$\vec{a}_{P/0} = \vec{a}_{P/1}$$

  $$\begin{aligned}
    \frac{d}{dt} \vec{Q}_{/0} & = \frac{d}{dt} \vec{Q}_{/1} + \frac{d}{dt} \left( m \vec{v}_{O_1/0}\right) \\
    \dot{\vec{Q}}_{/0} & = \dot{\vec{Q}}_{/1}
  \end{aligned}$$

  essendo $\frac{d}{dt} \vec{v}_{O_1/0} = \vec{a}_{O_1/0} = \vec{0}$.

Di conseguenza, il secondo principio della dinamica assume la stessa forma quando è riferito a un sistema di riferimento inerziale qualsiasi,

$$\dot{\vec{Q}} = \vec{R}^{ext} \ ,$$

e mentre la regola di trasformazione delle veloctià e delle posizioni rispetto ai diversi sistemi di riferimento inerziali è data dalle leggi

$$\begin{cases}
  \vec{v}_{P/0} = \vec{v}_{P/1} + \vec{v}_{O_1/0} \\
  \vec{r}_{P/0} = \vec{r}_{P/1} + \vec{v}_{O_1/0} t + \vec{r}_{O_1/0} \\
\end{cases}$$

che costituiscono le leggi della **relatività galileiana**, che legano due sistemi inerziali.


