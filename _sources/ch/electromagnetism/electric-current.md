(physics-hs:electromagnetism:electric-current)=
# Corrente elettrica

<!--
- corrente elettrica:
  - descrizione microscopica: materiale elettricamente neutro, con $e^-$ liberi di conduzione
  - def come flusso di carica: dalla descrizione micro alla descrizione macroscopica, media, ("fenomenologica"?)
-->

## Definizioni
```{prf:definition} Corrente elettrica
:label: electric-current

La corrente elettrica (attraverso una superficie $S$, in un dato istante di tempo $t$) può essere definita come il **flusso di carica elettrica** $\Delta Q$ che attraversa una supercie in un intervallo di tempo $\Delta t$, al tendere di $\Delta t$ a zero.
```

A seconda del livello di [dettaglio necessario](physics-hs:intro:current-status:micro-macro), si può dare una descrizione microscopica o macroscopica della corrente elettrica. Localmente, è possibile definire una **densità macroscopica di carica elettrica**

$$\lim_{\Delta V(P) \rightarrow 0} \dfrac{\sum_{k \in \Delta V(P)} q_k}{\Delta V} = \rho(P)$$

e una **densità macroscopica di corrente elettrica** come la media pesata delle velocità delle cariche, $\vec{v}$,

$$\lim_{\Delta V(P) \rightarrow 0} \dfrac{\sum_{k \in \Delta V(P)} q_k \vec{v}_k}{\Delta V_P} = \vec{j}(P)$$

La **corrente elettrica** attraverso una superficie $S$ viene definita come il flusso di carica elettrica attraverso la superficie $S$,

$$i = I_{S} = \Phi_{S}(\vec{j}) \ .$$

(electric-current-density:def)=
###  Densità di corrente elettrica
```{prf:definition} Densità di corrente elettrica
:label: electric-current-density

$$\lim_{\Delta V(P) \rightarrow 0} \dfrac{\sum_{k \in \Delta V(P)} q_k \vec{v}_k}{\Delta V_P} = \vec{j}(P)$$

```


<!--
````{list-table}
:header-rows: 0
* - ![](../../media/electric-current.png)
  - ![](../../media/electric-current-solids.png)
````
-->

```{note} 
E' possibile - anzi è molto comune - misurare **corrente elettrica** anche in **materiali elettricamente neutri**. Ad esempio, la [conduzione elettrica in solidi conduttori](physics-hs:electromagnetism:electric-current:solids:conductor) avviene per il moto medio degli elettroni liberi di conduzione, mentre i nuclei positivi sono in media fermi. I gas conducono corrente elettrica solo se sottoposti a un campo elettrico sufficentemente intenso da separare alcuni elettroni dai nuclei degli atomi: quello che si forma è un gas ionizzato, o plasma, e la corrente elettrica è il risultato del moto in una direzione degli elettroni (negativi) e nella direzione opposta degli ioni positivi - i nuclei ai quali è stato strappato qualche $e^-$.

Nell'ipotesi di avere due sostanze diverse con densità di carica carica $\rho^+$, $\rho^-$ e velocità media delle due sostanze $\vec{v}^+$, $\vec{v}^-$, la corrente densità di corrente elettrica è

$$\vec{j} = \rho \vec{v} = \rho^+ \vec{v}^+ + \rho^- \vec{v}^- \ . $$

Nel caso in cui il materiale sia neutro, la densità di carica elettrica è nulla, $0 = \rho = \rho^+ + \rho^- =$ e quindi $\rho^+ = - \rho^-$ e la densità di corrente elettrica può essere scritta come $\vec{j} = \rho^- (\vec{v}^- - \vec{v}^+)$.
```

(electric-current:cable)=
```{example} Corrente in un cavo elettrico di piccola sezione
**todo**
```

<!--
```{figure} ../../media/electric-current-solids.png
---
width: 30%
align: right
---
```
-->

<!--
La corrente elementare attraverso la superficie elementare $\Delta S$ è
V
$$\Delta i = \Phi_{\Delta S}(\vec{j}) = \vec{j} \cdot \hat{n} \Delta S = \frac{\sum_k q_k \vec{v}_k}{\Delta V} \cdot \hat{n} \Delta S = $$
-->

(physics-hs:electromagnetism:charge-conservation)=
## Legge di conservazione della carica elettrica
Il principio di conservazione della carica elettrica afferma che la carica elettrica non si crea né si distrugge. E' quindi possibile scrivere il bilancio di carica elettrica per un volume $V$,

