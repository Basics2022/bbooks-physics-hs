(physics-hs:intro)=
# Introduzione alla fisica

La fisica si occupa dello studio della natura, di tutti i fenomeni naturali che possono essere descritti tramite un processo di **misura** di **grandezze fisiche**; l'indagine si basa sul **metodo scientifico** con lo scopo di formulare alcuni princìpi sui quali costruire un modello o una teoria fisica, tramite un processo deduttivo che fa uso degli strumenti della logica e della matematica.

````{only} html
**Contenuti.**

```{dropdown} [Grandezze fisiche](physics-hs:intro:physical-quantities)
Dopo aver dato la definizione di una grandezza fisica, viene presentato il sistema internazionale di unità di misura (SI) attualmente in uso, distinguendo tra le unità di misura fondamentali e quelle derivate. Nelle sezioni successive viene fatta una prima discussione discorsiva di alcune grandezze fisiche.
```
```{dropdown} [Processo di misura](physics-hs:intro:measurements)
Viene definita l'attività di misurazione di una grandezza fisica. Viene fornito un modello generale di uno strumento di misura, e vengono definite **accuratezza** e **precisione** in termini di valore medio e deviazione standard di una serie di misurazioni. Vengono poi presentate alcune caratteristiche degli strumenti di misura (fondo scala, risoluzione, linearità, sensibilità; ordine dello strumento: funzione di trasferimento, banda passante, guadagno,...); infine viene discussa l'intrusività dello strumento di misura nel sistema.
```
```{dropdown} [Metodo scientifico](physics-hs:intro:scientific-method)
Viene discusso il metodo scientifico. Viene introdotto il principio di falsificabilità di Popper, e viene illustrato il metodo di Fisher per il test di validità delle ipotesi.
```
```{dropdown} [Sensi](physics-hs:intro:sensing)
Dopo aver introdotto le grandezze fisiche, gli strumenti di misura, e la necessità del metodo scientifico per la costruzione della conoscenza su esperienze e misure riproducibili, vengono discussi alcuni sensi dell'essere umano, trattando i nostri recettori e i nostri organi che portano all'elaborazione dell'informazione da parte del cervello come un sistema di misura. Con questa discussione dovrebbe risultare chiaro come mai "i nostri sensi ci possono ingannare", o meglio perché i nostri sensi sono strumenti di misura limitati.
```
```{dropdown} [Stato corrente](physics-hs:intro:current-status)
Infine viene discusso lo stato corrente del sapere, almeno la parte ben consolidata e che ha già avuto applicazioni diffuse, che risulterà molto utile per affrontare e comprendere la costruzione di alcune teorie e modelli, prima di affrontarli nella loro parte più quantitativa/matematica.
Vengono poi discussi i limiti di applicazione di alcune teorie fisiche: in alcuni casi i limiti sono dovuti alla caduta della validità del modello con previsioni sbagliate, in altri casi opposti si manifestano limiti pratici di modelli dettagliati che forniscono le stesse previsioni di modelli più semplici a un costo $O((10^{23})^n)$ volte superiore.

<span style="color:red">Uncomment! And fill the secion</span>
<!--
 In particolare
- la **teoria atomica della materia** affermatasi nel XIX secolo, riconosce che la materia è composta da componenti elementari, gli atomi
- i primordiali **modelli atomici** sviluppati a inizio XX secolo (Rutherford) riconoscono che gli atomi non sono così elementari come si pensava, ma che sono dei sistemi elettricamente neutri, con un nucleo positivo e degli elettroni negativi,
Queste due teorie forniscono alcuni modelli microscopici per spiegare il comportamento macroscopico dei sistemi trattati nei capitoli sulla termodinamica e sull'elettromagnetismo.
-->
```

````



<span style="color:red">Uncomment</span>

<!--
- metodo scientifico: 
  - metodo induttivo/metodo deduttivo, o due fasi di un processo?
  - una nuova teoria scientifica deve essere in grado di fornire previsioni che i modelli già presenti non sono in grado di dare
  - **principio di falsificabilità di Popper** - o **possibilità di confutazione**: la conoscenza è un processo in continua evoluzione; una teoria scientifica è tale solo se si espone alla possibilità di essere falsificata; una teoria scientifica; una teoria scientifica viene considerata valida (almeno entro alcuni limiti dei fenomeni studiati) fino a quando non viene dimostrata erronea: "non basta un numero elevato di esperimenti per dimostrare la validità di un modello, ma è sufficiente un solo esperimento per dimostrare che quel modello è sbagliato". La scienza non può essere verificata, ma al contrario può essere falsificata.
  - Questo procedimento viene riassunto nel [test di verifica delle ipotesi di Fisher](https://basics2022.github.io/bbooks-programming-hs/ch/statistics/hp-test.html#test-di-verifica-delle-ipotesi)


**Metrologia e misura.**
- Grandezza fisica
- ...

**Metodo scientifico.**
- Inferenza
- Falsificabilità

**Costruzione modelli e teorie fisiche.** Grazie al metodo scientifico è possibile riconoscere le leggi fisiche. Un modello fisico è il risultato di un processo di astrazione e rappresentazione di fenomeno fisico osservato, utilizzando il linguaggio della matematica. Una teoria fisica viene costruita:
- a partire da un numero limitato di leggi fisiche indipendenti tra di loro - cioè sono un numero minimo di informazioni, necessarie per costruire una teoria - in accordo con le attività sperimentali, usati come **princìpi della teoria**; in generale, questi princìpi:
  - possono mostrare limiti di validità, definiti anche dall'accuratezza richiesta al modello;
  - non sono dimostrabili all'interno della teoria stessa: essi sono il punto di partenza della teoria stessa, e se fossero dimostrabili, non sarebbero affermazioni indipendenti - e quindi si potrebbe ridurre l'insieme dei princìpi della teoria;
  - devono essere in accordo con i risultati di teorie fisiche più dettagliate, quando disponibili.
- usando gli strumenti della **logica** e della **matematica** per:
  - costruire modelli dei fenomeni fisici
  - derivando risultati e conseguenze dei princìpi; secondo il metodo scientifico, nella fase di sviluppo di una nuova teoria o di un modello, queste conseguenze devono essere sottoposte alla verifica sperimentale:
    - una teoria scientifica è sempre soggetta a falsificabilità
    - i modelli costruiti possono essere affetti da incertezza, o inaccuratezza per la mancata rappresentazione di tutti i fenomeni coinvolti. In ambito ingegneristico, la verifica tra modello matematico e fisico è spesso un'attività fondamentale e avviene tramite la taratura di alcuni parametri del modello.

**Contenuti.**
- Metodo scientifico:
  - ricerca di princìpi fisici in accordo con le attività sperimentali
  - deduzione di una teoria, a partire dai princìpi
- Grandezze fisiche:
  - fondamentali e derivate
    - lunghezza, aree e volumi
    - massa e densità
    - tempo
  - processo e strumenti di misura:
    - logica **todo** *?*
    - analisi dati, errori
- **Astrazione** e costruzione di **modelli**, con il linguaggio matematico
- Rappresentazione dei dati
  - ...
- Sapere attuale

-->
