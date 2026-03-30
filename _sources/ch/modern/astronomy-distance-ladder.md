(physics-hs:modern:astronomy:distance-ladder)=
# Scala delle distanze cosmiche

In questa pagina viene ripercorso il calcolo delle distanze cosmiche, secondo quella che viene definita la **scala delle distanze cosmiche**: partendo dalle dimensioni e dalle distanze, di Terra, Luna e Sole, passando per le dimensioni e la forma delle orbite dei pianeti, continuando con la distanza delle stelle vicine e le dimensioni della nostra galassia, la Via Lattea, e finendo con la distanza della stelle remote e delle altre galassie.

L'aumento delle distanze misurate procede in un ordine cronologico, grazie alla costruzione di nuove conoscenze sulle conoscenze pregresse, al progresso tecnologico che fornisce strumenti migliori e alla scoperta e alla comprensione di nuovi fenomeni fisici utili nella misura di oggetti così remoti. Il racconto viene costruito seguendo l'ordine presentato nei consigliatissimi video di 3Blue1Brown con Terence Tao[^3b1b-tao-1][^3b1b-tao-2], con l'aggiunta di dettagli degli ancora più consigliatissimi video di Alan Zamboni, aka CURIUSS, su Henrietta Swan Leavitt[^curiuss-leavitt] e Cecilia Payne-Gaposchkin[^curiuss-payne], gli osservatori e le donne di Harvard, Schwarzshild, e i due studiosi Hertzsprung-Russell del diagramma, e il materiale fornito dall'Università del Nebraska[^nebraska-spectroscpic-parallax].

