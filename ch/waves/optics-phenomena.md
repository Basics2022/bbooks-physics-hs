(physics-hs:waves:optics:geometric:phenomena)=
# Fenomeni ondulatori in ottica


## Interferenza - o sovrapposizione di cause ed effetti
In molti casi, i fenomeni ondulatori sono meccanismi di trasmissione di un'informazione in sistemi lineari, nei quali vale il **principio di sovrapposizione di cause e degli effetti**.

## Polarizzazione

## Effetto Doppler
L'effetto Doppler[^doppler-1842] è un effetto dovuto al moto relativo tra sorgente e ricevente, che è origine della differenza tra la frequenza del segnale emesso dalla sorgente del segnale e la frequenza del segnale misurato dal ricevente.

```{prf:example} Red-shift
```

## Riflessione

## Rifrazione

(physics-hs:waves:optics:geometric:phenomena:snell)=
### Rifrazione discreta - Legge di Snell e coefficienti di Fresnel

- Legge di Snell per la direzione di trasmissione

   $$ \dfrac{\sin \theta_2}{\sin \theta_1} = \dfrac{n_2}{n_1}$$

- Coefficienti di Fresnel per la polarizzazione della luce riflessa e trasmessa

```{prf:example} Arcobaleno
```

```{prf:example} Riflessione totale
```

```{prf:example} Polarizzazione della luce riflessa
```

### Rifrazione continua - Principio di Fermat

```{prf:example} Miraggi
```
```{prf:example} Schlieren 
```
```{prf:example} Osservazioni astronomiche attraverso l'atmosfera
```

(physics-hs:waves:optics:geometric:phenomena:dispersion)=
## Dispersione
Alcuni materiali sono dispersivi, cioè la velocità di propagazione nel materiale di una perturbazione dipende dalla sua frequenza, $c(f)$, e quindi il coefficiente di rifrazione è funzione della frequenza,

$$n(f) = \frac{c_0}{c(f)} \ .$$


```{prf:example} Prismi, tra Newton, Pink Floyd e [spettrografia](physics-hs:waves:optics:applications:spectrography)
:label: em-waves:dispersion:prism

Un prisma costruito con un materiale dispersivo permette di scomporre la radiazione elettromagnetica nei suoi componenti elementari con diversa frequenza (e quindi lunghezza d'onda).

Ad esempio, l'acqua ha un indice di rifrazione che varia da $n_{red} = 1.33$ per la radiazione con lunghezza d'onda $\lambda_{red} = 700 \, \text{nm}$ corrispondente alla luce di colore rosso, a $n_{violet} = 1.339$ per la radiazione con lunghezza d'onda $\lambda_{violet} = 400 \, \text{nm}$ corrisponendente alla luce di colore viola.

Legame tra lunghezza d'onda e frequenza: $c = \frac{\omega}{k} = \lambda \, f$, dalle relazioni $\omega = 2 \pi f$, $\lambda = \frac{2 \pi }{k} = \frac{c}{f}$.

Il comportamento della radiazione descritta dai [principi dell'ottica geometrica](physics-hs:waves:optics:geometric:principles), e dalla legge di Snell in particolare, prevede che l'angolo di rifrazione della luce trasmessa dipende quindi dalla lunghezza d'onda,

$$\sin \theta_t(f) = \frac{n_1}{n_2(f)} \, \sin \theta_i(f) \ .$$

A seconda del contenuto in frequenza della radiazione, la scomposizione del segnale può manifstarsi:
- per **spettri continui** come la formazione di un arcobaleno con un angolo più piccolo rispetto alla normale alla superficie per il colore viola e un angolo maggiore per il colore rosso. Ad esempio, con un angolo di incidenza $\theta_i = 45^\circ$, l'angolo formato dalla radiazione viola è di $31.85^\circ$ mentre l'angolo della radiazione rossa è $32.11^\circ$.
- per **spettri discreti** come la formazione di una serie di righe spettrali corrispondenti alle componenti discrete nel segnale

```

```{prf:example} Arcobaleno

**Arcobaleno principale.**

**Arcobaleno secondario.**

```

(physics-hs:waves:optics:geometric:phenomena:diffraction)=
## Diffrazione
...

---
**Riferimenti.**
[^young-1802]: Thomas Young, 1802, *Theory of Light and Colours*.

[^doppler-1842]: C.A.Doppler, 1842 *On the coloured light of the binary stars and some other stars of the heavens*. L'effetto Doppler viene proposto per la prima volta nel 1842, nell'ambito delle osservazioni astronomiche. ...la pubblicazione avviene prima della formulazione completa delle equazioni di Maxwell e quindi dell'esistenza di un primo modello matematico che riconoscesse la luce come fenomeno elettromagnetico. Nonostante questo, seguendo i risultati di T.Young, Doppler è convinto che la luce sia un fenomeno ondulatorio. Oltre alla discussione dell'effetto Doppler, la pubblicazione conteine altre affermazioni/convinzioni di Doppler sulla natura della luce, non supportate da prove o evidenze, che si riveleranno sbagliate (es. luce come onda longitudinale)
