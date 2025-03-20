(physics-hs:waves:optics:geometric:lenses)=
# Lenti e strumenti ottici

- Lenti sottili sferiche:
  - caratteristiche
  - tipi: conv
  
- Strumenti ottici e caratteristiche:
  - distanza focale
  - ingrandimento
  - messa a fuoco
  - apertura - diaframma
  - tempi di esposizione - otturatore
  - profondità di campo
  
- Problemi:
  - aberrazione
  - ...
  
- L'occhio umano

(physics-hs:waves:optics:geometric:lenses:thin)=
## Lenti sottili

(physics-hs:waves:optics:geometric:lenses:equation)=
### Equazione delle lenti sottili sferiche

Raggi paralleli incidenti su una lente sferica covessa sottile convergono in un unico punto sull'asse della lente, chiamato **fuoco della lente**, a una distanza $f$ dalla lente, chiamata **lunghezza focale**. Per una lente sottile esiste una relazione tra i raggi di curvatura $R_1$, $R_2$ delle superficie della lente, gli indifici di rifrazione del mezzo $n_1$ e della lente $n_L$ e la lunghezza focale $f$,

$$\frac{1}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{1}{R_1} + \frac{1}{R_2} \right) \ .$$

```{list-table}
:header-rows: 0
* - ![](../../media/lenses-geometry-small.png)
```


```{dropdown} Dimostrazione

Nel limite degli angoli piccoli da poter ritenedere buona l'approssimazione $\theta \sim \sin \theta \sim \tan \theta$, gli angoli dei versori normali alle lenti nei punti per i quali passa il raggio luminoso, a distanza $h$ dall'asse della lente sono

$$\phi_1 \sim \frac{h}{R_1} \qquad , \qquad \phi_2 \sim \frac{h}{R_2} \ .$$

Nel limite di piccoli angoli, gli angoli formati dai raggi luminosi entrante $\xi_1$ e uscente $\xi_2$ con l'asse della lente sono

 $$\xi_1 = \frac{h_o - h}{d_0} \qquad , \qquad \xi_2 = \frac{h_i + h}{d_i} \ , $$ (eq:lens:angles:approx)

Siano $\theta_1$, $\theta_{L1}$ gli angoli rispetto alla normale della superficie del raggio incidente entrante nella lente e trasmesso nella lente, $\theta_{L2}$, $\theta_2$ gli angoli rispetto alla normale locale rel raggio uscente dalla lente.

L'applicazione della [legge di Snell](physics-hs:waves:optics:geometric:phenomena:snell) fornisce le relazioni

  $$\begin{aligned}
    \frac{n_L}{n_1} & = \frac{\sin \theta_1}{\sin \theta_{L1}} \qquad , \qquad
    \frac{n_L}{n_1} & = \frac{\sin \theta_2}{\sin \theta_{L2}} 
  \end{aligned}$$

mentre la geometria del problema

$$\begin{aligned}
  \theta_1    & = \phi_1 - \xi_1 \\
  \xi_2       & = \theta_2 - \phi_2 \\
  \theta_{2L} & = \phi_2 + \xi_{1L} = \phi_2 + \phi_1 - \theta_{1L} 
\end{aligned}$$

Quindi segue la relazione tra l'angolo $\xi_2$ del raggio luminoso trasmesso dalla lente e l'angolo $\xi_1$ incidente sulla lente,

$$\begin{aligned}
  \xi_2
  & = \theta_2 - \phi_2 = \frac{n_L}{n_1} \theta_{L2} - \phi_2 = \\
  & = \frac{n_L}{n_1} \left( \phi_2 + \phi_1 - \frac{n_1}{n_L} \theta_1 \right) - \phi_2 = \\
  & = \frac{n_L}{n_1} \left( \phi_2 + \phi_1 - \frac{n_1}{n_L} \left( \phi_1 - \xi_1 \right) \right) - \phi_2 = \\
\end{aligned}$$
  
$$
  \xi_2 = \left( \frac{n_L}{n_1} - 1 \right) \left( \phi_2 + \phi_1 \right) + \xi_1 
$$ (eq:lens:angles:relation)

**Lunghezza focale.** La lunghezza focale si ottiene per raggi incidenti paralleli $\xi_1 = 0$, $h_0 = h$. Il fuoco della lente si trova sull'asse, e quindi $h^*_i = 0$. La distanza del fuoco dalla lente è definita **lunghezza focale**, $d^*_i = f$. Utilizzando l'approssimazione per piccoli angoli, $\xi_2 = \frac{h}{f}$, e quindi

$$\frac{h}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{h}{R_2} + \frac{h}{R_1} \right) \ ,$$

ed è quindi valida per ogni valore di $h$ e quindi per ogni raggio parallelo l'equazione delle lenti sottili

$$\frac{1}{f} = \left( \frac{n_L}{n_1} - 1 \right) \left( \frac{1}{R_1} + \frac{1}{R_2} \right) \ .$$

```

