(physics-hs:modern:astronomy:distance-ladder)=
# Scala delle distanze cosmiche

In questa pagina viene ripercorso il calcolo delle distanze cosmiche, secondo quella che viene definita la **scala delle distanze cosmiche**: partendo dalle dimensioni e dalle distanze, di Terra, Luna e Sole, passando per le dimensioni e la forma delle orbite dei pianeti, continuando con la distanza delle stelle vicine e le dimensioni della nostra galassia, la Via Lattea, e finendo con la distanza della stelle remote e delle altre galassie.

L'aumento delle distanze misurate procede in un ordine cronologico, grazie alla costruzione di nuove conoscenze delle conoscenze pregresse, al progresso tecnologico che fornisce strumenti più precisi e alla scoperta e alla comprensione di nuovi fenomeni fisici utili nella misura di oggetti così remoti. Il racconto viene costruito seguendo l'ordine presentato nei consigliatissimi video di 3Blue1Brown con Terence Tao[^3b1b-tao-1][^3b1b-tao-2], con l'aggiunta di dettagli degli ancora più consigliatissimi video di Alan Zamboni, aka CURIUSS, su Henrietta Swan Leavitt[^curiuss-leavitt] e Cecilia Payne-Gaposchkin[^curiuss-payne], gli osservatori e le donne di Harvard, Schwarzshild, e i due studiosi Hertzsprung-Russell del diagramma, e il materiale fornito dall'Università del Nebraska[^nebraska-spectroscpic-parallax].

Qualitativamente possono essere riconosciute diverse fasi:
- antichità: Terra, Luna, Sole
- età moderna: Copernico e Keplero: orbite dei pianeti;...
- età contemporanea: Donne calcolatrici di Harvard;...; Hubble e red-shift (dimensioni ed espansione dell'universo)

## Dimensioni Terra
Metodo: ombra di un bastone normale

$$R_E = 6.37 \cdot 10^{3} \, km $$

## Distanza Terra-Luna e dimensioni Luna
Metodo: eclisse lunare per la distanza; sorgere della Luna per le dimensioni

$$\begin{aligned}
  R_{EM} & = \dots \\
  R_{M}  & = \dots \\
\end{aligned}$$

(physics-hs:modern:astronomy:distance-ladder:sun)=
## Dimensioni Sole e Distanza Sole-Terra
La coincidenza che si può osservare durante le **eclissi solari** permette di stimare il rapporto tra le dimensioni del Sole e la distanza Terra-SOle

$$\frac{R_{S}}{R_{ES}} \sim \frac{R_{M}}{R_{EM}} \ .$$

Per calcolare i valori assoluti, serve poter detemrminare una delle due grandezze fisiche, come ad esempmio la distanza Terra-Sole:
- gli antichi greci stimarono la distanza Terra-Sole usando le fasi lunari: il metodo usava la misura dell'angolo in cui si osservava la mezza luna (che non corrisponde con la quadratura). Il metodo utilizzato dagli antichi incontrava i limiti tecnologici disponibili all'epoca, a cominciare dall'assenza di strumenti affidabili per misurare il tempo, soprattutto durante la notte; poichè la misura si fonda sulla misura di un angolo "piccolo", un piccolo errore ha ripercussioni enormi sulla stima della distanza: così, i greci stimarono una distanza Terra-Sole circa 20 volte il valore attualmente accettato, **todo** *discutere limiti tecnologici, sensibilità di errori di misura, metodi per ridurre incertezza con misure ripetute...; collegamento a strumenti per la misura del tempo*
- ...bisogna aspettare il XVII e il XVIII secolo per la proposta di J.Gregory e **E.Halley** (1656-1742) e la realizzazione della misura che sfruttasse la [parallasse solare durante il passaggio di Venere davanti al Sole avvenuto nel 1761 e nel 1769](physics-hs:modern:astronomy:distance-ladder:sun:venus), dati riassunti da J.Lalande nel 1771 nella misura di 8.6" di parallasse solare, equivalente a circa 24000 raggi terrestri, circa il 2.5\% maggiore della misura comunemente accettata oggi (di cosa? raggio medio? semiasse maggiore?...).

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

Il periodo di rivoluzione dei pianeti è proporzionale alla potenza $\frac{3}{2}$ del semiasse maggire $a$ della traiettoria, $T \sim a^{\frac{3}{2}}$.

```

La dimostrazione delle leggi di Keplero con le [equazioni della dinamica](physics-hs:mechanics:dynamics) e della [legge di gravitazione universale di Newton](physics-hs:mechanics:actions:gravitation:newton), nell'ambito del [sistema dei due corpi](physics-hs:mechanics:dynamics:motion:central), fu uno dei primi successi e verifiche della probabile[^kepler-newton-falsification] bontà della teoria di Newton della dinamica. Vedi anche [moti centrali](physics-hs:mechanics:dynamics:motion:central).

[^kepler-newton-falsification]: Come già mostrato nella sezione sul [metodo scientifico](physics-hs:intro:scientific-method), non esiste una prova definitivia della validità di un modello ma, al contrario, un modello scientifico è un modello sottoposto a continua verifica e la possibilità di essere falsificato: mentre non è possibile avere la certezza assoluta della validità del modello, un sempre numero maggiore di prove e di verifiche aiuta a stabilire i limiti di validità del modello e a confermarne la bontà all'interno di questi limiti.

**todo** *aggiungere lo script sul metodo usato da J.Kepler per la formulazione delle sue leggi a partire dalle misure*

Per stabilire le dimensioni assolute delle orbite nel sistema solare era necessario conoscere almeno una dimensione assoluta: la misura della distanza tra Terra e Sole, definita come **unità astronomica**, $\text{UA}$, fu ottenuta per la prima volta grazie alle misure del 1761 e del 1769 del transito di Venere davanti al Sole.

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
