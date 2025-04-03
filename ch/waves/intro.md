(physics-hs:waves:intro)=
# Introduzione ai fenomeni ondulatori

**Cosa intendiamo per onda?** Il termine onda è comunemente associato alla propagazione di una perturbazione - rispetto a una condizione di equilibrio - di una quantità fisica nello spazio e nel tempo, in grado di trasportare energia e in molti casi con una **velocità di propagazione** ben definita[^wave-speed].

Da un punto di vista matematico, la propagazione di perturbazioni di diverse quantità fisiche è governata dallo **stesso modello matematico**:
così, ad esempio, lo stesso modello matematico governa la trasmissione delle onde meccaniche nella materia e delle onde elettromagnetiche nella materia o nel "vuoto" - di materia[^space-physical-properties].
Poiché lo stesso modello matematico descrive la propagazione di diversi disturbi in vari ambiti della natura, questi sistemi possono mostrare formalmente gli stessi **fenomeni caratteristici** come interferenza, effetto Doppler, e - in presenza di ostacoli - riflessione, rifrazione, diffrazione, scattering da particelle o superfici irregolari. 
L'interazione con ostacoli può dipendere dalle dimensioni relative dell'ostacolo e della *lunghezza d'onda*, vedi {prf:ref}`wave-length`, della perturbazione.

La propagazione di disturbi di intensità "sufficientemente piccola" può essere descritta con un modello lineare, l'*equazione delle onde*. La linearità di un problema consente di utilizzare il **principio di sovrapposizione delle cause e degli effetti**, e scomporre perturbazioni con "forma complessa" come somma di [perturbazioni più semplici](physics-hs:waves:equation:solutions).

Da quanto detto nell'introduzione, dovrebbe risultare sensato il programma di questo capitolo.
- L'[equazione delle onde in diversi sistemi fisici](physics-hs:waves:equation:examples) viene ricavata a partire da equazioni di bilancio. Partendo da equazioni di bilancio differenti, in ambiti differenti, in alcuni casi si arriva allo stesso modello matematico: l'equazione delle onde.
- Una volta ricavata l'equazione delle onde in diversi ambiti, dovrebbe risultare sensato investire un po' di tempo per discutere il modello matematico - indipendente dall'applicazione -, descrivendone
  - le [soluzioni elementari](physics-hs:waves:equation:solutions), che possono essere composte in un problema lineare per ricavare una soluzione generale
  - le [caratteristiche dei fenomeni ondulatori](physics-hs:waves:phenomena), che possono manifestarsi


---

<!--
La perturbazione di diverse quantità fisiche in vari ambiti delle scienze è governata dallo **stesso modello matematico**, e quindi diversi fenomeni fisici mostrano formalmente le stesse caratteristiche.
-->