(physics-hs:waves:optics:geometric:lenses:image-focus)=
### Formazione dell'immagine

Dato un **piano dell'oggetto** $\pi_o$ a distanza $d_o$ dalla lente, i raggi luminosi provenienti da ogni punto $P_o$ del piano $\pi_o$ passanti per la lente sottile convergono in un unico punto $P_i$ di un piano $\pi_i$, detto **piano dell'immagine**, a distanza $d_i$ dalla lente con

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \ .$$

Questa condizione è la condizione di **messa a fuoco**, e comporta un rapporto di magnificazione dell'immagine

$$\frac{h_i}{h_o} = \frac{d_i}{d_o} \ ,$$

dove $h_o$, $h_i$ sono le distanze dall'asse della lente nel piano dell'oggetto e dell'immagine.

<!--
- Piano dell'immagine e **messa a fuoco**.
  - Dimostrazione che tutti i raggi luminosi provenienti da un punto convergono in un unico punto nel piano di formazione dell'immagine - messa a fuoco.
  - Mancata messa a fuoco
-->

```{list-table}
:header-rows: 0
* - ![](../../media/lenses-image-1ray.png)
* - ![](../../media/lenses-image-3rays.png)
```

```{dropdown} Piano dell'immagine

Esiste un piano, il piano di formazione dell'immagine, dove tutti i raggi provenienti da ogni punto di un piano, il piano dell'oggetto, convergono a un punto. In questo piano, l'immagine è a fuoco. Introducendo le approssimazioni {eq}`eq:lens:angles:approx` nella relazione {eq}`eq:lens:angles:relation` tra gli angoli dei raggi incidente e trasmesso dalla lente, si ottiene la relazione

$$\frac{h_i + h}{d_i} = \left(\frac{n_L}{n_1} - 1 \right)\left(\frac{h}{R_1}+\frac{h}{R_2}\right) + \frac{h_o - h}{d_o} \ ,$$

$$\frac{h_i}{d_i} = \frac{h}{f} + \frac{h_o}{d_o} - h \left( \frac{1}{d_o} + \frac{1}{d_i} \right) = \frac{h_o}{d_o} + h \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right)\ .$$

Esprimendo la distanza $h$ in funzione dell'angolo del raggio incidente $\xi_1$,

 $$h = h_o - d_o \, \xi_1 \ ,$$

si ottiene una relazione tra la distanze dall'asse dei punti dell'oggetto $h_o$ e dell'immagine formata $h_i$, la distanza dalla lente dell'oggetto e del piano di formazione dell'immagine $d_o$, $d_i$, della lunghezza focale e dell'angolo $\xi_1$ dei raggi incidenti passanti per la lente dei raggi incidenti passanti per la lente,,

$$\begin{aligned}
  \frac{h_i}{d_i}
  & = h_o \left( \frac{1}{d_o} + \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) - \xi_1 d_o \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \\
  & = h_o \left( \frac{1}{f} - \frac{1}{d_i} \right) - \xi_1 d_o \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \\
\end{aligned}$$

e quindi esprimere $h_i$ come funzione degli altri parametri

$$h_i(\xi_1; f; d_o, d_i, h_o) = h_o \left( \frac{d_i}{f} - 1 \right) - \xi_1 d_o d_i \left( \frac{1}{f} - \frac{1}{d_o} - \frac{1}{d_i} \right) \ .$$

In generale, i raggi provenienti da un oggetto arrivano in punti differenti su un piano generico a distanza $d_i$ dalla lente, poiché la distanza $h_i$ dipende dall'angolo $\xi_i$, tenendo costanti gli altri parametri.

Nel caso in cui $h_i$ non dipende da $x_i$, tutti i raggi provenienti dallo stesso punto dell'oggetto convergono nello stesso punto del piano. Questa è la condizione di **messa a fuoco**, e definisce la relazione tra lunghezza focale, distanza dell'oggetto e distanza del piano di formazione dell'immagine,

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i} \ .$$

```

```{dropdown} Magnificazione

Nelle condizioni di messa a fuoco, si può quindi scrivere

$$h_i = h_o \left( \frac{d_i}{f} - 1 \right) = d_i \frac{h_o}{d_o} \ ,$$

o in termini della magnificazione

 $$\frac{h_i}{h_o} = \frac{d_i}{d_o} \ .$$

```

