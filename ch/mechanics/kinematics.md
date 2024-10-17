(physics-hs:mechanics:kinematics)=
# Cinematica

La cinematica si occupa della descrizione del moto dei sistemi, senza indagarne le cause. La cinematica si occupa della descrizione dello stato di un sistema, e della sua variazione, nello spazio.

Lo stato di un sistema è definito da un insieme di variabili indipendenti, o coordinate, dette **gradi di libertà**.  Il numero di gradi di libertà coincide con la dimensione della varietà (**todo** *dello spazio?*) nel quale si svolge il moto.

La posizione di un **punto** libero nello spazio euclideo $E^n$ ($n=2$ piano, $n=3$ spazio. **todo** ref alla definizione di spazio euclideo in matematica:geometria) è definito da un insieme di $n$ coordinate:
- un punto libero nel piano ha 2 gradi di libertà (traslazione);
- un punto libero nello spazio ha 3 gradi di libertà (traslazione). 

Lo stato di un **corpo rigido** è definito dalla posizione di un suo punto nello spazio e dalla sua orientazione: 
- un corpo rigido nel piano ha 3 gradi di libertà, 2 per definire la posizione di un suo punto nello spazio (traslazione) e 1 per definire la sua orientazione (rotazione) rispetto a un asse ortogonale al piano; 
- un corpo rigido nello spazio ha 6 gradi di libertà, 3 per definire la posizione di un suo punto nello spazio (traslazione) e 3 per definire la sua orientazione (rotazione)

(physics-hs:mechanics:kinematics:point)=
## Cinematica del punto

**Posizione di un punto.** $P - O = \vec{r}_P$

**Velocità di un punto.** $\vec{v}_P = \dfrac{d \vec{r}_P}{dt}$

**Accelerazione di un punto.** $\vec{a}_P = \dfrac{d \vec{v}_P}{dt} = \dfrac{d^2 \vec{r}_P}{d t^2}$

(physics-hs:mechanics:kinematics:rigid)=
## Cinematica di un corpo rigido

(physics-hs:mechanics:kinematics:rigid-2d)=
### Problemi nel piano

- **Posizione di un punto.** 

$$Q - O = \vec{r}_Q$$

- **Orientazione del corpo.**

$$P - Q = \vec{r}_{QP} = \cos \theta \, \vec{r}_{QP}^0 + \sin \theta \, \hat{n} \times \vec{r}_{QP}^0$$

- **Velocità di un punto.**

$$\vec{v}_P = \dfrac{d \vec{r}_P}{dt}$$

- **Velocità angolare del corpo**, $\vec{\omega} = \dot{\theta} \hat{n}$.

$$\begin{aligned}
  \dfrac{d \vec{r}_{QP}}{dt} 
  & = \dfrac{d}{dt} \left(  \cos \theta \, \vec{r}_{QP}^0 + \sin \theta \, \hat{n} \times \vec{r}_{QP}^0 \right) = \\
  & = \dot{\theta} \left( -\sin \theta \, \vec{r}_{QP}^0 + \cos \theta \, \hat{n} \times \vec{r}_{QP}^0 \right) = \\
  & = \dot{\theta} \hat{n} \times \left( \sin \theta \, \hat{n} \times \vec{r}_{QP}^0 + \cos \theta \, \vec{r}_{QP}^0 \right) = \\
  & = \dot{\theta} \hat{n} \times \vec{r}_{QP} \ ,
\end{aligned}$$ 

avendo usato l'identità vettoriale 

$$\vec{n} \times (\vec{n} \times \vec{w}) = \hat{n} \underbrace{(\hat{n} \cdot \vec{w})}_{=0} - \vec{w} \underbrace{(\hat{n} \cdot \hat{n})}_{=1} = - \vec{w} \ .$$

- **Accelerazione di un punto.**

$$\vec{a}_P = \dfrac{d \vec{v}_P}{dt} = \dfrac{d^2 \vec{r}_P}{d t^2}$$

- **Accelerazione angolare del corpo**, $\vec{\alpha} = \dot{\vec{\omega}} = \ddot{\theta} \hat{n}$.

$$\begin{aligned}
 \dfrac{d^2 \vec{r}_{QP}}{dt^2}
   & = \dfrac{d}{dt} \left( \vec{\omega} \times \vec{r}_{QP} \right) = \\
   & = \dfrac{d \vec{\omega}}{dt} \times \vec{r}_{QP} + \vec{\omega} \times \dfrac{d \vec{r}_{QP}}{dt}= \\
   & = \alpha \times \vec{r}_{QP} + \vec{\omega} \times \left( \vec{\omega} \times \vec{r}_{QP} \right) \ .
\end{aligned}$$ 




