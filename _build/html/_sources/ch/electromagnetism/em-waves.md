(physics-hs:electromagnetism:em-waves)=
# Onde elettromagnetiche

Le onde elettromagnetiche sono perturbazioni del campo elettromagnetico $\vec{e}(\vec{r},t)$, $\vec{b}(\vec{r},t)$ governate da un'[equazione delle onde](physics-hs:waves:equation:examples) che si propagano nello spazio e nel tempo con una velocità ben definita e dipendente dal mezzo di propagazione: in un materiale omogeneo e isotropo, la velocità delle perturbazioni è uguale in ogni punto e in ogni direzione, e ha valore assoluto $c = \frac{1}{\sqrt{\mu \varepsilon}}$. Il campo elettronagmetico esiste e le sue perturbazioni si propagano anche in assenza di materia, nel cosiddetto *"vuoto di materia ma non di proprietà fisiche"*. Usando la costante dielettrica e la permeabilità del "vuoto", la velocità delle onde elettromagnetiche - la velocità della luce, il modo comune per chiamare la radiazione elettromagnetica nel visibile, cioè che riusciamo a [percepire con gli occhi](physics-hs:intro:sensing:sight) - nel vuoto è 

$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \ .$$ 

La **velocità della luce** nel vuoto è considerata ad oggi una **costante della natura**. Un primo esperimento che portò a questa conclusione fu l'[esperimento di Michelson e Morley](physics-hs:electromagnetism:em-waves:speed:michelson-morley) del 1887. La costanza della 



```{dropdown} **1865 - Maxwell - il modello matematico.**
Le equazioni di Maxwell forniscono un modello matematico per i fenomeni dell'elettromagnetismo classico. Sotto opportune condizioni, le equazioni prevedono la possibilità che il campo elettromagnetico possa propagarsi come un fenomeno ondulatorio. La rapida oscillazione di un cariche elettriche - e quindi una corrente alternata ad alta frequenza - è una sorgente di onde elettromagnetiche: un modello di questa sorgente è un dipolo oscillante, una realizzazione pratica fondamentale sono le antenne per le trasissioni di onde EM.

Ai tempi, non era ancora chiaro che la luce visibile fosse un effetto EM, un esempio di onde EM con una particolare lunghezza d'onda e frequenza percepibile dall'occhio umano, i nostri percettori della vista.

Le equazioni di Maxwell prevedevano una velocità di propagazione delle onde EM nel vuoto non lontana dalle migliori misure disponibili allora per la velocità della luce. La natura ondulatoria mostrata dalla luce (riflessione, diffrazione, rifrazione, interferenza, e anche polarizzazione) e le misure di velocità simili a quelle previste dal modello di Maxwell portarono all'interpretazione della luce come fenomeno EM, e diedero forti argomenti a sostegno della natura ondulatoria nel dibattito sulla natura corpuscolare o ondulatoria della luce.
```

<!--
```{dropdown} Misure della velocità della luce
**todo**
```
-->

```{dropdown} **1886-89 - Hertz - la prova sperimentale.**

Gli esperimenti del 1887-88 di H.R.Hertz(1857-1894)[^emwave-bragg][^emwave-fst] dimostrarono sperimentalmente l'esistenza delle onde, come fenomeno fisico:
- capace di propagare nello spazio senza bisogno di un conduttore (**todo** *fondamentale per le applicazioni radio di Marconi*)
- con le caratteristiche tipiche delle onde (riflessione, diffrazione, rifrazione, intereferenza, e polarizzazione)
- con la velocità di propagazione prevista dal modello di Maxwell, e simile alle misure della velocità della luce.

**todo** *descrizione esperimento, e qualche dettaglio sull'apparato sperimentale, e semplice modello matematico con l'elettrotecnica sviluppata nel capiolo precedente* **risonanza**

**todo** *commento dei video allegati, se necessario*

Hertz fece altre esperienze significative:
- in un esperimento del 1887 sulle onde elettromagnetiche osserva l'**effetto fotoelettrico**, riportando l'osservazione senza fornire una spiegazione - che non aveva, e che verrà data da A.Einstein nel suo *annus mirabilis* 1905, alle origini della meccanica quantitica - ma di cui evidenza la necessità di ulteriori indagini
- condusse un esperimento fallimentare con il quale pensò di dimostrare che i raggi catodici non avevano carica elettrica, risultato dovuto a un apparato sperimentale inadeguato; con lo stesso esperimento, nel 1897 J.J.Thompson dimostrò che i raggi catodici avevano carica elettrica e stimò il rapporto $\frac{\text{carica}}{\text{massa}}$ delle particelle che costituivano i raggi catodici: J.J.Thomson aveva scoperto l'elettrone.
 
**todo** *controllare citazioni* H.R.Hertz riteneva inutile ai fini pratici la sua scoperta (!), cosa presto smentita da **Marconi**...
```

