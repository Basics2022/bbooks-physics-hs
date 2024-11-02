(physics-hs:mechanics:models)=
# Modelli

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

