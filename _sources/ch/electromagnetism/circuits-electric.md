(physics-hs:electromagnetism:circuits-electric)=
# Circuiti elettrici

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

(physics-hs:electromagnetism:circuits-electric:components)=
## Componenti

(physics-hs:electromagnetism:circuits-electric:components:resistor)=
### Resistenza elettrica
La legge costitutiva della resistenza elettrica è

$$v = R i$$

(physics-hs:electromagnetism:circuits-electric:components:capacitor)=
### Condensatore
La legge costitutiva di un condensatore è

$$i = C \dot{v}$$

(physics-hs:electromagnetism:circuits-electric:components:inductor)=
### Induttore
La legge costitutiva di un induttore è

$$v = L \dot{i}$$

(physics-hs:electromagnetism:circuits-electric:components:generator-v)=
### Generatore di tensione

$$v = e$$

(physics-hs:electromagnetism:circuits-electric:components:generator-i)=
### Generatore di corrente

$$i = a$$


## Regimi di funzionamento
### Regime stazionario

### Transitori

### Regime periodico

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
