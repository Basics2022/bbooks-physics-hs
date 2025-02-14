(physics-hs:mechanics:intro:vocabulary)=
# Concetti in meccanica classica

(physics-hs:mechanics:intro:vocabulary:physical-dimensions)=
## Grandezze fisiche

(physics-hs:mechanics:intro:vocabulary:physical-dimensions:fundamental)=
### Grandezze fisiche fondentali
Le grandezze fisiche fondamentali del [sistema internazionale di misura](physics-hs:intro:physical-quantities:system:is) coinvolte nello studio della meccanica classica sono: **spazio** $[L]$, **tempo** $[t]$ e **massa** $[m]$.

(physics-hs:mechanics:intro:vocabulary:physical-dimensions:derived)=
### Grandezze fisiche derivate
Nello sviluppo della teoria matematica della meccanica classica risulta conveniente definire delle quantità fisiche, con le loro dimensioni fisiche derivate.

La **cinematica** si occupa di descrivere la posizione dei corpi nello spazio (pensato come euclideo) in funzione del tempo, indipendentemente dalle sue cause. La variazione della **posizione** $[L]$ di un punto nello spazio in funzione del tempo definisce la sua **velocità** $[L][t]^{-1}$, e la variazione della velocità nel tempo definisce l'**accelerazione** $[L][t]^{-2}$;[^rotations]

[^rotations]: In maniera analoga ma diversa, l'orientazione di un corpo (rigido) nello spazio può essere definito tramite **angoli** $[1]$ o parametri riportabili ad essi; la variazione dell'orientazione del corpo in funzione del tempo viene rappresentata dalla sua **velocità angolare** $[t]^{-1}$; la variazione della velocità angolare nel tempo viene rappresentata dalla sua **accelerazione angolare** $[t]^{-2}$. Una trattazione completa delle rotazione e della dinamica dei corpi rigidi nello spazio 3-dimensionale è al di fuori degli obiettivi di un'introduzione alla meccanica classica, poiché - per non fare porcherie, almeno - richiederebbe una certa dimestichezza con strumenti matematici con i quali difficilmente si ha dimestichezza - o forse nemmeno li si è mai visti. In ogni modo, è disponibile il materiale pensato per l'università per una trattazione completa di rotazioni e [meccanica classica](https://basics2022.github.io/bbooks-physics-mechanics/intro.html).

L'**inerzia** di un sistema rappresenta la sua resistenza al cambiamento del suo stato di moto, quando soggetto ad azioni e dipende dalla sua **massa** $[m]$ e dalla sua distribuzione nel sistema: per sistemi continui di dimensione finita è quindi importante consocerne la **densità** $[m][L]^{-n}$ per poterne stimare le proprietà di inerzia riassumibili nel momento statico $[m][L]$ e **momento di inerzia** $[m][L]^2$. La massa - e la sua distribuzione - e le quantità introdotte in cinematica possono essere combinate in *quantità dinamiche* che compaiono in dinamica nelle equazioni che governano il moto dei sistemi: in particolare vengono definiti i concetti di **quantità di moto** (massa per velocità) $[m][L][t]^{-1}$ e **momento della quantità di moto** (o **momento angolare**) $[m][L]^2[t]^{-1}$.

Le **azioni** sono quelle interazioni che possono agire su un sistema modificandone il moto, se questa modifica è consentita dai vincoli del sistema stesso. Vengono introdotte le **forze** $[m][L][t]^{-2}$ e i **momenti** $[m][L]^2[t]^{-2}$. Legati ai concetti di azioni, possono essere introdotti i concetti di **lavoro** ("forza per spostamento) $[m][L]^2[t]^{-2}$ e di **potenza** (lavoro per unità di tempo) $[m][L]^2[t]^{-3}$; in alcuni casi, il lavoro fatto da azioni su un sistema contribuisce all'aumento di una quantità 

La **dinamica** si occupa di descrivere il moto dei sistemi, cause incluse. Le equazioni della dinamica legano la variazione delle quantità dinamiche alle azioni agenti sul sistema.


## Modelli
...

<span style="color:red">Muovere in una sezione "Introduzione alla meccanica", per rendere lo schema uniforme con Termodinamica ed Elettromagnetismo: prime esperienze; approccio di Newton (grandezze fisiche e concetti); modelli</span>

Quando si costruisce una teoria scientifica, è spesso necessario compiere uno sforzo di astrazione (**todo** *come conosciamo? Discorso filosofico...*), di modellazione dei fenomeni di interesse. Un buon modello è in grado di rappresentare con la precisione (**todo** *o accuratezza?*) richiesta il fenomeno studiato, essere in accordo con attività sperimentali e garantire capacità di previsione che coinvolgono tali fenomeni.

Nello studio della meccanica e della fisica in generale, si è soliti distinguere gli elementi oggetti di studio da tutti gli altri elementi:
- **sistema**, unione degli elementi oggetti di studio
- **ambiente esterno**, tutto quello che non fa parte del sistema

In meccanica, è necessario uno sforzo di modellazione per costruire un modello matematico che rappresenti:
- i componenti meccanici, che costituiscono il sistema
- le connessioni tra componenti meccanici del sistema, o le connessioni con l'ambiente esterno
- le azioni che operano sul sistema, dovute alle interazioni del sistema con l'esterno o scambiate tra componenti del sistema

A seconda del livello di dettaglio richiesto, si possono definire diversi modelli di componenti meccanici in base a:
- dimensioni:
  - sistemi puntiformi, di dimensioni trascurabili per il problema di interesse
  - sistemi estesi, di dimensioni non trascurabili per il problema di interesse; a seconda della loro deformabilità e/o del livello di dettaglio dell'analisi:
    - rigidi
    - deformabili
- inertia:
  - massa non trascurabile
  - massa trascurabile

**Esempio.** Analisi di un aereo:
- per lo studio di traiettorie e prestazioni, può essere considerato come un sistema puntiforme
- per uno studio preliminare di equilibrio e dinamica del velivolo, può essere usato un modello esteso rigido
- per lo studio accurato dell'equilibrio, della dinamica del volo e del progetto aero-servo-elastico l'aereo viene modellato come un insieme di elementi: viene usato un modello esteso deformabile dotato di massa per molti elementi strutturali, connessi tramite vincoli



