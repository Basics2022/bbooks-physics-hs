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





