(physics-hs:modern:einstein:special)=
# Relatività speciale

```{prf:axiom} Invarianza delle leggi fisiche
 Non esiste un sistema di riferimento assoluto: il fenomeno fisico è **assoluto**[^relativity-absolute], cioè **invariante**, indipendente dal sistema di riferimento usato per descriverlo.
```
```{prf:axiom} Costanza della velocità della luce
In accordo con le equazioni di Maxwell dell'elettromagnetismo e con l'[esperimento di Michelson-Morley](physics-hs:electromagnetism:em-waves:speed:michelson-morley), la **velocità della luce è costante**. Questa è inoltre la **velocità massima** della trasmissione di informazioni nello spazio, tale da garantire la [**causalità**](physics-hs:todo:causality), vedi [Velocità della luce e causalità](physics-hs:modern:einstein:special:causality).
```

[^relativity-absolute]: A dispetto del nome della teoria, "relatività", e delle vaccate che si sentono "tutto è relativo, come diceva Einstein", la teoria della relatività è un trionfo, il trionfo definitivo, dell'assolutismo: i fenomeni fisici sono indipendenti da chi li osserva, in matematichese sono indipendenti dal sistema di coordinate usato per descrivere il fenomeno; le equazioni della fisica devono quindi essere scritte con oggetti matematici che rispecchiano questa invarianza, i tensori. 
Le equazioni che governano la natura sono invarianti alla scelta del sistema di riferimento usato per descriverle o, detto altrimenti, un fenomeno fisico non dipende da chi lo osserva (almeno se questa osservazione non interagisce con il fenomeno stesso, come succede in meccanica quantistica, vedi[QM:Misura](physics-hs:modern:quantum:basics:measurements), [QM:Indeterminazione di Heisenberg](physics-hs:modern:quantum:basics:uncertainty)).

Esiste però una classe di sistemi di riferimento "privilegiata" per la descrizione del fenomeno fisico (almeno in relatività speciale), la classe dei *sistemi riferimento inerziali*: l'espressione delle equazioni della fisica sono le stesse quando sono scritte con le coordinate di sistemi di riferimento inerziali. Questo non è vero per un sistema di riferimento qualsiasi.

Alcune conseguenze: tempo e spazio non sono più assoluti se presi indipendentemente, lo spazio-tempo lo è; il tempo non è più lo stesso per tutti gli osservatori, e quindi si perde il concetto di simultaneità; le trasformazioni di Galileo non rappresentano più le trasformazioni di coordinate tra due sistemi inerziali: queste devono essere sostituite dalle trasformazioni di Lorentz, le stesse trasformazioni di coordiante rispetto alle quali l'equazione delle onde (come quella ricavata dalle equazioni dell'elettromagnetismo di Maxwell) sono invarianti

- Un **evento** è definito dalle informazioni della posizione e dell'istante temporale (rispetto a un osservatore?) nel quale avviene.

*Rispetto a un'origine $P - O = ct \mathbf{E}_0 + x \mathbf{E}_1$; perché si può definire un sistema di riferimento per tutto lo spazio tempo? Perché in relatività ristretta si considera lo spazio-tempo piatto, non curvo (analogia con lo spazio euclideo, anche se diverso...Minkowski,...)*

```{admonition} FitzGerald
:class: dropdown
bla bla
```

```{admonition} Lorentz
:class: dropdown
bla bla
```

```{admonition} Poincaré
:class: dropdown
bla bla
```

```{admonition} Minkowski
:class: dropdown
bla bla
```

(physics-hs:modern:einstein:special:lorentz)=
## Relatività e trasformazioni di Lorentz

Si ricavano qui le trasformazioni di Lorentz che legano le coordinate spazio-tempo di due osservatori inerziali in moto relativo uniforme, lungo la direzione identificata dalle coordinate $x$, $x'$. Le trasformazioni di Lorentz seguono (quasi) in maniera indolore, dopo aver ribadito (0) la definizione della velocità nello spazio di un evento misurata da un'osservatore, (1) la costanza della velocità di un evento che corrisponde alla propagazione di un segnale luminoso, la cui misura è uguale per ogni osservatore, e (2,3) la simmetria della descrizione del moto relativo:

0. la velocità (3-dimensionale) di un punto rispetto all'osservatore $Oxt$, visto dallo stesso osservatore è definita come la derivata della coordinata spaziale rispetto alla coordinata temporale misurata dall'osservatore,

   $$v = \dfrac{d x}{d t}$$

1. la velocità della luce nel vuoto misurata da entrambi gli osservatori è uguale a $c$ in modulo; quindi i raggi luminosi che viaggiano verso le $x$ e $x'$ positive e in verso opposto sono rispettivamente

  $$
  c = \dfrac{d x_+}{ dt } = \dfrac{d x'_+}{ dt ' }
  \quad , \quad
  - c = \dfrac{d x_-}{ dt } = \dfrac{d x'_-}{ dt ' }
  $$

2. la velocità di $O'$ rispetto a $O$ misurata da $O$ è uguale e contraria alla velocità di $O$ rispetto a $O'$ misurata da $O'$,

   $$v := v_{O'/O} = \dfrac{d x_{O'}}{d t} = - \dfrac{d x'_{O}}{d t'} = - v'_{O/O'}$$

3. l'intervallo di tempo di $O'$ letto da $O$ è uguale all'intervallo di tempo di $O$ letto da $O'$

Per motivi di composizione delle trasformazioni tra più sistemi di riferimento, vedi {prf:ref}`relativity:velocity-composition`, viene considerata una trasformazione lineare. Come dimostrato in seguito, le trasformazioni di Lorentz tra le coordinate dei due sistemi inerziali appena descritti sono (**todo** *ipotesi su una "posizione iniziale" delle origini*)

$$
\begin{cases}
  c t = \gamma \left( c t' - \frac{v}{c} x' \right) \\
    x = \gamma \left(-\frac{v}{c} c t' + x' \right) \\
\end{cases}
\quad , \quad
\begin{cases}
  c t'= \gamma \left( c t' + \frac{v}{c} x  \right) \\
    x'= \gamma \left( \frac{v}{c} c t' + x  \right) \\
\end{cases}
$$

con $\gamma = \left[ 1 - \left(\frac{v}{c}\right)^2 \right]^{-\frac{1}{2}}$. Da queste trasformazioni seguono i fenomeni di *contrazione delle lunghezze*, *dilatazione dei tempi* e il *"paradosso"[^twin-non-paradox] dei gemelli*

