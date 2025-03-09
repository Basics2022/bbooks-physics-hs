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

## Distanza Terra-Luna e dimensioni Luna
Metodo: eclisse lunare per la distanza; sorgere della Luna per le dimensioni

## Dimensioni Sole e Distanza Sole-Luna
Metodo:
- eclisse solare per il rapporto dimenisoni-distanza $\frac{R_S}{R_M} = \frac{D_{ES}}{D_{EM}}$;
- fasi lunari per la distanza Terra-Sole. Il metodo utilizzato dagli antichi ha però una sensibilità della misura alla variabile misurata enorme, e la tecnologia allora disponibile non consentiva misure precise della variabile misurata;...

## Orbite pianeti
Keplero: ...

## Stelle vicine
Metodo: parallasse usando l'"orbita della Terra attorno al Sole"

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