```{dropdown} **1894-95 - Marconi - le prime applicazioni.**

**todo** *due parole sul contensto storico, la stesura dei cavi sottomarini e transoceanici del telegrafo - in cui erano coinvolti anche personaggi del calibro di Kelvin -, e rivoluzione della radio per le comunicazioni*

Oggi, le onde EM hanno un enorme numero di applicazioni.
- Onde radio: comunicazioni e connessioni: radio, televisione, cellulari, Wi-Fi, Bluetooth; navigazione: GPS, radar; controlli da remoto: radiocomando (anche con ostacoli tra sorgente e ricevitore); astronomia: radio telescopi
- Micro-onde: cottura; radar: per previsioni del tempo,...; comunicazioni: satellitari,...; astronomia: radiazione cosmica di fondo
- IR: radiazione termica: termocamere, visori notturi,...; controlli da remoto: telecomando (senza ostacoli in mezzo...)
- Visibile: tutte le applicazioni legate alla vista, es. fotografia e schermi: schermi di camere, cellulari, computer, TV,...; laser:...; comunicazioni: fibra ottica
- UV: sterilizzazione;...
- X: applicazioni medicali (raggi X per radiografia); scanner: sicurezza aeroporti,...; astronomia: telscopi sensibili ai raggi X
- $\gamma$: sterilizzazione:...; trattamenti medici: radioterapia su cellule tumorali,...; astronomia: eventi più energentici dell'universo emettono raggi $\gamma$

```

**todo** <span style="color:red">è possibile arrivare a un equazione per le onde senza passare dalle equazioni in forma differenziale? Magari con qualche analogia meccanica governata dalle equazioni delle onde. Se sì, in maniera sufficiente formale, figata</span>


(physics-hs:electromagnetism:em-waves:hertz)=
## Esperimenti di Hertz

(physics-hs:electromagnetism:em-waves:light)=
## Luce e spettro elettromagnetico

Spettro elettromagnetico...


(physics-hs:electromagnetism:em-waves:spectrography)=
## Spettrografia
Diffrazione per scomporre la luce in uno spettro:
- prisma
- seguendo la *teoria ondulatoria della luce* di Young, Arago e Fresnel, **Fraunhofer** (1815) sviluppa i **reticoli di** [**diffrazione**](physics-hs:waves:effects:diffraction) per sfruttarne l'interferenza, effetto tipico dei fenomeni che hanno *comportamento ondulatorio*; questo progresso tecnologico consente un miglioramento della risoluzione spettrale e la costruzione di strumenti universali affidabili per la spettroscopia
- verso la metà del XIX secolo vengono svolti i primi lavori sistematici sugli spettri di emissione e di assorbimento di diverse sostanze; si scoprono gli spettri discreti di emissione e di assorbimento (che coincidono per la stessa sostanza) e che questi possono essere usati per riconoscere la composizione chimica delle sostanze;
- Kirchhoff riconosce le condizioni per l'emissioni di spettri continui e discreti
- 1895, Rontgen scopre i raggi $X$, poi identificati come radiazione elettromagnetica - come la luce - ad alta frequenza
- ...

**Applicazioni.** **todo** *storiche: analisi chimiche, cristallografia,...; moderne: applicazioni in medicina,...*

**Riferimenti.**
[^emwave-bragg]: [Onde magnetiche, con Sir L.Bragg](https://www.youtube.com/watch?v=Vwjcn4Vl2iw) per la Royal institution
[^emwave-fst]: [Esperimenti di Hertz con le onde elettromagnetiche](https://www.youtube.com/watch?v=xNTHbiKmwNQ) della Fondazione Scienza e Tecnica di Firenze
- f*cking genius: puntate su Hertz e Marconi
- cercare pubblicazioni di Hertz
