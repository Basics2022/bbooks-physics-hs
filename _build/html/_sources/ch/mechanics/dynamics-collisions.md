(physics-hs:mechanics:dynamics:collisions)=
# Collisioni

Una descrizione dettagliata delle collisioni tra sistemi qualsiasi va ben al di là dello scopo di un primo approccio alla meccanica.

Qui, ci si limiterà allo studio di collisioni che:
- possono essere caratterizzate unicamente da un *coefficiente di ritorno*, $\varepsilon$ **todo**
- avvengono in intervalli di tempo ridotti, al limite nulli

Questi urti comportano delle variazioni finite delle quantità dinamiche in intervalli di tempo finiti, vengono definiti **urti impulsivi** (**todo** *verificare*) e  rappresentano un esempio di moto "non regolare", per il quale le equazioni cardinali della dinamica devono essere scritte in forma incrementale.

**todo** *approfondimento su forze impulsive e delta di Dirac?*

Tra due istanti temporali immediatamente precedente e immediatamente successivo all'urto tra due sistemi possono essere trascurate tutte le azioni agenti sul sistema complessivo tranne quelle **impulsive** dovute all'**urto**, e ad eventuali **reazioni vincolari** (vedi esercizi),

$$\begin{aligned}
  \vec{I}^{ext}   & = \Delta \vec{Q} = \Delta \vec{Q}_1 + \Delta \vec{Q}_2 \\
  \vec{J}_H^{ext} & = \Delta \vec{\Gamma}_H + \dot{\vec{x}}_H \times \Delta \vec{Q} = \Delta \vec{\Gamma}_{H,1} + \Delta \vec{\Gamma}_{H,2} \\
  L^{ext} + L^{int} & = \Delta K = \Delta K_1 + \Delta K_2 \ ,
\end{aligned}$$



E' bene osservare che in assenza di forze e momenti impulsivi esterni - anche dovuti a eventuali vincoli - ai due sistemi che collidono, la quantità di moto e il momento della quantità di moto del sistema complessivo si conservano in un urto.
Al contrario, in generale, l'**energia cinetica non si conserva** poiché dipende anche dalla potenza delle azioni interne che includono quelle impulsive scambiate durante l'urto.

## Problemi

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione tra blocchi su piano orizzontale liscio
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-1d.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione tra blocchi su piano orizzontale scabro
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-1d-friction.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Rimbalzo di una palla
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-bouncing-ball.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione di un sistema massa-molla con una parete
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-bouncing-block-spring.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisioni tra due blocchi e una parete rigida
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-bouncing-blocks.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Proiettile su pendolo con massa concentrata
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-pendulum-0.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Proiettile su pendolo con massa distribuita
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-pendulum-1.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Proiettile su bersaglio di poligono di tiro
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-pendulum-2.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione su sistema libero rigido di masse concentrate
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-rod-1.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```

<!-- Esercizio ************************************************************* -->
::::{grid}
:gutter: 2

:::{grid-item-card} Collisione su sistema libero rigido a massa distribuita
:columns: 8

:::

:::{grid-item-card} 
:columns: 4

![](../../media/collisions-rod-2.png)
<!-- *Didascalia, se necessaria* -->
:::

::::

```{dropdown} Soluzione.
```