```{list-table}
:header-rows: 0
* - ![](../../media/lenses-image-focus.png)
* - ![](../../media/lenses-image-focus-out-1.png)
* - ![](../../media/lenses-image-focus-out-2.png)
```

## Lenti sempici
Per lenti sottili semplici a geometria costante, e quindi lunghezza focale costante $f$, la distanza $d_i$ del piano dell'immagine dalla lente è determinata una volta nota la distanza dell'oggetto $d_o$ che si vuole mettere a fuoco. Risulta quindi determinato anche il coefficiente di magnificazione dell'immagine.

<span style="color:red">**todo** Riogranizzare le sezioni</span>


**Caratteristiche obiettivi.** La *lunghezza focale* di un obiettivo rappresenta la *distanza focale* più corta che si più ottenere con l'obiettivo mantenendo l'immagine a fuoco, o con la messa a fuoco all'infinito. Equiparando l'obiettivo a una lente sottile **todo**

**Diaframma e otturatore.** Nelle macchine fotografiche:
- il diagramma regola l'**apertura** e di conseguenza l'**intensità luminosa** ("la quantità di luce" per unità di tempo) che entra nell'obiettivo e va a formare l'immagine
- l'otturatore regola il **tempo di esposizione** del sensore alla luce. Solo durante questo intervallo di tempo il sensore riceve la luce esterna, che oggi va a caricare elettricamente la matrice del sensore digitale, e una volta andava a impressionare la pellicola

Il prodotto di intensità luminosa e tempo di esposizione viene definita **esposizione**,

$$ \text{esposizione} = \text{apertura} \times \text{tempi} \ .$$

Così ad esempio:
- un'esposizione troppo bassa non sarà in grado di impressionare "a sufficienza" il sensore e la foto risulterà quindi buia
- un'esposizione troppo alta impressionerà il sensore più del dovuto, e la foto risulterà quindi artificialmente troppo luminosa. Al limite, un'esposizione eccessiva porta alla saturazione del sensore, che produrrà quindi una foto completamente bianca, o "bruciata".

<span style="color:red">**todo** Aggiungere immagine diaframma</span>

**Profondità di campo.** La profondità di campo può essere definito come l'intervallo di distanza tra una distanza minima e la distanza massima nei quali gli oggetti risultano a fuoco. La profondità di campo dipende principalmente da 3 fattori:
1. l'apertura
2. la distanza dal soggetto
3. la distanza focale della lente

All'aumentare dell'apertura, al diminuire della distanza dal soggetto, e all'aumentare della distanza focale diminuisce la profondità di campo.

<span style="color:red">**todo** Aggiungere immagini</span>

**Tipi di obiettivo.**
- fisheye: $7-16 \, mm$
- grandangolare: $10-42 \, mm$
- standard: $50-85-100 \, mm$
- teleobiettivo: $100-800 \, mm$

**Lunghezza focale e angolo di campo.** All'aumentare della lunghezza focale si riduce l'angolo di campo.

**Effetto sulle proporzioni di oggetti a distanza diversa: angolo di campo, dimensioni relative e prospettiva.** Lunghezze focali piccole rendono oggetti a distanza diversa di dimensione molto diversa (dovuto ad angolo di campo maggiore, e distanze minori dal soggetto principale)

```{prf:example} Lente di ingrandimento
:class: dropdown
:label: magnifying-lens

Esprimiamo le distanze $d_o$ e $d_i$ come multipli della lunghezza focale della lente, $d_o = f D_o$, $d_i = f D_i$  per ottenere così un'[adimensionalizzazione](physics-hs:todo:non-dimensional) dell'equazione del paino dell'immagine

$$1 = \frac{1}{D_o} + \frac{1}{D_i} \ .$$

Data la distanza dell'oggetto, il piano dell'immagine si trova quindi a 


```

