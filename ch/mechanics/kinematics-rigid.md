```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```

(physics-hs:mechanics:kinematics:rigid)=
# Cinematica di un corpo rigido

La cinematica di corpo rigido è definita dalla posizione di un suo punto materiale e dalla propria orientazione in funzione del tempo. In generale, per definire la posizione di corpo rigido nello spazio 3-dimensionale servono 6 parametri: 3 coordinate per definire la posizione di un punto materiale $Q$ e 3 parametri per definire l'orientazione del corpo nello spazio. Per definire la posizione di un corpo rigido che compie un moto piano servono 3 parametri: 2 coordinate per definire la posizione di un punto e 1 parametro per definirne l'orientazione.

**todo** definizione di moto piano

```{note}
Questo materiale è rivolto a studenti delle scuole superiori, e si limita a discutere il moto 2-dimensionale di corpi rigidi. Una discussione del moto 3-dimensionale di corpi rigidi richiede l'uso e la dimestichezza con oggetti matematici che non sono introdotti nei primi anni delle scuole superiori - e purtroppo troppo spesso nemmeno nei corsi universitari dei primi anni -, i tensori.

Al prezzo di non poter trattare i problemi meccanici più generali, questa scelta evita di richiedere la conoscenza dell'algebra tensoriale o di introdurre formule in forma quantomeno discutibile. Per una discussione completa del problema, si rimanda al materiale pensato per studenti più maturi: **todo**
- algebra vettoriale e tensoriale **todo**
- meccanica classica **todo**
```

<!--
(physics-hs:mechanics:kinematics:rigid-2d)=
## Problemi nel piano
-->

## Posizione dei punti di un corpo rigido

- **Posizione del un punto materiale di riferimento, $Q$.** 

$$Q - O = \vec{r}_Q$$

- **Posizione di tutti i punti materiali $P$ del corpo rigido, e orientazione del corpo.** Nell'ipotesi di moto 2-dimensionale, il vettore tra due punti materiali $\vec{r}_{QP} = P-Q$ può essere scritto in funzione del vettore $\vec{r}_{QP}^0$ nella configurazione di riferimento del corpo e della rotazione di un angolo $\theta$ attorno a un asse di direzione $\hat{n}$ costante e perpendicolare al piano del moto,

$$P - Q = \vec{r}_{QP} = \cos \theta \, \vec{r}_{QP}^0 + \sin \theta \, \hat{n} \times \vec{r}_{QP}^0$$

  La posizione di un punto materiale $P$ di un corpo rigido rispetto al sistema di riferimento scelto, può essere quindi scritta come

  $$\begin{aligned}
    P - O & = Q - O + P - Q = \\
          & = \vec{r}_{OQ} + \cos \theta \, \vec{r}_{QP}^0 + \sin \theta \, \hat{n} \times \vec{r}_{QP}^0  \ .
  \end{aligned}$$

## Velocità dei punti di un corpo rigido
- **Velocità del punto materiale di riferimento, $Q$**

$$\vec{v}_Q = \dfrac{d \vec{r}_Q}{dt}$$

- **Velocità di tutti i punti materiali $P$ del corpo rigido, e velocità angolare del corpo**, $\vec{\omega} = \dot{\theta} \hat{n}$. La velocità relativa di un punto $P$ rispetto al punto di riferimento $Q$ viene calcolata con la derivata del vettore $\vec{r}_{QP}$ rispetto al tempo, ricordando che $\hat{n}$ è costante e quindi $\frac{d}{dt} \hat{n} = \vec{0}$,

  $$\begin{aligned}
    \dfrac{d \vec{r}_{QP}}{dt} 
    & = \dfrac{d}{dt} \left(  \cos \theta \, \vec{r}_{QP}^0 + \sin \theta \, \hat{n} \times \vec{r}_{QP}^0 \right) = \\
    & = \dot{\theta} \left( -\sin \theta \, \vec{r}_{QP}^0 + \cos \theta \, \hat{n} \times \vec{r}_{QP}^0 \right) = \\
    & = \dot{\theta} \hat{n} \times \left( \sin \theta \, \hat{n} \times \vec{r}_{QP}^0 + \cos \theta \, \vec{r}_{QP}^0 \right) = \\
    & = \dot{\theta} \hat{n} \times \vec{r}_{QP} = \\
    & = \vec{\omega} \times \vec{r}_{QP} \ ,
  \end{aligned}$$ 

  avendo definito la **velocità angolare**, $\vec{\omega} = \dot{\theta} \hat{k}$ per un moto 2-dimensionale, e usato l'identità vettoriale 

  $$\vec{n} \times (\vec{n} \times \vec{w}) = \hat{n} \underbrace{(\hat{n} \cdot \vec{w})}_{=0} - \vec{w} \underbrace{(\hat{n} \cdot \hat{n})}_{=1} = - \vec{w} \ .$$

```{note}
La formula 

$$\vec{v}_P - \vec{v}_Q = \vec{\omega} \times (P - Q)$$

vale anche per moti 3-dimensionali. In questo caso però **non** è possibile scrivere $\vec{\omega} = \dot{\theta} \hat{n}$.
  ```

  La velocità di un punto materiale $P$ di un corpo rigido rispetto al sistema di riferimento scelto, può essere quindi scritta come

  $$\begin{aligned}
    \vec{v}_P & = \vec{v}_{Q/O} + \vec{v}_{P/Q} = \\
              & = \vec{v}_{Q/O} + \vec{\omega} \times (P - Q) \ .
  \end{aligned}$$

## Accelerazione dei punti di un corpo rigido
- **Accelerazione del punto materiale di riferimento, $Q$**

$$\vec{a}_P = \dfrac{d \vec{v}_P}{dt} = \dfrac{d^2 \vec{r}_P}{d t^2}$$

- **Accelerazione di tutti i punti materiali $P$ del corpo rigido, e accelerazione angolare del corpo**, $\vec{\alpha} = \dot{\vec{\omega}} = \ddot{\theta} \hat{n}$. L'accelerazione relativa di un punto $P$ rispetto al punto di riferimento $Q$ viene calcolata con la derivata seconda del vettore $\vec{r}_{QP}$ rispetto al tempo, ricordando che $\hat{n}$ è costante e quindi $\frac{d}{dt} \hat{n} = \vec{0}$,

  $$\begin{aligned}
   \dfrac{d^2 \vec{r}_{QP}}{dt^2}
     & = \dfrac{d}{dt} \left( \vec{\omega} \times \vec{r}_{QP} \right) = \\
     & = \dfrac{d \vec{\omega}}{dt} \times \vec{r}_{QP} + \vec{\omega} \times \dfrac{d \vec{r}_{QP}}{dt}= \\
     & = \alpha \times \vec{r}_{QP} + \vec{\omega} \times \left( \vec{\omega} \times \vec{r}_{QP} \right) \ .
  \end{aligned}$$

L'accelerazione di un punto materiale $P$ di un corpo rigido rispetto al sistema di riferimento scelto, può essere quindi scritta come

  $$\begin{aligned}
    \vec{a}_P & = \vec{a}_{Q/O} + \vec{a}_{P/Q} = \\
              & = \vec{a}_{Q/O} + \alpha \times \vec{r}_{QP} + \vec{\omega} \times \left( \vec{\omega} \times \vec{r}_{QP} \right) \ .
  \end{aligned}$$





