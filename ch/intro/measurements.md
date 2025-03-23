(physics-hs:intro:measurements)=
# Misura

L'attività di misurazione consiste nell'assegnazione di un valore - o meglio di un intervallo di valori che tenga conto dell' - alla grandezza fisica oggetto dell'operazione, confrontata con una [grandezza fisica omogenea](physics-hs:intro:measurements:homogeneous) di riferimento, chiamata unità di misura.

Una grandezza fisica può quindi essere espressa come il prodotto di un valore numerico $\{ M \}$ e un'unità di misura $[M]$,

$$M = \{ M \} [ M ] \ .$$

(physics-hs:intro:measurements:homogeneous)=
```{prf:definition} Grandezze fisiche omogenee
:label: def-dimensions-homonegneous

Due **grandezze fisiche omogenee** sono grandezze fisiche della stessa natura, che - in maniera equivalente:
- possono essere riferite alla stessa unità di misura
- possono essere confrontate con un rapporto che restituisce un valore numerico - privo di dimensioni fisiche
- hanno le stesse dimensioni fisiche.
```

(physics-hs:intro:measurements:unit-system)=
## Sistema di misura
...
### Sistema internazionale di misura
... qui o nella sezione sulle [grandezze fisiche](physics-hs:intro:physical-quantities)?

(physics-hs:intro:measurements:instruments)=
## Strumenti di misura

(physics-hs:intro:measurements:instruments:characteristics)=
### Caratteristiche della misura

(physics-hs:intro:measurements:instruments:characteristics:accuracy)=
#### Accuratezza e precisione
**Accuratezza.** E' una misura della differenza tra il valoremedio di una serie di misure e il *valore vero* della grandezza misurata.

:::{admonition} Valore vero

**todo**
:::

**Precisione.** Dispersione delle misure, indipendentemente dall'accuratezza della misura, quantificabile con la varianza, la deviazione standard o altri indicatori di dispersione delle misure.

**Ripetibilità e riproducibilità.** I concetti di ripetibilità e riproducibilità sono indicatori di *precisione* che quantificano l'accordo tra una serie di misure della stessa grandezze fisica.

Il termine ripetibilità si riferisce a misurazioni svolte nelle stesse condizioni (metodo, operatore, strumento di misura, luogo dell'esperimento), il concetto di riproducibilità si riferisce a misurazioni in cui viene modificata almeno una delle condizioni.

Esempi di errori di repricabilità sono: variazioni proprie della grandezza misurata, errori di lettura, disturbi sui sistemi di misura (interferenza elettromagnetica, vibrazioni, variazioni nelle condizioni ambientali,...).

Errori di riproducibilità possono evidenziare errori sistematici nel processo di misura, come ad esempio: errore nell'impostazione, posizione e/o orientamento, alimentazione dello strumento, oltre a metodologie inadeguate o comportamenti fraudolenti da parte degli autori dell'attività.

:::{admonition} Crisi di riproducibilità
<!--:class: tip -->

**todo**

:::

#### Fondo scala, risoluzione, linearità, sensibilità, rumore
**Fondo scala.**

**Risoluzione.**

**Linearità.**

**Sensibilità.** 

(physics-hs:intro:measurements:order)=
#### Risposta degli strumenti - ordine 0, 1, 2,$\dots$
Un trasduttore è uno strumento che legge una grandezza in ingresso $u(t)$ e ne produce un'altra in uscita, $y(t)$. La grandezza in uscita, tipicamente una grandezza elettrica per molti strumenti, è quella che viene effettivamente letta. La procedura di **taratura** di uno strumento permette di associare alla lettura della grandezza letta in uscita $y(t)$ il valore della variabile che si desidera misurare $u(t)$.

**Risposta degli strumenti.** (strumenti di ordine $0$, $1$, $2$) Gli strumenti di ordine 0 forniscono una relazione algebrica tra la grandezza in ingresso e la grandezza in uscita, $y(t) = c \, u(t)$. Altri strumenti hanno una dinamica interna, e la relazione tra la grandezza in uscita e la grandezza in ingresso non è algebrico, ma dinamico. In generale, questi strumenti sono caratterizzati da una funzione di trasferimento, cioè di un legame tra ingresso e uscita che è funzione della frequenza del segnale in ingresso: la frequenza massima - o l'intervallo di frequenze - del segnale che uno strumento è in grado di misurare accuratamente è una caratteristica dello strumento. Questa caratteristica è chiamata **banda passante**.

Il termine passante è riferito al fatto che un sistema dinamico definisce una relazione tra il segnale in ingresso e in uscita, e questo legame dipende di solito dalla frequenza del segnale in ingresso. 

- **todo-list** [**Fourier**](physics-hs:todo:fourier)
- [Materiale di matematica per le scuole superiori](https://basics2022.github.io/bbooks-math-miscellanea-hs/intro.html):
  - capitolo sulle [equazioni ordinarie differenziali (ODE)](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/ode.html)
    - sezione sulle ODE lineari e sulla [risposta in frequenza](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/ode-lti.html#risposta-in-frequenza-di-sistemi-del-primo-e-del-secondo-ordine) a forzanti armoniche e ad altre forzanti caratteristiche

```{exercise} Strumento di ordine zero
:label: instrument-order-zero-exercise
**todo**
```
```{exercise} Strumento del primo ordine - esempio termometro
:label: instrument-order-one-exercise
**todo**
```
```{exercise} Strumento del secondo ordine - esempio accelerometro
:label: instrument-order-two-exercise
**todo**

Per un esempio più dettagliato, quando si avranno le competenze sufficienti, si rimanda alla sezione sull'[accelerometro capacitivo MEMS](instrumentation:list:accelerometer:mems)
```

(physics-hs:intro:measurements:instruments:intrusivity)=
### Intrusività
L'intrusività di una misura può essere definita come l'entità della modifica del processo sotto indagine introdotta dalla strumentazione necessaria alla misura delle grandezze di interesse.

L'intrusività di alcuni strumenti verrà indagata durante il corso. Viene fatto qui un elenco degli strumenti di cui verrà discussa l'intrusività nel sistema:
- meccanica:
- termodinamica:
- elettromagnetismo:
  - [amperometro](physics-hs:electromagnetism:electromagnetism-steady:experience-faraday:amperometer)
  - [voltmetro](physics-hs:electromagnetism:electromagnetism-steady:experience-faraday:voltmeter)


