(physics-hs:electromagnetism:circuits-electric)=
# Circuiti elettrici

(physics-hs:electromagnetism:circuits-electric:approx)=
## Approssimazione circuitale
L'ingegneria elettrica si occupa principamente di sistemi con correnti intense ma bassa frequenza. In questo regime di funzionamento, le equazioni di Maxwell che governano i fenomeni elettromagnetici possono essere semplificate
1. nelle regioni esterne alle pareti di eventuali condensatori presenti nel sistema, la derivata nel tempo del flusso del campo di spostamente è trascurabile,
2. il campo magnetico $\vec{b}$ e la sua derivata nel tempo sono rilevanti solo in alcune regioni dello spazio, e quindi confinati a componenti dotati di induttanze - come possono essere motori elettrici.

Al di fuori di queste regioni le equazioni di Maxwell {eq}`eq:principles:maxwell` si riducono quindi alle equazioni in regime stazionario

$$\begin{cases}
  \Phi_V(\vec{d}) = Q_f \\
  \Gamma_{\partial S}(\vec{e}) + \dot{\Phi}_S(\vec{b}) = 0 \\
  \Phi_V(\vec{b}) = 0 \\
  \Gamma_{\partial S}(\vec{h}) - \dot{\Phi}_S(\vec{d}) = \Phi_S(\vec{j}_f)
\end{cases}
\qquad \rightarrow \qquad
\begin{cases}
  \Phi_V(\vec{d}) = Q_f \\
  \Gamma_{\partial S}(\vec{e}) = 0 \\
  \Phi_V(\vec{b}) = 0 \\
  \Gamma_{\partial S}(\vec{h}) = \Phi_S(\vec{j}_f)
\end{cases}$$ (eq:principles:maxwell:el-circuit)

Anche se non è possibile fornirne una dimostrazione in termini semplici, queste approssimazioni hanno una conseguenza fondamentale: a bassa frequenza,
- i componenti elettrici possono essere analizzati **"agli effetti esterni"**: ogni componente componente ha il proprio comportamento caratteristico determinato dalla sua natura e descritto dalla sua equazione costitutiva, ma si interfaccia con l'esterno solo tramite i **morsetti della porta elettrica**, nella stra-grande maggior parte dei casi i cavi elettrici con i quali il componente può essere collegato ad altri componenti in un circuito
- si può trascurare la trasmissione del campo elettromagnetico come onde elettromagnetiche, anche la potenza irradiata tramite queste è trascurabile. Il bilancio di energia dei componenti di un sistema elettrico può essere riportato alla potenza trasmessa tramite i morsetti della porta elettrica, che assume l'espressione $P = v i$: la variazione di energia interna di un componente è uguale alla potenza trasferita tramite la sua porta elettrica,

  $$\dfrac{d E}{dt} = v i$$ (eq:el-circuit:power)

- poiché non avviene la trasmissione di onde elettromagnetiche, il problema elettromagnetico a basse frequenze è molto semplificato rispetto al problema elettromagnetico generale: mentre il problema elettromagnetico generale prevede che venga risolto il campo elettromagnetico in tutte le regioni dello spazio, l'approccio circuitale permette - quando applicabile - di considerare solo i componenti elettromegnetici collegati tramite conduttori che sotituiscono il sistema.[^circuit-math:pde-ode] 

[^circuit-math:pde-ode]: Dal punto di vista matematico, il problema elettromagnetico generale è governato da equazioni differenziali alle derivate parziali (PDE), ben oltre le possibilità di uno studente di scuola superiore. L'approccio circuitale permette di formulare il problema elettromagnetico in termini di equazioni differenziali ordinarie nel caso instazionario, equazioni algebriche nel caso stazionario (o periodico, in seguito a opportune trasformazioni): non proprio il problema più semplice possibile, ma un problema comunque affrontabile anche da parte di studenti delle scuole superiori.

(physics-hs:electromagnetism:circuits-electric:electric-cable)=
## Cavi elettrici
Nell'ambito dell'approssimazione circuitale, i cavi elettrici con sezione ridotta rispetto alle dimensioni del circuito possono essere trattati come elementi 1-dimensionali, delle curve con proprietà geometriche (linea media, sezione) e fisiche (resistività).

