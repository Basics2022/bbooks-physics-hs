(physics-hs:mechanics:dynamics:problems-extra)=
# Altri problemi

Questi problemi sono pensati per persone con un livello di preparazione maggiore; alcuni esercizi potrebbero richiedere degli strumenti matematici che non sono a disposizione dal fruitore medio, e nemmeno a uno sopra la media, di questo materiale.

````{exercise} Conservazione del momento angolare, nell'esperimento della ruota
Si considera una piattaforma libera di ruotare rispetto all'asse $z$ di sistema di riferimento cartesiano inerziale $Oxyz$. L'angolo di rotazione è indicato con $\theta$. Sulla piattaforma è montata una ruota, libera di ruotare attorno all'asse passante per il suo mozzo. Il mozzo è a sua volta libero di ruotare rispetto all'asse $x_1$ solidale con la piattaforma.

La piattaforma è inizialmente ferma, mentre la ruota è in moto con velocità angolare $\vec{\omega}^b_{0} = \omega^b_{0} \hat{y}_2$. La ruota viene girata da una coppia interna in modo tale da portare l'asse $\hat{x}_2$ allineato con l'asse $z$. Si chiede di determinare lo stato finale del sistema.

```{dropdown} Soluzione con le leggi di conservazione
```
```{dropdown} Soluzione con le equazione del moto
:open:

Si introducono i seguenti sistemi di riferimento per studiare il moto del sistema, ed esprimere le rotazioni come rotazioni parziali:
- il sistema $Oxyz$ inerziale
- il sistema $Ox_1 y_1 z_1$ solidale con la piattaforma, ruotato di un angolo $\theta$ rispetto a $O x y z$ attorno all'asse $z$
- il sistema $Ox_2 y_2 z_2$ solidale con il mozzo della ruota, ruotato di un angolo $\phi$ rispetto a $O x_1 y_1 z_1$ attorno all'asse $x_1$
- il sistema $Ox_3 y_3 z_3$ solidale con la ruota. *Data la simmetria della ruota, si può evitare di introdurre questo sistema di riferimento*

Le leggi di trasformazione dei vettori di queste basi sono

$$
\begin{cases}
  \hat{x} = \cos \theta \hat{x}_1 - \sin \theta \hat{y}_1 \\
  \hat{y} = \sin \theta \hat{x}_1 + \cos \theta \hat{y}_1 \\
  \hat{z} = \hat{z}_1 \\
\end{cases}
\quad , \quad
\begin{cases}
  \hat{x}_1 = \cos \theta \hat{x} + \sin \theta \hat{y} \\
  \hat{y}_1 =-\sin \theta \hat{x} + \cos \theta \hat{y} \\
  \hat{z}_1 = \hat{z} \\
\end{cases}
$$

$$
\begin{cases}
  \hat{x}_1 = \hat{x}_2 \\
  \hat{y}_1 = \cos \phi \hat{y}_2 - \sin \phi \hat{z}_2 \\
  \hat{z}_1 = \sin \phi \hat{y}_2 + \cos \phi \hat{z}_2 \\
\end{cases}
\quad , \quad
\begin{cases}
  \hat{x}_2 = \hat{x}_1 \\
  \hat{y}_2 = \cos \phi \hat{y}_1 + \sin \phi \hat{z}_1 \\
  \hat{z}_2 =-\sin \phi \hat{y}_1 + \cos \phi \hat{z}_1 \\
\end{cases}
$$

La ruota e la piattaforma vengono modellati come corpi rigidi. Le loro proprietà inerziali sono quindi costanti rispetto ai sistemi di riferimento materiali, solidali con essi,

$$\begin{aligned}
  \mathbb{I}_G^p & = I^p_x \hat{x} \hat{x} + I^p_x \hat{y} \hat{y} + I^p_z \hat{z} \hat{z} \\
  \mathbb{I}_G^w & = I^w_x \hat{x}_2 \hat{x}_2 + I^w_y \hat{y}_2 \hat{y}_2 + I^w_x \hat{z}_2 \hat{z}_2 \\
\end{aligned}$$

Le equazioni dinamica del bilancio della quantità di moto di un corpo rigido è

$$\dot{\Gamma}_H = - \dot{\vec{x}}_H \times \vec{Q} + \vec{M}_H^e \ ,$$

e se viene riferita al centro di massa $G$ del sistema, l'equazione dinamica diventa $\dot{\Gamma}_G = \vec{M}_G^e$, con il momento della quantità di moto $\vec{\Gamma}_G = \mathbb{I}_G \cdot \vec{\omega}$.

Le velocità angolari di piattaforma e ruota sono

$$\begin{aligned}
  \vec{\omega}^p & = \dot{\theta} \hat{z} \\
  \vec{\omega}^w
  & = \dot{\theta} \hat{z} + \dot{\phi} \hat{x}_1 + \dot{\psi} \hat{y}_2 = \\
  & = \dot{\theta} (\sin \phi \hat{y}_2 + \cos \phi \hat{z}_2) + \dot{\phi} \hat{x}_2 + \dot{\psi} \hat{y}_2 = \\
\end{aligned}$$

I momenti angolari di piattaforma e ruota sono

$$\begin{aligned}
  \vec{\Gamma}_G^p & = \mathbb{I}_G^p \cdot \vec{\omega}^p = I_z^p \dot{\theta} \hat{z} \\
  \vec{\Gamma}_G^w 
  & = \mathbb{I}_G^w \cdot \vec{\omega}^w = \\
  & = [I^w_x \hat{x}_2 \hat{x}_2 + I^w_y \hat{y}_2 \hat{y}_2 + I^w_x \hat{z}_2 \hat{z}_2] \cdot [ \dot{\phi} \hat{x}_2 + ( \dot{\theta} \sin \phi + \dot{\psi} ) \hat{y}_2 + \dot{\theta} \cos \phi \hat{z}_2 ] \\
  & =  I^w_x \dot{\phi} \hat{x}_2 + I^w_y (\dot{\theta} \sin \phi + \dot{\psi} ) \hat{y}_2 + I^w_z \dot{\theta} \cos \phi \hat{z}_2 = \\
  & =  I^w_x \dot{\phi} \hat{x}_1 + I^w_y (\dot{\theta} \sin \phi + \dot{\psi} ) (\cos \phi \hat{y}_1 + \sin \phi \hat{z}_1) + I^w_z \dot{\theta} \cos \phi (-\sin \phi \hat{y}_1 + \cos \phi \hat{z}_1) = \\
  & =  I^w_x \dot{\phi} \hat{x}_1 + \hat{y}_1 \left( ( I^w_y - I^w_z) \dot{\theta} \sin \phi \cos \phi + \dot{\psi} \cos \phi \right) + \hat{z}_1 \left( I^w_y \dot{\theta} \sin^2 \phi + I^w_z \dot{\theta} \cos^2 \phi + I^w_y \dot{\psi} \sin \phi  \right) = \\
  & = I^w_x \left( \ddot{\phi} \hat{x}_1 + \dot{\phi} \dot{\theta} \hat{y}_1 \right) + \hat{y}_1 \frac{d}{dt}() - \dot{\theta} \hat{x}_1 () + \hat{z}_1 \frac{d}{dt} \left( \right)
\end{aligned}$$

L'energia cinetica dei due corpi è

$$\begin{aligned}
  K^p & = \frac{1}{2} \vec{\omega}^p \cdot \mathbb{I}^p_G \cdot \vec{\omega}^p = \\
      & = \frac{1}{2} I^p_z \dot{\theta}^2 \\
  K^w 
  & = \frac{1}{2} \vec{\omega}^w \cdot \mathbb{I}^w_G \cdot \vec{\omega}^w = \\
  & = \frac{1}{2} [\dot{\phi} \hat{x}_2 + ( \dot{\theta} \sin \phi + \dot{\psi} ) \hat{y}_2 + \dot{\theta} \cos \phi \hat{z}_2] \cdot [ I^w_x \dot{\phi} \hat{x}_2 + I^w_y (\dot{\theta} \sin \phi + \dot{\psi} ) \hat{y}_2 + I^w_z \dot{\theta} \cos \phi \hat{z}_2 ] = \\
  & = \frac{1}{2} [ I^w_x \dot{\phi}^2 + I^w_y(\dot{\theta}\sin\phi + \dot{\psi})^2 + I^w_z \dot{\theta}^2 ]
\end{aligned}$$

I momenti esterni agenti sulla ruota sono dovuti ai vincoli e alle azioni (interne al sistema complessivo) scambiate con la piattaforma; i momenti esterni agenti sulla piattaforma includono anche le reazioni vincolari a terra.

$$\begin{aligned}
  \vec{M}^{wp} = \dots
\end{aligned}$$
<!--  \vec{M}^{wp} = M_{x,1} \hat{x}_1 + M_{y,1} \hat{y}_1 + M_{z,1} \hat{z}_1 + M_{x,2} \hat{x}_2 + M_{z,2} \hat{z}_2 = -->






```

````