$$\dot{Q}_V = - \Phi_{\partial V}(\vec{j}) = - I_{\partial V} \ .$$

La variazione di carica elettrica per unità di tempo contenuta all'interno del volume è uguale alla carica elettrica netta entrante nel volume attraverso la sua superficie, cioè la corrente elettrica attraverso la sua superficie $\partial V$.

In parole povere, la differenza di carica elettrica tra due istanti del sistema è uguale alla carica che è entrata meno la carica che è uscita.

- **todo** esempi/esercizi con misura della corrente e della carica elettrica, con strumenti di misura (misura o modello di strumento, come bilance)

## Corrente elettrica nella materia
In questa sezione viene discussa la conduzione della carica elettrica nella materia. Diversi materiali hanno proprietà e meccanismi di conduzione molto differenti, (facilmente) spiegabili con una descrizione del fenomeno a livello microscopico. Così, molto velocemnte:
- i solidi conduttori (metalli,...) hanno ottime proprietà di conduzione, dovute alla presenza di elettroni (di conduzione) condivisi tra tutti gli atomi del materiale, non localizzati ma liberi di muoversi all'interno del materiale. L'applicazione di un campo elettrico di intensità modesta ne causa facilmente il moto, e quindi il materiale dimostra una buona conduzione.
- i solidi isolanti: non ci sono cariche libere condivise, facili da muovere con l'applicazione di un campo elettrico di intensità modesta; se sottoposto a campi elettrici intensi, oltre la *rigidità del dielettrico*, si possono verificare scariche all'interno del mezzo
- liquidi...
- gas neutri, in assenza di portatori di carica liberi, le molecole del gas sono elettricamente neutre e il mezzo si comporta da isolante perfetto. E' necessaria una causa esterna, spesso un campo elettrico elevato (o anche temperatura?), che produca la **ionizzazione** di alcune delle molecole del gas, cioè la separazione di elettroni dalla restante parte dell'atomo (che diventa uno ione, con carica elettrica positiva). Un gas ionizzato costituito da elettroni e ioni liberi con carica netta nulla è definito **plasma**

(physics-hs:electromagnetism:electric-current:solids:conductor)=
### Solidi conduttori
**Conduttori.** I solidi hanno una struttura microscopica con gli atomi disposti in un reticolo, senza libertà di movimento medio, con alcuni elettroni non localizzati attorno al singolo atono, ma "condivisi" e libersi di muoversi tra tutti gli atomi del solido: queste cariche elettriche libere di muoversi permettono una buona conduzione di corrente elettrica, e vengono chiamati **elettroni di conduzione**.

Senza "forzanti esterne", come ad esempio campi elettrici, il moto degli elettroni di conduzione non ha direzioni privilegiate: poiché il moto delle cariche libere è casuale senza direzioni privilegiate, la velocità media è nulla (la velocità è una grandezza vettoriale!) e la corrente elettrica è nulla. Se le velocità delle cariche libere ha una direzione preferenziale, la loro velocità media, $\vec{v}^-$, e quindi la corrente elettrica, non è nulla. Se il solido di interesse è in quiete rispetto all'osservatore, allora le cariche elettriche positive hanno $\vec{v}^+ = \vec{0}$, e la [densità di corrente elettrica](electric-current-density:def) diventa $\vec{j} = \rho^- \vec{v}^-$.

<!--
**Isoltanti.** ...
-->

(physics-hs:electromagnetism:electric-current:solids:conductor:ohm)=
#### Conduttori di Ohm
```{prf:definition} Conduttore di Ohm - legge di Ohm in forma locale
In un conduttore di Ohm, il campo elettrico $\vec{e}(\vec{r},t)$ è proporzionale alla densità di corrente elettrica $\vec{j}(\vec{r},t)$. Per un solido isotropo, senza direzioni preferenziali, la **forma locale - differenziale - della legge di Ohm**: 

$$
\vec{j}(P) = \sigma(P) \, \vec{e}(P)
\qquad \ , \qquad
\vec{e}(P) = \rho_R(P) \, \vec{j}(P)
$$ (ohm:local)

essendo la resistività $\rho_R$, e la conduttanza $\sigma = \frac{1}{\rho_R}$ le costanti di proporzionalità, caratteristiche del materiale.
```