```{dropdown} Alcuni esempi
Alcuni fenomeni fisici governati dall'equazione delle onde sono:
- le onde meccaniche nella amteria che si manifestano sotto forma di vibrazione. Alcuni esempi sono:
  - la vibrazione delle corde tese di strumenti a corda. Lo stato a riposo della corda viene perturbato da un'azione esterna (lo sfregamento di un arco per le viole, il pizzicamento per la chitarra, la percussione per pianoforte). La perturbazione introdotta si trasmette poi lungo la corda tesa con una dinamica descritta dall'equazione delle onde, ed è visibile come perturbazione della posizione della corda
  - i terremoti. Lo stato a riposo delle rocce nel sottosuolo viene alterato dal cedimento improvviso di una condizione di equilibrio, a causa del raggiungimento del carico di rottura. Questo movimento improvviso, quasi impulsivo, introduce una perturbazione della posizione delle che si trasmette *attraverso i diversi strati* della Terra sotto forma di onde sismiche, che vengono percepite come terremoti quando arrivano sulla superficie terrestre. Il punto in cui si verifica il cedimento è l'*ipocentro*, mentre la sua proiezione sulla superficie terrestre è l'epicentro*; in media, l'intensità della perturbazione diminuisce con la distanza dall'ipocentro
  - il suono. Lo stato di quiete dell'aria o di un altro fluido viene perturbato da un'azione esterna, che introduce una perturbazione di pressione - tipicamente il movimento di una superficie solida come può essere la vibrazione degli strumenti a corda discussi sopra, ma non solo: **todo** getti e spettro in fluidi, fuoco,.... Questa perturbazione si trasmette all'interno del fluido come onda di pressione. Quando una perturbazione con contenuti sensibili in frequenza tra i $20 \, \text{Hz}$ e i $20 \, \text{kHz}$ raggiunge l'[orecchio umano](physics-hs:intro:sensing:hearing), questo è in grado di convertire il segnale di pressione in segnale nervoso che il nostro cervello elabora come suono
- le [onde elettromagnetiche](physics-hs:electromagnetism:em-waves): il movimento di cariche elettriche produce perturbazioni nel campo elettromagnetico presente in una regione dello spazio; queste perturbazioni del campo elettromagnetico si trasmettono sotto forma di onde. Secondo il modello atomico, la materia è composta da componenti elementari in cui la carica elettrica è divisa tra una carica netta positiva nel nucleo e carica netta negativa degli elettroni. La vibrazione termica degli atomi produce il moto microscopico di cariche elettriche. Questo moviemnto di cariche produce emissione di radiazione elettromagnetica da parte di ogni corpo, come descritto dalle leggi dell'irraggiamento. A seconda della frequenza della radiazione, questa può essere percepita dai sensi umani sotto forma di luce o calore, può essere percepita dall'effetto dell'abbronzatura, o può essere utilizzata per le comunicazioni, o per applicazioni scientifiche o mediche.

```

<!--
La perturbazione di diverse quantità fisiche in vari ambiti delle scienze è governata dallo **stesso modello matematico**, e quindi mostrano formalmente le stesse caratteristiche: così si osservano onde meccaniche nei mezzi continui (solidi: onde nei solidi elastici, onde sismiche; fluidi: onde di pressione in acustica, onde in un liquido - come le onde del mare) o onde elettromagnetiche nello spazio[^space-physical-properties].
-->

[^wave-speed]: In molti problemi, la propagazione di perturbazioni di ampiezza limitata è governata da un problema lineare. Quando è valido un modello lineare, la velocità di propagazione dell'onda dipende dalle caratteristiche del mezzo e del suo stato di equilibrio, e non dall'ampiezza delle perturbazioni: ad esempio, le onde acustiche in un gas si propagano con una velocità che dipende tipicamente dalla natura del gas e dalla sua temperatura, per un gas ideale perfetto $c = \sqrt{\gamma R T}$; la luce si propaga nel vuoto con una velocità che dipende solo da costanti della natura, $c_0 := \frac{1}{\sqrt{\varepsilon_0 \mu_0}}$. In alcuni contesti, la propagazione di perturbazioni di ampiezza "sufficientemente grande" sono descritte da un problema non-lineare, e lì la storia si complica...**todo** *esempi: equazione delle acque basse, equazione dei gas comprimibili. Questi casi apparentemente differenti, sono descritti da equazioni simili; in entrambi i casi la dinamica delle perturbazioni non è banale e può dare origine a* **urti**, *nel primo caso chiamati salti idraulici, nel secondo caso onde d'urto*

[^space-physical-properties]: Spazio magari "vuoto di materia" ma non di proprietà fisiche, come dimostrato dalla propagazione delle onde EM, e l'assenza di un mezzo - l'*etere luminifero* - per spiegarne la propagazione. Vedi esperimento di Michelson-Morley.

<!--
**Esempi.**
- Onde meccaniche nei mezzi continui:
  - nei solidi
    - elastici
    - onde sismiche
  - nei fluidi
    - onde di pressione (densità e altre proprietà meccaniche) e suono
- Onde EM; lo spettro EM comprende
  - onde radio, micro, IR, luce visibile, UV, $\gamma$, $X$

**Soluzioni particolari.**
- Onde piane stazionarie e viaggianti
- Onde sferiche nello spazio 3-dimensionale

**Caratteristiche dei fenomeni ondulatori.**
-->
