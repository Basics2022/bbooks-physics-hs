(physics-hs:mechanics:inertia)=
# Inerzia

## Massa e distribuzione di massa

La massa è la grandezza fisica che rappresenta la quantità di materia (**todo** *Non confonderla con la mole, definita come quantità di sostanza, una volta affermatasi la teoria atomica*)

In meccanica classica, la può essere definita in maniera operativa:
- tramite la sua [interazione gravitazionale](physics-hs:mechanics:actions:gravitation) con altri corpi dotati di massa
- come una misura della resistenza di un sistema ai cambiamenti del suo stato di moto in risposta a una forza applicata, come sarà chiaro dalle equazioni della [dinamica](physics-hs:mechanics:dynamics)






## Quantità dinamiche
Come sarà chiaro nello sviluppo delle [equazioni di moto di un sistema](physics-hs:mechanics:dynamics:eom:points), la definizione di alcune grandezze dinamiche additive risulta naturale, fornendo dei concetti utili e sintetici per la costruzione di un modello e l'interpretazione dei fenomeni fisici.

Queste grandezze dinamiche combinano la massa e la sua distribuzione con le grandezze cinematiche del sistema. In particolare, risulta utile definire tre grandezze:
- quantità di moto
- momento della quantità di moto
- energia cinetica

Le [equazioni del moto](physics-hs:mechanics:dynamics:eom) dei sistemi rappresentano delle equazioni differenziali che mettono in relazione la variazione di queste quantità dinamiche con la causa di queste variazioni, in generale riconducibile ad [azioni](physics-hs:mechanics:actions) agenti sul sistema.

Sotto opportune ipotesi, queste grandezze dinamiche sono costanti del moto, come descritto dalle [leggi di conservazione](physics-hs:mechanics:dynamics:conservation).

Le 3 grandezze dinamiche possono avere espressioni diverse, a seconda del sistema di interesse. Nel caso di corpi rigidi, queste possono essere espresse in termini di velocità di un punto materiale e della velocità angolare del corpo.

### Punto

$$\begin{aligned}
  \vec{Q}_P     & = m_P \, \vec{v}_P \\
  \vec{L}_{P,H} & = m_P \, (P - H) \times \vec{v}_P \\
   K_P          & = \frac{1}{2} m_P \left| \vec{v}_P \right|^2
\end{aligned}$$

### Sistemi di punti - distribuzione discreta di massa

$$\begin{aligned}
  \vec{Q}       = \sum_i \vec{Q}_i     & = \sum_i  m_i \, \vec{v}_i \\
  \vec{L}_{H}   = \sum_i \vec{L}_{i,H} & = \sum_i  m_i \, (P_i - H) \times \vec{v}_i \\
   K            = \sum_i  K_i          & = \sum_i  \frac{1}{2} m_i \left| \vec{v}_i \right|^2
\end{aligned}$$

#### Sistema di punti rigidi

Usando la definizione di centro di massa

$$m G = \sum_i m_i P_i$$

e legge del moto rigido

$$\vec{v}_i - \vec{v}_P = \vec{\omega} \times (P_i - P)$$

le quantità dinamiche possono essere espresse in funzione della velocità del punto di riferimento $P$ e della velocità angolare del sistema, tramite la massa e le altre quantità inerziali

- la quantità di moto

$$\begin{aligned}
  \vec{Q} = \sum_i m_i \vec{v}_i
        & = \sum_i m_i \left( \vec{v}_P + \vec{\omega} \times (P_i - P) \right) = \\
        & =  m \vec{v}_P + \vec{\omega} \times m (G - P) 
\end{aligned}$$

- momento della quantità di moto

$$\begin{aligned}
  \vec{L}_H = \sum_i m_i (P_i - H) \times \vec{v}_i
        & = \sum_i m_i \left( P_i - P + \vec{r}_P - \vec{r}_H \right) \times \vec{v}_i = \\
        & = \sum_i m_i \left( P_i - P \right) \times \vec{v}_i + \left( P - H \right) \times \vec{Q}  = \\
        & = \sum_i m_i \left( P_i - P \right) \times \left( \vec{v}_P - \left( P_i - P \right) \times \vec{\omega} \right) + \left( P - H \right) \times \vec{Q}  = \\
        & = m (G - P) \times \vec{v}_P - \sum_i m_i \left( P_i - P \right) \times \left( \left( P_i - P \right) \times \vec{\omega} \right) + \left( P - H \right) \times \vec{Q}  = \\
        & = \mathbb{I}_P \cdot \vec{\omega} +  m (G - P) \times \vec{v}_P + \left( P - H \right) \times \vec{Q}
\end{aligned}$$

Nel caso di moto 2-dimensionale e velocità angolare perpendicolare a questo piano, **todo**

$$\begin{aligned}
  \vec{r}_{i/P} & := P_i - P = \left( x_i - x_P \right) \hat{x} + \left( y_i - y_P \right) \hat{y} \\
  \vec{\omega} & = \dot{\theta} \, \hat{z}
\end{aligned}$$

$$\begin{aligned}
  - \vec{r}_{i/P} \times \left( \vec{r}_{i/P} \times \hat{\omega} \right) 
  & = - ( \Delta x_i \hat{x} + \Delta y_i \hat{y} ) \times \left[ ( \Delta x_i \hat{x} + \Delta y_i \hat{y} ) \times \dot{\theta} \hat{z} \right] = \\ 
  & = - \dot{\theta} ( \Delta x_i \hat{x} + \Delta y_i \hat{y} ) \times \left( - \Delta x_i \hat{y} + \Delta y_i \hat{x} \right) = \\
  & = \left( \Delta x_i^2 + \Delta y_i^2 \right) \dot{\theta} \, \hat{z} \ .
\end{aligned}$$

e l'espressione del momento della quantità di moto diventa

$$\vec{L}_{H} = I_P \, \vec{\omega} +  m (G - P) \times \vec{v}_P + \left( P - H \right) \times \vec{Q}$$

con 

$$I_P = \sum_i m_i \left[ \left(x_i - x_P\right)^2 + \left(y_i - y_P\right)^2 \right]$$

### Sistemi estesi con distribuzione continua di massa

#### Sistemi rigidi
