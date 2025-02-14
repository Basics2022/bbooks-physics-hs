(physics-hs:intro:physical-quantities)=
# Grandezze fisiche

Una grandezza fisica è una proprietà di un sistema o di un fenomeno fisico che può essere [misurata](physics-hs:intro:measurements) e il cui valore può essere espresso in relazione a un'unità di misura omogenea.


Un **sistema di misura** è formato da un insieme di unità di misura *fondamentali* associate a grandezze fisiche, dalle quali è possibile ricavare le unità di misura *derivate* per tutte le altre grandezze fisiche.

Il **sistema internazionale** di unità di misura (SI) usa sette **grandezze fisiche fondamentali**.

| Grandezza fisica             | Simbolo dimensionale | Unità di misura       | Simbolo |
| :--------------------------- | :------------------: | :-------------------- | :-----: |
| lunghezza                    | $[L]$                | metro                 | $m$     |
| intervallo di tempo          | $[T]$                | secondo               | $s$     |
| massa                        | $[M]$                | chilogrammo           | $kg$    |
| temperatura                  | $[\Theta]$           | Kelvin                | $K$     |
| quantità di sostanza         | $[N]$                | mole                  | $mol$   |
| intensità di corrente        | $[I]$                | Ampére                | $A$     |
| intensità luminosa           | $[J]$                | candela               | $cd$    |

