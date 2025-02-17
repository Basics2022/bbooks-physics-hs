(physics-hs:mechanics:dynamics:examples)=
# Esempi


(physics-hs:mechanics:dynamics:examples:pendulum)=
## Pendolo

```{prf:example} Oscillazioni libere - Isocronismo delle piccole oscillazioni
:label: pendulum-free
:class: dropdown

L'equazione dinamica che governa l'oscillazione libera di un pendolo sul quale non agiscono azioni dissipative

$$I \ddot{\theta} + m g \ell \sin \theta = 0 \ ,$$

può essere ricavata dall'equazione di bilancio del momento della quantità di moto attorno alla cerniera del pendolo, o dalla conservazione dell'energia meccanica in assenza azioni non conservative, (esercizio {ref}`pendulum-eom`).

Questo sistema ha una posizione di equilibrio stabile in $\overline{\theta} = 0$.
Le piccole oscillazioni attorno all'equilibrio stabile sono descritte dall'equazione linear(izzata) del sistema, usando l'approssimazione $\sin \theta \sim \theta$ per $\theta$ "piccoli",

$$I \ddot{\theta} + m g \ell \theta = 0 \ ,$$

equazione tipica di un sistema massa-molla, il cui stato ha un andamento periodico armonico con pulsazione $\Omega = \sqrt{\frac{m g \ell}{I}}$. Data la condizione iniziale $\theta(0) = \theta_0$, $\dot{\theta}(0) = 0$, l'evoluzione nel tempo dell'angolo è

$$\theta(t) = \theta_0 \, \cos \left( \sqrt{\frac{m g \ell}{I}} \, t \right) \ .$$

E' immediato notare l'**isocronismo del pendolo** nel regime di **piccole oscillazioni**: la pulsazione e quindi il periodo dell'oscillazione non dipendono dall'ampiezza $\theta_0$ dell'oscillazione.  

```

```{prf:example} Oscillazioni con dissipazione
:label: pendulum-free-damped
```

```{prf:example} Oscillazioni con dissipazione e forzante
:label: pendulum-free-damped-forced
```

```{prf:example} Pendolo in sistemi non inerziali - Accelerazione
:label: pendulum-noninertial-acceleration
```

```{prf:example} Pendolo in sistemi non inerziali - Rotazione della Terra
:label: pendulum-noninertial-earth-rotation

```