```{prf:example} Confronto tra obiettivi (di lenti semplici)
:class: dropdown
:label: lenses-simple

Vengono usati due obiettivi formati da una lente semplice sottile[^real-lenses] con lunghezza focale $f_1 = 50 \, mm$ e $f_2 = 200 \, mm$ per fare 4 foto mettendo a fuoco a distanza $d_o$

$$d_o \in \left\{ 10 \, cm, \, 30 \, cm, \, 1 \, m, 3 \, m, \, 5 \, m, \, 10 \, m \right\}.$$

Si determinano le distanze del piano dell'immagine per ottenere una messa a fuoco e il coefficiente di magnificazione. Per l'obiettivo con lunghezza focale $f_1 = 50 \, mm$

| $d_o$                   | $d_i$          | $m = d_i/d_o$    |
| :---------------------: | :------------: | :--------------: |
| $10 \, cm$              | $0.1000 \, m$  | $1.0000$         |
| $30 \, cm$              | $0.0600 \, m$  | $0.2000$         |
| $1 \, m$                | $0.0526 \, m$  | $0.0580$         |
| $3 \, m$                | $0.0508 \, m$  | $0.0169$         |
| $5 \, m$                | $0.0505 \, m$  | $0.0101$         |
| $10\, m$                | $0.0503 \, m$  | $0.0050$         |

mentre per il teleobiettivo con lunghezza focale $f_2 = 200 \, mm$

| $d_o$                   | $d_i$          | $m = d_i/d_o$    |
| :---------------------: | :------------: | :--------------: |
| $10 \, cm$              | $-0.2000 \, m$ | $-2.000$         |
| $30 \, cm$              |  $0.6000 \, m$ | $2.0000$         |
| $1 \, m$                |  $0.2500 \, m$ | $0.2500$         |
| $3 \, m$                |  $0.2143 \, m$ | $0.0714$         |
| $5 \, m$                |  $0.2083 \, m$ | $0.0417$         |
| $10\, m$                |  $0.2041 \, m$ | $0.0204$         |

Alcune osservazioni:
- la distanza $d_i$ negativa per lente con lunthezza focale $f_2 = 200 \, mm$ e oggetto distante $d_o = 10 \, cm$ dovrebbe far pensare che non sono rispettati i limiti del modello, o che si incontrano limiti tecnologici nella realizzazione della messa a fuoco di un oggetto troppo vicino per un teleobiettivo. La distanza minima di messa a fuoco di teleobiettivi - come di altri obiettivi - nelle applicazioni pratiche viene fornita sulle schede tecniche dell'obiettivo; anche la distanza dipende dal particolare obiettivo, si può pensare una distanza minima di messa a fuoco dell'ordine di $1.5 - 2 \, m$ per i $200 \, mm$, come reperibile per un obiettivo Canon[^canon-200mm];
- altri limiti tecnici per strumenti con una lente semplice derivano dalla distanza $d_i$ necessaria alla messa a fuoco; gli obiettivi reali hanno più lenti per trattatare alcuni problemi che si avrebbero con una lente singola (aberrazione cromatica), e possono essere progettati per rendere l'obiettivo più compatto rispetto a quanto sarebbe richiesto dalla distanza $d_i$ di una lente singola. Così, ad esempio un obiettivo Nikon con lunghezza focale $800 \, mm$ ha una lunghezza di circa $385\, mm$[^nikon-800mm]; i teleobiettivi rimangono comunque degli strumenti ingombranti ($140 \, mm$ di diametro), pesanti ($2.4 \, kg$), costosi $2000$€ (2025), e quindi principalmente riservati a professionisti.
- il fattore di magnificazione è determinato dalla distanza dell'oggetto $d_o$, non è possibile compiere un ingrandimento. In seguito, nell'esempio {prf:ref}`zoom` viene discusso un semplice meccanismo che permette l'ingrandimento dell'immagine (e quindi la riduzione dell'angolo di campo).



  
[^real-lenses]: Gli obiettivi usati nelle applicazioni reali sono formati da un gran numero di lenti, tutt'altro che sottili, ma qui possiamo provare a fare qualche esercizio. Dai risultati dell'esercizio, anche se ottenuti con l'approssimazione di lenti sottili, dovrebbero essere chiari alcuni limiti pratici nella realizzazione di obiettivi con lenti semplici: 

[^canon-200mm]: [Scheda tecnica di un obiettivo Canon $200 \, mm$](https://www.canon.it/lenses/ef-200mm-f-2-8l-ii-usm-lens/specification.html).

[^nikon-800mm]: {scheda tecnica di un obiettivo Nikon $800 \, mm$](https://www.nikon.it/it_IT/product/lenses/mirrorless/nikkor-z-800mm-f62.3-vr-s)

```

## Lenti

```{prf:example} Messa a fuoco
```

```{prf:example} Auto-focus

- Per convoluzione
- Per contrasto
```

```{prf:example} Zoom
:class: dropdown
:label: zoom

L'esempio {prf:ref}`lenses-simple` sulle lenti semplici ha mostrato come il rapporto di magnificazione, e quindi l'ingrandimento, in quei sistemi sia determinato dalla distanza dell'oggetto.

Zoom: sistema afocale (modifica l'ingrandimento angolare) + lente focale (si occupa della generazione dell'immagine)

```

## Lenti spesse
[Lenti spesse, wikipedia](https://it.wikipedia.org/wiki/Lente_spessa)
