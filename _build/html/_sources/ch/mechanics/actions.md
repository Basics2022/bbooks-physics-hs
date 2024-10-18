(physics-hs:mechanics:actions)=
# Azioni

<span style="color:red">
## Approfondimento: le 4 interazioni fondamentali
- gravitazionale: ~ massa
- elettromagnetica: ~ carica elettrica
- nucleare debole: ~ decadimenti nucleari
- nucleare forte: ~ tra particelle elementari (quark) in particelle sub-atomiche
</span>

## Introduzione ai modelli
<span style="color:red">**todo** qui? O una volta che sono state definite le azioni distribuite?</span>

Esempio, forze concentrate, se la regione di interazione è "sufficientemente" (cosa significa sufficientemente? **todo** bontà nel modello nella descrizione del fenomeno di interesse,...) limitata rispetto alle dimensioni del sistema

## Modelli
- azioni:
  - forze
  - momenti, e coppie di forze
  - campi di forze, esempio campo gravitazionale
  - forze distribuite, in un volume, in una superficie (pressione) o su una curva

- sistemi di forze equivalenti:
  - risultante delle forze

- esempi: gravità (legge di gravitazione universale, gravità nei pressi della superficie terrestre), molle e smorzatori leggeri, forze di contatto (reazione normale e attrito)

## Sistemi di forze equivalenti


## Esempi

### Gravità
#### Legge di gravitazione universale
La forza $\vec{F}_{12}$ esercitata da un corpo di massa $m_2$ in $P_2$ su un corpo di massa $m_1$ in $P_1$ è descritta dalla **legge di gravitazione universale di Newton**,

$$\vec{F}_{12} = G \dfrac{m_1 m_2}{r_{12}^2} \hat{r}_{12} \ ,$$

avendo indicato con $\vec{r}_{12} = (P_2 - P_1)$ il vettore che punta dal punto $P_1$ al punto $P_2$, $r_{12} = |\vec{r}_{12}|$ il suo modulo, e $\hat{r}_{12} = \frac{\vec{r}_{12}}{|\vec{r}_{12}|}$ il vettore unitario lungo la stessa direzione.

Nella formula, $G = \dots$ indica la costante di gravitazione universale, considerata una costante della natura **todo**

#### Campo di gravità

Il campo di gravità generato da una massa $m_2$ posta in $P_2$ è **todo** una funzione dello spazio che associa a ogni punto $P$ un vettore,

$$\vec{g}(\vec{r}_1) = \dfrac{\vec{F}_{12}}{m_1} = G \dfrac{m_2}{r_{12}^2} \hat{r}_{12} \ ,$$

**todo** abituarsi al concetto di campo, introdotto a partire dalla definizione operativa con *massa test*
**todo** PSCE
**todo** noto il campo di gravità $\vec{g}(P)$, la forza di gravità percepita da un sistema di massa $m$ in $P$ può essere scritta come

 $$\vec{F} = m \vec{g}(P)$$

#### Campo di gravità nei pressi della superficie terrestre
All'interno di un dominio limitato nei pressi della superficie terrestre, è comune approssimare il campo di gravitazione terrestre come un campo uniforme, diretto lungo la verticale locale verso il centro della terra e di intensità $g = G \frac{M_E}{R_E^2}$.

E' possibile derivare questo modello, approssimando il vettore posizione rispetto al centro della terra $P - P_E \sim R_E \hat{r}$ e il versore che identifica la direzione da un punto del dominio al centro della Terra con la verticale locale $\hat{r}_{12} \sim - \hat{z}$

$$\vec{g}(\vec{r}) = - G \dfrac{M_E}{R_E^2} \hat{z} = - g \hat{z} \ .$$


- lavoro e potenza di una forza

- azioni conservative
