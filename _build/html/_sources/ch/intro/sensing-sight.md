(physics-hs:intro:sensing:sight)=
# Vista
La vista è il senso che permette di recepire stimoli luminosi attraverso i nostri occhi. Lo stimolo luminoso è uno stimolo elettromagnetico che può essere percepito dall'occhio umano. Una perturbazione elettromagnetica può essere caratterizzata da intensità e frequenza - o analogamente, lunghezza d'onda: l'occhio umano è in grado di recepire segnali elettromagnetici con lunghezza d'onda tra circa i $400 \, \text{nm}$ e i $700 \, \text{nm}$.

Seguendo il percorso lungo la catena di misura dello stimolo esterno, la radiazione elettromagnetica, che arriva all'occhio:
- viene raccolta dalla parte anteriore dell'occhio e indirizzata verso la zona della retina dove sono presenti i fotorecettori, addetti a convertire il segnale elettromagnetico in stimolo nervoso. L'azione di pupilla e cristallino operano come l'apertura e la messa a fuoco di una [lente](physics-hs:waves:optics:geometric:lenses):
  - l'**apertura** della **pupilla** permette di regolare la potenza del segnale da inviare ai fotorecettori: in condizione di luce intensa, la pupilla mantiene limitata la potenza del segnale riducendo il suo diametro, e quindi la superficie attraverso quale passa la perturbazione luminosa; in condizioni di luce poco intensa la pupilla si dilata per permettere il passaggio di una quantità maggiore di luce poco intensa;
  - il **cristallino** - in combinazione con le altre regioni dell'occhio - permette la **messa a fuoco** del segnale sulla retina, dove sono presenti i fotorecettori che devono convertire il segnale in stimoli nervosi
- nella zona centrale della retina, i fotorecettori convertono i segnali elettromagnetici in segnali nervosi; questi vengono trasdotti dal nervo ottico al cervello, dove avviene l'elaborazione del segnale.


**Riferimenti e sezioni future:** [Lenti](physics-hs:waves:optics:geometric:lenses); [Ottica e occhio](physics-hs:waves:optics:eye); [Onde elettromagnetiche](physics-hs:electromagnetism:em-waves).

(physics-hs:intro:sensing:sight:photoreceptors)=
## Fotorecettori e intensità luminosa
Nell'occhio umano esistono due tipi differenti di fotorecettori:
- i coni, specializzati nella visione dei colori; visione fototipica con intensità luminosa sufficientemente intensa; esistono tre tipi di conoi nell'occhio umano[^eye-cones-animals]; i coni sono sensibili a illuminazione superiore a circa $10^{-3} \, cd/m^2$
- i bastoncelli, specializzati nella visione del movimento e dei contorni; i bastoncelli hanno un'alta sensibilità alla luce rispetto ai coni (cioè sono in grado di percepire luce di intensità minore), ma non sono in grado di distintuere i colori;

[^eye-cones-animals]: In alcuni animali l'occhio può avere un numero diverso di tipi di coni, specializzati su diverse lunghezze d'onda della radiazione elettromagnetica. Riferimenti: [Do colours which are not visible to human eyes exist?](https://physics.stackexchange.com/q/786679). Non è così raro che anche l'occhio umano abbia un quarto tipo di cono a casua di variazioni genetiche (circa il 12% delle donne). Questo significa che vedono un maggior numero di colori? Può essere, ma in generale no, poiché il quarto cono dovrebbe essere specializzato su segnali diversi dagli altri tre coni - per poter aggiungere informazioni - e il cervello deve essere in grado di processare queste informazioni - per effettivamente aggiungere dettagli alla nostra rappresentazione.

In diverse condizioni di luminanza $[lux]$, partecipano al senso della vista diversi fotorecettori ed è quindi possibile distinguere tre diversi di visione:
- $L = 10^{-2} - 10^{5} \text{ lux}$ visione fotopica, cioè la visione a colori grazie ai coni
- $L = 10^{-2} - 10^{0} \text{ lux}$ visione mesopica, cioè la visione dovuta all'attività contemporanea di coni e bastoncelli; è tipica della luce crepuscolare[^eye-day-luminance]
- $L = 10^{-5} - 10^{0} \text{ lux}$ visione scotopica, cioè la visione notturna dovuta ai bastoncelli.

[^eye-day-luminance]: [Intervalli di luminosità della vista umana](https://www.researchgate.net/figure/Approximate-luminance-ranges-of-human-vision-and-corresponding-photoreceptors_fig2_50297383). La luminosità durante una giornata può variare di diversi ordini di grandezza, passando dai $10^{-6}-10^{-4} \, cd/m^2$ di una notte senza luna, $10^{-3}-10^{-1} \, cd/m^2$, $10^{0}-10^{1} \, cd/m^2$ del crepuscolo, $10^{1}-10^{3} \, cd/m^2$ di un ambiente chiuso illuminato, $10^{3}-10^{6} \, cd/m^2$ in ambiente aperto in una giornata limpida di sole.

**todo** Uniformare unità di misura $lux$ e $cd/m^2$; distinguere fra regimi di visione e partecipazione di coni e bastoncelli; fare riferimento a paragrafo su luce e grandezze legate all'intensità (forse sulla versione in inglese)

(physics-hs:intro:sensing:sight:avg-eye)=
## Intensità luminosa e occhio medio

- definizione di occhio medio
- definizione di un'unità di misura che dipende dalla percezione umana, la [*candela*]()
- metodo: fotometria con flicker[^flicker-photometry] per la costruzione della [funzione di trasferimento](physics-hs:intro:measurements:order) dei fotorecettori, intensità in funzione della lunghezza d'onda del segnale

[^flicker-photometry]: Esempio di [flicker photometry](https://www.youtube.com/watch?v=XAPTrzODofw) per determinare la funzione di trasferimento dell'occhio umano ai diversi colori; il rapido sfarfallamento - il flickering - di diverse coppie degli stessi colori a frequenze $f_1$, $f_2$ a diverse differenze di intensità $I_{1,k}$ $I_{2,k}$, permette di determinare la sensibilità relativa dell'occhio umano ai due colori: indicando il "pallino" $k^*$ nel quale non viene percepito sfarfallare di intensità, e conoscendo l'intensità "vera" dei due segnali $r = I^*_{1}(f_1)/ I^*_{2}(f_2)$ **todo** specificare meglio il funzionamento, magari nella sezione sull'[intensità luminosa](physics-hs:intro:physical-quantities:luminosity).


