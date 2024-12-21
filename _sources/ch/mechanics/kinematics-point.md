````{only} html
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
````

(physics-hs:mechanics:kinematics:point)=
# Cinematica del punto

La cinematica di un punto $P(t)$ è completamente definita dalla sua posizione nello spazio in funzione del tempo. La configurazione di un sistema puntiforme in un istante temporale è data dalla sua posizione rispetto a un punto $O$ preso come origine, come riferimento. Lo stato di un sistema puntiforme in un determinato istante temporale è definito dalla sua posizione e dalla sua velocità. Rispetto a un'origine considerata indipendente dal tempo, la posizione del punto $P$ è definita dal vettore euclideo $\vec{r}_P(t) = P(t) - O$ che congiunge l'origine $O$ con il punto $P$, la velocità e l'accelerazione sono rispettivamente la derivata prima e seconda della posizione rispetto al tempo,

$$\begin{aligned}
   \vec{r}_P(t) & := P(t) - O & \text{(posizione di $P$ rispetto a $O$)} \\
   \vec{v}_P(t) & := \frac{d \vec{r}_P}{dt}(t) & \text{(velocità di $P$ rispetto a $O$)} \\
   \vec{a}_P(t) & := \frac{d^2 \vec{r}_P}{dt^2}(t) = \frac{d \vec{v}_P}{dt}(t) & \text{(accelerazione di $P$ rispetto a $O$)} \\
\end{aligned}$$


(physics-hs:mechanics:kinematics:point:motion)=
## Moti particolari

(physics-hs:mechanics:kinematics:point:motion:a-0)=
### Moto non accelerato
Un moto non accelerato di un punto $P$ rispetto a un sistema di riferimento con origine in $O$ può essere definito dalla condizione di accelerazione nulla 

$$\vec{a}_P = \ddot{\vec{r}}_P(t) = \vec{0} \ ,$$

la cui integrazione due volte in tempo fornisce le leggi della velocità e dello spazio

$$\begin{cases}
  \vec{v}_P(t) & = \vec{c}_1 \\
  \vec{r}_P(t) & = \vec{c}_1 \, t + \vec{c}_2 \ .
\end{cases}$$

**todo** dimostrazione come esercizio con procedimento

Si nota che la condizione di accelerazione nulla implica la condizione di velocità costante. **todo**

accompagnata da condizioni tra di loro compatibili (**todo** *fare esempio di condizioni non compatibili, es. velocità diverse in due istanti temporali diversi*) che identifichino unicamente il moto, come possono essere ad esempio:

- posizione e velocità a un istante temporale

  $$\begin{cases}
    \vec{r}(t_0) = \vec{r}_0 \\
    \vec{v}(t_0) = \vec{v}_0
  \end{cases}$$
 
  Le leggi del moto possono diventano 

  $$\begin{cases}
    \vec{v}_P    & = \vec{v}_0  \\
    \vec{r}_P(t) & = \vec{v}_0 \, ( t - t_0 ) + \vec{r}_0 \ ,
  \end{cases}$$

  **todo** dimostrazione come esercizio con procedimento

- posizione in due istanti temporali

  $$\begin{cases}
    \vec{r}(t_0) = \vec{r}_0 \\
    \vec{r}(t_1) = \vec{r}_1
  \end{cases}$$

  Le leggi del moto possono diventano 

  $$\begin{cases}
    \vec{v}_P    & = \frac{\vec{r}_1 - \vec{r}_0}{t_1 - t_0} \\
    \vec{r}_P(t) & = \vec{v}_P \, ( t - t_0 ) + \vec{r}_0 \ ,
  \end{cases}$$
  
  **todo** dimostrazione come esercizio con procedimento

<span style="color:red">
**todo** moto rettilineo; uso dei sistemi di riferimento
</span>

(physics-hs:mechanics:kinematics:point:motion:a)=
### Moto uniformemente accelerato
Un moto uniformemente accelerato di un punto $P$ rispetto a un sistema di riferimento con origine in $O$ può essere definito dalla condizione di accelerazione costante