- Nello studio della [meccanica classica](physics-hs:mechanics:intro) sono sufficienti le unità di misura di [**lunghezza**](physics-hs:intro:physical-quantities:space), [**tempo**](physics-hs:intro:physical-quantities:time) e [**massa**](physics-hs:intro:physical-quantities:mass).
- Nello studio della [termodinamica classica](physics-hs:thermodynamics:intro) vengono introdotte le unità di misura di [**temperatura**](physics-hs:intro:physical-quantities:temperature) e [**quantità di sostanza**](physics-hs:intro:physical-quantities:mole). Entrambe sono riconducibili a una descrizione microscopica atomistica della materia: l'unità di misura della sostanza rappresenta il numero di molecole - componenti elementari discreti - presenti in un determinato volume, in determinate condizioni termodinamiche del sistema; la temperatura rappresenta una misura macroscopica - mediata - dell'agitazione molecolare (dell'energia) dei componenti elementari della materia.
- Nello studio dell'[elettromagnetismo classico](physics-hs:electromagnetism:intro) viene introdotta l'unità di misura della corrente elettrica.

 Infine, l'[**intensità luminosa**](physics-hs:intro:physical-quantities:luminosity) è un'unità di misura "strana", considerabile non necessaria: mentre tutte le altre unità di misura cercano di essere indipedenti dalla [percezione umana](physics-hs:intro:sensing), l'intensità luminosa rappresenta la **percezione dell'occhio umano** medio di quella parte di radiazione elettromagnetica che comunemente chiamiamo luce. L'intensità luminosa non è altro che la potenza (quantità fisica derivata) della radiazione elettromagnetica (con dimensioni fisiche derivabili dalle prime sei unità di misura fondamentali) "scalata" dalla percezione umana.

Un'introduzione alle singole grandezze fisiche verrà presentata nelle prossime sezioni.

**Multipli e sottomultipli.** A parte rare eccezioni[^multiples-exceptions], è comune usare multipli e sottomultipli delle unità di misura che siano potenze intere con base $10$. A parte il "residuo storico" del "chilo" nell'unità di misura della massa (il sistema CGS usava il grammo come unità di misura), non compaiono prefissi nelle unità di misura. I prefissi associati ai multipli e sottomultipli di una grandezza sono


| Prefisso                     | Simbolo              | Multiplo              |
| :--------------------------- | :------------------: | :-------------------- |
| Peta                         | $P$                  | $10^{15} $            |
| Tera                         | $T$                  | $10^{12} $            |
| Giga                         | $G$                  | $10^{9}  $            |
| Mega                         | $M$                  | $10^{6}  $            |
| Chilo                        | $k$                  | $10^{3}  $            |
| Etto                         | $h$                  | $10^{2}  $            |
| Deca                         | $da$                 | $10^{1}  $            |
| -                            |                      | $10^{0}  $            |
| Deci                         | $d$                  | $10^{-1} $            |
| Centi                        | $c$                  | $10^{-2} $            |
| Milli                        | $m$                  | $10^{-3} $            |
| Micro                        | $\mu$                | $10^{-6} $            |
| Nano                         | $n$                  | $10^{-9} $            |
| Pico                         | $p$                  | $10^{-12}$            |
| Femto                        | $f$                  | $10^{-15}$            |


[^multiples-exceptions]: Come esempio, è comune usare sottomultipli in base $10$ del secondo (nelle gare sportive è comune misurare i tempi fino al centesimo o al millesimo di secondo; per la misura di impulsi molto brevi si usano i micro $10^{-6}$, i nano $10^{-9}$, i pico $10^{-12}$, i femto $10^{-15}$ -secondi), per i multipli nella vita quotidiana si è soliti le potenze in base $60$ - o dei residui di sistemi con base $12$ - del secondo (minuto $60 \, s$, ora $60 \, min = 60^2 \, s$, giorno $24 \, h = 24 \cdot 60 \cdot 60 \, s$)

**Altri sistemi di misura.** 
- Sistema **CGS** (centimetro-grammo-secondo): proposto da Gauss nel 1832 (**todo** *ref*), con tre unità di misura fondamentali per lunghezza, tempo e massa. 

    | Grandezza fisica             | Unità di misura       | Simbolo |
    | :--------------------------- | :-------------------- | :-----: |
    | lunghezza                    | centimetro            | $cm$    |
    | intervallo di tempo          | secondo               | $s$     |
    | massa                        | grammo                | $g$     |

    All'epoca della proposta, esistevano diverse [scale di temperatura](physics-hs:thermodynamics:foundation:experiments:t-scales) empiriche, non esisteva ancora una mcomprensione matura della termodinamica, si intuiva la natura atomica della materia ma esistevano ancora modelli consistenti (confusione tra i chimici dopo gli studi di Dalton che venne risolta con Avogadro e Canizzaro vero il 1860), e gli studi sull'elettromagnetismo non avevano ancora prodotto il modello consistente rappresentato dalle equazioni di Maxwell. 
    
    Nel 1874, al sistema CGS originario furono aggiunte le unità di misura della temperatura e delle grandezze elettromagnetiche da parte di Kelvin e Maxwell, dopo la proposta da parte di Kelvin di una scala termodinamica di temperatura[^kelvin-1848] e la formulazione di un modello completo dell'elettromagnetismo classico da parte di Maxwell[^maxwell-1865].

[^kelvin-1848]: W.Thomson (1848), *"On an Absolute Thermometric Scale"*
[^maxwell-1865]: J.C.Maxwell (1865), *"A dynamical theory of  the electromagnetic field"*

- Sistema **MKS** (metro-chilogrammo-secondo): 

- Sistema **imperiale** sistema adottato nell'impero britannico a partire dal 1824 per legge, e rimasto in uso per legge fino al 1965. Una volta capita la logica lineare alla base della costruzione del SI di misura, questo sistema di misura sembra figlio di un demonio particolarmente ingegnoso, da concepire una scala di multipli e sottomultipli irregolare. Alcuni suoi residui rimangono di uso comune nel mondo anglosassone, e in alcuni settori. Tra gli stati nazionali si distinguono gli Stati Uniti e la Liberia, da loro creata, per la resistenza nell'uso della scala Fahrenheit di temperatura, scala arbitraria di temperatura con origine e ampiezza del grado differente dalla scala termodinamica Kelvin o dalla scala Celsius in uso in tutto il resto del mondo; tra i settori industriali, rimangono tracce o più che tracce nell'ambito dei trasporti e nel settore aeronautico: in questo ambito particolare, la costruzione delle grandezze derivate partorisce unità di misura che possono essere solo figlie del demonio originario che ha partorito questo sistema. Senza dilungarci oltre: in questo materiale non si farà mai uso del sistema imperiale; qui ci siamo fatti due risate, utili a ricordarci la semplicità del SI e di non usare mai il sistema imperiale se non costretti. Per chi volesse approfondire, può partire dal [collegamento alla pagina di Wikipedia in italiano](https://it.wikipedia.org/wiki/Sistema_imperiale_britannico).



<!--
(physics-hs:intro:physical-quantities:system)=
## Sistema di misura

- grandezze fondamentali e derivate
- unità di misura

(physics-hs:intro:physical-quantities:system:is)=
### Sistema di misura internazionale
-->

**Brevissima storia.** Della costruzione del moderno sistema di misura.
-  Inizialmente unità di misura convenzionali, facilmente riconducibili all'esperienza quotidiana degli esseri umani ai tempi in cui le unità vengono definite. Nuove unità di misura fondamentali vengono introdotte quando quelle già definite non sono sufficienti a rappresentare nuove grandezze fisiche.
- Successivamente[^si-history] unità di misura riconducibili a grandezze fisiche facilmente replicabili in maniera stabile in laboratorio.
-  Recentemente, dopo la scoperta di alcune grandezze costanti in natura, le unità di misura "classiche" sono state ri-definite in termini di queste costanti della natura mantenendo il loro valore originale.[^new-def-si]



[^new-def-si]: Il valore delle unità di misura classiche è stato mantenuto seguendo un criterio di **comodità**: la comodità di 1) non ridefinire tutto con una serie di conversioni e la comodità di 2) evitare l'utilizzo di unità di misura di dimesioni molto diverse rispetto alle grandezze che caratterizzano l'esperienza quotidiana, e quindi l'uso di valori numerici caratterizzati da potenze enormi o molto piccole. Ad esempio, una volta notato che la velocità della luce sembra essere una costante della natura, potrebbe sembrare naturale scegliere la velocità della luce o qualche suo sottomultiplo. Usando le unità di misura del sistema fondamentale, la velocità della luce è di circa $c = 299792458 \, m/s \approx 3 \cdot 10^{8} \, m/s$. Definendo $c$ come nuovaunità di misura della velocità, dovremmo esprimere un limite di velocità di $v = 100 \, km/h = 27.28 \, m/s = 9.27 \cdot 10^{-8} \, c$: non proprio il massimo, se non ci si fa prima l'abitudine - e probaiblmente nemmeno dopo! Potremmo definire l'unità di misura per la velocità come $10^{-8} \, c$ per non dover trattare la potenza nel valore numerico delle velocità di tutti i giorni. Oppure potremmo continuare a fare quello che facciamo: abbiamo ben presente quanto sono un metro o un chilometro, e quanto sono un secondo o un'ora, e possiamo continuare a usare i $m/s$ o $km/h$ come unità di misura derivate dal rapporto di una misura di lunghezza e una di tempo, immaginandoci la velocità come distanza percorsa in un intervallo di tempo (quantificate in unità di misura intelligibili per l'esperienza nella nostra vita quotidiana).

[^si-history]: Storia della creazione dei principali sistemi di misura **todo** *link? Scrivere due parole?*

<!--
**Massa, lunghezza e tempo.**

**Temperatura.**

**Quantità di sostanza.**

**Carica elettrica.**

**Intensità luminosa.**
-->


<!--
- Come conosciamo il mondo? Come misuriamo il mondo?
- Necessità di avere delle grandezze di riferimento stabili o facilmente riproducibili in maniera precisa, da usare come unità di misura delle grandezze fisiche.
- Nell'antichità, dall'esperienza:
  - spazio:
    - importanza di misurare le distanze (es. distanze da percorrere), le aree (es. misura dei campi,...), e i volumi
    - grandezze di riferimento: lunghezze ideali di parti anatomiche umane: cubito, pollice, piede,...
  - tempo: 
    - alternanza di luce e buio, alternanza delle stagioni, alternanza di configurazioni degli astri osservati dalla terra; queste alternanze scandiscono
    - grandezze di riferimento: intervalli temporali scanditi dalla natura
  - peso:
    - misura della quantità di merce, quantità di denaro o materiali preziosi, per le prescrizioni mediche (apothecary,...)
    - grandezze di riferimento: grano (basato su un seme ideale di cereale), libbra (dallo strumento usato per la misura del peso/massa, *libra* = bilancia)
- In epoca moderna:
  - aggiornamento delle grandezze di riferimento
    - Parigi tra fine XVIII e XIX secolo:
      - lunghezza: metro (1791) come $1/10.000.000$ la distanza tra l'equatore e il polo nord sul meridiano terrestre passante per Parigi
      - tempo: **todo**
      - **todo**
  - nuove grandezze fisiche misurate nelle nuove scienze, chimica, termodinamica ed elettromagnetismo:
    - quantità di sostanza
    - temperatura
    - corrente elettrica
    - luminosità
- XX-XXI secolo: continuo aggiornamento delle unità di misura, usando definizioni più precise e replicabili, tramite misure non disponibili solo qualche decennio prima
-->