La dimensione ridotta della sezione permette quindi di trascurare la tridimensionalità del problema generale e di assumere che le grandezze siano uniformi su ogni sezione - o non tanto diverse dal loro valore medio: la velocità media *di deriva* $\vec{v}$ delle cariche e quindi la [densità di corrente](electric-current-density:def), $\vec{j} = \rho \vec{v}$, ha la stessa direzione dell'asse locale del conduttore.

La corrente può quindi essere espressa come

$$i = \vec{j} \cdot \hat{n} A \simeq j A \ ,$$ (eq:cable:current-current-density)

avendo indicato con $\hat{n}$ la normale della sezione e $A$ la superficie della sezione del cavo, e potendo considerare solo il valore scalare delle grandezze fisiche se si considera una sezione perpendicolare all'asse del cavo elettrico.

**todo** *aggiungere immagine*

(physics-hs:electromagnetism:circuits-electric:kirchhoff-laws)=
## Leggi di Kirchhoff

Le leggi di Kirchhoff trasformano l'equazioni di governo del problema elettromagnetico opportunamente semplificate nell'ambito delle basse frequnze nelle due leggi fondamentali dei circuiti.

**Legge ai nodi.** La somma delle correnti entranti in un nodo di un circuito elettrico è nulla. Questa legge è una conseguenza della legge del bilancio della carica {eq}`eq:principles:charge` per un sistema di volume nullo - o sistema che non può accumulare carica, $\dot{Q}_V$, come si considera un cavo di un circuito elettrico operante a bassa frequenza.

$$0 = \Phi_{\partial V}(\vec{j}) = \sum_{k} \vec{j}_k \cdot \hat{n}_k \, A_k = \sum_{k} i_k \ ,$$

dove la somma viene svolta su tutti i conduttori $k$ collegati al nodo considerato.

**Legge alle maglie.** La somma delle tensioni su una maglia di un circuito elettrico è nulla, nelle regioni in cui la derivata del flusso del campo magnetico è trascurabile - ad esempio, fuori da motori elettrici e trasformatori. Questa legge è una conseguenza della legge di Faraday nel caso in cui la derivata del flusso del campo magnetico sia nulla, e che quindi il campo elettrico possa essere scritto in termini di potenziale elettrico

$$0 = \Gamma_{\partial S}(\vec{e}) = \sum_{k} \Delta v_k \ ,$$

dove la somma viene svolta su tutti i lati $k$ della maglia del circuito considerata.

(physics-hs:electromagnetism:circuits-electric:components)=
## Componenti

In questa sezione vengonoo presentati i principali componenti che possono costituire un circuito, nella sezione successiva vengono analizzate alcuni possibili collegamenti di questi componenti e alcuni circuiti elementari.
I componenti sono caratterizzati dalla loro legge costitutiva - determinata dalla loro natura e struttura interna - ma che descrive completamente il componente elettrico "agli effetti esterni", cioè ai morsetti della sua porta elettrica, in termini di corrente $i$ e differenza di tensione ai morsetti. Per completezza, e per uniformarsi a quello che viene fatto comunemente, si introducono le due **convenzioni di segno** di differenza di tensione e corrente per due classi di componenti:
- **generatori**, componenti che producono potenza elettrica
- **utilizzatori**, componenti che - tipicamente - assorbono potenza elettrica

**todo** Immagini delle due convenzioni

(physics-hs:electromagnetism:circuits-electric:components:resistor)=
### Resistenza elettrica
La legge costitutiva della [resistenza elettrica lineare](physics-hs:electromagnetism:electric-current:solids:conductor:ohm) è determinata dalla legge di Ohm {eq}`ohm:integral:first:R` per resistenze lineari

$$v = R i \ ,$$

avendo usato la convenzione degli utilizzatori.

(physics-hs:electromagnetism:circuits-electric:components:capacitor)=
### Condensatore
La legge costitutiva di un [condensatore](physics-hs:electromagnetism:electrostatics:capacitor) è

$$i = C \dfrac{d v}{dt}$$

(physics-hs:electromagnetism:circuits-electric:components:inductor)=
### Induttore
La legge costitutiva di un induttore è