$$\vec{a}_P = \ddot{\vec{r}}_P(t) = \vec{a} \ ,$$

la cui integrazione due volte in tempo fornisce le leggi della velocità e dello spazio

$$\begin{cases}
  \vec{v}_P(t) & = \vec{a} t               + \vec{c}_1 \\
  \vec{r}_P(t) & = \dfrac{1}{2}\vec{a} t^2 + \vec{c}_1 \, t + \vec{c}_2 \ .
\end{cases}$$

**todo** dimostrazione come esercizio con procedimento

accompagnata da condizioni tra di loro compatibili che identifichino unicamente il moto, come possono essere ad esempio:

- posizione e velocità a un istante temporale

  $$\begin{cases}
    \vec{r}(t_0) = \vec{r}_0 \\
    \vec{v}(t_0) = \vec{v}_0
  \end{cases}$$
 
  Le leggi del moto possono diventano 

  $$\begin{cases}
    \vec{v}_P(t) & = \vec{a} t                     + \vec{v}_0  \\
    \vec{r}_P(t) & = \dfrac{1}{2}\vec{a} (t-t_0)^2 + \vec{v}_0 \, ( t - t_0 ) + \vec{r}_0 \ ,
  \end{cases}$$

  **todo** dimostrazione come esercizio con procedimento

- posizione in due istanti temporali... **todo**
  
  **todo** dimostrazione come esercizio con procedimento

<span style="color:red">
**todo** moto piano (rettilineo se $\vec{a}$, $\vec{v}_0$ sono allineati); uso dei sistemi di riferimento
</span>

(physics-hs:mechanics:kinematics:point:motion:circular)=
### Moto circolare
La cinematica di un punto su una traiettoria circolare (**todo** è un vincolo!) può essere rappresentato usando un sistema di **coordinate polari** con origine coincidente con il centro della circonferenza

$$r = R \ , \quad \theta_P(t)=\text{**todo**}$$

o in coordinate cartesiane

$$\begin{cases}
 x_P(t) = R \, \cos \theta_P(t) \\
 y_P(t) = R \, \sin \theta_P(t) \\
\end{cases}$$

che permettono di identificare il punto $P$ con il raggio vettore rispetto all'origine

$$\vec{r}_P = R \cos \theta_P(t) \hat{x} + R \sin \theta_P(t) \hat{y} \ .$$

- Definizione vettori $\hat{r}$, $\hat{\theta}$ **todo** *dipendenza di questi versori dalla posizione di $P$ nello spazio, e quindi in generale dal tempo
- La velocità e l'accelerazione del punto **todo**
  - direzione e modulo di velocità e accelerazione

$$\begin{cases}
  \vec{v}_P(t) & = R \dot{\theta}(t) \left( -\sin \theta_P(t) \hat{x} + \cos \theta_P(t) \hat{y} \right) = R \dot{\theta}(t) \hat{\theta}(t) \\
  \vec{a}_P(t) & = R \ddot{\theta}(t) \left( -\sin \theta_P(t) \hat{x} + \cos \theta_P(t) \hat{y} \right) + \\
               & + R \ddot{\theta}^2(t) \left( -\cos \theta_P(t) \hat{x} - \sin \theta_P(t) \hat{y} \right)     
                 = R \ddot{\theta}(t) \hat{\theta}(t) - R \dot{\theta}^2(t) \hat{r}(t) \ .
\end{cases}$$

(physics-hs:mechanics:kinematics:point:motion:circular-uniform)=
#### Moto circolare uniforme
Il moto circolare uniforme ha modulo della velocità costante, 

$$|\vec{v}_P| = |R \dot \theta_P|$$

e la derivata nel tempo della coordinata $\theta_P$ è costante **todo**

- **todo** pulsazione, periodo, frequenza,...

(physics-hs:mechanics:kinematics:point:motion:harmonic)=
### Moto armonico lungo un segmento
Un moto armonico lungo un segmento può essere definito come la proiezione di un punto che compie un moto circolare uniforme su una circonferenza che ha il segmento come diametro **todo**



## Problemi



