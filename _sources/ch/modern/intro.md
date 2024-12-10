(physics-hs:modern:intro)=
# Introduzione alla fisica del XX secolo

## Scoperta dell'elettrone - J.J.Thompson

```{dropdown} Moto di una carica in un campo elettromagnetico uniforme stazionario
:open:

Una volta scelto un sistema di riferimento (*così da poter identificare la posizione di un punto nello spazio con un vettore posizione $\vec{r} = R-O$ rispetto all'origine*), il campo elettromagnetico (rispetto al sistema di riferimento, **todo** *aggiungere sezione su relatività per elettromagnetismo, anche galileiana come approssimazione a bassa velocità*) in una regione dello spazio viene rappresentato dai campi vettoriali, 

$$\vec{e}(\vec{r},t) \, \quad \vec{b}(\vec{r},t) \ ,$$

che permettono di esprimere il campo elettrico e il campo magnetico come funzioni della variabile spazio $\vec{r}$ e tempo $t$.

La posizione di un punto $P$ nello spazio è identificata dal raggio vettore $\vec{r}_P(t)$, in generale funzione del tempo per punti in moto. La velocità e l'accelerazione del punto $P$ riferite al sistema di coordinate scelto sono rispettivamente la derivata prima e seconda del raggio vettore,

$$\vec{v}_P(t) = \frac{d \vec{r}_P}{d t} \ , \quad
  \vec{v}_P(t) = \frac{d \vec{r}_P}{d t} \ .$$

Una carica elettica di intensità $q_P$ in moto con una velocità $\vec{v}_P$ in un punto dello spazio $\vec{r}_P(t)$ in cui è presente un campo elettromagnetico $\vec{e}(\vec{r}_P,t)$, $\vec{b}(\vec{r}_P,t)$ è soggetta alla **forza di Lorentz**,

$$\vec{F}_P(t) = q_P \left[ \vec{e}(\vec{r}_P(t),t) - \vec{b}(\vec{r}_P(t),t) \times \vec{v}_P(t) \right] \ .$$

e l'equazione del moto per la carica è

$$m_P \frac{ d^2 \vec{r}_P}{dt^2} = q_P \left[ \vec{e}(\vec{r}_P(t),t) - \vec{b}(\vec{r}_P(t),t) \times \frac{d \vec{r}_P}{dt} \right] \ .$$

Una volta inteso che le quantità che compaiono nell'equazione sono riferite al punto $P$, per alleggerire un po' la notazione si fanno cadere i pedici $_P$.

In generale, l'equazione del moto è un'equazione differenziale del secondo ordine non lineare, se il campo magnetico dipende dallo spazio o se il campo elettrico varia linearmente nello spazio. Se il campo elettromagnetico è costante (costante in tempo) e uniforme (costante in spazio), $\vec{e}(\vec{r},t) = \vec{E}$, l'equazione del moto,

$$m \ddot{\vec{r}} = q \left[ \vec{e} - \vec{b} \times \dot{\vec{r}} \right] \ .$$

è una ODE lineare a coefficienti costanti.



```


## Misura della carica dell'elettrone - Millikan

## Modello atomico di Rutherford - Geiger-Mardsen

## Lo spin - Stern-Gerlach