Qualitativamente possono essere riconosciute diverse fasi:
- antichità: Terra, Luna, Sole
- età moderna: Copernico e Keplero: orbite dei pianeti;...
- età contemporanea: Donne calcolatrici di Harvard;...; Hubble e red-shift (dimensioni ed espansione dell'universo)

```{dropdown} Unità di misura in astronomia
:
A causa delle dimensioni molto diverse delle distanze misurate, vengono introdotte diverse unità di misura

| Unità di misura                 |  Definizione                                    | in $m$                | in $au$             | in $ly$    |
| :------------------------------ | :---------------------------------------------- | :-------------------: | :-----------------: | :--------: |
| chilometro, $kg$                |                                                 | $10^3$                | ...                 | ...        |
| unità astronomica, $au$, $UA$   | distanza media Terra-Sole                       | $1.49 \cdot 10^{11}$  | $1$                 | ...        |
| anno luce, $ly$, $al$           | distanza percorsa nel vuoto da luce in 1 anno   | ...                   | $6.33\cdot 10^{4}$  | ...        |
| parsec, $pc$                    | distanza corrispondente a $1''$ di parallasse per il semiasse maggiore dell'orbita terestre    | ...                   | $2.06\cdot 10^{5}$  | $3.26$     |
| redshift                        | ...                                             | ...                   | ...                 | ...        |

```


```{dropdown} Scala delle distanze cosmiche, esempi e ordini di grandezza

Alcune dimensioni **todo** aggiungere incertezza

| Grandezza fisica                                     | Misura                     | Incremento                       |
| :--------------------------------------------------- | :------------------------: | :------------------------------: |
| Raggio Luna                                          | $1737 \, km$               |                                  |
| Raggio Terra                                         | $6378 \, km$               | $3.7$                            |
| Distanza Terra-Luna                                  | $3.84 \cdot 10^{5} \, km$  | $60.2$                           |
| Raggio Sole                                          | $6.96 \cdot 10^{5} \, km$  | $1.8$                            |
| Distanza Terra-Sole                                  | $1.49 \cdot 10^{8} \, km$  | $214.1$                          |
| Dimensioni sistema solare (asse maggiore Nettuno)    | $9.08 \cdot 10^{9} \, km$  | $60.9$                           |
| Distanza Sole-Proxima Centauri (stella pi vicina)    | $4.3 \, ly $               | $4.5 \cdot 10^6$                 |
| Dimensioni Via Lattea, la nostra galassia            | $5.3 \cdot 10^4 \, ly$     | $1.2 \cdot 10^4$                 |
| Distanza Via Lattea Andromeda, galassia più vicina   | $2.5 \cdot 10^6 \, ly$     | $47.2$                           |
| Galassie più lontane[^distant-galaxies]              | $\sim 30 \cdot 10^9 \, ly$ | $1.2 \cdot 10^4$                 |

[^distant-galaxies]: Nel caso delle galassie più lontane osservate, cosa stiamo osservando? Stiamo osservando ora la luce emessa da eventi remoti in spazio-tempo, e trasmessa attraverso di esso: detto male, stiamo osservando una traccia di un evento passato in un punto remoto nello spazio.
```


(physics-hs:modern:astronomy:distance-ladder:earth-radius)=
## Dimensioni Terra

La Terra non ha forma sferica, ma è "schiacciata ai poli". Il raggio medio vale circa

$$R_E = 6.373 \cdot 10^{3} \, \text{k}m \ ,$$

mentre raggio equatoriale e polare valgono rispettivamente $6.378 \cdot 10^{3} \, \text{km}$ e $6.357 \cdot 10^{3} \, \text{km}$.

**Eratostene** di Cirene (**III secolo a.C.**) usò la miusra della lunghezza dell'ombra di un bastone di dimensioni note a mezzogiorno in due città differenti, Alessandria d'Egitto ($31^\circ 11'51'' \text{N}$ $29^\circ 53'33'' \text{E}$) e Siene, l'odierna Assuan ($24^\circ 05' \text{N}$ $32^\circ 56' \text{E}$). 

```{prf:example} Sensibilità del valore del raggio alle misure

Distanza tra le due città, $d = 5000$ stadi, con $1$ stadio compreso tra i $155 \, \text{m}$ e i $160 \, \text{m}$. Dalla misura dell'ombra nello stesso istante tra le due città, Eratostene trovò un angolo di circa $\Delta \theta = 7.2^\circ$, $1/50$ di angolo giro. Con trigonometria elementare, l'espressione della lunghezza di un arco di circonferenza dati raggio e angolo sotteso vale

$$d = R \, \theta =  R \frac{2 \pi}{360^\circ} \theta[^\circ] \ ,$$

con gli angoli espressi in radianti dove non specificato. Quindi 

$$R = \frac{360^\circ}{\theta[^\circ]} \frac{d}{2 \pi} = 50 \times \frac{5000 \times ( 155 \div 160 ) \text{m}}{2 \pi} = (6167.25 \div 6366.20) \text{m} \ .$$

**Sensibilità agli errori di misura.**
* Errore sulla distanza $\Delta d$ implica un errore assoluto $\Delta R = \frac{1}{\theta} \Delta d$, e quindi un errore relativo $\frac{\Delta R}{R} = \frac{\Delta d}{d}$.
* Errore sull'angolo $\Delta \theta$ implica un errore assoluto $\Delta R = \left( \frac{1}{\theta + \Delta \theta} - \frac{1}{\theta} \right) d = - \frac{\Delta \theta}{\theta^2} d + o(\Delta \theta)$, e un errore relativo $\frac{\Delta R}{R} = - \frac{\Delta \theta}{\theta}$

avendo usato l'espansione in serie di Taylor per la funzione $f(\Delta \theta)$, valutata in $\Delta \theta = 0$ - nessun errore di misura -, $\frac{1}{\theta + \Delta \theta} = \frac{1}{\theta} - \frac{\Delta \theta}{\theta^2}$, con $f'(\Delta \theta) = - \frac{1}{( \theta + \Delta \theta)^2}$.

<!--
Conti con le misure note ad oggi, cioè sapendo le coordinate delle due città, cioè senza confondere la latitudine di Assuan con quella del Tropico del Cancro, $23^\circ 27' \text{N}$.

-->

```



(physics-hs:modern:astronomy:distance-ladder:moon-sun)=
## Luna e Sole

La Luna è l'unico satellite naturale della Terra. La Luna percorre una traiettoria all'incirca ellittica attorno alla Terra con semiasse maggiore $a_{EM} = 384.4 \cdot 10^{3} \, \text{km}$ ed eccentricità $e = 0.0549$. La Luna ha raggio medio $R_M = 1.738 \cdot 10^{3} \, \text{km}$.

Il Sole è la stella al "centro" del [sistema solare](astronomy-solar-system). La Terra percorre una traiettoria all'incirca ellittica attorno al Sole con semiasse maggiore di circa $a_{ES} = 149.6 \cdot 10^{6} \, \text{km}$ ed eccentricità $e = 0.0167$. La distanza media tra Terra e Sole - poco minore del semiasse maggiore dell'orbita, data la piccola eccentricità dell'orbita stessa - è usata come definizione dell'**unità astronomica**. Il Sole ha raggio medio $R_S = 695.475 \cdot 10^{3} \, \text{km}$.

**Coincidenza astronomica.** Il Sole e la Luna hanno la stessa dimensione (angolare) apparente nel cielo, poiché il valore del rapporto delle loro distanze dalla Terra $\frac{a_{ES}}{a_{EM}} \sim 390$ è simiile al rapporto dei loro raggi $\frac{R_S}{R_M} \sim 400$ - con un errore di circa il 2%. 

```{list-table}
:header-rows: 0
* - ![Eclissi di Sole: durante un'eclissi di Sole](../../media/solar-eclipse.png)
```

**Aristarco di Samo** (**III secolo a.C**) fu in grado di stimare i valori del raggio della Luna e del Sole e le dimensioni delle loro orbite, conoscendo i periodi di rivoluzione della Terra attorno al Sole, e della Luna attorno alla Terra, misurando l'angolo della Luna a metà rispetto alla quadratura, e il tempo necessario alla Luna per entrare in un'eclissi e il tempo di eclissi totale. Aristarco 
- si accorse che il Sole è molto più grande della Terra:
  - alla distanza della Luna dalla Terra, un'approsimazione di raggi solari paralleli produrrebbe quindi una sovrastima delle dimensioni dell'ombra terrestre sulla Luna
  - date le dimensioni relative, è il Sole che gira attorno a un granello come la Terra?
- si imbatté nei limiti tecnologici dell'epoca, nella misura dell'angolo sulla traiettoria in cui la Luna appare a metà. Un errore su un angolo piccolo:
  - produsse un errore grande sulla stima delle dimensioni del Sole e della sua distanza dalla Terra. Aristarco stimò che il raggio del Sole fosse 20 volte più grande del raggio della Terra, invece delle circa 400 volte effettive
  - produsse un errore piccolo sulla stima delle dimesnioni della Luna

````{prf:example} Il metodo di Aristarco

Quando possibile, viene usata l'approssimazione di angoli piccoli che permette di confondere l'angolo (espresso in radianti) con il suo seno e la sua tangente, $\alpha \sim \sin \alpha \sim \tan \alpha$.

```{list-table}
:header-rows: 0
* - ![Metodo di Aristarco](../../media/dynamics/aristarco.png)
```

**Misura dell'angolo $\theta$, e rapporto distanze $\frac{a_{ES}}{a_{EM}}$.** Aristarco pensò di misurare l'angolo $\theta$ tra la posizione della Luna in quadratura e la Luna a metà. La sua misura di $\theta = 2.5^\circ$ portò a una stima del rapporto tra la dimensione dell'orbita della Terra attorno al Sole e della Luna attorno alla Terra di

$$\frac{a_{ES}}{a_{EM}} = \frac{1}{\sin \theta} \sim 22.9 \ .$$

Oggi sappiamo che il valore dell'angolo è circa $0.5^\circ$ e il rapporto è circa $400$. Mentre la stima di Aristarco del rapporto è circa 20 volte (!!!) inferiore al valore reale, la stima del raggio della Luna è poco sensibile a tale errore - vedi sotto - e ciò permise ad Aristarco di trovarne un valore sufficientemente accurato.

**Coincidenza astronomica.** Poiché Luna e Sole hanno la stessa dimensione apparente in cielo, questo permette di scrivere

$$\frac{a_{ES}}{a_{EM}} \sim \frac{R_S}{R_M} \ ,$$

considerato noto da Aristarco. Questo rapporto viene definito $r$.

**Eclissi lunare.** Aristarco usò la misura del tempo impiegato dalla Luna per entrare in eclissi $T_{in}$ e il tempo di eclissi totale $T_{tot}$ per la stima della dimensione del raggio lunare $R_M$,

$$\begin{cases}
  \Omega_M T_{in}  & = \frac{2 R_M}{a_{EM}} \\
  \Omega_M T_{tot} & = \frac{2 \ell - 2 R_M}{a_{EM}} \ ,
\end{cases}$$

con $\ell$ il raggio dell'ombra della Terra sulla traiettoria della Luna. Facendo il rapporto tra le ultime due espressioni, è possibile trovare una relazione tra il raggio lunare e la dimensione dell'ombra,

$$\ell = R_M \left[  1 + \frac{T_{tot}}{T_{in}} \right] \ .$$

Il rapporto tra i tempi viene definito $\tau$. Usando la similitudine dei triangoli,

$$
 R_M  = \frac{1+r}{r} \frac{1}{2+\tau} R_E \ .
$$

```{dropdown} Similitudine triangoli - dettagli

$$\begin{aligned}
 \frac{R_S - R_E}{a_{ES}} & = \frac{R_S - \ell}{a_ES + a_EM} \\
 \frac{r R_M - R_E}{r a_{EM}} & = \frac{r R_M - R_M \left( 1 + \tau \right)}{( r + 1 ) a_{EM}} \\
 \frac{R_{E}}{r} & = R_M \left( 1 - \frac{r}{r+1} + \frac{1+\tau}{1+r} \right) \\
 \frac{R_{E}}{r} & = R_M \frac{2 + \tau}{1 + r} \\
 R_M & = \frac{1+r}{r} \frac{1}{2+\tau} R_E \ .
\end{aligned}$$

```

**Osservazione.** La prima frazione è poco sensibile anche a grandi errori di $r$ per $r \gg 1$: per questa ragione, mentre la stima di Aristarco di $r^{Ari} = 22.9$ era sbagliata di circa $20$ volte rispetto al valore reale $r=400$, il suo effetto nella stima di $R_M$ è molto piccolo

$$\frac{1+r^{Ari}}{r^{Ari}} = 1.044 \quad , \quad \frac{1+r}{r} = 1.0025 \ ,$$

circa il 4%.

**Valore del raggio lunare, $R_M$.** Con la misura dell tempo (massimo) di un'eclissi totale di circa $T_{tot} = 1\text{h}47'$, e il tempo di inizio dell'eclissi $T_{in} = 1 \text{h}$, il rapporto dei tempi è circa

$$\tau = \frac{T_{tot}}{T_{in}} \sim \frac{107'}{60'} = 2.675 \ ,$$

e la stima di Aristarco del raggio lunare è

$$R_M \sim \frac{1.044}{3.783} R_E = 0.284 \cdot R_E \ ,$$

o, con il valore del raggio terrestre $R_E = 6373 \, \text{km}$,

$$R_M \sim 1758 \, \text{km} \ .$$


````


```{prf:example} Raggi paralleli e sovrastima dimensioni dell'ombra terrestre sulla Luna

L'approssimazione di raggi paralleli corrisponde all'ipotesi che l'ombra della Terra sulla Luna abbia le stesse dimensioni della Terra, e quindi equivale a imporre nel sistema di equazioni

$$\begin{cases}
  \Omega_M T_{in}  & = \frac{2 R_M}{a_{EM}} \\
  \Omega_M T_{tot} & = \frac{2 \ell - 2 R_M}{a_{EM}} \ ,
\end{cases}$$

il valore $\ell = R_E$. Dal rapporto tra le due equazioni si ottiene quindi

$$\frac{R_E}{R_M} - 1 = \tau \ ,$$

$$R_M = \frac{1}{1+\tau} R_E$$

```

```{prf:example} Ombra e penombra

Il Sole non è una sorgente luminosa puntiforme...

```


```{prf:example} E.Halley, I.Newton e la gravitazione universale
Halley prevede la periodicità della comparsa della cometa, alla quale fu dato il suo nome, applicando le [leggi della dinamica](physics-hs:mechanics:dynamics) e la [**legge di gravitazione universale di Newton**](physics-hs:mechanics:actions:gravitation:newton).

- 1986: ultima apparizione
- ...
- 1222: ispirazione per le conquiste di G.Khan a occidente
- 1066: segno premonitore per la battaglia di Hastings
```

## Orbite pianeti
Osservazioni astronomiche di:
- N.Copernicus (1473-1573): **modello eliocentrico** e **periodo di rivoluzione** dei pianeti attorno al Sole; dati risalenti alle osservazioni astronomiche dell'età antica
- T.Brahe (1546-1601)

| Pianeta                      | Periodo[^copernicus-britannica-periods]  |
| :--------------------------- | :------------------: |
| Mercurio                     | $88$ giorni          |
| Venere                       | $225$ giorni         |
| Terra                        | $1.0$ anno           |
| Marte                        | $1.9$ anni           |
| Giove                        | $12.0$ anni          |
| Saturno                      | $30.0$ anni          |

[^copernicus-britannica-periods]: [Britannica, Nicolaus Copernicus](https://www.britannica.com/biography/Nicolaus-Copernicus/Copernicuss-astronomical-work)

J.Kepler (1571-1630) fu in grado di definire la **forma delle orbite** e le **dimensioni relative** delle orbite pianeti del sistema solare. I risultati sono riassunti nelle **tre leggi di Keplero**.

```{prf:proposition} Prima legge di Keplero
:label: kepler-first

Le orbite dei pianeti del sistema solare sono ellissi[^kepler-first], e il Sole si trova in uno dei due fuochi.

```

[^kepler-first]: Come viene dimostrato con le equazioni della dinamica di Newton, la tratiettoria ellittica è la traiettoria prevista nel problema dei due corpi. Modelli più raffinati considerano l'influenza della totalità dei pianeti - e non usano le equazioni del problema dei due corpi isolati; per la traiettoria di Mercurio risulta poi non trascurabile l'effetto descritto dalla teoria della relatività generale di Einstein, nella previsione della precessione del perielio.

```{prf:proposition} Seconda legge di Keplero
:label: kepler-second

I pianeti percorrono le orbite con una velocità areolare (con vertice il Sole) costante.

```

```{prf:proposition} Terza legge di Keplero
:label: kepler-third

Il periodo di rivoluzione dei pianeti è proporzionale alla potenza $\frac{3}{2}$ del semiasse maggire $a$ della traiettoria, $T \propto a^{\frac{3}{2}}$, come mostrato in figura {numref}`fig-kepler-3`.

```

<!--
```{list-table}
:header-rows: 0
* - ![Terza legge di Keplero.](script/kepler_third_law.png)
```
-->

(label-target)=
```{figure} script/kepler_third_law.png
---
width: 100%
name: fig-kepler-3
---
Analisi della terza legge di Keplero: confronto tra scala lineare (pianeti interni ed esterni) e scala logaritmica.
```

La dimostrazione delle leggi di Keplero con le [equazioni della dinamica](physics-hs:mechanics:dynamics) e della [legge di gravitazione universale di Newton](physics-hs:mechanics:actions:gravitation:newton), nell'ambito del [sistema dei due corpi](physics-hs:mechanics:dynamics:motion:central), fu uno dei primi successi e verifiche della probabile[^kepler-newton-falsification] bontà della teoria di Newton della dinamica. Vedi anche [moti centrali](physics-hs:mechanics:dynamics:motion:central).

[^kepler-newton-falsification]: Come già mostrato nella sezione sul [metodo scientifico](physics-hs:intro:scientific-method), non esiste una prova definitivia della validità di un modello ma, al contrario, un modello scientifico è un modello sottoposto a continua verifica e la possibilità di essere falsificato: mentre non è possibile avere la certezza assoluta della validità del modello, un sempre numero maggiore di prove e di verifiche aiuta a stabilire i limiti di validità del modello e a confermarne la bontà all'interno di questi limiti.

**todo** *aggiungere lo script sul metodo usato da J.Kepler per la formulazione delle sue leggi a partire dalle misure*

Per stabilire le dimensioni assolute delle orbite nel sistema solare era necessario conoscere almeno una dimensione assoluta: la misura della distanza tra Terra e Sole, definita come **unità astronomica**, $\text{UA}$, fu ottenuta per la prima volta grazie alle misure del 1761 e del 1769 del transito di Venere davanti al Sole.

<iframe 
    src="script/mars_recon_canvas_click_touch.html" 
    width="100%" 
    height="900px" 
    frameborder="0" 
    scrolling="auto">
</iframe>


(physics-hs:modern:astronomy:distance-ladder:sun:venus)=
## Distanza Sole, Terra, Venere
La parallasse solare è usata per stimare la distanza Terra, Venere, Sole osservando il passaggio di Venere tra Terra e Sole da diverse località[^venus-transit-ohio]. **todo** *Usare i dati disponibili sul sito NASA, [NASA, Eclipse Web Site](https://eclipse.gsfc.nasa.gov/OH/transit12.html)*

[^venus-transit-ohio]: [Ohio State University, Astronomy 161: An Introduction to Solar System Astronomy. Lecture 26: Ho Far to the Sun? The Venus Transits of 1761 and 1769](https://www.astronomy.ohio-state.edu/pogge.1/Ast161/Unit4/venussun.html).

Sia $D$ la latitudine di due località differenti, la proiezione delle due immagini di Venere sul Sole hanno distanza $R_S \left( \cos \varphi_1 - \cos \varphi_2 \right)$. I due angoli $\varphi_1$, $\varphi_2 = \varphi_1 + \Delta \varphi$ non erano distinguibili dall'osservazione diretta, ma vengono stimati dal tempo di transito delle due immagini di Venere sul Sole,

$$\frac{\Delta t_2}{\Delta t_1} = \frac{\sin \varphi_2}{\sin \varphi_1}$$

$$\sin \varphi_2 = \sin ( \varphi_1 + \Delta \varphi ) \sim \sin \varphi_1 + \Delta \varphi \, \cos \varphi_1 = \sin \varphi_1 \left[ 1 + \frac{\cos \varphi_1}{\sin \varphi_1} \Delta \varphi \right] $$

$$\Delta \varphi = \left( \frac{\Delta t_2}{\Delta t_1} - 1 \right) \frac{\sin \varphi_1}{\cos \varphi_1}$$

Dalla similitudine dei triangoli per angoli piccoli della parallasse,

$$\dfrac{D}{R_{ES} - R_{VS}} = \dfrac{R_S(\cos \varphi_1 - \cos \varphi_2)}{R_{VS}} \sim \dfrac{R_S(\cos \varphi_1 - \cos \varphi_1 + \Delta \varphi \sin \varphi_1)}{R_{VS}} = \dfrac{R_S}{R_{VS}} \sin \varphi_1 \Delta \varphi$$

e scrivendo la lunghezza del tratto di traiettoria di Venere con due espressioni (usando l'angolo $\theta$ - noto - visto dalla Terra, coincidente con l'angolo di vista del Sole, poiché si considera il passaggio di Venere attraverso quell'angolo di vista; usando l'angolo rispetto al Sole $\psi$, e assumendo una traiettoria circolare qui per semplicità, con $\frac{\psi}{2 \pi} = \frac{\Delta t}{T}$),

$$R_{VS} \psi = (R_{ES} - R_{VS}) \theta \quad \rightarrow \quad \frac{R_{ES}}{R_{VS}} = \frac{\psi}{\theta} - 1 \ ,$$

e usando il rapporto $r = \frac{R_S}{R_{ES}}$ [noto grazie all'eclissi solare](physics-hs:modern:astronomy:distance-ladder:sun) si possono ricavare

$$D = r R_{ES} \frac{\psi}{\theta} \sin \varphi_1 \Delta \varphi 
\quad \rightarrow \quad
R_{ES} = D \frac{\theta}{r \psi} \frac{1}{\sin \varphi_1 \, \Delta \varphi} \ , $$

e dalla stima della distanza Terra-Sole $R_{ES}$ si può risalire alla stima delle altre grandezze $R_{S}$, $R_{VS}$.

## Stelle vicine
Metodo: parallasse usando l'orbita della Terra "attorno al Sole"

## Stelle lontane
Per le stelle lontane, il metodo di parallasse con il moto di rivoluzione della Terra non è sufficiente a fornire una misura (o come nel caso degli antichi della misura della distanza Terra-Sole, la misura è paragonabile all'errore di misura). La parallasse stellare consente di misurare circa il centesimo di arcsec, $\dots \, \text{arcsec}$ o $\frac{1}{\dots} \, \text{parsec}$[^britannica-parallax][^se-parallax][^esa-parallax], con la conversione tra parsec e anno luce $1 \, \text{parsec} = 3.26 \text{a.l.}$

Oggi sappaimo che la Grande Nube di Magellano è di circa $48 \, \text{kpc}$ o $160.000 \, \text{al}$,  **todo** *Ma quali erano i limiti tecnologici nel 1912, all'epoca degli studi di H. Swan Leavitt?*

H.Swan Leavitt: "C'è una notevole correlazione tra la luminosità apparente e il periodo di oscillazione delle stelle variabili". Le variabili più luminose sono quelle con il periodo più lungo. Si assume che le stelle appartenenti alla nube di Magellano siano alla stessa di distanza, e quindi la loro luminosità apparente sia legata alla loro luminosità assoluta dalla stessa costante geometrica.

- H.Hertzsprung (1913) parallasse con il moto del Sole nella Galassia?
- H.Shapley (1918) confronto con stelle cefeide con distanza nota per parallasse?

```{prf:example} Parallasse
:class: dropdown

- Rivoluzione della Terra attorno al Sole
- Moto del Sole: parallasse statistica di Hertzsprung, e calibrazione del diagramma di H-R
  - Moto proprio delle stelle vicine:
    - gli astronomi avevano notato piccoli spostamenti della posizione delle stelle nel tempo; il moto non era casuale, ma si poteva riscontrare unmoto ordinato, riconducibile al moto relativo del Sole rispetto alle altre stelle
    - Herschel (1783) determina la direzione di moto del Sole, detto **apice solare**, di circa $250 \text{km/s}$ rispetto al centro della Galassia (e di circa $20 \, text{km/s}$ rispetto alle stelle vicine. **todo** *controllare*)
    -  dal moto di gruppi di stelle, H stima la distanza media; confronta il moto proprio e la velocità radiale misurata con effetto Doppler; stima della distanza e calibrazione del diagramma H-R
- Missioni spaziali. Esempio: Hubble (1990), Hipparcos (1989-1993), GAIA (2013-...) dell'European Space Agency (ESA).
```

```{prf:example} Conversioni
:class: dropdown

- Parsec: distanza alla quale il raggio dell'orbita terrestre sottende un angolo di un secondo di arco
- anno luce: distanza percorsa dalla luce nel vuoto in un anno
- unità astronomica: distanza Terra-Sole
```
Le misure sulla superficie terrestre dell'intensità della radiazione proveniente dalle stelle consente solo di misurarne la **luminosità apparente**, o il flusso, senza poter determinare indipendentemente la luminosità assoluta - o reale -  e la distanza della sorgente luminosa dall'apparato di misura - la distanza della stella dalla Terra.

Solo l'osservazione delle stelle variabili nella nube di Magellano, a una distanza di circa $$ permise di determinare un'informazione aggiuntiva per misurare indipendentemente luminosità assoluta e distanza. La nube di Magellano è ricca di **stelle variabili**. 

```{dropdown} Luminosità apparente
L'intensità della luce emessa registrato da un osservatore a distanza $r$ dal corpo varia in maniera inversamente proporzionale al quadrato della distanza

$$I \propto \frac{1}{r^2} \ ,$$

poiché il flusso attraverso diverse superfici è costante, e la superficie delle superfici varia con il quadrato della distanza,

$$\overline{\Phi} = I(r) S(r) \propto I(r) r^2 \ .$$

Sulla Terra è possibile misurare direttamente solo l'intensità della radiazione ricevuta, senza poter conoscere indipendentemente luminosità assoluta (intensità emessa) e distanza. Senza altre informazioni misura di un flusso $\overline{\Phi}$ potrebbe venire dalle due stelle seguenti

$$\begin{aligned}
  & \Phi_0, \, r_0 && \\
  & \Phi_1 = 4 \Phi_0 , \, r_1 = 2 r_0 && I_1 \propto \frac{\Phi_1}{r_1^2} = \frac{4 \Phi_0}{(2 r_0)^2} = \frac{\Phi_0}{r_0^2} \propto I_0
\end{aligned}$$
```

```{dropdown} Cefeidi e stelle variabili
```



## La Via Lattea
## Stelle remote e altre galassie



## Riferimenti
[^3b1b-tao-1]: [Terence Tao on how we measure the cosmos | The Distance Ladder Part 1](https://www.youtube.com/watch?v=YdOXS_9_P4U&t=51s) 
[^3b1b-tao-2]: [How to measure the universe | The Cosmic Distance Ladder Part 2](https://www.youtube.com/watch?v=hFMaT9oRbs4) 
[^curiuss-leavitt]: [La Donna che misurò l'Universo - Geni Impolverati\#03 - CURIUSS](https://www.youtube.com/watch?v=OlBVFvuDLVs&t=72s)
[^curiuss-payne]: [La Donna che sussurrava alle stelle - Geni Impolverati\#04 - CURIUSS](https://www.youtube.com/watch?v=q1ZnrXz3NSw&t=538s)
[^nebraska-spectroscpic-parallax]: [Astronomy Education at the University of Nebraska-Lincoln - Cosmic Distance Ladder Lab](https://astro.unl.edu/naap/distance/distance.html)
[^se-parallax]: [SE: What's the farthest object as determined only by parallax?](https://astronomy.stackexchange.com/questions/19666/whats-the-farthest-object-as-determined-only-by-parallax); [SE: Limit of stellar parallax](https://astronomy.stackexchange.com/questions/31711/what-is-the-maximum-distance-measurable-with-parallax) e ulteriori collegamenti.
[^britannica-parallax]: [Enciclopedia Britannica - Parallasse solare](https://www.britannica.com/science/parallax/Solar-parallax)
[^esa-parallax]: [ESA - Educational support: stellar distances](https://sci.esa.int/web/education/-/35616-stellar-distances?fbodylongid=1661) *tenendo conto dell'avviso: Currently, sci.esa.int is under review and not being updated. For the latest information and news from ESA science missions and scientific results, please visit esa.int. For in-depth technical information aimed at ESA's scientific communities, you may also wish to consult cosmos.esa.int.* 

<!--
{cite:p}`FonteToffolRicci2018`
```{bibliography} bibliography.bib
```
-->