[^twin-non-paradox]: Il paradosso dei gemelli non è strettamente un paradosso, è solo una manifestazione dei meccanismi del mondo che sono inaspettati rispetto alla nostra percezione, forgiata sull'esperienza della vita quotidiana. E' solo un esempio in cui i nostri [sensi ci ingannano](physics-hs:intro:sensing:mislead). Secondo la [Treccani](https://www.treccani.it/enciclopedia/paradosso_(Enciclopedia-della-Matematica)/), comunque, il termine "paradosso" può essere applicato nell'accezione ampia a questo genere di situazioni, o affermazioni che contrastano con un'opinione comune o un risultato ritenuto ovvio. Il termine preferibile per un paradosso logico della forma "A e non A" è "antinomia". Esempi di antinomia sono: "questa frase è falsa"; il paradosso del barbiere: un barbiere deve radere tutti e solo le persone che non si radono da sole. Ma chi rade il barbiere? Non può farsi radere da altre persone; se non si rade da solo, infrange la regola perché sta radendo una persona che si rade da sola; se non si rade, allora non sta radendo una persona che non si rade da sola.


```{dropdown} Dimostrazione delle trasformazioni di Lorentz a partire dalle 3 osservazioni

Si parte dalla trasformazione lineare generale tra le coordinate dei due sistemi di riferimento inerziali

$$
\begin{cases}
  c t' = A c t + B x \\
    x' = C c t + D x
\end{cases}
\qquad , \qquad
\begin{cases}
  c t  = A' c t' + B' x' = \frac{D}{AD - BC} c t' - \frac{B}{AD-BC} x'  \\
    x  = C' c t' + D' x' =-\frac{C}{AD - BC} c t' + \frac{A}{AD-BC} x'  
\end{cases}
$$

e si ricavano i valori dei quattro coefficienti $A$, $B$, $C$, $D$ con le condizioni che (1) traducono la costanza della velocità della luce misurata da due osservatori inerziali, e (2,3) la simmetria delle descrizioni relative

1. Un raggio di luce viaggiante verso destra e uno viaggiante verso sinistra hanno rispettivamente velocità

   $$\begin{aligned}
      \pm 1 & = \dfrac{\Delta x_{\pm}}{c \Delta t} \\
      \pm 1 & = \dfrac{\Delta x'_{\pm}}{c \Delta t'} = \frac{C \Delta ct + D \Delta x}{ A \Delta ct + B \Delta x} = \frac{C  + D \frac{\Delta x}{\Delta ct}}{ A  + B \frac{\Delta x}{\Delta ct}} = \frac{C \pm D}{A \pm B}
   \end{aligned}$$

   e quindi le due relazioni

   $$\begin{cases}
      C + D =  A + B \\
      C - D = -A + B \\
   \end{cases}
   \qquad \rightarrow \qquad
   \begin{cases}
       A = D \\
       B = C
   \end{cases}
   $$

<!-- **todo** With derivatives, and not increments
   $$\begin{aligned}
      \pm 1 & = \dfrac{d x_{\pm}}{c dt} \\
      \pm 1 & = \dfrac{d x'_{\pm}}{c dt'} = \dfrac{c dt}{c dt'} \dfrac{d}{c dt} \left( C c t + Dx \right) + \dfrac{dx}{c dt'} \dfrac{d}{dx} \left( C c t + Dx \right)  \\
      & = \frac{D}{AD-BC}\left( C + D \dfrac{d x_{\pm}}{dt} \right) - \frac{C}{AD-BC}\left( C + D \dfrac{d x_{\pm}}{dt} \right)
   \end{aligned}$$
-->
2. Moto relativo di $O$ e  $O'$. La posizione di $O'$ è definita dalla condizione $x'_{O'/O'} = 0$

   $$\frac{v}{c} = \dfrac{\Delta x_{O'/O}}{\Delta c t} = \frac{-\frac{C}{AD-BC} \Delta c t'}{\frac{D}{AD - BC} \Delta c t'}
   \qquad \rightarrow \qquad
   C = - \frac{v}{c} D
   $$

   La posizione di $O$ è definita dalla condizione $x_{O/O}$

   $$- \frac{v}{c} = \dfrac{\Delta x'_{O/O'}}{\Delta c t'} = \frac{C \Delta c t}{A \Delta c t}
   \qquad \rightarrow \qquad
   C = - \frac{v}{c} A
   $$

3. L'ultima relazione deriva dalla simmetria delle letture degli intervalli di tempo

   $$\begin{aligned}
     A \Delta c t_{O'} + B \Delta x_{O'} & = \frac{1}{AD-BC} \left( D \Delta t'_{O} - B \Delta x'_{O} \right) \\
     A  + B \frac{\Delta x_{O'}}{\Delta c t_{O'}} & = \frac{1}{AD-BC} \left( D - B \frac{\Delta x'_{O}}{\Delta t'_{O}}  \right) \\
   \end{aligned}$$

   e quindi, usando $A = D$, $B = C = -\frac{v}{c}A$, $v:=\frac{\Delta x_{O'}}{\Delta c t_{O'}} = - \frac{\Delta x'_{O}}{\Delta c t'_{O}}$

   $$A - \left(\frac{v}{c}\right)^2 A = \frac{1}{A^2 \left[1 - \left(\frac{v}{c}\right)^2 \right]} A \left[ 1 - \left(\frac{v}{c}\right)^2 \right]$$

   e risolvendo, si possono ricavare i coefficienti della trasformazione di Lorentz,

   $$\begin{aligned}
      A & = D = \frac{1}{\sqrt{1 - \left( \frac{v}{c} \right)^2}} \\
      B & = C = - \frac{v}{c} \frac{1}{\sqrt{1 - \left( \frac{v}{c} \right)^2}} 
   \end{aligned}$$

```


(physics-hs:modern:einstein:special:causality)=
## Velocità della luce e causalità



```{prf:example} Trasformazione di coordinate tra 3 sistemi di riferimento e composizione delle velocità
:label: relativity:velocity-composition

Nemmeno continuando a comporre velocità positive può essere superata la velocità della luce...

```

## Dilatazione dei tempi e contrazione delle lunghezze

## "Paradosso" dei gemelli

## Geometria della relatività speciale
Intervallo tra due eventi(invariante); tempo proprio; metrica di Minkowski



