(physics-hs:waves:optics:geometric)=
## Ottica geometrica

**Approssimazione con raggi di luce.** I raggi luminosi sono qualitativamente delle linee geometriche che indicano la propagazione della luce. Essi possono essere definiti come delle curve perpendicolari in ogni punto ai fronti d'onda del campo elettromagnetico.

**todo** 
- *discutere approssimazione geometrica, con raggi luminosi; quando vale?*
- *aggiungere immagini per questa approssimazione: bridging EM field and geometrical optics, some examples: free space homogeneous medium; discontinuous medium; continuously varying in-homogeneous medium: miraggio e fata morgana*

(physics-hs:waves:optics:geometric:principles)=
### Princìpi dell'ottica geometrica
**Propagazione rettilinea in un mezzo omogeneo.** In un mezzo omogeneo, con indice di rifrazione $n$ ({prf:ref}`refraction-index`) uniforme, i raggi luminosi si propagano su traiettorie rettilinee.


**Legge di Snell - riflessione e rifrazione tra mezzi discontinui.** Per soddisfare le condizioni di continuità del campo elettromagnetico in corrispondenza di una discontinuità di proprietà fisiche, un raggio che si propaga nel mezzo 1 e incidente su una discontinuità con il mezzo 2 con un angolo $\theta{1,i}$ con la direzione normale, in generale:
- viene riflesso con lo stesso angolo 

   $$\theta_{1,r} = \theta_{1,i}$$

- viene trasmesso con angolo $\theta_{2,t}$, tale che

   $$\frac{\sin \theta_{2,t}}{\sin \theta_{1,i}} = \dfrac{n_1}{n_2} = \dfrac{c_2}{c_1} \ .$$

**todo** *Stabilire i coefficienti di riflessione e trasmissione. Scrivere sezione in physics-electromagnetism*

**Riflessione totale.** Quando $\frac{c_2}{c_1} > 1$ esiste un angolo di incidenza limite oltre al quale non avviene trasmissione nel secondo mezzo. Il valore massimo della funzione $\sin$ è 1; la condizione limite, di riflessione totale si ottiene quando 

$$1 = \sin \theta_{2,t} = \frac{c_2}{c_1} \sin \theta_{1,i} \qquad \rightarrow \qquad $$

**Principio di Fermat.** La propagazione di un raggio luminoso può essere riformulata con il principio di Fermat: un raggio luminoso da una sorgente a un osservatore percorre la traiettoria con tempo di percorrenza minimo.

```{prf:example} Principio di Fermat e legge di Snell
Data un'interfaccia piana, $y=0$, tra due mezzi con indice di rifrazione $n_1$, $n_2$, una sorgente luminosa con coordinate cartesiane $(x_s, y_s)$, $y_s > 0$, e un osservatore con coordinate $(x_o, y_o)$, $y_o < 0$, viene chiesto di determinare il percorso del raggio luminoso usando il principio di Fermat e verificare che il risultato è in accordo con la legge di Snell.

Si scrive il tempo di percorrenza $\Delta t$ in funzione della coordinata $x$ del punto dell'interfaccia per il quale passa il raggio luminoso desiderato.

$$\begin{aligned}
\Delta t(x) 
  & = \Delta t_1(x) + \Delta t_2(x) = \\
  & = \frac{\Delta \ell_1(x)}{c_1} + \frac{\Delta \ell_2(x)}{c_2} = \\
  & = n_1 \frac{\sqrt{(x-x_s)^2 + y_s^2}}{c_0} + n_2 \frac{\sqrt{(x-x_o)^2 + y_o^2}}{c_0} = \\
\end{aligned}$$

$$
c_0 \dfrac{d \Delta t}{dx}(x) 
= \frac{n_1}{c_0} \frac{1}{2} \left( (x-x_s)^2 + y_s^2 \right)^{-\frac{1}{2}} 2 (x-x_s)
+ \frac{n_2}{c_0} \frac{1}{2} \left( (x-x_o)^2 + y_o^2 \right)^{-\frac{1}{2}} 2 (x-x_o)
$$

$$\begin{aligned}
  & 0 = c_0 \dfrac{d \Delta t}{dx}(x^*) \\
  & \rightarrow \quad n_1 \frac{x^* - x_s}{\sqrt{(x^*-x_s)^2 + y_s^2}} = n_2 \frac{x_o - x^*}{\sqrt{(x^*-x_o)^2 + y_o^2}} \\ 
  & \rightarrow \quad n_1 \sin \theta_1 = n_2 \sin \theta_2 \ .
\end{aligned}$$


```




