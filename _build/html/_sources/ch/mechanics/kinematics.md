<!--
````{only} html
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
````
-->

(physics-hs:mechanics:kinematics)=
# Cinematica

La cinematica si occupa della descrizione del moto dei sistemi, senza indagarne le cause. La cinematica si occupa della descrizione dello stato di un sistema, e della sua variazione, nello **spazio** in funzione del **tempo**.

**Cosa si intende per spazio e per tempo in meccanica classica?** Il modello di spazio che aveva in mente Newton - e che può essere ritenuto un ottimo modello di spazio in molte circostanze anche oggi - è lo **spazio Euclideo**, nel quale non ci sono direzioni o posizioni "speciali" (isotropo e uniforme), e nel quale valgono i postulati e i risultati della geometria euclidea. Questo modello di spazio 3-dimensionale può essere descrito dalle coordinate cartesiane, e la distanza tra due punti può essere calcolata con il teorema di Pitagora applicato alle differenze di coordinate. Dal punto di vista operativo, lo spazio è quell'entità fisica nella quale si possono misurare distanze e angoli con **righello** e **gonomiometro** (o altri strumenti meno rudimentali). Una volta scelto un punto dello spazio come origine, i punti dello spazio possono essere rappresentati come vettori di uno spazio euclideo.
Il **tempo** invece può essere definito come la grandezza fisica associabile al susseguirsi degli eventi e che può essere misurata con un **orologio**.

In meccanica classica, spazio e tempo sono considerati **indipendentemente entità assolute**[^spacetime-einstein], cioè indipendenti dall'osservatore: due osservatori diversi dotati di strumenti per la misura di distanze, angoli e tempo (accurati e tarati), concordano sulla misura della distanza tra qualsiasi coppia di punti dello spazio, dell'angolo tra qualsiasi coppia di direzioni e di qualsiasi intervallo di tempo. Come discusso nell'esempio {prf:ref}`invariance-space-and-time`, due osservatori che usano sistemi di coordinate diversi possono non concordare sulle coordinate dei punti ma concordano sulle distanze e sugli angoli.

[^spacetime-einstein]: Questo non è più vero nella [meccanica di Einstein](physics-hs:modern:einstein:special), teoria compatibile con i fenomeni elettromagnetici e l'evidenza sperimentale che la velocità della luce è finita. Nell'ambito della teoria della relatività di Einstein, spazio e tempo non sono più due entità assolute: due osservatori in moto relativo non concordano sulle misure di lunghezze, di angoli e di intervalli di tempo. Spazio e tempo sono due componenti di un'entità assoluta 4-dimensionale, lo spazio-tempo. Potrà sembrare strano, ma così è: è sempre bene ricordarsi che la nostra esperienza quotidiana è abbastanza limitata e di come i nostri sensi possono ingannarci.

La posizione di un punto nello spazio euclideo è rappresentabile con un vettore (una volta scelto un punto come origine nello spazio); un istante di tempo è rappresentabile con un numero scalare. La descrizione generale di una rotazione nello spazio 3-dimensionale richiede strumenti al di fuori dello scopo di questo materiale, i tensori; limitandoci qui al moto piano di sistemi estesi, la rotazione in un moto piano può essere rappresentata con l'angolo di rotazione rispetto a una direzione di riferimento (e quindi una quantità scalare) o con un vettore ortogonale al piano del moto di valore modulo uguale all'angolo di rotazione. La discussione generale della cinematica dei corpi rigidi nello spazio 3-dimensionale viene affrontata nel materiale di [meccanica per gli studenti universitari](https://basics2022.github.io/bbooks-physics-mechanics/ch/kinematics.html).

```{prf:example} Invarianza di spazio e tempo.
:label: invariance-space-and-time
:class: dropdown

Dati i punti nel piano, $A$, $B$, $C$, ... e due osservatori... 
 
$$\begin{cases}
x_2 = \dots \\
y_2 = \dots \\
\end{cases}$$

essi non concordano sulle coordinate e l'istante dei tre eventi,


ma concordano sulle distanze, sugli angoli (e sull'area, come concorderebbero sul volume di solidi), e sull'intervallo temporale tra i tre eventi,


```

```{prf:definition} Configurazione di un sistema
:label: system-configuration

La **configurazione di un sistema** viene definita da un insieme minimo (non ridondante) di variabili indipendenti, o coordinate, dette **gradi di libertà**.  Il numero di gradi di libertà di un sistema dipende dalla dimensione dello spazio nel quale avviene il moto, dal numero e dal tipo degli elementi che lo compongono e dai vincoli che connettono gli elementi del sistema tra di loro o con l'ambiente esterno.
```

La scelta dell'insieme dei gradi di libertà usati per descrivere la configurazione di un sistema non è univoca, e di solito viene guidata da un criterio di "comodità" e di "semplicità" del problema da risolvere. La scelta dei gradi di libertà non influenza la configurazione del sistema, che è quindi *invariante* alla scelta dei gradi di libertà.

```{prf:definition} Stato di un sistema
:label: system-state

In generale, in meccanica classica lo **stato di un sistema** è definito dalla sua configurazione e dalla derivata prima nel tempo delle variabili che definiscono i gradi di libertà: questo è sensato per sistemi meccanici la cui dinamica è governata da *equazioni differenziali ordinarie del secondo ordine*.
```

La configurazione di un **punto libero** nello [spazio euclideo $E^n$](https://basics2022.github.io/bbooks-math-miscellanea-hs/ch/analytic_geometry/euclidean_space.html) ($n=2$ piano, $n=3$ spazio) è definita dalla sua posizione nello spazio, tramite un insieme di $n$ coordinate:
- un punto libero nel piano ha 2 gradi di libertà (traslazione);
- un punto libero nello spazio ha 3 gradi di libertà (traslazione). 

La configurazione di un **corpo rigido libero** è definita dalla posizione di un suo punto nello spazio e dalla sua orientazione: 
- un corpo rigido nel piano ha 3 gradi di libertà, 2 per definire la posizione di un suo punto nello spazio (traslazione) e 1 per definire la sua orientazione (rotazione) rispetto a un asse ortogonale al piano; 
- un corpo rigido nello spazio ha 6 gradi di libertà, 3 per definire la posizione di un suo punto nello spazio (traslazione) e 3 per definire la sua orientazione (rotazione)