$$v = L \dfrac{d i}{dt}$$

(physics-hs:electromagnetism:circuits-electric:components:generator-v)=
### Generatore di tensione

$$v = e$$

(physics-hs:electromagnetism:circuits-electric:components:generator-i)=
### Generatore di corrente

$$i = a$$

(physics-hs:electromagnetism:circuits-electric:components:diode)=
### Diodo

**todo**

(physics-hs:electromagnetism:circuits-electric:components:configurations)=
## Collegamenti in serie e in parallelo

**Collegamento in serie.** Un collegamento in serie di componenti passivi lineari dello stesso tipo prevede che la stessa corrente passi attraverso ogni componente, $i_n = i, \forall n=1:N$, e che la differenza totale di tensione tra il "morsetto di entrata" del primo elemento e il "morsetto di uscita" dell'ultimo elemento è la somma delle differenze di tensione, $v = \sum_{n=1:N} v_n$. Segue quindi che:
- per resistenze in serie, $R_n$, la resistenza equivalente è uguale alla somma delle resistenze

   $$v = \sum_n v_n = \sum_n \left( R_n \, i_n \right) = \left( \sum_n R_n \right) i = R_{series} \, i \qquad \rightarrow \qquad R_{series} = \sum_n R_n$$

- per condensatori in serie, $C_n$, l'inverso della capacità equivalente è uguale alla somma degli inversi delle capacità,

   $$\dfrac{d v}{dt} = \sum_n \dfrac{d v_n}{dt} = \sum_n \left( \frac{1}{C_n} \, i_n \right) = \left( \sum_n \frac{1}{C_n} \right) i = \dfrac{1}{C_{series}} \, i \qquad \rightarrow \qquad \frac{1}{C_{series}} = \sum_n \frac{1}{C_n}$$

- per induttori in serie, $L_n$, l'induttanza equivalente è uguale alla somma delle induttanze,

   $$v = \sum_n v_n = \sum_n \left( L_n \, \dfrac{d i_n}{d t} \right) = \left( \sum_n L_n \right) \dfrac{d i}{dt} = L_{series} \, \dfrac{d i}{dt} \qquad \rightarrow \qquad L_{series} = \sum_n L_n$$

Di conseguenza, la resistenza e l'induttanza di resistenze e induttori in serie è maggiore della massima resistenza/induttanza del sistema; la capacità equivalente di condensatori in serieo è minore della minima capacità dei condensatori del sistema.

**Collegamento in parallelo.** Un collegamento in parallelo di componenti passivi lineari dello stesso tipo prevede che si verifichi la stessa differenza di tensione tra i morsetti di ogni componente, $v_n = i, \forall n=1:N$, e che la corrente che passa attraverso ogni componente sia in generale diversa e la somma delle correnti sia uguale alla corrente ai due nodi estremi del collegamento, $\sum_{n=1:N} i_n = i$. Segue quindi che:
- per resistenze in parallelo, $R_n$, l'inverso della resistenza equivalente è uguale alla somma degli inversi delle resistenze

   $$i = \sum_n i_n = \sum_n \left( \frac{1}{R_n} \, i_n \right) = \left( \sum_n \frac{1}{R_n} \right) i = \frac{1}{R_{\parallel}} \, i \qquad \rightarrow \qquad \frac{1}{R_{\parallel}} = \sum_n \frac{1}{R_n}$$

- per condensatori in parallelo, $C_n$, la capacità equivalente è uguale alla somma delle capacità,

   $$i = \sum_n i_n = \sum_n \left( C_n \, \dfrac{d v_n}{d t} \right) = \left( \sum_n C_n \right) \dfrac{d v}{dt} = C_{\parallel} \, \dfrac{d v}{dt} \qquad \rightarrow \qquad C_{\parallel} = \sum_n C_n$$

- per induttori in serie, $L_n$, l'inverso dell'induttanza equivalente è uguale alla somma dell'inverso delle induttanze,

   $$\dfrac{d i}{dt} = \sum_n \dfrac{d i_n}{dt} = \sum_n \left( \frac{1}{L_n} \, v_n \right) = \left( \sum_n \frac{1}{L_n} \right) v = \dfrac{1}{L_{\parallel}} \, v \qquad \rightarrow \qquad \frac{1}{L_{\parallel}} = \sum_n \frac{1}{L_n}$$