In un [cavo elettrico](electric-current:cable), nell'ipotesi di grandezze uniformi sulla sezione - o riferendosi alle grandezze medie -, si può integrare la legge in forma locale su un tratto di lunghezza elementare, $d \ell$,

$$\begin{aligned}
 \underbrace{e \, d \ell}_{- d v} \, A & = \rho_R \, \underbrace{j \, A}_{i} \, d \ell \\
 \rightarrow \quad dv & = - \dfrac{\rho_R \, d \ell}{A} \, i = - dR \, i \ , 
\end{aligned}$$

avendo introdotto la differenza di potenziale elementare $d v$ tra gli estremi del tratto di cavo elementare, proporzionale alla corrente che transita nel cavo tramite la **resistenza elettrica** elementare $dR$.

Queste relazioni che ben descrivono il comportamento di cavi elettrici conduttori in un ampio regime di funzionamento, sono le leggi Ohm.

```{prf:definition} Leggi di Ohm per cavi elettrici

 - **Prima legge di Ohm.** La differenza di potenziale agli estremi di un cavo di lunghezza elementare è proporzionale alla corrente, tramite la resistenza elettrica elementare,

   $$dv = - dR \, i \ ,$$ (ohm:integral:first)

 - **Seconda legge di Ohm.** La resistenza elettrica di un cavo è direttamente proporzionale alla resistività del materiale, alla lunghezza del cavo, e inversamente proporzionale alla sezione del cavo,

   $$dR = \frac{\rho_R \, d\ell}{A} \ .$$ (ohm:integral:second)

```

(physics-hs:electromagnetism:electric-current:solids:dielectric)=
### Solidi dielettrici

(physics-hs:electromagnetism:electric-current:gas)=
### Conduzione nei gas
**todo** *blabla*
- fenomeno fisico: ionizzazione; necessario campo elettrico intenso **(!)**
- apparati sperimentali: tubo di Crookes, attuatori al plasma,...
- spiegazione (immediata utilizzando modello atomistico della materia): campo elettrico elevato "strappa" $e^-$ dagli atomi dei gas (rarefatti). Un atomo inizialmente neutro viene **ionizzato**: gli elettroni hanno carica negativa, lo ione (l'atomo al quale sono stati sottratti gli elettroni) ha carica positiva. Queste due entità hanno ora carica elettrica netta, e subiscono l'accelerazione dovuta all'interazione con un campo elettrico, che si manifesta con la [forza di Lorenz](physics-hs:electromagnetism:lorentz) $\vec{F} = q \vec{e}$ agente sulle particelle cariche. L'equazione del moto è $m \ddot{r} = q \vec{e}$. Il moto di corpi di carica diversa si sviluppa quindi in due direzioni opposte:
  - moto delle cariche positive nella stessa direzione del campo elettrico
  - moto delle cariche negative in direzione opposta al campo elettrico
Esperimenti:
- Goldstein (1886) si concentra sul moto delle cariche positive: tubi di Crookes con sostanze diverse producono "particelle" (**todo** *Goldstein aveva in mente la natura discreta di quello che stava osservando? In quali termini si esprimeva?*) con rapporto $\frac{\text{carica}}{\text{massa}}$ caratteristici della sostanza, ma diversi da sostanza a sostanza. Spiegazione di oggi: gli ioni di sostanze diverse hanno massa e carica che dipendono dalla sostanza di partenza
- [Thomson](modern:experiments:thomson:electron) (1897) si concentra sul moto delle cariche negative, scoprendo che il rapporto $\frac{\text{massa}}{\text{carica}}$ è indipendente dalla sostanza contenuta nel tubo di Crookes. Viene scoperto/introdotto il concetto di elettrone, come unità di carica "elementare".
- Rontgen e i raggi X **todo** *link a Rontgen: raggi X, Becquerel: fosforescenza, emissione di raggi e radioattività naturale; coniugi Curie*

(physics-hs:electromagnetism:electric-current:semiconductor)=
### Conduzione nei semiconduttori
 cenni all'elettronica: diodi, transistor, ...


(physics-hs:electromagnetism:electric-current:instruments)=
## Strumenti: misura e generazione
**todo**
  - strumenti per misurare corrente e tensione: amperometro e voltmetro
  - generatori di "spinta": generatori di tensione
  - resistenza al moto: la resistenza elettica