Di conseguenza, la resistenza e l'induttanza di resistenze e induttori in parallelo è minore della minima resistenza/induttanza del sistema; la capacità equivalente di condensatori in parallelo è maggiore della massima capacità dei condensatori del sistema.

(physics-hs:electromagnetism:circuits-electric:circuits)=
## Casi particolari

(physics-hs:electromagnetism:circuits-electric:circuits:open)=
### Circuito aperto
Un circuito è aperto in assenza di una chiusura fisica (con un cavo) di una maglia, o si comporta come tale in presenza di un lato attraverso il quale è impedito il passaggio di corrente elettrica,

$$i = 0 \ .$$

(physics-hs:electromagnetism:circuits-electric:circuits:short)=
### Cortocircuito
Un cortocircuito si verifica attraverso un componente con caduta di tensione nulla,

$$v = 0 \ .$$

Se un cortocircuito si manifesta in un'intera maglia, questa è percorsa da corrente infinita - in un modello lineare, che non consideri i limiti di validità; nella realtà si incontrano effetti non lineari molto prima, o scintille, esplosioni, o altri effetti distruttivi - spesso caratterizzati da resistenza nulla. **todo** *controllare generalità di questa condizione*

(physics-hs:electromagnetism:circuits-electric:regimes)=
## Regimi di funzionamento
(physics-hs:electromagnetism:circuits-electric:regimes:dc)=
### Regime stazionario - la corrente continua

Il regime di funzionamento di un circuito in corrente continua prevede che il valore della corrente elettrica e delle variabili del sistema siano costanti - nella vita reale, "sufficientemente costanti".

In questo regime di funzionamento, i condensatori si comportano come cirtuiti aperti, poiché $i = C \frac{dv}{dt} = 0$; gli induttori si comprano come cortocircuiti, $v = L \frac{d i}{d t} = 0$.

(physics-hs:electromagnetism:circuits-electric:regimes:dt)=
### Transitorio

Tipici problemi di transitorio tra due condizioni stazionarie sono le dinamiche di carica/scarica di un condensatore in seguito alla chiusura/apertura di un interruttore.

**Circuito RLC.** **todo**

(physics-hs:electromagnetism:circuits-electric:regimes:ac)=
### Regime periodico - la corrente alternata

Il regime periodico armonico è caratteristico del funzionamento dei circuiti elettr(omagnetici) in corrente alternata, che abbiamo in molti reti elettriche contemporanee, dalla produzione (tramite generatori), alla trasformazione ad alta tensione per un trasporto efficiente su grandi distanze, l trasporto (anche se si sta diffondendo un nuovo tipo di trasporto in corrente continua ad alta tensione, *HVDC*), alla trasformazione a media e poi bassa tensione per la distribuzione e l'utilizzo.

Utilizzando il formalismo dei **fasori** per rappresentare grandezze periodiche armoniche a frequenza costante $f = \frac{\Omega}{2 \pi}$, si può scrivere

$$v(t) = V e^{-i \Omega t} \ ,$$

con $V \in \mathbb{C}$. **todo** 

**Analisi circuiti.**

**Analisi potenza.**


(physics-hs:electromagnetism:circuits-electric:regimes:ac-tri)=
#### Sistemi trifase
Vantaggi:
- funzionamento generatori ed utilizzatori naturale
- trasformazione in AC naturale
- trasmissione efficiente

- dalle leggi fisiche alle leggi di Kirchhoff, ipotesi (validità e non-validità dell'approccio circuitale)

- componenti:
  - resistenze
  - condensatori
  - induttori
  - generatori

- regimi di funzionamento: in DC, (trascurando gli effetti EM: no campi magnetici esterni, *ogni circuito è una spira*...), e in AC
  - stazionario
    - bilancio di energia: "generatori" di energia elettrica, "perdite" nelle resistenze
      - approfondimenti:
      - pile <span style="color:red"> Collegamento ad altre parti: termodinamica? chimica?</span>
  - transitorio:
    - esempio: carica/scarica condensatore
  - armonico, AC:
    - ... 
